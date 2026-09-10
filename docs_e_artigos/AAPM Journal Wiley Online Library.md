---
title: "AAPM Journal | Wiley Online Library"
source: "https://aapm.onlinelibrary.wiley.com/doi/10.1002/mp.13763"
author:
  - "[[Ehsan Samei]]"
  - "[[Donovan Bakalyar]]"
  - "[[Kirsten L Boedeker|Kirsten L. Boedeker]]"
  - "[[Samuel Brady]]"
  - "[[Jiahua Fan]]"
  - "[[Shuai Leng]]"
  - "[[Kyle J. Myers]]"
  - "[[Lucretiu M Popescu|Lucretiu M. Popescu]]"
  - "[[Juan Carlos Ramirez Giraldo]]"
  - "[[Frank Ranallo]]"
  - "[[Justin Solomon]]"
  - "[[Jay Vaishnav]]"
  - "[[Jia Wang]]"
published:
created: 2026-08-23
description: "BackgroundThe rapid development and complexity of new x-ray computed tomography (CT) technologies and the need for evidence-based optimization of image quality with respect to radiation and contras..."
tags:
  - "clippings"
---
[PDF](https://aapm.onlinelibrary.wiley.com/doi/epdf/10.1002/mp.13763 "ePDF")

## Abstract

### Background

The rapid development and complexity of new x-ray computed tomography (CT) technologies and the need for evidence-based optimization of image quality with respect to radiation and contrast media dose call for an updated approach towards CT performance evaluation.

### Aims

This report offers updated testing guidelines for testing CT systems with an enhanced focus on the operational performance including iterative reconstructions and automatic exposure control (AEC) techniques.

### Materials and Methods

The report was developed based on a comprehensive review of best methods and practices in the scientific literature. The detailed methods include the assessment of 1) CT noise (magnitude, texture, nonuniformity, inhomogeneity), 2) resolution (task transfer function under varying conditions and its scalar reflections), 3) task-based performance (detectability, estimability), and 4) AEC performance (spatial, noise, and mA concordance of attenuation and exposure modulation). The methods include varying reconstruction and tube current modulation conditions, standardized testing protocols, and standardized quantities and metrology to facilitate tracking, benchmarking, and quantitative comparisons.

### Results

The methods, implemented in cited publications, are robust to provide a representative reflection of CT system performance as used operationally in a clinical facility. The methods include recommendations for phantoms and phantom image analysis.

### Discussion

In line with the current professional trajectory of the field toward quantitation and operational engagement, the stated methods offer quantitation that is more predictive of clinical performance than specification-based approaches. They can pave the way to approach performance testing of new CT systems not only in terms of acceptance testing (i.e., verifying a device meets predefined specifications), but also system commissioning (i.e.\, determining how the system can be used most effectively in clinical practice).

### Conclusion

We offer a set of common testing procedures that can be utilized towards the optimal clinical utilization of CT imaging devices, benchmarking across varying systems and times, and a basis to develop future performance-based criteria for CT imaging.

## 1 Introduction

The rapid development and complexity of new x-ray computed tomography (CT) technologies, the increased utilization of CT, and the need for evidence-based optimization of image quality with respect to radiation and contrast media dose call for an updated approach to evaluating the performance of CT systems. In light of the availability and increasing clinical use of new CT technologies, it is particularly important to assess image quality using task-specific metrics that are more relevant to predicting the performance of a CT system and protocols for clinical imaging tasks.

A prevalent new CT technology uses statistical and iterative reconstruction (IR) algorithms to decrease image noise to facilitate use of decreased radiation dose levels. The nonlinear nature of these algorithms results in object-dependent resolution and noise performances. Thus, traditional image quality metrics, such as contrast-to-noise ratio, have become inadequate indicators of clinical imaging performance. While such traditional image quality indicators retain their relevance for evaluation of CT equipment technical performance, they fall short as surrogates of clinical performance, for either product evaluation or optimization purposes. Furthermore, automatic exposure control (AEC) techniques such as tube current modulation (TCM) have become ubiquitous in the clinical practice of CT. Methods are needed to characterize the performance of TCM techniques to better inform users as to how the system's radiation output is adapted to patient attributes.

