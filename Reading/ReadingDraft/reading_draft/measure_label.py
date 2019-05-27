from skimage import data,filters,color,io,feature,measure,transform
import skimage.morphology as sm
import scipy.misc
import skimage.filters.rank as sfr
from skimage.morphology import disk

# 删除小块连通区域

# 只保留最大的区域
def delete_label(label_image ):
    areas = [r.area for r in measure.regionprops(label_image)]
    areas.sort()
    # print(areas)
    if len(areas) > 1:
        for region in measure.regionprops(label_image):
            if region.area < areas[-1]:
                for coordinates in region.coords:
                    label_image[coordinates[0], coordinates[1]] = 0
    binary = label_image > 0
    return binary,areas

# 得到只有有i个连通区域的图像
def get_max(binary, areas, i):
    label_image = sm.remove_small_holes(binary, areas[i])
    return label_image

# 截取水尺图片
def get_roi_img(label_image, img):
    label_image = measure.label(label_image)
    region = measure.regionprops(label_image)
    # 截取水尺图片
    minr, minc, maxr, maxc = region[0].bbox
    roi_img = img[minr:maxr, minc:maxc, :]
    return roi_img

# 找到旋转角度
def get_angle(img):
    # 在-20度-20度之间测试
    angle = [i for i in range(-10, 10, 1)]
    dir = [0 for i in range(len(angle))]
    # 对图片进行旋转
    for i, value in enumerate(angle):
        angle_img = transform.rotate(img, value, resize=True)
        # scipy.misc.imsave('D:/USER/Desktop/软件工程/1/01原图'+str(i)+'.jpg', angle_img)
        # 删除小块区域
        label_image = measure.label(angle_img)
        binary, areas = delete_label(label_image)
        # 只留下最大的连通区域
        label_image = get_max(binary, areas, -1)
        # 获取区域的左上角和左下角
        label_image = measure.label(label_image)
        # dst = color.label2rgb(label_image)  # 根据不同的标记显示不同的颜色
        # scipy.misc.imsave('D:/USER/Desktop/软件工程/1/02区域图' + str(i) + '.jpg', dst)
        region = measure.regionprops(label_image)
        minr, minc, maxr, maxc = region[0].bbox
        # 求出区域的面积
        dir[i] = (maxr-minr) * (maxc-minc)
    # 找出区域面积最小时的选择角度
    min_dir = min(dir)
    key = 0
    for i, value in enumerate(dir):
        if value == min_dir:
            key = i
            break
    return angle[key]

# 获取右侧线段的距离
def get_right_line_dist(angle_img, label_image):
    size = angle_img.shape
    rows = size[0]
    cols = size[1]
    first_line_cols = 0
    # 记录上一条线条的rows
    line_rows = -1
    # 线段之间的距离
    line_dir = []
    all_line = []
    left_line = []
    right_line = []
    regions = measure.regionprops(label_image)
    for i, region in enumerate(regions):
        if i == len(regions) - 2:
            break
        minr, minc, maxr, maxc = region.bbox
        l = [minr, minc, maxr, maxc]
        all_line.append(l)
        # 找到右边的线段
        if minc > cols * 0.4 and maxc > cols * 0.6:
            # 如果是右侧第一条线段
            if line_rows == -1:
                line_rows = minr
            else:
                r = minr
                line_dir.append(r - line_rows)
                line_rows = r
            l = [minr, minc, maxr, maxc]
            right_line.append(l)
        else:
            l = [minr, minc, maxr, maxc]
            left_line.append(l)
            # Y = np.array([minr, minr, maxr, maxr])
            # X = np.array([minc, maxc, maxc, minc])
            # rr, cc = draw.polygon(Y, X)
            # draw.set_color(dst, [rr, cc], [0, 0, 0])
    # scipy.misc.imsave('D:/USER/Desktop/软件工程/14直线.jpg',dst)
    # print(line_dir)
    return line_dir, all_line, left_line, right_line

# 计算出右边有多少个E与E之间的空 ,即左边有多少个完整的E
def get_left_E(line_dir):
    left_E = 0
    for i, line in enumerate(line_dir):
        if i == len(line_dir) - 1:
            break
        if line_dir[i + 1] > line * 1.5:
            left_E += 1
    return left_E

# 计算左边刻度中比右边刻度更高刻度数量
def get_left_hight(right_line, left_line):
    left_num = 0
    # 判断左边最高的线段是否高于右边最高的线段
    r_line = right_line[0][0]
    if left_line[0][0] < r_line:
        # 找到有多少条线段高
        for line in left_line:
            if line[0] < r_line:
                left_num += 1
            else:
                break
    return left_num

# 计算左边刻度中比右边刻度更低的刻度数量
def get_left_hight(right_line, left_line):
    left_num = 0
    r_line = right_line[-1][0]
    if left_line[-1][0] > r_line:
        # 找到有多少条线段低
        for line in left_line:
            if line[0] > r_line:
                left_num += 1
    return left_num