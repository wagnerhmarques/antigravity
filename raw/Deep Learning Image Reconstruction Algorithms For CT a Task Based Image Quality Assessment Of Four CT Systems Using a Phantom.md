---
title: "Deep-learning image reconstruction algorithms for CT: A task-based image quality assessment of four CT systems using a phantom"
source: "https://www.sciencedirect.com/science/article/pii/S2211568426000033"
author:
published:
created: 2026-08-25
description: "The purpose of this study was to assess the performance of iterative reconstruction (IR) and deep-learning image reconstruction (DLR) algorithms devel…"
tags:
  - "clippings"
---
[![Elsevier](https://www.sciencedirect.com/us-east-1/prod/60c70907fc6e955d91b577ca3b53d6d6c94b631b/image/elsevier-non-solus.svg)](https://www.sciencedirect.com/journal/diagnostic-and-interventional-imaging "Go to Diagnostic and Interventional Imaging on ScienceDirect")

## Diagnostic and Interventional Imaging

## Original articleDeep-learning image reconstruction algorithms for CT: A task-based image quality assessment of four CT systems using a phantom

[https://doi.org/10.1016/j.diii.2026.01.003](https://doi.org/10.1016/j.diii.2026.01.003 "Persistent link using digital object identifier")

Under a Creative Commons [license](http://creativecommons.org/licenses/by/4.0/)

Open access

## Highlights

- •
 Deep-learning image reconstruction algorithms have been developed to compensate for the limitations of the iterative reconstruction algorithms, particularly with regard to changes in noise texture.
- •
 Compared to iterative reconstruction algorithms\, deep-learning image reconstruction algorithms reduce noise magnitude and improve lesion detectability while maintaining, or even improving, noise texture and spatial resolution.
- •
 The emergence and development of new deep-learning image reconstruction algorithms opens up many possibilities for optimizing CT protocols and improving radiological care for patients.

- [Next article in issue](https://www.sciencedirect.com/science/article/pii/S2211568426000070)

## Keywords

Deep-learning image reconstruction algorithm

Iterative reconstruction algorithm

Multidetector computed tomography

Phantom studies

Task-based image quality assessment

## Abbreviations

C-CT

Canon Medical Systems CT system

CT

Computed tomography

CTDI <sub>vol</sub>

Volume CT dose index

CNN

Convolutional neural network

*d* '

Detectability index

DLR

Deep-learning image reconstruction algorithm

G-CT

General Electric Healthcare CT system

HU

Hounsfield unit

IR

Iterative reconstruction

NPS

Noise power spectrum

P-CT

Philips Healthcare CT system

ROI

Region of interest

TTF

Task-based transfer function

U-CT

United Imaging Healthcare CT system

## 1\. Introduction

In recent years, several developments have been made to improve the quality of CT-reconstructed images. For several years now, iterative reconstruction (IR) algorithms, hybrid or model-based IR have been replacing image reconstruction using analytical methods such as filtered back projection \[\]. These IR algorithms have made it possible to greatly reduce image noise and, conversely, reduce the radiation dose whilst maintaining suitable image quality for diagnosis \[\]. Low-dose and ultra-low-dose CT acquisitions have thus been developed for many clinical applications with high spontaneous contrast such as bone fracture detection or chest pain in the emergency room \[\]. However, these algorithms have limitations in that they modify the image texture by introducing smoothing, blurring, or coarse granularity, which may interfere with the radiologists' interpretation, particularly for low spontaneous contrast tissues such as those present on abdominal CT images \[,,\].

To compensate for the limitations of these IR algorithms, reconstruction algorithms based on deep learning (DLR) have been developed \[,,\]. These DLR algorithms consist of deep neural networks \[,\] or convolutional neural networks (CNNs) \[\] trained with high-quality datasets. In theory, these algorithms make it possible to differentiate signal-to-image noise in order to reduce image noise without altering the image texture \[\]. Furthermore\, depending on the type of dataset used to train deep neural networks or CNNs, the impact of these DLR algorithms on image texture may vary according to the DLR algorithm used and its level \[,,,, \]. In addition, the non-linear properties of IR algorithms, namely, the dependence of spatial resolution on contrast and image noise (radiation dose), are also found in certain DLR algorithms \[,,,, \]. Nevertheless, many clinical studies have shown an improvement in the diagnostic quality of abdominal CT images and a great potential for dose reduction with these DLR algorithms \[,,,,,,, \]. Preclinical studies on phantoms have also compared the performance of IR and DLR algorithms developed, but mostly for a specific CT manufacturer \[,,,, \]. As far as we know, no studies have ever evaluated the impact of DLR algorithms compared to IR algorithms developed by the main CT manufacturers on noise magnitude, noise texture, spatial resolution, and lesion detectability under clinical conditions using an abdominal CT scanner.

The purpose of this study was to compare the performance on image quality of IR and DLR algorithms developed by four CT scanner manufacturers. To this end, a task-based image quality assessment was performed using an image quality phantom under abdominal CT scanning conditions.

## 2\. Materials and methods

### 2.1. CT systems

Four CT systems produced by four different manufacturers were used in this study: Aquilion Prime (Canon Medical Systems, further referred to as C-CT), Revolution CT (General Electric Healthcare, further referred to as G-CT), CT5300 (Philips Healthcare, further referred to as P-CT) and uCT 780 (United Imaging Healthcare, further referred to as U-CT). The presents the IR and DLR algorithms available and used in clinical practice on each CT system for abdomen-pelvis CT examinations.

Table 1. Acquisition and reconstruction parameters used with four CT systems.

<table><thead><tr><th colspan="2">CT system</th><th>C-CT</th><th>G-CT</th><th>P-CT</th><th>U-CT</th></tr></thead><tbody><tr><td colspan="2">Tube voltage (kV)</td><td>120</td><td>120</td><td>120</td><td>120</td></tr><tr><td colspan="2">Pitch factor</td><td>0.813</td><td>0.984</td><td>1</td><td>0.9875</td></tr><tr><td colspan="2">Rot time (s/rot)</td><td>0.5</td><td>0.5</td><td>0.5</td><td>0.5</td></tr><tr><td colspan="2">Beam collimation (mm)</td><td>80 × 0.5</td><td>64 × 0.625</td><td>64 × 0.625</td><td>80 × 0.5</td></tr><tr><td rowspan="3" colspan="2">CTDI <sub>vol</sub> (mGy) (exposure, mAs)</td><td>10.90 (340)</td><td>11.06 (325)</td><td>11.03 (272)</td><td>11.04 (257)</td></tr><tr><td>6.10 (190)</td><td>6.05 (175)</td><td>6.00 (148)</td><td>6.07 (141)</td></tr><tr><td>1.90 (60)</td><td>1.90 (55)</td><td>1.78 (44)</td><td>1.77 (40)</td></tr><tr><td rowspan="4">IR algorithm</td><td>Name</td><td>AIDR3D</td><td>Asir-V</td><td>iDose <sup>4</sup></td><td>Karl 3D</td></tr><tr><td>Type</td><td>Hybrid</td><td>Partial model-based</td><td>Hybrid</td><td>Hybrid</td></tr><tr><td>Kernel used</td><td>FC08</td><td>Standard</td><td>B</td><td>B_SOFT_E</td></tr><tr><td>Level used</td><td>Standard</td><td>50 %</td><td>4</td><td>5</td></tr><tr><td rowspan="5">DLR algorithm</td><td>Name</td><td>AiCE</td><td>TrueFidelity™</td><td>Precise Image</td><td>DELTA</td></tr><tr><td>Neural network</td><td>DNN</td><td>DNN</td><td>CNN</td><td>CNN</td></tr><tr><td>Datasets from</td><td>Patients<br>Model-based IR</td><td>Phantoms & patients<br>FBP</td><td>Patients<br>Similar to FBP</td><td>Patients<br>FBP</td></tr><tr><td>Kernel used</td><td>Body Sharp</td><td>Standard</td><td>Soft tissue</td><td>SHARP</td></tr><tr><td>Level used</td><td>Standard</td><td>Medium</td><td>Smooth</td><td>2</td></tr><tr><td colspan="2">Slice thickness / increment (mm)</td><td>1 / 1</td><td>1.25 / 1.25</td><td>1 / 1</td><td>1 / 1</td></tr></tbody></table>

C-CT indicates Canon Medical Systems CT scanner (Aquilion Prime); G-CT indicates General Electric Healthcare CT scanner (Revolution CT); P-CT indicates Philips Healthcare CT scanner (CT5300); U-CT indicates United Imaging Healthcare CT scanner (uCT 780).

CNN indicates convolutional neural network; CTDI <sub>vol</sub> indicates volume CT dose index; DNN indicates deep neural network; DLR indicates deep-learning image reconstruction algorithm; FBP indicates filtered back projection; IR indicates iterative reconstruction algorithm.

### 2.2. Phantoms

Acquisitions were made on the 31cm-diameter section of the Mercury v4.0 image quality phantom (Gammex). The phantom size approximates the average patient undergoing abdominal CT examination (water equivalent diameter of 29.9 cm and body mass index of 27 kg/m²). The homogeneous part of this section was used to compute the noise power spectrum (NPS) (**A**) and the part containing the five inserts to calculate the task-based transfer function (TTF) (**B**).

![Fig 1](https://ars.els-cdn.com/content/image/1-s2.0-S2211568426000033-gr1.jpg)

Download: Download high-res image (200KB)

### 2.2. Acquisition and reconstruction parameters

For all CT systems, acquisitions were performed with a tube voltage of 120 kVp, a rotation time of 0.5 s/rot and pitch factor close to 1. The tube current modulation systems were disabled and tube current values were set to obtain three volume CT dose indexes (CTDI <sub>vol</sub>) of 11, 6 and 1.8 mGy. The first dose level corresponds to the national target value for optimization for abdominal-pelvic CT scan, the second corresponds to the low-dose level, and the last corresponds to the ultra-low dose level. Ten acquisitions were made for each dose level on each CT system.

Raw data were reconstructed using the standard reconstruction parameters used for abdomen-pelvis CT acquisitions with IR and DLR algorithms. summarized the parameters used for each CT system in terms of IR/DLR algorithms, IR/DLR levels and kernels. Images were reconstructed with a field of view of 330 mm and slice thickness close to 1 mm (1-mm increment).

### 2.3. Task-based image quality assessment

A task-based image quality assessment was performed using iQMetrix-CT software v1.2 \[\]. For each dose level and each IR/DLR level, the NPS and TTF were computed on all the data from the 10 acquisitions.

#### 2.3.1. Noise power spectrum

The NPS was computed using eight square regions of interest (ROIs) of 112 × 112 pixels placed on 100 consecutive axial slices (10 slices for each of the 10 acquisitions) (**A**) as follows ():(1) $N P S_{2 D} \left(f_{x} , f_{y}\right) = \frac{\Delta_{x} \Delta_{y}}{L_{x} L_{y}} \frac{1}{N_{R O I}} \sum_{i = 1}^{N_{R O I}} \left|F F T_{2 D} \left\{R O I_{i} \left(x , y\right) - F I T_{i} \left(x , y\right)\right\}\right|^{2}$ where *Δ <sub>x</sub>* and *Δ <sub>y</sub>* are the pixel size in the x- and y-directions, respectively; *FFT* is the fast Fourier transform; *L <sub>x</sub>* and *L <sub>y</sub>* are the lengths of the ROIs in the x- and y-directions; *N <sub>ROI</sub>* is the number of ROIs; $R O I_{i} \left(x , y\right)$ is the mean pixel value of a ROI measured at the position (x,y) and $F I T_{i} \left(x , y\right)$ is a second order polynomial fit of $R O I_{i} \left(x , y\right)$. The raw data NPS1D curves were fitted using an 11th order polynomial.

To assess noise magnitude, the square root of the area under the NPS2D curve was used and the average spatial frequency of the NPS1D curve, (f <sub>av</sub> \[\]) for the noise texture.

#### 2.3.2. Task-based transfer function

To assess the spatial resolution, the task-based transfer function (TTF) was computed using the circular edge technique \[\]. TTF was calculated on 100 consecutive axial slices (10 slices for each of the 10 acquisitions) on Solid Water® and on iodine at 10 mg/mL inserts (**B**). TTF values at 50 % (f <sub>50</sub>) were used to assess spatial resolution.

#### 2.3.3. Detectability index

The detectability indexes (*d* ’) of two clinical tasks were computed using a non-pre-whitening model observer with an eye filter according to the following equation () \[,\].(2) $wherein$u$and$v$are the spatial frequencies \in the x- and y-directions,$E$the eye filter that models the human visual system sensitivity \to different spatial frequencies, and$W \left(u , v\right)$the task function defined as ():(3)$W = \left|F F T_{2 D} \left\{h_{1} \left(x , y\right) - h_{0} \left(x , y\right)\right\}\right|$where$F F T$is the fast Fourier transform,$h_{1} \left(x , y\right)$and$h_{0} \left(x , y\right)$ are the object present and object absent hypotheses, respectively \[,,\].

Two 10 mm-diameter lesions were defined to represent the contrast of an unenhanced low-contrast task (*e.g*., non-vascular lesion or hematoma) and a contrast-enhanced high-contrast task (*e.g*., enhanced vascular or strongly enhanced parenchymal structure) \[,\]. The TTF outcomes of the Solid Water® insert and a contrast of 85 Hounsfield units (HU) were used for the first task and the outcomes of the iodine insert and a contrast of 350 HU for the second.

The shape signal was circular and the contrast profile was Gaussian for the two simulated lesions \[,\]. The interpretation conditions for calculating all *d* ’ indexes were a 180-mm display size, a 500-mm viewing distance, and the Eckstein visual function \[\].

### 2.3. Statistical analysis

Quantitative variables are expressed as means ± SDs \[\]. For each metric (noise magnitude, f <sub>av</sub>, f <sub>50</sub> and *d* ’ values), the relative difference between DLR and IR algorithms for a specific dose level ($D i$) was computed as follows ():(4) $M e a n d i f f e r e n c e \left(\%\right) = \frac{M e t r i c_{D L R , D i} - M e t r i c_{I R , D i}}{M e t r i c_{I R , D i}} \times 100$

For all dose levels, the mean relative difference and its respective SD was also computed.

## 3\. Results

### 3.1. Noise power spectrum

#### 3.1.1. Noise magnitude

For all CT systems, the noise magnitude decreased as the dose level increased for both IR/DLR algorithms and was lower with DLR than with IR at all dose levels ().

Table 2. Noise magnitude and average noise power spectrum spatial frequency (f <sub>av</sub>) obtained for all dose levels (CTDI <sub>vol</sub>) with the four CT systems.

<table><thead><tr><th>Variables</th><th>CTDI <sub>vol</sub> (mGy)</th><th>Algorithms</th><th>C-CT</th><th>G-CT</th><th>P-CT</th><th>U-CT</th></tr></thead><tbody><tr><td rowspan="9">Noise<br>magnitude<br>(HU)</td><td rowspan="3">1.8</td><td>IR</td><td>18.1</td><td>24.0</td><td>46.6</td><td>60.3</td></tr><tr><td>DLR</td><td>10.2</td><td>18.6</td><td>24.0</td><td>9.7</td></tr><tr><td>Relative difference (%)</td><td>−43.8</td><td>−22.7</td><td>−48.5</td><td>−83.8</td></tr><tr><td rowspan="3">6.0</td><td>IR</td><td>16.4</td><td>17.4</td><td>26.4</td><td>32.3</td></tr><tr><td>DLR</td><td>10.1</td><td>13.7</td><td>13.6</td><td>9.7</td></tr><tr><td>Relative difference (%)</td><td>−38.3</td><td>−20.9</td><td>−48.5</td><td>−70.0</td></tr><tr><td rowspan="3">11.0</td><td>IR</td><td>14.5</td><td>13.5</td><td>19.5</td><td>24.0</td></tr><tr><td>DLR</td><td>10.2</td><td>10.8</td><td>10.1</td><td>9.7</td></tr><tr><td>Relative difference (%)</td><td>−29.9</td><td>−19.8</td><td>−48.3</td><td>−59.7</td></tr><tr><td rowspan="9">f <sub>av</sub><br>(mm <sup>-1</sup>)</td><td rowspan="3">1.8</td><td>IR</td><td>0.179</td><td>0.214</td><td>0.268</td><td>0.359</td></tr><tr><td>DLR</td><td>0.187</td><td>0.242</td><td>0.286</td><td>0.348</td></tr><tr><td>Relative difference (%)</td><td>4.5</td><td>13.1</td><td>6.7</td><td>−3.1</td></tr><tr><td rowspan="3">6.0</td><td>IR</td><td>0.219</td><td>0.252</td><td>0.273</td><td>0.358</td></tr><tr><td>DLR</td><td>0.264</td><td>0.261</td><td>0.291</td><td>0.349</td></tr><tr><td>Relative difference (%)</td><td>20.5</td><td>3.6</td><td>6.6</td><td>−2.5</td></tr><tr><td rowspan="3">11.0</td><td>IR</td><td>0.234</td><td>0.259</td><td>0.273</td><td>0.358</td></tr><tr><td>DLR</td><td>0.300</td><td>0.264</td><td>0.291</td><td>0.362</td></tr><tr><td>Relative difference (%)</td><td>28.2</td><td>1.9</td><td>6.6</td><td>1.1</td></tr></tbody></table>

C-CT indicates Canon Medical Systems CT scanner (Aquilion Prime); G-CT indicates General Electric Healthcare CT scanner (Revolution CT); P-CT indicates Philips Healthcare CT scanner (CT5300); U-CT indicates United Imaging Healthcare CT scanner (uCT 780).

CTDI <sub>vol</sub> indicates volume CT dose index; DLR indicates deep-learning image reconstruction algorithm; IR indicates iterative reconstruction algorithm.

The reductions in noise magnitude between DLR and IR were similar regardless of the dose level for G-CT (−21.1 ± 1.5 \[SD\] %) and P-CT (−48.4 ± 0.1 \[SD\] %). For U-CT and C-CT, the reductions in noise magnitude between DLR and IR were more pronounced at 1.8 mGy (−43.8 % and −83.8 %, respectively) and decreased as the dose level increased (−29.9 % and −59.7 % at 11 mGy, respectively).

For DLR algorithms, the lowest noise magnitude values were found for C-CT and U-CT at 1.8 and 6 mGy but were similar for all four systems at 11 mGy (10.3 ± 0.5 \[SD\] HU).

#### 3.1.2. Noise texture

shows the normalized NPS curves obtained for the two algorithms and all dose levels for the four CT systems. A peak at low spatial frequencies was found on the NPS curves for all the DLR algorithms. This NPS peak had a low amplitude compared to the second NPS peak for all CT systems, except for U-CT at 1.8 and 6 mGy and G-CT at 1.8 mGy.

![Fig 2](https://ars.els-cdn.com/content/image/1-s2.0-S2211568426000033-gr2.jpg)

Download: Download high-res image (501KB)

For U-CT, the f <sub>av</sub> values were similar at all dose levels for each algorithm and between algorithms at each dose level (IR: 0.358 ± 0.001 \[SD\] mm <sup>-1</sup>, and DLR: 0.353 ± 0.008 \[SD\] mm <sup>-1</sup>). For P-CT, the f <sub>av</sub> values were similar depending on the dose (IR: 0.271 ± 0.003 \[SD\] mm <sup>-1</sup>, and DLR: 0.289 ± 0.003 \[SD\] mm <sup>-1</sup>) and f <sub>av</sub> values were greater by 6.6 ± 0.1 \[SD\] % on average with DRL compared to IR. For G-CT and C-CT, f <sub>av</sub> values increased as the dose level increased for both algorithms. The differences between IR and DLR were weak for G-CT and decreased as the dose level increased (13.1 % at 1.8 mGy, and 1.9 % at 11 mGy). For C-CT, the opposite was found and the differences were more pronounced (4.5 % at 1.8 mGy, and 28.2 % at 11 mGy).

For DLR algorithms and at all dose levels, the greatest f <sub>av</sub> values were found for U-CT ().

![Fig 3](https://ars.els-cdn.com/content/image/1-s2.0-S2211568426000033-gr3.jpg)

Download: Download high-res image (614KB)

### 3.2. Task-based transfer function

For both inserts, the f <sub>50</sub> values decreased between 11 and 1.8 mGy by −35.9 ± 1.2 (SD) % on average with IR, and −42.6 ± 0.5 (SD) % with DLR for C-CT, and by −27.7 ± 1.2 (SD) % and −39.4 ± 14.7 (SD) % for G-CT, respectively ( and ). For the Solid Water <sup>ࣨ</sup> insert, the f <sub>50</sub> values decreased between 11 and 1.8 mGy by −19.9 % for IR and −35.0 % for DLR with P-CT and by −10.6 % and −24.2 % with U-CT, respectively. For the iodine insert, similar f <sub>50</sub> values were found at all dose levels for IR and DLR for P-CT (0.286 ± 0.007 \[SD\] mm <sup>-1</sup>, and 0.361 ± 0.008 \[SD\] mm <sup>-1</sup>) and U-CT (0.419 ± 0.006 \[SD\] mm <sup>-1</sup>, and 0.465 ± 0.023 \[SD\] mm <sup>-1</sup>) ().

Table 3. Values of task-based transfer function at fifty percent (f <sub>50</sub>) for Solid Water® and iodine at 10 mg/mL inserts obtained for all dose levels (CTDI <sub>vol</sub>) with the four CT systems.

<table><thead><tr><th>Variables</th><th>CTDI <sub>vol</sub> (mGy)</th><th>Algorithms</th><th>C-CT</th><th>G-CT</th><th>P-CT</th><th>U-CT</th></tr></thead><tbody><tr><td rowspan="9">f <sub>50</sub><br>(mm <sup>-1</sup>)<br>Solid<br>Water®</td><td rowspan="3">1.8</td><td>IR</td><td>0.224</td><td>0.223</td><td>0.213</td><td>0.313</td></tr><tr><td>DLR</td><td>0.203</td><td>0.282</td><td>0.227</td><td>0.332</td></tr><tr><td>Relative difference (%)</td><td>−9.4</td><td>26.5</td><td>6.6</td><td>6.1</td></tr><tr><td rowspan="3">6.0</td><td>IR</td><td>0.302</td><td>0.277</td><td>0.255</td><td>0.337</td></tr><tr><td>DLR</td><td>0.285</td><td>0.384</td><td>0.316</td><td>0.376</td></tr><tr><td>Relative difference (%)</td><td>−5.6</td><td>38.6</td><td>23.9</td><td>11.6</td></tr><tr><td rowspan="3">11.0</td><td>IR</td><td>0.354</td><td>0.312</td><td>0.266</td><td>0.350</td></tr><tr><td>DLR</td><td>0.356</td><td>0.397</td><td>0.349</td><td>0.438</td></tr><tr><td>Relative difference (%)</td><td>0.6</td><td>27.2</td><td>31.2</td><td>25.1</td></tr><tr><td rowspan="9">f <sub>50</sub><br>(mm <sup>-1</sup>)<br>Iodine<br>insert</td><td rowspan="3">1.8</td><td>IR</td><td>0.261</td><td>0.275</td><td>0.278</td><td>0.412</td></tr><tr><td>DLR</td><td>0.293</td><td>0.293</td><td>0.352</td><td>0.439</td></tr><tr><td>Relative difference (%)</td><td>12.3</td><td>6.5</td><td>26.6</td><td>6.6</td></tr><tr><td rowspan="3">6.0</td><td>IR</td><td>0.357</td><td>0.351</td><td>0.289</td><td>0.420</td></tr><tr><td>DLR</td><td>0.390</td><td>0.434</td><td>0.365</td><td>0.474</td></tr><tr><td>Relative difference (%)</td><td>9.2</td><td>23.6</td><td>26.3</td><td>12.9</td></tr><tr><td rowspan="3">11.0</td><td>IR</td><td>0.402</td><td>0.376</td><td>0.292</td><td>0.424</td></tr><tr><td>DLR</td><td>0.507</td><td>0.583</td><td>0.367</td><td>0.482</td></tr><tr><td>Relative difference (%)</td><td>26.1</td><td>55.1</td><td>25.7</td><td>13.7</td></tr></tbody></table>

C-CT indicates Canon Medical Systems CT scanner (Aquilion Prime); G-CT indicates General Electric Healthcare CT scanner (Revolution CT); P-CT indicates Philips Healthcare CT scanner (CT5300); U-CT indicates United Imaging Healthcare CT scanner (uCT 780).

CTDIvol indicates volume CT dose index; DLR indicates deep-learning image reconstruction algorithm; IR indicates iterative reconstruction algorithm.

![Fig 4](https://ars.els-cdn.com/content/image/1-s2.0-S2211568426000033-gr4.jpg)

Download: Download high-res image (807KB)

Table 4. Values of detectability index (*d’*) of the unenhanced low-contrast task (10 mm and 85 HU) and the contrast-enhanced high-contrast task (350 HU) obtained for all dose levels (CTDI <sub>vol</sub>) with the four CT systems.

<table><thead><tr><th>Variables</th><th>CTDI <sub>vol</sub> (mGy)</th><th>Algorithms</th><th>C-CT</th><th>G-CT</th><th>P-CT</th><th>U-CT</th></tr></thead><tbody><tr><td rowspan="9"><em>d'</em><br>10 mm<br>85 HU</td><td rowspan="3">1.8</td><td>IR</td><td>2.15</td><td>1.73</td><td>0.90</td><td>0.86</td></tr><tr><td>DLR</td><td>3.78</td><td>2.45</td><td>1.84</td><td>5.53</td></tr><tr><td>Relative difference (%)</td><td>75.4</td><td>41.6</td><td>103.7</td><td>544.3</td></tr><tr><td rowspan="3">6.0</td><td>IR</td><td>2.61</td><td>2.59</td><td>1.65</td><td>1.58</td></tr><tr><td>DLR</td><td>4.68</td><td>3.54</td><td>3.57</td><td>5.60</td></tr><tr><td>Relative difference (%)</td><td>78.9</td><td>36.6</td><td>115.7</td><td>253.6</td></tr><tr><td rowspan="3">11.0</td><td>IR</td><td>3.13</td><td>3.47</td><td>2.27</td><td>2.17</td></tr><tr><td>DLR</td><td>5.23</td><td>4.52</td><td>4.91</td><td>5.68</td></tr><tr><td>Relative difference (%)</td><td>67.1</td><td>30.3</td><td>116.4</td><td>161.8</td></tr><tr><td rowspan="9"><em>d'</em><br>10 mm<br>350 HU</td><td rowspan="3">1.8</td><td>IR</td><td>9.78</td><td>7.80</td><td>3.96</td><td>3.61</td></tr><tr><td>DLR</td><td>18.70</td><td>10.20</td><td>8.49</td><td>23.36</td></tr><tr><td>Relative difference (%)</td><td>91.2</td><td>30.8</td><td>114.6</td><td>546.6</td></tr><tr><td rowspan="3">6.0</td><td>IR</td><td>11.58</td><td>11.49</td><td>7.07</td><td>6.75</td></tr><tr><td>DLR</td><td>21.08</td><td>15.72</td><td>15.10</td><td>23.49</td></tr><tr><td>Relative difference (%)</td><td>82.0</td><td>36.8</td><td>113.6</td><td>248.2</td></tr><tr><td rowspan="3">11.0</td><td>IR</td><td>13.49</td><td>15.02</td><td>9.61</td><td>9.12</td></tr><tr><td>DLR</td><td>22.94</td><td>18.96</td><td>20.38</td><td>23.56</td></tr><tr><td>Relative difference (%)</td><td>70.1</td><td>26.2</td><td>112.2</td><td>158.3</td></tr></tbody></table>

C-CT indicates Canon Medical Systems CT scanner (Aquilion Prime); G-CT indicates General Electric Healthcare CT scanner (Revolution CT); P-CT indicates Philips Healthcare CT scanner (CT5300); U-CT indicates United Imaging Healthcare CT scanner (uCT 780).

CTDIvol indicates volume CT dose index; DLR indicates deep-learning image reconstruction algorithm; IR indicates iterative reconstruction algorithm.

For the Solid Water <sup>ࣨ</sup> insert and all CT systems, the f <sub>50</sub> values were greater with DLR than with IR at all dose levels except for C-CT, for which the opposite was found at 1.8 and 6 mGy (**A** - **D** and ). For P-CT and U-CT, the differences in f <sub>50</sub> values between DLR and IR increased as the dose level increased. For DLR, the highest f <sub>50</sub> values were found for U-CT and G-CT at all dose levels.

![Fig 5](https://ars.els-cdn.com/content/image/1-s2.0-S2211568426000033-gr5.jpg)

Download: Download high-res image (598KB)

For the iodine insert, the f <sub>50</sub> values were greater with DLR than with IR at all dose levels and for all CT systems (E-H and ). At each dose level, similar improvements in f <sub>50</sub> values with DLR compared to IR were found for P-CT (26.2 ± 0.5 \[SD\] %). For C-CT, G-CT and U-CT, with DLR, the improvement in f <sub>50</sub> values compared to IR increased as the dose level increased. For DLR, the highest f <sub>50</sub> values were found with U-CT at 1.8 and 6 mGy and with G-CT at 11 mGy.

### 3.3. Detectability index

For all CT systems and both simulated lesions, the d’ values increased as the dose level increased (). For both simulated lesions and all dose levels, d’ values were greater on average with DLR than with IR by 77.5 ± 8.7 (SD) % for C-CT, 33.7 ± 5.6 (SD) % for G-CT and 112.7 ± 4.7 (SD) % for P-CT. For U-CT and both simulated lesions, *d* ’ values were 6.5 ± 0.03 (SD) times greater with DLR than with IR at 1.8 mGy, 3.5 ± 0.05 (SD) at 6 mGy and 2.6 ± 0.02 (SD) at 11 mGy.

![Fig 6](https://ars.els-cdn.com/content/image/1-s2.0-S2211568426000033-gr6.jpg)

Download: Download high-res image (253KB)

## 4\. Discussion

In the present study, the image quality performance of four DLR algorithms was compared with that obtained via their respective IR algorithms developed by four CT scanner manufacturers. A task-based image quality assessment was performed using an image quality phantom under abdominal CT examination conditions to accomplish this. DLR algorithms reduced image noise and improved the detectability of simulated abdominal lesions while maintaining similar or better noise texture compared to IR algorithms. Unlike IR algorithms, the impact of DLR algorithms on spatial resolution depends on the CT unit, the contrast of the insert, and the dose level.

The NPS results show that, regardless of the CT system and dose level used, noise magnitude values were lower with DLR algorithms than with IR algorithms. Noise magnitude reductions with DLR were independent of dose level for G-CT and P-CT. In terms of noise texture, the NPS curves shifted towards higher frequencies with DLR compared to IR for all CT systems, except for U-CT algorithms, whose NPS curves were located at the same spatial frequencies with both algorithms. Furthermore, for this DLR algorithm, a second NPS peak at low spatial frequencies was found on the NPS curves. This peak was also found on some NPS curves with DLR from other CT manufacturers, but with a lower magnitude. This might be related to the fact that these reconstruction algorithms reduce noise more significantly at higher frequencies, causing the noise at lower frequencies to become dominant in the residual noise. In addition, we found that the f <sub>av</sub> values were not influenced by dose levels for the DLR algorithms of P-CT and U-CT, whereas they varied slightly according to dose level for the DLR algorithms of C-CT and G-CT. In clinical routine, these combined results on noise magnitude and noise texture translate into less noisy DLR images with finer granularity than images produced with IR. Furthermore, the noise magnitude and f <sub>av</sub> results obtained in this study are consistent with the results published in several phantom studies using the DLR algorithms of C-CT, G-CT and P-CT \[,,,,,, \]. Finally, we found that the lowest noise magnitude values were found in the C-CT and U-CT DLR algorithms at 1.8 and 6 mGy, but that similar noise magnitude values were found for all DLR algorithms at 11 mGy. In addition, the highest f <sub>av</sub> values were found with the DLR algorithm of U-CT at all dose levels.

The TTF results demonstrate the more or less pronounced non-linear properties of the IR and DLR algorithms used. For each IR or DLR algorithm, the f <sub>50</sub> values were greater with the high-contrast insert than with the low-contrast insert. In addition, for both algorithms, the TTF curves shifted towards lower frequencies as the dose level decreased, resulting in a loss of spatial resolution. Furthermore, it should be noted that variations in TTF curves with the DLR algorithms of P-CT and U-CT IR were very weak for the high-contrast iodine insert. In all cases, we found that, for the two inserts studied, the f <sub>50</sub> values were better with DLR than with IR, with the exception of C-CT DLR algorithm for the low-contrast insert. Variations in spatial resolution according to dose level, insert contrast and algorithms, were visually apparent in the images of the inserts used in this study. Similar results on DLR algorithms depending on contrast and dose level, as well as their performance compared to IR algorithms, have been published in studies on the DLR algorithms of C-CT \[,\], P-CT \[,\], and G-CT \[,,\]. Finally, we found that the highest f <sub>50</sub> values were globally obtained with the DLR algorithms of U-CT and G-CT for both low- and high-contrast inserts.

The detectability index results for the two simulated abdominal lesions were greater with DLR algorithms than with IR for all CT systems and at all dose levels. The same trends were found in studies published on the DLR algorithms of C-CT, G-CT and P-CT \[,,,,,, \]. The improvement in d’ values with DLR algorithms compared to IR algorithms was directly related to the NPS and TTF results obtained and, therefore, on the performance of the IR algorithms used for comparison. The lowest variations in *d* ’ values were found between IR and DLR algorithms of G-CT, and the highest between IR and DLR algorithms of U-CT. For the former, variations in noise magnitude were lowest between the two algorithms whereas, for the latter, they were the highest. For G-CT, the slight differences in d’ values between IR and DLR may also be explained by the use of a partial model-based IR algorithm, which performs better than the hybrid IR algorithm used for other CT systems. Also, these differences might be explained by the different kernels used in the IR and DLR algorithms, particularly for U-CT, P-CT and C-CT (similar "Standard" kernel for IR/DLR algorithms of G-CT). Although the kernels used are advertised by the manufacturer as guaranteeing similar performances in terms of noise and spatial resolution, they may have different characteristics that might impact the NPS and TTF results and, therefore, the *d* ' values. Finally, these differences might also be related to the datasets used to train the CNNs and DDNs of the DLR algorithms used. Depending on the DLR algorithm, these datasets come from patients and/or phantoms reconstructed with different algorithms (filtered back projection or IR algorithms). In all cases, the results obtained in this study confirm that using DLR algorithms, rather than IR algorithms, generally produced images with less image noise, less image smoothing/blurring and higher spatial resolution, thus increasing the detectability of lesions. Several clinical studies have already demonstrated the impact of these DLR algorithms on improving patient care for abdominal and pelvic CT examinations by increasing the diagnostic quality of images whilst reducing the radiation dose \[,,,,,,, \]. Improving the quality of abdominal CT images with these algorithms may pave the way for ultra-low dose acquisitions which, so far, have been limited by the performance of IR algorithms, particularly for differentiating low-contrast abdominal structures.

This study has some limitations. First, the acquisitions were made on only one static phantom, and this phantom does not take into account the various morphologies of patients undergoing abdominal CT examinations. Besides, the inserts used to simulate lesions in the phantom do not represent exactly the same features as the anatomical structures of patients. Second, only one quantitative standard reconstruction kernel and one single IR/DLR level were used. Although the parameters chosen correspond to those routinely used in clinical practice on the CT scanners studied, other parameters may have yielded different outcomes in terms of noise texture and spatial resolution. Third, most of these CT manufacturers have developed other DLR algorithms (new versions or new algorithms) that could produce different results and lead to a future update of the results presented here. Finally, no statistical analysis was performed as only one calculation of NPS, TTF per insert, and *d* ’ value per simulated lesion was made per dose level and per type of reconstruction.

In conclusion, we were able to confirm that using DLR algorithms, rather than IR algorithms, reduces the noise magnitude and improves lesion detectability while maintaining, or even improving, image texture and spatial resolution. The impact of each DLR algorithm on image quality improvement depends on the characteristics and performance of the IR algorithm used for the comparison and the version of the DLR algorithms used. The emergence and development of these new DLR algorithms opens up many possibilities for optimizing CT protocols to improve radiological care for patients.

## Human and animal rights

Not applicable for phantom studies.

The authors declare that the work described has not involved experimentation on humans or animals.

## Informed consent and patient details

Not applicable for phantom studies.

The authors declare that the work described does not involve patients or volunteers.

## Funding

This work did not receive any grant from funding agencies in the public, commercial, or not-for-profit sectors.

## CRediT authorship contribution statement

**Joël Greffier:** Conceptualization, Data curation, Formal analysis, Investigation, Methodology, Software, Supervision, Validation, Writing – original draft, Writing – review & editing. **Alexa Liogier:** Formal analysis, Investigation, Methodology, Software, Writing – original draft, Writing – review & editing. **Maxime Pastor:** Writing – original draft, Writing – review & editing. **Fabien de Oliveira:** Writing – original draft, Writing – review & editing. **Quentin Chaine:** Writing – original draft, Writing – review & editing. **Skander Sammoud:** Writing – original draft, Writing – review & editing. **Jean Paul Beregi:** Project administration, Resources, Supervision, Writing – original draft, Writing – review & editing. **Djamel Dabli:** Conceptualization, Data curation, Investigation, Methodology, Writing – original draft, Writing – review & editing.

## Declaration of competing interest

The authors declare that they have no known competing financial or personal relationships that could be viewed as influencing the work reported in this paper.

## Acknowledgements

The authors wish to thank Teresa Sawyers for expert editorial assistance.

## References

- ### Artificial Intelligence for radiation protection in medical imaging and radiotherapy: A perspective from the AI Working Party of ICRP Committee 3
 2026, Physica Medica
 Show abstract
- ### Deep-learning reconstruction in computed tomography: Cosmetic improvements should be backed by clinical evidence
 2026, Diagnostic and Interventional Imaging
- ### Quantitative CT biomarkers for predicting clinical outcomes after prostatic artery embolization: Results of the prospective pilot EMBOPERF study
 2026, Diagnostic and Interventional Imaging
 Show abstract
- ### Ultra-low dose chest-abdomen-pelvis CT with deep-learning image reconstruction for cancer follow-up: Impact on image quality and lesion detection
 2026, Diagnostic and Interventional Imaging
 Show abstract