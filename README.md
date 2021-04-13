# Average Filter

> Author : Ya Chen<br>
> Date : 2021 / 4 / 13

---

<br>
<div>

## Description

The idea of mean filtering is simply to replace each pixel value in an image with the <b>average</b> value of its neighbors, including itself. This has the effect of eliminating pixel values which are unrepresentative of their surroundings. Mean filtering is usually thought of as a convolution filter. Like other convolutions it is based around a kernel, which represents the shape and size of the neighborhood to be sampled when calculating the mean. Often a 3×3 square kernel is used, as shown in Figure 1, although larger kernels (e.g. 5 × 5 squares) can be used for more severe smoothing. (Note that a small kernel can be applied more than once in order to produce a similar but not identical effect as a single pass with a large kernel.)

<br>
<table border = '1'>
    <tr>
        <td> 1 / 9
        <td> 1 / 9
        <td> 1 / 9
    <tr>
        <td> 1 / 9
        <td> 1 / 9
        <td> 1 / 9
    <tr>
        <td> 1 / 9
        <td> 1 / 9
        <td> 1 / 9
</table>
<br>
We will divide the next implementation into three steps:

1. Select an experimental image
2. Apply a 3 by 3 Average Filter and to the image
3. Unsharp masking

</div>
<br>
<br>
<div>

## In-Output Example

### Input:

&emsp;&emsp; Original Image :<br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;
<img src = "https://i.imgur.com/2RAl6cv.jpg" width = "100">

### Output:

&emsp;&emsp; Gray Image :<br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;
<img src = "https://i.imgur.com/VMOW0jx.jpgg" width = "100">

&emsp;&emsp; Color Image Blured by Average Filter :<br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;
<img src = "https://i.imgur.com/2v5AMfl.jpg" width = "100">

&emsp;&emsp; Gray Image Blured by Average Filter:<br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;
<img src = "https://i.imgur.com/AOtcueH.jpg" width = "100">

&emsp;&emsp; Unshape The Color Image Been Blered :<br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;
<img src = "https://i.imgur.com/FHAQ1lq.jpg" width = "100">

&emsp;&emsp; Unshape The Gray Image Been Blered :<br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;
<img src = "https://i.imgur.com/tlvuXlJ.jpg" width = "100">

</div>