AAPM TG233 report was recently completed, and this paper serves as a summary of the report. The report aims to supplement and complement existing and prior equipment performance testing guidelines (e.g., AAPM Report 74 [1](#mp13763-bib-0001)) by addressing the more advanced aspects of current CT systems, such as IR and TCM. The goal of this report is to briefly summarize current performance evaluation metrics and quality control (QC) tests, and introduce advanced performance assessment methods within a single document.[1](#mp13763-note-1001_note_0 "Link to note") Pass-fail criteria or performance guidelines are not provided for the results of these advanced assessment methods; there are no manufacturer specifications or regulatory or accreditation performance requirements available for these quantities. Rather, in line with the current professional trajectory of the field toward operational engagement, it is hoped that the assessment methods described in this report will be adopted by the clinical medical physicist for the purposes of protocol optimization, and for indicating clinical imaging performance in a way that can be compared between systems and imaging protocols. These important assessment methods also pave the way to approach performance testing of new CT systems not only in terms of acceptance testing (i.e., verifying a device meets predefined specifications), but also for system commissioning (i.e.\, determining how the system can be used most effectively in clinical practice).

The full report is organized into five main sections. Sections [1](#mp13763-sec-0002) and [2](#mp13763-sec-0003) provide a summary of established techniques for characterizing the basic performance of CT systems, appropriate for ensuring that the equipment meets manufacturer specifications, as well as regulatory and accreditation requirements. These tests include a pre-test inspection of the CT system to ensure regulatory and basic safety compliance (see full report Section [1](#mp13763-sec-0003)), geometric performance, radiation output performance, and basic image quality performance (see full report Section [2](#mp13763-sec-0003)). The main body of the report is Section [3](#mp13763-sec-0058) and is reproduced here. This section targets operational performance of a CT system and clinical protocols, with metrics that more directly reflect clinical performance. The report also includes a section (Section [4](#mp13763-sec-0059)) on the clinical utility and future extensions of the work, reproduced in full here. The full report further includes a supplemental section (section 5) encompassing a list of acronyms, list of phantoms, list of evaluation software (reproduced below as Section [4](#mp13763-sec-0059)), and comparative tabular summary of intrinsic CT testing methods.

The characterization of a medical imaging system is most meaningful to the extent that it is predictive of the clinical outcome (Fig. [1](#mp13763-fig-0001)). The premise of TG233 is that beyond technical conformance and specifications, physics evaluation of CT systems can be more readily related to the clinical outcome, and thus can serve as a more meaningful surrogate of CT performance in patient care tasks, hence the term operational performance.

![Details are in the caption following the image](https://aapm.onlinelibrary.wiley.com/cms/asset/009703bd-2686-4f8b-8269-9db8d33353c0/mp13763-fig-0001-m.jpg)

Figure 1 Open in figure viewer PowerPoint Components of computed tomography performance evaluation in the technology domain (mainly Section 2 of the report) and operational domain (mainly Section 3 of the full report, Section of this summary report).

Many of the quantities and their associated assessment methodologies detailed in the report reflect work done by the imaging research community. The hope and premise of the report is that these quantities can be used by clinical physicists to assess operational performance. To reach this goal, consistent specific definitions for these quantities must be established and tools must be made publicly available to make such measurements practical in a clinical environment. This report aims to address both of these obstacles so as to foster their clinical use as a way to make the physics characterizations of CT more scientifically informed and clinically relevant.

## 2 Operational Performance

The basic system characteristics (summarized in Sections [1](#mp13763-sec-0002) and [2](#mp13763-sec-0003) of the full TG233 report) reflect the intrinsic performance of a CT system. While those characteristics provide a first-order depiction of a system's functionality, they do not reflect a number of features and attributes of CT systems that affect the quality of patient images. In this report, such attributes are recognized under the heading of Operational Performance. Operational performance characterization of a CT system aims to provide a metrology more closely reflective of performance of the system in clinical imaging. Operational performance characterization should thus provide a stronger clinical basis by which to evaluate the system's performance, and supports further use of the measurements for optimizing the system for targeted image quality or dosimetric goals. Furthermore, this section describes several system characterization methodologies designed to assess important CT adaptive technologies that have been introduced to reduce radiation dose and optimize image quality (e.g., TCM or IR) for which established physics testing methods are not well suited to address.

The manner in which these characterization assessment methods could or should be applied in a clinical context is still emerging; adaptation of these methods, for example, for regulatory compliance or accreditation purposes, would require considerable additional effort before clinical adoption could be required. However, the ubiquity of newer CT technologies, such as TCM and IR, and their large impact on image quality, mandate that the clinical medical physicist be involved in their characterization, implementation, and optimization. Thus, this report aims to provide a common “toolset” that a clinical physicist can use for characterization and optimization purposes.

Pass/fail criteria are not provided for these testing methods as such data are not yet available based on peer performance or concordance with clinical outcome data. Further, such data are expected to be application- and radiologist-specific. The approach of this section is a departure from traditional conformance/specification based (i.e., pass-fail) physics testing. The idea is not to pass or fail a system based on these measurements, but rather to use these measurements to improve the understanding and utilization of the technology. The philosophy and metrology of operational performance aims to make the evaluation more reflective of clinical performance with the use of phantoms that offer greater variability, as would be expected in real patients (e.g., phantoms that reflect variations in patient size), and more technology-relevant methods (e.g., testing methods that accommodate potential system nonlinearities).

Table [^1] lists the quantitative metrics described in this report with the descriptions and mathematical definitions of each metric described in subsequent sections. The tests involved require imaging specific types of phantoms; some appropriate phantoms are suggested in this report. The imaging can be done using any protocol that the user may wish to evaluate. Typically, these tests should be performed under sample conditions of interest representative of the protocol and dose conditions used or to be used clinically (e.g., typical head and body protocols as common reflections of clinical operation). However, comparing tests conducted across different systems is possible if a common protocol is used. A set of suggested testing protocols are thus listed in Table [^2]. These protocols aim to provide an overall broad characterization of the system, in lieu of or in addition to any specific protocol(s) of interest that the user may wish to evaluate.

<table><thead><tr><th>Attribute</th><th>Section</th><th>Metric</th><th>Definition</th></tr></thead><tbody><tr><td rowspan="6">Tube current modulation</td><td rowspan="6"><a href="#mp13763-sec-0003">2</a>.A</td><td><i>g <sub>mA</sub></i></td><td>Functional dependence of tube current on water equivalent diameter for a given phantom</td></tr><tr><td><i>g <sub>n</sub></i></td><td>Functional dependence of noise on water equivalent diameter for a given phantom</td></tr><tr><td>α, <i>R <sub>A</sub></i></td><td>Exponent and the correlation coefficient of ln(mA) = α(<i>d <sub>w</sub></i>) + β relationship, for a given phantom</td></tr><tr><td>s, <i>R <sub>n</sub></i></td><td>Slope and the correlation coefficient of n = s(<i>d <sub>w</sub></i>) + t relationship, for a given phantom</td></tr><tr><td><i>C <sub>mA</sub>, C <sub>noise</sub></i></td><td>Spatial concordance, in mm, of the distance between a discontinuous change in thickness and the anticipated change in mA or noise</td></tr><tr><td><i>d <sub>min</sub></i>, <i>d <sub>max</sub></i></td><td>Diameters associated with mA of the system reaching its maximum or its minimum value</td></tr><tr><td rowspan="4">Spatial resolution</td><td rowspan="4"><a href="#mp13763-sec-0011">2</a>.B</td><td><i>TTF <sub>n,C</sub></i></td><td>Task Transfer Function (TTF) at defined measured noise and contrast level in the in-plane direction</td></tr><tr><td><i>zTTF <sub>n,C</sub></i></td><td>Task Transfer Function (TTF) at defined measured noise and contrast level in the z-direction (i.e., trans-axial direction)</td></tr><tr><td><i>f <sub>50</sub></i> and <i>f <sub>10</sub></i></td><td>Frequencies associated with 50% and 10% of in-plane TTF, respectively</td></tr><tr><td><i>zf <sub>50</sub></i> and <i>zf <sub>10</sub></i></td><td>Frequencies associated with 50% and 10% of z-direction TTF, respectively</td></tr><tr><td rowspan="5">Noise</td><td rowspan="5"><a href="#mp13763-sec-0023">2</a>.C</td><td><i>n</i></td><td>Noise magnitude (pixel standard deviation) at three dose levels</td></tr><tr><td><i>NPS <sub>n</sub></i></td><td>Noise power spectrum (NPS) at defined noise levels</td></tr><tr><td><i>f <sub>P</sub></i> and <i>f <sub>A</sub></i></td><td>Peak and average frequencies of the NPS</td></tr><tr><td><i>NUI</i></td><td>Noise nonuniformity index</td></tr><tr><td><i>η</i></td><td>Noise inhomogeneity index</td></tr><tr><td rowspan="2">Quasi-linear task-based performance</td><td rowspan="2"><a href="#mp13763-sec-0036">2</a>.D</td><td><i>d′</i></td><td>Detectability index for the detection of a target signal (e.g., 1, 5, and 10 mm circular signal having a specific contrast and contrast-profile) for a specific phantom size and noise or dose level</td></tr><tr><td><i>e′</i></td><td>Estimability index for estimating the volume of a target signal (e.g., 10 mm spherical signal having a specific contrast and contrast-profile) for a specific phantom size and noise or dose level</td></tr><tr><td rowspan="3">Spatial domain task-based performance</td><td rowspan="3"><a href="#mp13763-sec-0044">2</a>.E</td><td><i>LR</i></td><td>Localization success rate for identifying the presence of and location of a targeted signal</td></tr><tr><td><i>A <sub>LROC</sub></i></td><td>Area under the localization relative operating characteristic (LROC) curve for targeted localization tasks</td></tr><tr><td><i>A <sub>EFROC</sub></i></td><td>Area under the exponential transformed free response operating characteristic (EFROC) curve for targeted free-response detection tasks</td></tr></tbody></table>

<table><thead><tr><th>Nomenclature <a href="#mp13763-note-0001_23">a</a></th><th>CTDI (mGy) (32 cm phantom)</th><th>Tube potential (kV)</th><th>Tube current (mA)</th><th>Mode, pitch</th><th>Reconstruction</th></tr></thead><tbody><tr><td>TG233-F1</td><td>0.75</td><td rowspan="6">120</td><td rowspan="9">Fixed mA to achieve target CTDI ± 10%</td><td rowspan="6">Helical, ~1</td><td rowspan="13">FBP, IR at medium strength, higher than medium strength, and maximum strength settings “standard” kernel ~ 0.6 and 5 mm image thickness</td></tr><tr><td>TG233-F2</td><td>1.5</td></tr><tr><td>TG233-F3</td><td>3.0</td></tr><tr><td>TG233-F4</td><td>6.0</td></tr><tr><td>TG233-F5</td><td>12.0</td></tr><tr><td>TG233-F6</td><td>24.0</td></tr><tr><td>TG233-F3LK</td><td>3.0</td><td>70 (or 80)</td><td rowspan="3">Helical, ~1, unless a lower pitch is needed to achieve the CTDI</td></tr><tr><td>TG233-F3MK</td><td>3.0</td><td>100</td></tr><tr><td>TG233-F3HK</td><td>3.0</td><td>150 (or 140)</td></tr><tr><td>TG233-M2</td><td>1.5</td><td rowspan="3">120</td><td rowspan="3">TCM setting to achieve target CTDI ± 10%</td><td rowspan="3">Helical, ~1</td></tr><tr><td>TG233-M3</td><td>3.0</td></tr><tr><td>TG233-M4</td><td>6.0</td></tr><tr><td>TG233-M3-A</td><td>3.0</td><td>120</td><td>Same as above</td><td>Axial</td></tr></tbody></table>

- <sup><i>a</i></sup> F refers to fixed mA, M to tube current modulation (TCM), 1–6 to dose setting, and LK, MK, HK to low, medium, and high kV settings, respectively.

### 2.A Tube current modulation

#### 2.A.1 Objective

To characterize the tube current modulation (TCM) in terms of tube current and image noise as a function of attenuation. Two complementary tests are presented: One assesses how a CT system adapts the tube current to a discrete change in object attenuation and size, and the other how it does so in response to a continuous change.

#### 2.A.2 Important definitions

- – *Tube current*: It determines the number of electrons accelerated across the x-ray tube per unit time. It is expressed in units of milliAmperes (mA). The CT scanner radiation output, in terms of CTDI <sub>vol</sub>, is directly proportional to the tube current.
- – *Tube current modulation (TCM):* This scanner feature automatically adapts the x-ray tube current to the patient attenuation to achieve a specified level of image quality. Most modern CT systems can modulate the tube current in several directions (see angular and longitudinal modulation below) or synchronized with an ECG signal.
- – *Automatic exposure control (AEC):* Any system that automatically adapts the tube output (e.g., tube current, tube potential, etc.) according to the radiological properties of the patient. Technically, TCM is a specific implementation or type of AEC. However, in the literature, AEC and TCM are sometimes used synonymously.
- – *Angular modulation of the tube current (x–y modulation):* This TCM feature adapts the tube current as the x-ray tube rotates around the patient to compensate for attenuation changes at varying projection angles, attempting to control detector signal at different projection angles. The angular modulation usually uses one or two CT localizer radiographs (in some systems in combination with the detector signal from prior rotations) to estimate patient attenuation.
- – *Longitudinal modulation of the tube current (z-modulation):* This TCM feature adapts the tube current as patient attenuation changes in the longitudinal direction. The longitudinal modulation usually uses one or two CT localizer radiographs to estimate patient attenuation.

#### 2.A.3 Equipment

Various sets of phantoms can be used for this procedure\, depending on how complete of a characterization is sought. The *discrete adaptation test* utilizes a phantom of different fixed sizes (at least two) in the longitudinal direction. The *continuous adaptation test* uses a phantom with continuous changes in water-equivalent diameter in the longitudinal direction.[2](#mp13763-bib-0002) A phantom may also be used that includes a combination of both discrete and continuous changes in size.

#### 2.A.4 Procedures

The objective of this investigation is to assess how the CT system adapts the tube current as a function of object size with either discrete or continuous changes in attenuation under a fixed set of operating conditions.

For either test, start by defining a set of operating conditions according to scanner model and manufacturer for a routine adult body protocol using 120 kV. Scan in helical mode with pitch of ~1.0, and rotation time of 1 s (Table [^2], TG233-M2, M3, or M4). Alternatively use a sequential (axial) mode with rotation time of 1 s (Table [^2], TG233-M3-A). Use default TCM settings according to scanner model and manufacturer (i.e., noise index, standard deviation, quality reference mAs, etc.). Additional protocols may be used to ascertain the sizes at which the mA of the system maxes out to its highest value or bottoms down to its lowest, both of which can change as a function of the kV and the phantom size.

For the discrete adaptation test, scan at least two different-sized phantoms, each centered precisely, to assess the amount of tube current adaptation. Prior to each scan, perform one or two CT localizer radiographs covering the full range of the phantom, according to manufacturer recommendation (i.e., “AP” or “AP+lateral” directions). It is important to note that the order in which the CT localizer radiographs are obtained can affect the resulting TCM profile for certain systems. In such systems, often the final CT localizer radiograph is used for TCM prescription. Define a CT scan range that starts and ends at least half of the total collimation away from both edges of the phantom, otherwise the air boundary of the phantom will impact the results. Reconstruct the images using a standard body kernel. Reconstructing with thin slices (<1 mm) is preferred as it will provide a finely sampled mA profile, but at the cost of many more images to reconstruct, transfer, and process. Thus, thicker slices could be used but at the cost of potentially losing details in the extracted mA profile (see next section).

For the continuous adaptation test, use a phantom with continuously varied size or attenuation, position the phantom at isocenter and perform one or two CT localizer radiographs over the full range of the phantom, according to manufacturer recommendation (i.e. “AP” or “AP + lateral” directions). Define a CT scan range that starts and ends at least half of the total collimation away from both edges of the phantom. Reconstruct the images using a standard body kernel with an image thickness of 5 mm with an interval of 5 mm.

#### 2.A.5 Data analysis

For the discrete adaptation test use either the scan protocol page or the resulting images to record the mA (or mAs) and CTDI <sub>vol</sub> values of each of the CT scans performed with the different-sized phantoms (Fig. [2](#mp13763-fig-0002)). Note that mA or mAs per image is a scalar (often average) representation of the tube current, which can vary as a function of tube position. Also the CTDI <sub>vol</sub> can vary throughout the scan so the scanner reported value is also an averaged value. Trace a circular region of interest (ROI) at the center of the phantom and measure the standard deviation of the CT numbers. ROI should have a diameter of 1 cm or more. Repeat for three contiguous images near the center of the scan and report the average of the standard deviation for each of the phantom sizes.

![](https://aapm.onlinelibrary.wiley.com/cms/asset/8bec3ce1-b673-41b3-8cf2-b411148239f1/mp13763-fig-0002-m.jpg)

Figure 2 Open in figure viewer PowerPoint Example of size adaptation test of the tube current modulation (TCM). Images were acquired with a Siemens Definition AS64 scanner using adult body protocol, 120 kV, rotation time = 1 s, and pitch = 1.0. For this specific scanner and manufacturer, the TCM (CAREDose4D) was set with 210 quality reference mAs, with curves setting at “average.” Three CTDI phantoms of size 32, 16, and 10 cm were scanned independently using the same computed tomography (CT) technique described above. Prior to each CT scan, a CT localizer radiograph was acquired in the anteroposterior (AP) direction. The scan protocol page above shows the tube current values were adapted to 215, 43 and 23 mA for the 32, 16, and 10 cm CTDI phantoms, respectively. In Siemens CT systems, rather than reporting “mA” the system reports effective mAs, which is defined as the tube current time product divided by the pitch. Because rotation time and pitch were (conveniently) set to 1, in this special case, the effective mAs equals the mA values.

For the continuous adaptation test, the tube current values can be extracted from the DICOM header (tag 0018, 1151) of the CT images for each image position. These tube current values in a DICOM header typically represent the average tube current over all tube positions that contributed to that image. Trace a circular ROI (of at least 1 cm in diameter) at the center of the images and measure the standard deviation of the CT numbers. Report the overall average of the measured image noise as a function of phantom size. Figure [3](#mp13763-fig-0003) shows an example.

![](https://aapm.onlinelibrary.wiley.com/cms/asset/b0ae11e9-be55-4712-b6be-a707a89d17ef/mp13763-fig-0003-m.jpg)

Figure 3 Open in figure viewer PowerPoint Example of the continuous adaptation test of the tube current modulation (TCM) using a 32 cm CTDIvol phantom placed with one of the flat cross-sectional ends of the phantom on the table surface. (Left) Displays the anteroposterior (AP) CT localizer radiographs, with dotted lines in AP radiographs, indicating the computed tomography scan range. (Right) The tube current time product values (in units of mAs) are plotted as a function of z-axis position for the CTDI vol phantom. Data were collected with a single set of reference operating conditions using a Siemens Somatom Definition AS64 scanner using adult body protocol, 120 kV, rotation time of 1 s, and pitch of 1.0. The scanner-specific TCM (CAREDose4D) was set with 210 quality reference mAs with curves set to “average.” These data demonstrate that the TCM system adjusts the tube current continuously as the attenuation changes continuously.

For either test, with the size known at each position, apply a log-linear fit to mA versus phantom size, *d <sub>w</sub>* (water equivalent diameter), as ln(mA) = α(*d <sub>w</sub>*)+β and report the slope α and the linear correlation coefficient R *<sub>mA</sub>*. Apply a linear fit to the average of the measured standard deviation (n) versus phantom size (*d <sub>w</sub>*) as n = s(*d <sub>w</sub>*) + t, and report the slope s and the correlation coefficient R *<sub>n</sub>*. See Fig. [4](#mp13763-fig-0004) for an example. This analysis may also include ascertaining the sizes at which the mA of the system maxes out to its highest value or bottoms down to its lowest.

![](https://aapm.onlinelibrary.wiley.com/cms/asset/750fcb81-8927-4457-a498-aeee3883dba4/mp13763-fig-0004-m.jpg)

Figure 4 Open in figure viewer PowerPoint Example of the continuous adaptation test of the tube current modulation (TCM) using a tapered phantom (Mercury phantom, reconfigured for this test). (Left) Displays the anteroposterior (AP) computed tomography (CT) localizer radiographs, with dotted lines in AP radiographs, indicating the CT scan range. (Right) The tube current time product values (in units of mAs) are plotted as a function of size. Data were collected with a single set of reference operating conditions using a Siemens Somatom Definition AS64 scanner using adult body protocol, 120 kV, rotation time of 1 s, and pitch of 1.0. The scanner-specific TCM (CAREDose4D) was set with 210 quality reference mAs with curves set to “average.” These data demonstrate that the TCM system adjusts the tube current continuously as the attenuation changes continuously.

TG-233 recommends that size be described in terms of water-equivalent diameter. Water-equivalent diameter can be estimated using the methods described in AAPM report 220.[3](#mp13763-bib-0003) The analysis for the discrete adaptation test should further include Spatial Concordance (C <sub>mA</sub> or C <sub>noise</sub>, the distance between a discontinuous change in phantom size and the corresponding change in mA or noise, Fig. [5](#mp13763-fig-0005)).

![](https://aapm.onlinelibrary.wiley.com/cms/asset/c8f7e495-086a-4c04-9971-c158c77ec01c/mp13763-fig-0005-m.jpg)

Figure 5 Open in figure viewer PowerPoint Example of the spatial concordance, C, between a discontinuous change in phantom size and the corresponding change in mA (or noise). In this example, two CTDI phantoms were set up side-by-side and scanned using tube current modulation. The scout image from those scans is shown with the mA (red) and water-equivalent diameter (blue) shown for each slice position from the subsequent scans. The spatial concordance quantifies how “quickly” the CT system can adapt the tube current in concordance with an abrupt change in attenuation. In other words, it quantifies the lag between a change in attenuation, and the responsive change in tube current. A spatial concordance of zero would imply perfect adaption to changing patient size. It would be expected that wider x-ray beam collimation settings would correspond to a larger (i.e., poorer) spatial concordance. This example demonstrates the spatial concordance of mA, C mA. The spatial concordance of noise, C noise, could be measured in a similar fashion, substituting the mA profile for the slice-by-slice profile of measured noise. It may also be possible to estimate the spatial concordance using a continuously changing phantom; a comparison between different phantom types for doing this test has not yet been made.

#### 2.A.6 Precautions and caveats

Select a scan range “inside” the phantom in order to avoid imaging at edges along the z axis. As a rule of thumb, scan half a beam width inside of each edge of the phantom, as otherwise the air boundary of the phantom will impact the results. Note, however, that in some cases it may actually be of value to set the scan range over the ends of the phantom to observe the expected TCM behavior for very abrupt air-to-tissue interfaces (e.g., end of head or feet). For very large or very small phantoms, it is possible that no modulation occurs depending on the TCM settings. Note that the system mA maxing out to its highest value or bottoming down to its lowest can either be dictated by the system limitation, which can change as a function of the kV and the phantom size, or by the user protocol definition; some TCM implementations allow the user to select minimum and maximum settings and thus these settings may need to be adjusted in order to observe normal TCM behavior in such phantoms.

#### 2.A.7 Recommended performance metrics

- – Functional dependence of mA on water equivalent diameter, m *A(d <sub>w</sub>)*, for a given phantom
- – Functional dependence of noise on water equivalent diameter, *n(d <sub>w</sub>)*, for a given phantom
- – Slope α and the correlation coefficient (*R <sub>mA</sub>*) of ln(mA) = α(*d <sub>w</sub>*) + β relationship (g <sub>mA</sub>), for a given phantom
- – Slope s and the correlation coefficient (*R <sub>n</sub>*) of n = s(*d <sub>w</sub>*) + t relationship (g <sub>n</sub>), for a given phantom
- – Spatial concordance, *C*, (in mm) of mA and noise change with discontinuous changes in size, the distance between a discontinuous change in phantom size and the corresponding change in mA or noise (*C <sub>mA</sub>* and *C <sub>noise</sub>*)
- – Diameters associated with mA of the system reaching its maximum or its minimum value (*d <sub>min</sub>* and *d <sub>max</sub>*)

### 2.B Spatial resolution

#### 2.B.1 Objective

To characterize the in-plane and z-axis spatial resolution of the CT system under reference conditions and establish baseline values for specific imaging conditions with methods applicable to both linear and nonlinear reconstruction algorithms. Note that the methods in this section are suitable to assess the spatial resolution for low-contrast features. As noted below, the traditional methods to assess spatial resolution using high-contrast line-pair patterns (see Section [2.C](#mp13763-sec-0024) of full report) may not faithfully reflect the system's ability to resolve low-contrast features if nonlinear processing (e.g., iterative reconstruction) is used.

#### 2.B.2 Important definitions

- – *Point Spread Function (PSF):* the system output response to an input point object.
- – *Line Spread Function (LSF):* the system output response to an input line object.
- – *Edge Spread Function (ESF):* the system output response to an input edge (i.e., step) object.
- – *Modulation Transfer Function (MTF):* Fourier transform (magnitude) of the LSF (normalized by the DC component). The MTF is a metric of system resolution and describes the system contrast recovery as a function of spatial frequency. This formulation assumes a linear, shift-invariant (LSI) imaging system. Although a rigorous mathematical description of an LSI system is beyond the scope of this report, practically speaking, an LSI system is one whose output signal can be determined by convolving an input signal with the system's PSF, independent of the properties or location of the input (e.g., contrast, size, central vs. peripheral).
- – *Task Transfer Function (TTF):* the quasi-linear analog to the MTF. When the imaging system is known to behave nonlinearly (e.g., in the case of iterative reconstruction), a measured MTF may not represent the imaging system's response to an arbitrary input object (as would be the case for a truly linear system). In this scenario, the system resolution becomes dependent on the object contrast and background noise level.[4](#mp13763-bib-0004) Therefore, the MTF is not general but rather “task-specific” and is denoted as a TTF. A TTF is measured in identical fashion as an MTF. However, when reporting a TTF, the background noise (pixel standard deviation, SD), object's contrast, and object's radial location should be included. Denoting the MTF as the TTF emphasizes that the system resolution is influenced by those factors. This emphasis becomes important when computing task-based performance (see Section [2.D](#mp13763-sec-0037)) or when comparing resolution between different imaging systems or conditions. Traditionally, an MTF is measured using high-contrast objects while a TTF should be measured for objects of a contrast that represents the imaging task under study.

#### 2.B.3 Equipment

- – For in-plane spatial resolution, a phantom with circular insert rods of varying contrast such as the Mercury phantom or the CT ACR 464 phantom.
- – For z-axis spatial resolution, a phantom in which two sections of different materials interface to form an edge parallel to the axial plane (e.g., interface between modules 2 and 3 of the CT ACR 464 phantom).
- – Image analysis software capable of MTF calculations, see Section [4](#mp13763-sec-0059) below or section 5.C of the full report.

#### 2.B.4 Test procedures

#### In-plane resolution

Align the phantom on the scanner. Make sure the phantom rods are perpendicular to the image plane. Image the phantom under sample conditions of interest representative of the protocol and dose conditions used or planned clinically or protocols defined in Table [^2]. To achieve a reliable estimate of the TTF, the total effective CNR (CNR you would achieve from averaging all available images), ![urn:x-wiley:00942405:media:mp13763:mp13763-math-0001](https://aapm.onlinelibrary.wiley.com/cms/asset/ec5b5bf4-a8e8-466e-a8f6-fe58b78e3cf7/mp13763-math-0001.png), should be at least 15 according to Chen et al.[5](#mp13763-bib-0005) ![urn:x-wiley:00942405:media:mp13763:mp13763-math-0002](https://aapm.onlinelibrary.wiley.com/cms/asset/bf2074e7-267b-4fce-be49-077901adb397/mp13763-math-0002.png) can be computed as

![urn:x-wiley:00942405:media:mp13763:mp13763-math-0003](https://aapm.onlinelibrary.wiley.com/cms/asset/e37c4bb9-1dfe-4395-a28d-df3d6d52268d/mp13763-math-0003.png)

urn:x-wiley:00942405:media:mp13763:mp13763-math-0003

(1)

where ![urn:x-wiley:00942405:media:mp13763:mp13763-math-0004](https://aapm.onlinelibrary.wiley.com/cms/asset/b9ef0335-8a9f-4048-b3e9-3523c8828b13/mp13763-math-0004.png) is the CNR measured in an individual image, and ![urn:x-wiley:00942405:media:mp13763:mp13763-math-0005](https://aapm.onlinelibrary.wiley.com/cms/asset/85571600-f0ef-4aab-8943-9d1de7697c70/mp13763-math-0005.png) is the number of images in which the rod is visible. Alternatively, the number of images needed to achieve a ![urn:x-wiley:00942405:media:mp13763:mp13763-math-0006](https://aapm.onlinelibrary.wiley.com/cms/asset/da234236-76e2-4b7f-830a-f5e2734ff62e/mp13763-math-0006.png) of 15 can be computed as

![urn:x-wiley:00942405:media:mp13763:mp13763-math-0007](https://aapm.onlinelibrary.wiley.com/cms/asset/d49ca5bd-cd97-49e9-832e-b845a4a4deb9/mp13763-math-0007.png)

urn:x-wiley:00942405:media:mp13763:mp13763-math-0007

(2)

Acquire the necessary number of images to achieve this ![urn:x-wiley:00942405:media:mp13763:mp13763-math-0008](https://aapm.onlinelibrary.wiley.com/cms/asset/306e0f88-10a3-4754-8996-d1597908aaee/mp13763-math-0008.png) threshold. Note that this may involve repeated scans for low-contrast and low-dose conditions.

#### Z-axis resolution

Align the phantom such that the axial-plane interface is slightly angled (approximately 5°) with respect to the image plane. With the ACR phantom, this can be achieved by adjusting the screw in its support base. It is also possible to use the gantry tilt feature, if available. Image the phantom under all conditions of interest representative of the protocol and dose conditions used or planned clinically. Figure [6](#mp13763-fig-0006) illustrates this setup.

![](https://aapm.onlinelibrary.wiley.com/cms/asset/c89deadc-36b3-4939-86de-84538d196ba9/mp13763-fig-0006-m.jpg)

Figure 6 Open in figure viewer PowerPoint The technique for estimating both the in-plane and z-direction tube current modulation (TCM) from the CT ACR 464 phantom. The in-plane task transfer function is measured based on a circular region of interest (ROI) around one of the rods in module 1 (top left). From this ROI, it is possible to identify the center of the rod, and then calculate the distance of each pixel in the ROI from the center. The plot of HU values vs distance make up the edge spread function (ESF) (bottom left). The data points in the raw noisy ESF (blue dots) are binned and averaged to achieve a smooth ESF (red line). The derivative of the smooth ESF is estimated to get a line spread function, which is then Fourier transformed to get the task transfer function (bottom right). In the z-direction, a cylindrical volume of interest (VOI) is placed around the interface between modules 2 and 3 of the ACR phantom (top right). In this measurement, the phantom is set up with a slight angle relative to the tomographic axial plane. Using voxels within this ROI, the exact location of the edge interface is determined by fitting a plane. It is then possible to extract an ESF by calculating the distance of each voxel from this plane. Using that z-direction ESF, the z-direction TTF is then computed in identical fashion to the in-plane TTF. The TTF curves can be summarized by the spatial frequencies at which the TTF reaches 50% and 10%\, denoted as f 50 and f 10, respectively. Various free software resources are available to assist with these analyses (e.g., imQuest, see Section 4 ).

#### 2.B.5 Data analysis

#### In-plane resolution

Export the images to image analysis software to perform the TTF calculations (e.g., imQuest, see Section [4](#mp13763-sec-0059)). The calculations should follow the circular rod method introduced by Richard et al.[6](#mp13763-bib-0006) and further refined by Chen et al.[5](#mp13763-bib-0005), [7](#mp13763-bib-0007) In this method, a circular ROI with a radius about twice that of the phantom rod is roughly centered about the rod. The exact center location of the rod is estimated in each image by finding the maximum of the cross-correlation between the image data and an idealized image of the phantom rod at upsampled resolution (to allow higher precision in center identification).

The precise center location of the rod is estimated for each image and each pixel's radial distance from the center is calculated. An ESF is then generated by binning and averaging pixel CT numbers as a function of radial distance. Radial bin widths of 1/10th the image pixel size are recommended. The derivative of the ESF is taken to yield the LSF. The TTF is finally computed as the magnitude of discrete Fourier transform of the LSF (normalized by the DC component).

Once the TTF is computed, the 50% and 10% frequencies (f <sub>50</sub> and f <sub>10</sub>) can be determined and used to summarize the system resolution under the given acquisition/reconstruction conditions. It is also important to report the contrast and noise conditions under which the TTF was measured. This analysis is illustrated in Fig. [6](#mp13763-fig-0006).

#### Z-axis and 3D resolution

Export the images to image analysis software to perform the TTF calculations (e.g., imQuest, see Section [4](#mp13763-sec-0059)). The calculations should follow the slanted edge plane method described by Chen et al.[5](#mp13763-bib-0005) In this method, a virtual 2D plane is fit to the volumetric image data to determine the precise location and angle of the phantom plane edge. Based on this fit, a raw ESF is generated by plotting voxel intensity against signed (i.e., positive and negative) distance from this plane. The z-direction TTF is then calculated from this raw ESF using the same methods described above for the in-plane TTF. As a first approximation, the z-direction TTF is here assumed to be independent from the in-plane TTF to form a 3D TTF (i.e. ![urn:x-wiley:00942405:media:mp13763:mp13763-math-0009](https://aapm.onlinelibrary.wiley.com/cms/asset/d9907b09-4838-449f-bb34-1e7b0b7ab275/mp13763-math-0009.png)).

Once the TTF is computed, the frequencies associated with 50% and 10% TTF (f <sub>50</sub> and f <sub>10</sub>) can be determined and used to summarize the system resolution under the given acquisition/reconstruction conditions. It is also important to report the contrast and noise values at which the TTF was measured. This information is necessary not only in terms of the level of CNR needed for a robust TTF measurement (i.e., >15, noted above), but also with respect to the fact that in nonlinear CT systems, TTF can be a function of contrast and noise. Note that z-axis TTF and the slice sensitivity profile [8](#mp13763-bib-0008) reflect similar performance attributes of a CT system. This analysis is illustrated in Fig. [6](#mp13763-fig-0006).

#### 2.B.6 Precautions and caveats

When using this method, if ![urn:x-wiley:00942405:media:mp13763:mp13763-math-0010](https://aapm.onlinelibrary.wiley.com/cms/asset/2ecd45e9-ca1b-4131-b88d-e96947a0e9aa/mp13763-math-0010.png) is below the recommended threshold of 15, then the ESF should be further conditioned to minimize the influence of noise on the TTF measurement using the method described by Maidment et al.[9](#mp13763-bib-0009) Unfortunately, this data conditioning technique assumes that the ESF is monotonic. This assumption is usually violated for reconstruction kernels or algorithms with edge-enhancement and therefore this ESF conditioning technique should not be used for images with known or suspected edge-enhancement. Further, CT resolution can be location dependent (shift-variant) and thus the results should be ascribed to the radial location where the test object is located. The estimation should include a measure of uncertainty associated with the measurement. Estimation of the uncertainty can be done empirically by making repeated measurements on independent images, or approximated from expected percent error of the TTF as a function of CNR.[5](#mp13763-bib-0005)

Alternative methods for MTF characterization may also use high-contrast wires, beads, or foils (usually made of tungsten).[10](#mp13763-bib-0010) Such techniques, while established for conventional MTF measurements, are not recommended for ascribing the edge properties of low-contrast features when using CT systems deploying nonlinear reconstruction techniques.

#### 2.B.7 Recommended performance metrics

- – TTF at defined noise and contrast levels in the in-plane and z directions, *TTF <sub>n,C</sub>*, and *zTTF <sub>n,C</sub>.* The number of contrast levels (i.e., phantom inserts) needed depends on what the resolution measurements will be used for. For general system characterization, the four CT ACR 464 phantom inserts are sufficient. However, a focused assessment of the resolution properties of low-contrast signals might require a phantom with multiple rods of varying low contrast.
- – Frequencies associated with 50% and 10% on in-plane TTF, *f <sub>50</sub> and f <sub>10</sub>*, respectively
- – Frequencies associated with 50% and 10% on z-axis TTF, *zf <sub>50</sub> and zf <sub>10</sub>*, respectively

### 2.C Noise

#### 2.C.1 Objective

To characterize noise and noise texture of the CT system under reference conditions and establish baseline values for targeted imaging conditions with methods applicable to both linear and nonlinear reconstruction algorithms.

#### 2.C.2 Important definitions

- – Noise: Stochastic fluctuations of image pixel values due to measurement uncertainty (i.e., quantum or electronic noise). Fluctuations due to anatomical variations (i.e., anatomical noise) are not considered as noise in this report.
- – Noise magnitude: Standard deviation (SD) of pixel values.
- – Noise texture: Visual impression of the image noise (e.g. fine or coarse). CT images have a distinct noise texture as a result of the noise correlations introduced in the image reconstruction process. The noise texture has a large impact on the perceived quality of a CT image and can be quantitatively characterized by the noise autocorrelation or the noise power spectrum as described below.
- – Noise autocorrelation: Second-order statistic of the noise describing the correlations between any two noisy pixel values. When the noise is wide-sense stationary, the expected (i.e., average) correlation between any two pixels with a given spatial separation is the same, regardless of their absolute location. Wide-sense stationarity of the noise also implies that the noise magnitude is constant across the image FOV. Generally speaking, this condition is not globally satisfied in CT images but can usually be assumed to be true within a small local ROI.
- – Noise Power Spectrum (NPS): Fourier transform of the noise autocorrelation\, describing the distribution of noise variance in terms of spatial frequencies. Noise stationarity is assumed for computation of the NPS from the noise autocorrelation.
- – Noise nonuniformity: Variations in the noise magnitude or NPS across the image FOV. All CT images have some degree of global, slowly changing, noise nonuniformity [11](#mp13763-bib-0011) (e.g., noise in the mediastinum tends to be higher than noise in the lungs or the NPS has a different shape at isocenter compared to peripherally). Additionally, nonlinear reconstruction algorithms can introduce highly localized noise nonuniformity in image regions containing many anatomical structures and edges (e.g., lungs). This is due to the regularization used as an integral component of most commercial iterative reconstruction algorithms. As a general rule, these algorithms are attempting to minimize noise while preserving resolution. As a result, they tend to aggressively reduce noise in uniform image regions while less aggressively reducing noise in regions with many structures and edges. This can lead to highly nonuniform spatial distribution of noise.[12](#mp13763-bib-0012)

#### 2.C.3 Equipment

- – Water phantom(s) or other uniform phantoms of relevant diameter to mimic the attenuation of a patient's body or head such as the CT ACR 464 phantom, one of the Catphan phantoms, or the Mercury phantom [2](#mp13763-bib-0002).
- – Phantom with “anatomical” texture and structures (i.e., heterogeneous background). A phantom with detailed anthropomorphic structures is preferred (e.g., the Lungman phantom from Kyoto Kagaku, the Mercury texture inserts). If such a phantom is not available, a phantom filled with water and acrylic spheres or other round objects (with different attenuation than water) can be used.

#### 2.C.4 Procedures

#### Noise magnitude

The phantom(s) should be scanned sampling representative protocol and dose conditions of interest or those listed in Table [^2]. The protocols should ideally range from clinically relevant low dose to typical dose to high dose, as characterization at multiple dose levels enables interpolation of results for the intermediary values to facilitate comparison of results across systems, time, etc. Five ROIs, approximately 1% of the phantom area in size, should be placed at center, and at 12, 3, 6, and 9 o'clock. The peripheral ROIs should be placed approximately one ROI diameter away from the phantom border (see Fig. [7](#mp13763-fig-0007)). The noise magnitude (SD of pixel values) should be recorded and averaged across each ROI location and for at least three images. This process can use different slices from the same acquisition or the same slice from repeated acquisitions.

![](https://aapm.onlinelibrary.wiley.com/cms/asset/7f01cd7c-a44f-40a8-9a75-1e6f9664344f/mp13763-fig-0007-m.jpg)

Figure 7 Open in figure viewer PowerPoint Region of interest placement for measuring noise magnitude.

#### Noise texture

The phantom(s) should be scanned multiple times using three variations of the typical head and body protocols, including a clinically relevant low dose to a typical dose to a high dose. The number of repeated acquisitions needed depends on the length of the phantom. The target number of ROIs should be 100. A matrix of 64x64 pixels should be extracted near the center of each of the images (being careful to avoid potential artifacts). Multiple ROIs can be used from a single image if needed. The 2D NPS can be estimated from each ROI using the method described by Boedeker et al.[13](#mp13763-bib-0013) The 2D NPS data can be radially re-binned/averaged for 1D presentation.[14](#mp13763-bib-0014) The analysis can also extend to 3D [15](#mp13763-bib-0015).

#### Noise nonuniformity

A uniform or structured phantom is scanned a minimum of 20 times using a typical head or body protocol in the axial mode at a typical dose [12](#mp13763-bib-0012), [16](#mp13763-bib-0016) (the scalar statistic computed depends on the phantom type, see Section Noise nonuniformity). The scan should be performed with a single rotation and no table translation to minimize variability due to table motion between repeated scans. The spatial distribution of noise magnitude can be estimated on a voxel-by-voxel basis by taking the standard deviation of each voxel's CT number across the ensemble of repeated images as

![urn:x-wiley:00942405:media:mp13763:mp13763-math-0011](https://aapm.onlinelibrary.wiley.com/cms/asset/95266585-731e-4561-8bc7-9b7929b29bd1/mp13763-math-0011.png)

urn:x-wiley:00942405:media:mp13763:mp13763-math-0011

(3)

where, ![urn:x-wiley:00942405:media:mp13763:mp13763-math-0012](https://aapm.onlinelibrary.wiley.com/cms/asset/a5963dfe-c342-4d05-8e76-18ebb3b1ae63/mp13763-math-0012.png) is the noise magnitude of the ith voxel, M is the number of repeated scans, ![urn:x-wiley:00942405:media:mp13763:mp13763-math-0013](https://aapm.onlinelibrary.wiley.com/cms/asset/149e5672-5876-4cb7-93fa-6c06a68d5023/mp13763-math-0013.png) is the CT number of the ith voxel in the jth repeated image, and ![urn:x-wiley:00942405:media:mp13763:mp13763-math-0014](https://aapm.onlinelibrary.wiley.com/cms/asset/4639f5cb-3faa-40ab-9660-74bfbc71ab92/mp13763-math-0014.png) is the average CT number of the ith voxel across the ensemble of repeated images. ![urn:x-wiley:00942405:media:mp13763:mp13763-math-0015](https://aapm.onlinelibrary.wiley.com/cms/asset/7c100f66-c49a-4b28-8383-e7afbcb506ca/mp13763-math-0015.png) can be thought of as a spatial map of noise magnitude (i.e., how much does each pixel randomly fluctuate from scan to scan). Having this noise map allows one to visually assess noise nonuniformities. Scalar statistics can also be calculated from this noise map as described in section Noise nonuniformity.

#### 2.C.5 Data analysis

#### Noise magnitude and texture

For noise magnitude, the average pixel SD across a minimum of three images is used as the output. The three images could come from repeated acquisitions or from slices (ideally nonconsecutive) from the same acquisition. For noise texture, the peak frequency ![urn:x-wiley:00942405:media:mp13763:mp13763-math-0016](https://aapm.onlinelibrary.wiley.com/cms/asset/4a092cf5-a144-4d82-ad6a-ffb54c536453/mp13763-math-0016.png), and the average frequency ![urn:x-wiley:00942405:media:mp13763:mp13763-math-0017](https://aapm.onlinelibrary.wiley.com/cms/asset/74002c2b-d9ff-4523-9341-52674418fb0f/mp13763-math-0017.png) are reported as summary metrics, which describe the overall frequency content of the NPS as

![urn:x-wiley:00942405:media:mp13763:mp13763-math-0018](https://aapm.onlinelibrary.wiley.com/cms/asset/29e2ef06-d620-4308-b409-40f205f08947/mp13763-math-0018.png)

urn:x-wiley:00942405:media:mp13763:mp13763-math-0018

(4)

and

![urn:x-wiley:00942405:media:mp13763:mp13763-math-0019](https://aapm.onlinelibrary.wiley.com/cms/asset/7936859d-e76f-4826-9cc9-3badc903070f/mp13763-math-0019.png)

urn:x-wiley:00942405:media:mp13763:mp13763-math-0019

(5)

where ![urn:x-wiley:00942405:media:mp13763:mp13763-math-0020](https://aapm.onlinelibrary.wiley.com/cms/asset/3e284a73-03ea-4cd4-b501-3a2d3744089e/mp13763-math-0020.png) is the radial spatial frequency (i.e., ![urn:x-wiley:00942405:media:mp13763:mp13763-math-0021](https://aapm.onlinelibrary.wiley.com/cms/asset/e96f8c36-fa76-487f-b6bc-3486b98d5869/mp13763-math-0021.png)) and ![urn:x-wiley:00942405:media:mp13763:mp13763-math-0022](https://aapm.onlinelibrary.wiley.com/cms/asset/bd837c28-1d2a-4609-97a7-c9a025de23ae/mp13763-math-0022.png) is the radially re-binned/averaged 1D NPS (see Fig. [8](#mp13763-fig-0008)).[14](#mp13763-bib-0014)

![](https://aapm.onlinelibrary.wiley.com/cms/asset/1e3c4861-2713-48b5-802d-81e6e4bb5920/mp13763-fig-0008-m.jpg)

Figure 8 Open in figure viewer PowerPoint Noise texture analysis using the noise power spectrum.

#### Noise nonuniformity

Two scalar statistics have been described in the literature to quantify noise nonuniformity. Both are based on the spatial noise map, ![urn:x-wiley:00942405:media:mp13763:mp13763-math-0023](https://aapm.onlinelibrary.wiley.com/cms/asset/a6ce7807-c14d-4b3c-9a80-f4cabaf02e50/mp13763-math-0023.png) (see Section Noise nonuniformity). The first metric was introduced by Li et al and is called the “noise spatial nonuniformity index (NUI)”.[17](#mp13763-bib-0017) This metric is suitable to characterize how much the noise magnitude varies globally across the image FOV. It can be computed based on images of either a uniform or structured phantom. NUI is computed by making a series of ROI measurements (8 × 8 mm ROI size) spanning the FOV (but within the phantom) on ![urn:x-wiley:00942405:media:mp13763:mp13763-math-0024](https://aapm.onlinelibrary.wiley.com/cms/asset/78a07841-8c68-4dd5-ac40-f8d9a3c6bbc3/mp13763-math-0024.png). For the kth ROI location, the mean noise magnitude, ![urn:x-wiley:00942405:media:mp13763:mp13763-math-0025](https://aapm.onlinelibrary.wiley.com/cms/asset/2459572b-e1a4-40d2-b074-5ec4ee1741e0/mp13763-math-0025.png) is computed and the NUI is computed as the standard deviation of ![urn:x-wiley:00942405:media:mp13763:mp13763-math-0026](https://aapm.onlinelibrary.wiley.com/cms/asset/d28d31db-81e6-4a16-a94a-bcfb6f4f99f6/mp13763-math-0026.png) across all ROI locations (i.e., across all instances of k).

![urn:x-wiley:00942405:media:mp13763:mp13763-math-0027](https://aapm.onlinelibrary.wiley.com/cms/asset/682469f9-60a7-41fd-a4da-b30a6b161586/mp13763-math-0027.png)

urn:x-wiley:00942405:media:mp13763:mp13763-math-0027

(6)

The second scalar statistic that can be computed is the noise inhomogeneity index, ![urn:x-wiley:00942405:media:mp13763:mp13763-math-0028](https://aapm.onlinelibrary.wiley.com/cms/asset/f73a8697-ccf6-44e7-8316-d6e45bcafc45/mp13763-math-0028.png), as described by Solomon et al.[7](#mp13763-bib-0007) This metric is used to characterize highly irregular/structured spatial distributions of noise, which can appear in iteratively reconstructed images of structured (i.e., nonuniform background) phantoms.[7](#mp13763-bib-0007), [12](#mp13763-bib-0012) As such, this metric can only be computed using noise maps from a structured phantom. First, a histogram of ![urn:x-wiley:00942405:media:mp13763:mp13763-math-0029](https://aapm.onlinelibrary.wiley.com/cms/asset/0ca923f5-73a3-4a9a-9d27-d412f09a2876/mp13763-math-0029.png) is generated. This histogram should be based on voxels within the phantom only. If the histogram has two distinct peaks, the noise inhomogeneity index, ![urn:x-wiley:00942405:media:mp13763:mp13763-math-0030](https://aapm.onlinelibrary.wiley.com/cms/asset/ee03d16f-8b75-45c4-9124-27c77e5edac7/mp13763-math-0030.png), is calculated as the relative peak separation divided by the relative height difference in the peaks. Consider the locations of these two peaks on the histogram ![urn:x-wiley:00942405:media:mp13763:mp13763-math-0031](https://aapm.onlinelibrary.wiley.com/cms/asset/a8b52930-0907-4d12-ba46-c68affcab8c0/mp13763-math-0031.png) and ![urn:x-wiley:00942405:media:mp13763:mp13763-math-0032](https://aapm.onlinelibrary.wiley.com/cms/asset/2e5a0ab8-3352-429b-b0cf-f31115dcb903/mp13763-math-0032.png). ![urn:x-wiley:00942405:media:mp13763:mp13763-math-0033](https://aapm.onlinelibrary.wiley.com/cms/asset/d16c8b20-81b6-4536-ad5f-3338b26d1731/mp13763-math-0033.png) is calculated as

![urn:x-wiley:00942405:media:mp13763:mp13763-math-0034](https://aapm.onlinelibrary.wiley.com/cms/asset/d2364462-ebba-4359-9973-8f55cf73dcb4/mp13763-math-0034.png)

urn:x-wiley:00942405:media:mp13763:mp13763-math-0034

(7)

If the histogram does not have two peaks, then ![urn:x-wiley:00942405:media:mp13763:mp13763-math-0035](https://aapm.onlinelibrary.wiley.com/cms/asset/b0799cc2-16ea-41f8-8ee8-e3922c6d79fa/mp13763-math-0035.png) is not defined. Figure [9](#mp13763-fig-0009) illustrates this noise analysis.

![](https://aapm.onlinelibrary.wiley.com/cms/asset/e6807988-bbbb-4cd3-a9ca-d77f91376576/mp13763-fig-0009-m.jpg)

Figure 9 Open in figure viewer PowerPoint Example of how the noise inhomogeneity index,, is defined. This metric is meant to quantify the highly irregular and structured spatial distribution of noise that is sometimes observed in iteratively reconstructed images. In this example, a structured phantom simulating lung texture was scanned and images reconstructed using a commercially available iterative reconstruction algorithm. To measure, first a noise map,, is generated using repeated images of the same structured phantom (see Section noise nonuniformity). This noise map gives the standard deviation of the noise on a voxel-by-voxel basis and is shown on the left in this example. Next a histogram of is generated using only voxels within the phantom as shown on the right. If the histogram has two distinct peaks, as is the case in this example, then is calculated using the peak locations and their heights based on the equation shown above. This equation is simply the relative separation divided by the relative height difference between the two peaks. If the histogram does not have two peaks, is not defined.

#### 2.C.6 Precautions and caveats

The formulation of the NPS assumes that the noise is wide-sense stationary within the ROI. This assumption may not be valid for very large ROIs due to the known global nonuniformity of CT noise. Ensure the areas sampled for noise determination represent predefined local areas void of artifacts and noise disparity. In the assessment of noise nonuniformity, noise is estimated from an “ensemble” of repeated images. As such, any differences between repeated scans (e.g., phantom motion or different scan settings) will translate into increased variance across this ensemble of images. This could positively bias the measured noise compared to true noise, especially for structured phantoms. Care should be taken to perform the repeated scans in the most reproducible manner possible.

#### 2.C.7 Recommended performance metrics

- – Noise magnitude (pixel standard deviation) at three dose levels*, n*
- – NPS at defined noise levels, *NPS <sub>n</sub>*
- – Peak and average frequencies of the NPS, *f <sub>P</sub>* and *f <sub>A</sub>*
- – Noise nonuniformity index, NUI
- – Noise inhomogeneity index, *η*

### 2.D Quasi-linear task-based performance

#### 2.D.1 Objective

To characterize CT system performance in terms of a Fourier domain-task-based detectability index using the quasi-linear assumption of linear and wide-sense stationary system behavior within a local spatial, contrast, and noise domain. The underlying idea behind task-based image quality assessment is to quantify image quality by estimating how well a human or mathematical observer (i.e., reader) could perform some predefined task (e.g.\, detection of a subtle signal) on the images in question.[18](#mp13763-bib-0018) Thus a task-based image quality metric is more related to how well an image *performs* in delivering diagnostic information. As a result, task-based image quality metrics are well suited to characterize or compare image quality between imaging conditions in which noise magnitude, noise texture, or resolution might be variable. CNR on the other hand is only useful as a very simple first-order approximation of low-contrast detectability under fixed noise texture and resolution conditions. In other words, it would not be appropriate to compare different reconstruction kernels or algorithms on the basis of CNR. Specifically, using CNR as the basis of estimating dose reduction potential for iterative reconstruction algorithms (compared to FBP) or different kernels should not be done and could provide highly misleading and suboptimal results.[19](#mp13763-bib-0019) As such, the task-based image quality metrics described in Sections [2.D](#mp13763-sec-0037) and [2.E](#mp13763-sec-0045) effectively supersede traditional metrics such as CNR for the assessment of low-contrast detectability in modern CT systems.

#### 2.D.2 Important definitions

- – *Detectability index (d'):* a task-based detection performance metric (often referred to as d' or d-prime). Any task-based image quality assessment technique has three primary components: (a) a task to be performed (usually the detection of a subtle lesion/signal), (b) an observer to perform the task (typically a mathematical detection algorithm, sometimes a human reader), and (c) images to be assessed. Based on the foundational mathematics of signal detection theory,[18](#mp13763-bib-0018) one can imagine an ensemble of images acquired under identical conditions, some with a target signal to be detected and some without. The observer processes the image data and outputs a scalar response variable for each image, proportional to the observer's confidence that a signal is present. This results in two distributions of the response variable (signal-present and signal-absent). The greater the separation between those distributions, the better the observer is at correctly detecting the signal. The detectability index, d', quantifies this degree of separation and is essentially the signal-to-noise ratio of the observer's response variable for the aforementioned signal-present and signal-absent distributions. Mathematically, the square of d' is the squared difference in the distribution means\, divided by their average variances. One would expect a different d' for different tasks\, different observers, or images acquired under different conditions. In this section, the task considered is the detection of a circular signal as defined by a task function (*W <sub>task</sub>*, see below) and the mathematical observer used is a non-prewhitening matched filter (NPW, see below). It turns out that one can compute the detectability index, ![urn:x-wiley:00942405:media:mp13763:mp13763-math-0042](https://aapm.onlinelibrary.wiley.com/cms/asset/6105bfa8-a7bd-459b-954a-96d6b5a3b40b/mp13763-math-0042.png), for this observer in the Fourier domain based on measurements of system resolution (TTF), and noise (NPS) as shown below. To do this calculation, it is also necessary to define the properties (e.g., size, shape, contrast, and contrast-profile) of the signal be detected. These properties are encoded in the task function, *W <sub>task</sub>* (see below)*.* The detectability index is interpreted as a metric of image quality due to its relation to low-contrast detectability (i.e., an increase in ![urn:x-wiley:00942405:media:mp13763:mp13763-math-0043](https://aapm.onlinelibrary.wiley.com/cms/asset/a6861dd9-cec4-4335-ae7c-9ba98b9a817b/mp13763-math-0043.png) implies the signal is easier to detect and thus image quality is better). Such Fourier-domain metrics have been shown to agree closely with human observer studies for linear shift-invariant (LSI) systems [20](#mp13763-bib-0020) and are being adapted for use in nonlinear systems that are evaluated in a quasi-linear state (e.g., IR algorithms).[7](#mp13763-bib-0007), [21](#mp13763-bib-0021), [22](#mp13763-bib-0022)
- – *Task Function (W <sub>task</sub>):* Fourier transform of the signal to be detected (e.g. a 10-mm circular lesion with a contrast of 10 HU). As mentioned above and described in detail below, measuring d' involves defining the properties (size, shape, contrast, and contrast-profile) of the signal to be detected. These properties can be encoded in this task function. Common task functions correspond to circular low-contrast signals having diameters between 1 to 10 mm. Suggested mathematical formulations are provided below.
- – *Non-prewhitening matched filter (NPW):* this observer model compares the image of interest to a template consisting of the expected signal via cross-correlation. This model has been shown to correlate strongly with human performance for low-contrast detection tasks.[7](#mp13763-bib-0007), [21](#mp13763-bib-0021), [22](#mp13763-bib-0022) The detectability index for this model, ![urn:x-wiley:00942405:media:mp13763:mp13763-math-0044](https://aapm.onlinelibrary.wiley.com/cms/asset/875c6897-7e7b-4810-9779-80946f8e085e/mp13763-math-0044.png), can be computed in the Fourier domain for a given *W <sub>task</sub>* based on measurements of the system's TTF and NPS as shown below.
- – *Estimability index (e')*: a performance metric related to the expected accuracy of volumetric measurements in CT images with given three-dimensional noise and resolution properties. A higher e' implies a higher degree of expected volumetric accuracy.

#### 2.D.3 Equipment

- – Phantom with circular inserts (>2 cm diameter) of various materials (i.e., contrast levels). Phantom should also contain uniform regions for noise analysis (e.g., CT ACR 464 phantom for constant size or Mercury phantom for variable size measurements).
- – Image analysis software capable of NPS, MTF/TTF, and detectability calculations, see Section [4](#mp13763-sec-0059) below.

#### 2.D.4 Procedures

Position and align the phantom on the table. Acquire a CT localizer radiograph and define the scan range to incorporate the entire phantom. The phantom is scanned following protocols interest representative of the protocol and dose conditions or those listed in Table [^2]. The protocols should ideally range from clinically relevant low dose to typical dose to high dose.

#### 2.D.5 Data analysis

For each acquisition and phantom insert, estimate the TTF using the methods described in Section [2.B](#mp13763-sec-0012).B. Define a task function, *W <sub>task</sub>* by first synthesizing an ideal image of a signal to be detected. Then *W <sub>task</sub> is defined as the Fourier transform of this synthesized signal.* As common approximations, the shape of the signal may be circular with either a rectangular or designer contrast-profile (Figure [10](#mp13763-fig-0010)),[5](#mp13763-bib-0005), [23](#mp13763-bib-0023) respectively, formulated as

![urn:x-wiley:00942405:media:mp13763:mp13763-math-0045](https://aapm.onlinelibrary.wiley.com/cms/asset/b28e74e6-b09b-48b4-a2e7-4fc3c1dd9d7b/mp13763-math-0045.png)

urn:x-wiley:00942405:media:mp13763:mp13763-math-0045

(8)

where c is the value of the signal at a radial distance *r*, *C* denotes the peak contrast of the signal against the background in HU, ![urn:x-wiley:00942405:media:mp13763:mp13763-math-0046](https://aapm.onlinelibrary.wiley.com/cms/asset/206fe7d4-b78b-4ef3-b065-136dc36d5dce/mp13763-math-0046.png) is the rect function, *D* is the signal diameter, and *n* is a constant dictating the sharpness of the edge of the designer contrast-profile (as n decreases, edge sharpness increases, recommended value is 1, with alternative values ranging between 0.25 to 2). Note that in the designer profile equation, D denotes the diameter at which the contrast reaches zero. The apparent (i.e., visual) diameter of the signal might be lower than D depending on the chosen value of n. In some cases, it is useful to parameterize the object's diameter by its full-width-at-half-maximum (FWHM), which can be computed as a function of D:

![urn:x-wiley:00942405:media:mp13763:mp13763-math-0047](https://aapm.onlinelibrary.wiley.com/cms/asset/73f8c43a-e7af-4c7c-a8a9-5bd634275054/mp13763-math-0047.png)

urn:x-wiley:00942405:media:mp13763:mp13763-math-0047

(9)

![](https://aapm.onlinelibrary.wiley.com/cms/asset/4c4555bc-6805-41a7-9cae-5a61c9ac390b/mp13763-fig-0010-m.jpg)

Figure 10 Open in figure viewer PowerPoint Examples of the synthesized signals to be detected. The Fourier transform of such a signal is the task function, W task, which is an important component of the detectability index calculation. Signals of three sizes are shown, with the top rows showing signals with a designer contrast profile and the bottom row with a rectangular contrast profile.

Three diameters for the signals are recommended: large (10 mm), medium (5 mm), and small (1 mm). Note that the contrast, *C,* of the signal should roughly match the contrast of the insert used to measure the TTF. An ideal range is between 10 and 100 HU. Next calculate W <sub>task</sub> by taking the Fourier transform of the synthesized image. Finally calculate ![urn:x-wiley:00942405:media:mp13763:mp13763-math-0048](https://aapm.onlinelibrary.wiley.com/cms/asset/0b40fb16-04e2-421f-8004-11c4dd204138/mp13763-math-0048.png) as

![urn:x-wiley:00942405:media:mp13763:mp13763-math-0049](https://aapm.onlinelibrary.wiley.com/cms/asset/82bad68a-e70b-4f09-a387-7209d235a90d/mp13763-math-0049.png)

urn:x-wiley:00942405:media:mp13763:mp13763-math-0049

(10)

where u and v are the spatial frequencies corresponding to the x and y direction, respectively. This formulation of the detectability index, based on the non-prewhitening matched filter, assesses detection in two-dimensional images, thus using 2D integrals. The analysis may be extended to 3D using the 3D TTF and NPS. Using the recommended protocols above, it is possible to assess image quality as a function of dose, tube potential, tube current modulation setting, phantom size, task size, task contrast, image thickness, reconstruction algorithm, and reconstruction kernel, thus offering a system characterization over a wide sampling of operational settings.

The analysis can further be extended to estimability for specific estimation tasks such as assessment of a lesion volume. For those tasks, an estimability index can be computed as

![urn:x-wiley:00942405:media:mp13763:mp13763-math-0050](https://aapm.onlinelibrary.wiley.com/cms/asset/ea855493-7a64-418d-89fd-3ce448e78a39/mp13763-math-0050.png)

urn:x-wiley:00942405:media:mp13763:mp13763-math-0050

(11)

where W is Fourier transform of the derivative of a spherical signal's edge profile in the definitions of Eq. ([^3]) (constructed in 3D), and M is a template function associated with a lesion segmentation algorithm.[24](#mp13763-bib-0024) The template function reflects the contribution of the lesion segmentation algorithm to the estimation process (volume estimation in this case). This function is expected to be reflective of the method employed by the specific segmentation algorithm. In this case, a typical algorithm is assumed to be seeking spherical features as a basis of the segmentation.

#### 2.D.6 Precautions and caveats

When creating W <sub>task</sub>, be sure that the assumed contrast of the object to be detected and the insert used to measure the TTF are similar. Also be sure to report the contrast of the insert and noise conditions under which the TTF was measured.

Non-prewhitening matched filter is only one among many such observer models that can be used to integrate and extend the resolution and noise properties of an imaging system toward the performance for a defined task.[25](#mp13763-bib-0025) In this report we note the use of only one model (NPW) to standardize the process based on a model that has shown strong correlation with observer data.[18](#mp13763-bib-0018), [26](#mp13763-bib-0026) Future extensions may include other models provided the details are disclosed and an efficient analysis strategy is made available.

The Fourier-based methodology to characterize imaging system performance assumes a quasi-linear shift-invariant system response and locally wide-sense stationary noise statistics. Thus, the testing conditions and image and noise features should be carefully selected to closely match the patient imaging conditions.

Using all combinations of settings in Table [^2] will result in 96 CT series and multiple d' values depending on the phantom used (384 if using the CT ACR 464 phantom, 2400 if using the Mercury phantom). The interpretation of this complete dataset can be practically prohibitive for routine testing but with automation can be done for the initial system characterization and updated as a basis for comparing or optimizing clinical protocols.

#### 2.D.7 Recommended performance metrics

- – Detectability indices for the task of detecting target reference circular signals (e.g., 1, 5, and 10 mm features at specific CT numbers with rectangular or designer morphology) for the targeted phantom size and noise or dose level.
- – Estimability index for the task of estimating the volume of a target reference spherical signal (e.g., 10 mm feature at specific CT number with rectangular or designer morphology) for the targeted phantom size and noise or dose level.

### 2.E Spatial domain task-based performance

#### 2.E.1 Objective

To evaluate a CT system in terms of the ability of the images to enable an observer (either a human or a computer algorithm) to perform a signal-detection task using the image pixel values themselves. Spatial domain methods are available for characterizing signal detectability for known signals as well as detection of signals that have unknown or variable aspects, including size, contrast, or location. Tasks in which the signal is not exactly known to the observer, because the signal is deterministic but the observer has missing information about it (where the signal is, or its size or amplitude), are more similar to clinical tasks. Even more similar to a clinical task are ones in which the signal is random in some way. Tasks with variable or unknown signal characteristics can offer advantages over signal-known-exactly tasks when evaluating image quality, including the need for fewer images as well as the ability to make use of signals with a larger range of contrast levels while still resulting in meaningful comparisons between image acquisition protocols or reconstruction algorithms.

#### 2.E.2 Important definitions

- – *ROC:* receiver/relative operating characteristic.
- – *LROC*: localization relative operating characteristic.
- – *FROC*: Free-response operating characteristic.
- – *EFROC:* exponential transformed free response operating characteristic.
- – *MRMC*: multiple-readers multiple cases study.
- – *AUC*: area under the curve of any of the operating characteristic curves above.

#### 2.E.3 Equipment

- – *FDA MITA Phantom*. The FDA MITA phantom has a set of four low-contrast embedded rods that facilitate the evaluation of CT systems in a single image. Using rods as targets in the phantom also allows multiple images to be utilized in a system evaluation from a single reconstructed 3D image.
- – Catphan Custom Modules: A phantom design consisting of five identical spherical signals arranged symmetrically about the center.[27](#mp13763-bib-0027) Modules with signals of different size or contrast can be used depending on the scanner type or operating regime being evaluated. This design has the advantage that it can be used for 3D image evaluations because the spherical targets are limited in the z-axis, unlike the rod objects utilized in the FDA MITA phantom.
- – The practitioner may consider using other phantoms containing objects with sizes and contrasts relevant to the task being evaluated. This includes anthropomorphic structured phantoms with embedded signals. Note that the specifics of the analysis method may somewhat depend on the phantom design (e.g., number of repeated images needed, 2D vs 3D signals, etc.).

#### 2.E.4 Procedures

The phantom is imaged using the representative protocol and dose conditions of interest or those listed in Table [^2]. The images are scored by human observers or computational algorithms (so-called observer models). The specifics of collecting the scoring data from either method are outlined below.

This characterization mostly applies to situations when a multiplicity of conditions may need to be compared (e.g., effect of dose on signal detection). The number of images required is based on the desired statistical power of the final results; the targeted operating points and the performance difference can be compared between the conditions. As an example, with the custom module arrangement,[27](#mp13763-bib-0027) 20 signal-present and 20 signal-absent image samples were needed for showing the difference in performance between a standard filtered back-projection implementation and an iterative reconstruction algorithm.

#### Human observer methodology

Both the FDA MITA phantom and the Catphan custom modules are designed to allow for unknown-location signal detection experiments with human observers. To set up such an experiment, the evaluator crops regions of interest (ROIs) from the reconstructed images such that a signal is located within the ROI, with a chosen distance from the ROI edge to avoid boundary effects. The ROIs are selected such that each contains only one signal. Furthermore, for a set of image scans, the locations of the boundaries of the ROIs are adjusted so that the signals have different locations within the ROIs, making it so that the signal locations are random to the observer when presented as a sequence of such ROIs. Figure [11](#mp13763-fig-0011) shows such an example of random 5 × 5 cm <sup>2</sup> ROI selections applied on an FDA MITA phantom image, and 4 × 4 cm <sup>2</sup> ROI randomly selected on Catphan custom modules. A different set of such ROI selections can be made for each of a set of image scans, enabling the signal to be located at different positions in the set of ROIs for an observer signal-detection experiment with signal-location uncertainty.

![](https://aapm.onlinelibrary.wiley.com/cms/asset/b4f2074e-e17d-430e-816d-e3bd47d6795d/mp13763-fig-0011-m.jpg)

Figure 11 Open in figure viewer PowerPoint Example of random selection of regions of interest (ROI). a) 5 × 5 cm 2 ROIs in FDA MITA phantom; the ROIs are allowed to overlap. b) 4 × 4 cm ROIs in a Catphan custom module with identical signals; the ROIs are not allowed to overlap.

It should be noted that for the FDA MITA phantom, which contains four different signals with different size-contrast values, the detection of each signal type could be studied separately, with ROIs that overlap across the signal size-contrast experiments \[Fig. [11](#mp13763-fig-0011) (a)\]. However, if the results for different signals are subsequently combined, for example, to examine the impact of signal size for a given imaging protocol or reconstruction algorithm, then the possible correlations due to overlap between the ROIs must be accounted for in the calculation of the error bars.

Because the signals in a Catphan custom module are identical, and meant to be studied together, the ROIs should not overlap \[Fig. [11](#mp13763-fig-0011) (b)\] in order to assure independence of each ROI reading.

Once the ROIs have been specified, the next step is to present them to the human observer for data collection. In an LROC study, the reader views signal-present and signal-absent ROIs individually, and is asked to rate the probability that a signal is present and indicate the signal location. (Of course, the reader is blind to whether a signal is truly present in the ROI, and if it is present, where it is located.) A simpler experimental design is to display only the signal-present ROIs and ask the reader to indicate the signal location. In this case, the correct-localization success rate is the performance metric.

The simplest experiment of all is the location-known-exactly experiment, in which the observer is told where the signal would be if it were present, as well as a full description of it size, shape, contrast, etc. The observer simply scores each ROI using a scale that indicates their certainty that the signal is present. While this experimental design is common, the extent of information provided to the observer makes the signal highly detectable for all but very low-contrast situations when the background is also known as it is in the phantoms described here. It should be noted that the advent of 3D printing is bringing new opportunities for creating phantom images with nonuniform backgrounds, which is showing promise for the use of known-location signal-detection experiments at higher contrasts than are feasible in flat-background phantom experiments.

It is widely known that human observers vary in skill, and thus it is important when evaluating an imaging system with human observers to use a sample of readers so that the study results generalize to other readers and not just the one(s) used in the study. The term “multi-case multi-reader” (MRMC) study design is used to refer to such studies, where “case” refers to the images used in the evaluation experiment here.

#### Observer model methodology

Mathematical observer models are a powerful alternative to human observers for CT performance evaluation. Section [2.D](#mp13763-sec-0037) described one such example, where the figure of merit was based on an observer model that evaluates the images in the Fourier domain. In the spatial domain, the observer model is one that takes in the image pixel data and applies an algorithm that is typically inspired by human perception experiments. The literature describes spatial-domain observers that have been shown to be very good predictors of human performance.[25](#mp13763-bib-0025), [28](#mp13763-bib-0028) - [33](#mp13763-bib-0033) The task performed by the observer model can involve a signal searching (or image scanning) algorithm. Several approaches are possible for signal searching. One such procedure consists of applying a signal-matching template at all locations of a given image area (or volume). Subsequently, the practitioner can retrieve the list of the most suspicious locations following one of the methods.[27](#mp13763-bib-0027) The results can be analyzed as described below. In the case of the FDA MITA phantom, special area search restrictions need to be applied, so that the search for a given signal size, using a specialized template, would not be confused by the presence of the other signals of different size.

#### 2.E.5 Data analysis

Whether the observer in a spatial-domain evaluation is a human or an observer model, the data analysis method is virtually identical. Below we describe the data analysis methods for various experimental designs and provide references for more information. Publicly available software resources are noted in Section [4](#mp13763-sec-0059) below.

#### Localization success and LROC analysis of ROI reading scores

If only the signal localization marks are recorded, then the localization success rate can be used as a performance metric. More information is acquired in an LROC study with readers providing confidence scores. The data can be analyzed using LROC methods, with the area under the LROC curve (LROC-AUC) as the performance metric.[34](#mp13763-bib-0034), [35](#mp13763-bib-0035) An adaptation for LROC of the method [36](#mp13763-bib-0036) can be used for an MRMC study design.

#### Free-response data analysis of the automatic signal-search scores

The results returned by the image scanning procedure follows a free-response image reading methodology: the observer marks and scores all “potentially” suspicious locations (above a certain score or probability of signal presence), and the data can be analyzed using free-response operating characteristic (FROC) analysis. A variation of this method using the exponential transformation of abscissa, EFROC,[37](#mp13763-bib-0037) is particularly advantageous for use with this type of phantom data.

In many circumstances there is a need to evaluate image quality for a multiplicity of conditions, for example, across a broad range of doses to determine the dependence of signal detectability on dose. The number of images required for such an evaluation will be based on the desired statistical power for drawing conclusions regarding statistical significance of the difference between conditions. As an example, with the Catphan custom module arrangement,[27](#mp13763-bib-0027) 20 signal-present and 20 signal-absent image samples were needed for showing the difference in performance between a standard filtered back-projection implementation and an iterative algorithm.

#### 2.E.6 Precautions and caveats

The current FDA MITA phantom allows only 2D evaluations, and the effective noise level for a given dose depends on image thickness. Ideally\, doubling the thickness is equivalent to doubling the dose. However, rebinning, interpolation, filtering (along the *z* -axis), regularization, and other procedures that are algorithm-dependent may lead to a different *effective* image thickness than the *nominal* image thickness that is defined by the chosen size of the voxels. As a result, the signal detection performance may vary with the image thickness for the compared conditions. In order to assess this effect, we suggest measuring the *z* -axis resolution at low contrast.[5](#mp13763-bib-0005) The z-axis resolution for the algorithms being compared should be shown to be non-inferior to that of the standard algorithm. A recent review paper by Vaishnav et al consolidated information relevant to objectively assessing iterative algorithms and their dose reduction potential using task-based methodologies.[38](#mp13763-bib-0038)

A general aspect of using signal-matching templates as observer models for search tasks is that they may not necessarily yield optimal detection performance. This is due to the fact that the optimal performance depends not only on matching the signals, but also on avoiding the false-signals, which itself depends on the noise pattern as well as on the template used. As opposed to the case of the location-known detection tasks in which the optimal matching template can often be analytically derived (or estimated), in search-matching templates, the statistical population of false-signal locations depends on the template used, and thus template optimization is nontrivial, requiring a heuristic approach. As the signal-searching template depends on a number of parameters (e.g., search window size), a generally recommended approach for showing the optimality and stability of the results is to do a sensitivity and uncertainty analysis. It should be noted that such an analysis is necessary for interpretation of the results obtained via any observer model or detection paradigm.

Because signal search tasks take into account the rather extreme occurrences of false, signal-like, features randomly appearing in the image, they are particularly sensitive to changes in the noise magnitude and pattern, in addition to emulating more closely some clinical diagnostic tasks. When applied with phantoms as presented here, the signal search task procedures make better use of the image area, thus being more efficient in terms of assessing image quality with a finite amount of image data.

The number of images needed to calculate spatial domain task-based image quality metrics could limit their utility for routine clinical physics testing, especially when exploring a large parameter space of system acquisition and reconstruction settings.

There is a large body of scientific literature related to the use of observer models as the basis of image quality assessment in medical images. For practical purposes, only a small portion of that literature is represented in this report. Interested readers are encouraged to review ICRU Report 54 [18](#mp13763-bib-0018) and a comprehensive review article by Barret et al.[25](#mp13763-bib-0025) for a more in-depth understanding of task-based image quality assessment and different types of observer models.

#### Fourier and spatial-domain observers

Fourier and spatial-domain observers strive to predict task-based measures of image quality, while accounting for characteristics of the signal to be detected as well as the deterministic and stochastic properties of the imaging system. Spatial-domain methods are applied directly to the acquired images. Publicly available software allows for the calculation of performance estimates and their statistical uncertainties (see iMRMC and iQModelo in Section [4](#mp13763-sec-0059) below). The number of images needed for reasonable error bars supporting statistical comparisons between conditions will depend on the inherent detectability of the signal, the number of ROIs per image, and the size of the search area in the case of a search task.

The Fourier methods described in this report make use of measures of the characteristics of the imaging system in terms of resolution and noise, and a subsequent calculation to derive a task-based figure of merit. The calculation of the uncertainty of the resulting figure of merit requires an understanding of the uncertainties of each of the underlying components of the performance estimate, and the impact of that uncertainty on the final estimate.

Ongoing work in the field is addressing the need for more realistic (virtual and physical) phantoms that more closely resemble clinical tasks.[12](#mp13763-bib-0012), [39](#mp13763-bib-0039) - [44](#mp13763-bib-0044) The literature regarding the use of observer models that correlate well with human performance continues to grow and mature, elucidating the circumstances for which Fourier or various spatial-domain observer models are useful surrogates of human performance. Finally, a more complete understanding of the relationship between the numbers of scans used for each approach and the resulting uncertainty in the performance metric is an area of active investigation.[5](#mp13763-bib-0005), [26](#mp13763-bib-0026)

#### 2.E.7 Recommended performance metrics

- – Localization success rate for targeted tasks, *LR*
- – Area under the LROC curve for targeted tasks, *A <sub>LROC</sub>*
- – Area under the EFROC curve for targeted tasks, *A <sub>EFROC</sub>*

## 3 Clinical Utility and Future Extensions

The characterization procedures and resulting metrics delineated in Section [2](#mp13763-sec-0003) act as a first step in providing common analysis techniques and metrics that can characterize the anticipated clinical performance of a CT system based on physical measurements. The tests described in Section [2](#mp13763-sec-0003) provide advanced methods to assess modern CT systems that have advanced technologies such as AEC and iterative reconstruction available. As noted earlier, the goal of these procedures are not so much to verify the technical or engineering specifications of CT systems, or to pass or fail a device, but rather to characterize the system in terms that aid in improving and optimizing its clinical utilization. That is the rationale, for example, to ascertain the system performance not just in terms of tube potential accuracy, but in terms of resolution or task-based detection.

The utility of the operational performance noted above can be exemplified in a few specific applications:

It is not uncommon for providers of radiological services to have a diverse fleet of CT equipment with scanners of different makes and models. This diversity poses a challenge in providing images with consistent quality due to differences between scanner models. For example, images from different scanner models tend to have a unique visual impression. This difference in the overall “look” of the images is especially noticeable across different CT manufacturers and is due in large part to differences in image reconstruction methods that then lead to differences in noise texture. The metrology delineated in this report can be used as a basis to match protocols across CT systems of different makes and models, providing a method to adjust the acquisition parameters for each system such that the systems would deliver consistent image quality within a target range.

Because noise texture is one of the primary image properties that defines a human reader's visual impression of the image, being able to achieve similar noise texture across scanners models helps to achieve much more consistent images. The primary factor that determines the noise texture is the kernel used in image reconstruction. Kernels could be matched across scanners from different manufacturers to achieve similar noise texture based on noise power spectrum (NPS) analysis similar to that described in this report.[14](#mp13763-bib-0014) This matching can be expanded to include resolution (TTF) and noise magnitude as well, while at the same time meeting constraints in the dose level of the examination.[45](#mp13763-bib-0045) This method relies on the f <sub>A</sub> and f <sub>50</sub> metrics of noise and resolution that are described in Sections [2.B](#mp13763-sec-0012) and [2.C](#mp13763-sec-0024) of this summary paper, respectively. An illustration of what this might look like in practice is shown in Fig. [12](#mp13763-fig-0012).

![](https://aapm.onlinelibrary.wiley.com/cms/asset/7aa93731-a33a-451e-b886-bdaf35a9ade4/mp13763-fig-0012-m.jpg)

Figure 12 Open in figure viewer PowerPoint An example illustrating how the advanced metrics described in this report could be used in practice to help match image quality across different scanner models. The left panel (a) shows the task transfer function (TTF) (top), noise power spectrum (middle), and f A vs f 50 (i.e., noise texture vs resolution) for six different scanner models (A–F). Each scanner's reconstruction settings were chosen to achieve similar resolution and noise texture properties based on minimizing differences between f and f across scanner models. The gray circles in the scatter plot each represent a possible reconstruction kernel or iterative setting available on the scanners and the colored dots represent the chosen reconstructions corresponding to each scanner. The right panel (b) shows a series of synthesized contrast-detail images that represent what images from each scanner would look like given their TTF and NPS, and with dose adjusted to achieve equal noise magnitude as that of scanner A at a reference dose. The contrast-detail diagrams let one visually assess the smallest and lowest contrast signal that one would expect to be able to detect given the noise and resolution properties of each scanner. Visual inspection of these images confirms similar expected detectability across scanner models.

One step beyond achieving *consistent* image quality is the goal of *optimizing* image quality. The metrics derived from the tests in this report could be used to ascertain the system performance as a function of protocol parameters, so that a desired image quality and dose can be targeted based on the indication and the patient attributes for existing or new protocol definitions. Fourier-domain task-based image quality metrics similar to those described in Section [2.D](#mp13763-sec-0037) of this report could be used as a tool to help balance the competing demands of image quality and radiation dose when defining CT protocols for a large multivendor clinical facility.[46](#mp13763-bib-0046) Estimating detectability for a large variety of clinical protocols, patient sizes, lesion sizes, and lesion contrasts, the dose needed to detect a lesion of a given size and contrast for a given patient size can be ascertained and displayed to help a user estimate how changes in radiation dose would be expected to affect detectability of targeted lesions across a patient population \[Fig. [13](#mp13763-fig-0013) (a)\]. Similarly metrology can be applied using spatial-domain task-based image quality metrics to determine the achievable dose reduction of differing reconstruction algorithms.[33](#mp13763-bib-0033) Scanning a phantom with low-contrast signals at various dose levels, reconstructing the data with FBP and iterative algorithms, the magnitude of possible dose reduction using iterative reconstructions can be ascertained based on desired detectability \[Fig. [13](#mp13763-fig-0013) (b)\].

![](https://aapm.onlinelibrary.wiley.com/cms/asset/3ca79d5c-abf8-4779-a834-df9f1f2c0009/mp13763-fig-0013-m.jpg)

Figure 13 Open in figure viewer PowerPoint Example of (a) the graphical interface developed by Zhang et al. 46 to help a user balance the trade-offs between radiation dose and image quality (i.e.\, detectability) as a function of patient size and lesion characteristics. Also an example of (b) the trade-offs between radiation dose, reconstruction method, and detectability as demonstrated by Favazza et al. 33 That work determined the detectability of low-contrast signals under all the shown conditions using spatial-domain task-based image quality metrics. Those detectability data were then used to determine the achievable dose reduction from the iterative reconstruction algorithm in question.

Performance evaluation as detailed in this report advances the field beyond specifications toward actual clinical performance. It paves the way toward a number of possibilities, even beyond the few noted above. These possibilities have not been fully delineated within the present report, but they offer exciting prospects for the future direction of CT metrology and clinical optimization:
1. Performance monitoring: The methodology provides the means to monitor the performance of a CT system in terms of metrics that are more directly related to clinical performance, as opposed to engineering attributes.
2. Quantitation: Task-based performance evaluation lends itself to defining tasks beyond detection, thus enabling the use and conformance of CT systems to provide precise quantitative output. Characterization of CT performance for the task of estimating lesion volume was briefly discussed in this report but more work is required to extend that characterization to other important areas of quantitative CT imaging such as measuring the shape, texture, or material composition of a lesion.
3. Benchmarking: The methodology enables benchmarking the performance of a CT imaging operation in terms of its similarity to other practices (e.g., in peer institutions) or desired clinical performance.
4. Registries: The methodology provides quantitative values to be used for CT image quality registries within state, national, or international systems.
5. System development: In design and construction of CT systems, the system can be designed and calibrated based on targeted image quality output beyond engineering specifications the dependence of which to clinical performance is less certain.
6. Conformance: The metrics can be used as a basis for accreditation and conformance validation of CT operations to desired targets to improve consistency across CT operations.

The above goals can be approached by conducting data-collection trials from existing imaging operations using the methods described in Section [2](#mp13763-sec-0003), so that target performance values can be ascertained (e.g., the desired f <sub>50</sub> for a clinical CT system, protocol, or indication). The future direction of the material presented in this report falls along this pathway.

## 4 Performance Evaluation Software

Several of the testing methods described in the TG233 report and this associated paper require involved calculations. Although it is possible (and acceptable) for any willing physicist to write and implement their own code to do these calculations accordingly to the procedures described, it is understood that many clinical physicists do not have the resources or time to do so. A number of free software packages are available to assist in these tasks. A few examples of such software packages are listed below.
- imQuest: CT image analysis tool used to extract tube current modulation profiles and measure spatial resolution, noise properties, and quasi-linear task-based performance based on the methods in this report. The tool is designed to work with the CT ACR 464 and Mercury phantoms, but could be used with any phantoms with similar features. [http://deckard.mc.duke.edu/~samei/tg233.html](http://deckard.mc.duke.edu/~samei/tg233.html)
- iMRMC: Statistical analysis tool used to help do spatial domain task-based performance assessment. The tool helps size and analyze multi-reader multi-case (MRMC) reader studies. [https://github.com/DIDSR/iMRMC](https://github.com/DIDSR/iMRMC)
- iQModelo: Tool including parametric statistical methods for ROC performance analysis of linear model observers. [https://github.com/DIDSR/IQmodelo](https://github.com/DIDSR/IQmodelo)

## Acknowledgments

Authors gratefully acknowledge the input and refinements by Nicholas Bevins, Guang-Hong Chen, Dianna Cody, Eric Gingold, Loretta Johnson, David Jordan, Xiang Li, Jeffrey Limmer, Cynthia McCollough, Michael McNitt-Gray, and Christina Skourou.

## Conflict of Interest

Jiahua Fan is an employee of GE Healthcare. Lucretiu Popescu is an employee of Neusoft Medical Systems. Kirsten Boedeker and Jay Vaishnav are employees of Canon. Juan Carlos Ramirez Giraldo is an employee of Siemens Healthineers. Ehsan Samei, Duke University has a non-exclusive license agreement with the Sun Nuclear Corporation in commercializing the Mercury Phantom. His proceeds from the sale of the phantom are donated to the AAPM Research and Education fund.

## References

## Citing Literature

[Download PDF](https://aapm.onlinelibrary.wiley.com/doi/pdf/10.1002/mp.13763)

back

[^1]: <table><thead><tr><th>Attribute</th><th>Section</th><th>Metric</th><th>Definition</th></tr></thead><tbody><tr><td rowspan="6">Tube current modulation</td><td rowspan="6"><a href="#mp13763-sec-0003">2</a>.A</td><td><i>g <sub>mA</sub></i></td><td>Functional dependence of tube current on water equivalent diameter for a given phantom</td></tr><tr><td><i>g <sub>n</sub></i></td><td>Functional dependence of noise on water equivalent diameter for a given phantom</td></tr><tr><td>α, <i>R <sub>A</sub></i></td><td>Exponent and the correlation coefficient of ln(mA) = α(<i>d <sub>w</sub></i>) + β relationship, for a given phantom</td></tr><tr><td>s, <i>R <sub>n</sub></i></td><td>Slope and the correlation coefficient of n = s(<i>d <sub>w</sub></i>) + t relationship, for a given phantom</td></tr><tr><td><i>C <sub>mA</sub>, C <sub>noise</sub></i></td><td>Spatial concordance, in mm, of the distance between a discontinuous change in thickness and the anticipated change in mA or noise</td></tr><tr><td><i>d <sub>min</sub></i>, <i>d <sub>max</sub></i></td><td>Diameters associated with mA of the system reaching its maximum or its minimum value</td></tr><tr><td rowspan="4">Spatial resolution</td><td rowspan="4"><a href="#mp13763-sec-0011">2</a>.B</td><td><i>TTF <sub>n,C</sub></i></td><td>Task Transfer Function (TTF) at defined measured noise and contrast level in the in-plane direction</td></tr><tr><td><i>zTTF <sub>n,C</sub></i></td><td>Task Transfer Function (TTF) at defined measured noise and contrast level in the z-direction (i.e., trans-axial direction)</td></tr><tr><td><i>f <sub>50</sub></i> and <i>f <sub>10</sub></i></td><td>Frequencies associated with 50% and 10% of in-plane TTF, respectively</td></tr><tr><td><i>zf <sub>50</sub></i> and <i>zf <sub>10</sub></i></td><td>Frequencies associated with 50% and 10% of z-direction TTF, respectively</td></tr><tr><td rowspan="5">Noise</td><td rowspan="5"><a href="#mp13763-sec-0023">2</a>.C</td><td><i>n</i></td><td>Noise magnitude (pixel standard deviation) at three dose levels</td></tr><tr><td><i>NPS <sub>n</sub></i></td><td>Noise power spectrum (NPS) at defined noise levels</td></tr><tr><td><i>f <sub>P</sub></i> and <i>f <sub>A</sub></i></td><td>Peak and average frequencies of the NPS</td></tr><tr><td><i>NUI</i></td><td>Noise nonuniformity index</td></tr><tr><td><i>η</i></td><td>Noise inhomogeneity index</td></tr><tr><td rowspan="2">Quasi-linear task-based performance</td><td rowspan="2"><a href="#mp13763-sec-0036">2</a>.D</td><td><i>d′</i></td><td>Detectability index for the detection of a target signal (e.g., 1, 5, and 10 mm circular signal having a specific contrast and contrast-profile) for a specific phantom size and noise or dose level</td></tr><tr><td><i>e′</i></td><td>Estimability index for estimating the volume of a target signal (e.g., 10 mm spherical signal having a specific contrast and contrast-profile) for a specific phantom size and noise or dose level</td></tr><tr><td rowspan="3">Spatial domain task-based performance</td><td rowspan="3"><a href="#mp13763-sec-0044">2</a>.E</td><td><i>LR</i></td><td>Localization success rate for identifying the presence of and location of a targeted signal</td></tr><tr><td><i>A <sub>LROC</sub></i></td><td>Area under the localization relative operating characteristic (LROC) curve for targeted localization tasks</td></tr><tr><td><i>A <sub>EFROC</sub></i></td><td>Area under the exponential transformed free response operating characteristic (EFROC) curve for targeted free-response detection tasks</td></tr></tbody></table>

[^2]: <table><thead><tr><th>Nomenclature <a href="#mp13763-note-0001_23">a</a></th><th>CTDI (mGy) (32 cm phantom)</th><th>Tube potential (kV)</th><th>Tube current (mA)</th><th>Mode, pitch</th><th>Reconstruction</th></tr></thead><tbody><tr><td>TG233-F1</td><td>0.75</td><td rowspan="6">120</td><td rowspan="9">Fixed mA to achieve target CTDI ± 10%</td><td rowspan="6">Helical, ~1</td><td rowspan="13">FBP, IR at medium strength, higher than medium strength, and maximum strength settings “standard” kernel ~ 0.6 and 5 mm image thickness</td></tr><tr><td>TG233-F2</td><td>1.5</td></tr><tr><td>TG233-F3</td><td>3.0</td></tr><tr><td>TG233-F4</td><td>6.0</td></tr><tr><td>TG233-F5</td><td>12.0</td></tr><tr><td>TG233-F6</td><td>24.0</td></tr><tr><td>TG233-F3LK</td><td>3.0</td><td>70 (or 80)</td><td rowspan="3">Helical, ~1, unless a lower pitch is needed to achieve the CTDI</td></tr><tr><td>TG233-F3MK</td><td>3.0</td><td>100</td></tr><tr><td>TG233-F3HK</td><td>3.0</td><td>150 (or 140)</td></tr><tr><td>TG233-M2</td><td>1.5</td><td rowspan="3">120</td><td rowspan="3">TCM setting to achieve target CTDI ± 10%</td><td rowspan="3">Helical, ~1</td></tr><tr><td>TG233-M3</td><td>3.0</td></tr><tr><td>TG233-M4</td><td>6.0</td></tr><tr><td>TG233-M3-A</td><td>3.0</td><td>120</td><td>Same as above</td><td>Axial</td></tr></tbody></table>

- <sup><i>a</i></sup> F refers to fixed mA, M to tube current modulation (TCM), 1–6 to dose setting, and LK, MK, HK to low, medium, and high kV settings, respectively.

[^3]: ![urn:x-wiley:00942405:media:mp13763:mp13763-math-0045](https://aapm.onlinelibrary.wiley.com/cms/asset/b28e74e6-b09b-48b4-a2e7-4fc3c1dd9d7b/mp13763-math-0045.png)

urn:x-wiley:00942405:media:mp13763:mp13763-math-0045

(8)

*r* *C* ![urn:x-wiley:00942405:media:mp13763:mp13763-math-0046](https://aapm.onlinelibrary.wiley.com/cms/asset/206fe7d4-b78b-4ef3-b065-136dc36d5dce/mp13763-math-0046.png) *D* *n*