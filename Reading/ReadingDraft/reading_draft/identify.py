import scipy.misc
import skimage.filters.rank as sfr
import skimage.morphology as sm
from skimage import filters, color, io, measure, transform
from skimage.morphology import disk
from image import image_address
from Reading.ReadingDraft.reading_draft import measure_label as ml


# 根据image对象读取刻度
def get_calibration(image, max_num):
    # 获取图片的绝对路径
    address = image_address.get_image_address('水尺1.jpg')
    # address = image_address.get_image_address(image.path)
    # 读取图像
    img = io.imread(address, as_grey=False)
    # 将图像灰度化处理
    gray_img = color.rgb2gray(img)
    scipy.misc.imsave(image_address.get_image_address('img\\01灰度化.jpg'),gray_img)
    # 对比度增强滤波。求出局部区域的最大值和最小值，然后看当前点像素值最接近最大值还是最小值，然后替换为最大值或最小值。
    median_img=sfr.median(gray_img,disk(3))
    scipy.misc.imsave(image_address.get_image_address('img\\02滤波.jpg'),median_img)
    # sobel 边缘检测
    edges_img = filters.sobel(median_img)
    scipy.misc.imsave(image_address.get_image_address('img\\03边缘检测.jpg'),edges_img)
    # 二值化处理
    thresh = filters.threshold_yen(edges_img)
    bin_img =(edges_img <= thresh)*1.0
    scipy.misc.imsave(image_address.get_image_address('img\\04二值化.jpg'),bin_img)
    bin_img_2 = 1- bin_img
    scipy.misc.imsave(image_address.get_image_address('img\\04二值化01.jpg'),bin_img_2)
    # 对连通区域进行操作
    # 删除小块区域
    label_image =measure.label(bin_img_2)
    binary, areas = ml.delete_label(label_image)
    # 只留下最大的连通区域
    label_image = ml.get_max(binary, areas, -1)
    dst = color.label2rgb(label_image)  # 根据不同的标记显示不同的颜色
    scipy.misc.imsave(image_address.get_image_address('img\\05连通区域-大-颜色.jpg'), label_image)
    # 截取水尺图片
    roi_img = ml.get_roi_img(label_image, img)
    scipy.misc.imsave(image_address.get_image_address('img\\06截取水尺.jpg'),roi_img)
    # 找到旋转角度
    angle = ml.get_angle(label_image)
    # 灰度化
    gray_img = color.rgb2gray(roi_img)
    scipy.misc.imsave(image_address.get_image_address('img\\07灰度化.jpg'),gray_img)
    # 水平边缘检测
    edges_img=filters.sobel_h(gray_img)
    scipy.misc.imsave(image_address.get_image_address('img\\08水平检测.jpg'),edges_img)
    # 二值化
    thresh = filters.threshold_yen(edges_img)
    bin_img =(edges_img <= thresh)*1.0
    scipy.misc.imsave(image_address.get_image_address('img\\09二值化.jpg'),bin_img)
    # 骨架提取
    # skelet_img  = bin_img
    skelet_img = sm.skeletonize(bin_img)*1.0
    scipy.misc.imsave(image_address.get_image_address('img\\10骨架提取.jpg'), skelet_img)
    # 去除小于15个像素的线段
    dist = skelet_img > 0
    label_image=sm.remove_small_objects(dist, min_size=15, connectivity=2)
    scipy.misc.imsave(image_address.get_image_address('img\\11去除线段.jpg'), label_image)
    # 旋转
    angle_img = transform.rotate(label_image, angle, resize=True)
    scipy.misc.imsave(image_address.get_image_address('img\\12旋转.jpg'),angle_img)
    # 提取所有的直线
    label_image = measure.label(label_image)
    dst = color.label2rgb(label_image)
    scipy.misc.imsave(image_address.get_image_address('img\\13直线.jpg'),dst)
    # 得到右侧线段的距离
    line_dir, all_line, left_line, right_line = ml.get_right_line_dist(angle_img, label_image)
    # 计算出右边有多少个E与E之间的空 ,即左边有多少个完整的E
    left_E = ml.get_left_E(line_dir)

    # 左边刻度中比右边刻度更高或更低的刻度数量
    # 判断左边最高的线段是否高于右边最高的线段
    left_hight_num = ml.get_left_hight(right_line, left_line)
    # 判断左边最低的线段是否低于右边最低的线段
    left_low_num = ml.get_left_hight(right_line, left_line)
    left_num = left_hight_num + left_low_num
    # 刻度线段的数量
    draft_num = left_num + left_E + len(right_line)
    # print(draft_num)
    drafe = max_num - (draft_num*25)
    print("刻度:"+str(drafe))
    return drafe


print(get_calibration(1,775))
