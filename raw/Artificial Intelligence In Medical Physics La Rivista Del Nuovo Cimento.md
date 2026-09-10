---
title: "Artificial intelligence in medical physics - La Rivista del Nuovo Cimento"
source: "https://link.springer.com/article/10.1007/s40766-025-00073-4"
author:
  - "[[N Amoroso|N. Amoroso]]"
  - "[[R Errico|R. Errico]]"
  - "[[E Pantaleo|E. Pantaleo]]"
  - "[[A Monaco|A. Monaco]]"
  - "[[R Bellotti|R. Bellotti]]"
published: 2025-08-26
created: 2026-08-25
description: "Artificial intelligence (AI) has profoundly transformed medical physics across its entire spectrum. Starting from data acquisition, AI has introduced innov"
tags:
  - "clippings"
---
## Abstract

Artificial intelligence (AI) has profoundly transformed medical physics across its entire spectrum. Starting from data acquisition, AI has introduced innovations in the processing of imaging data, including denoising and image enhancement. It plays a key role in diagnosis by maximizing the informational content of medical data and supporting clinical decision-making, enhancing both interpretability and transparency through the emerging field of Explainable AI. AI has made significant contributions in areas such as radiotherapy planning optimization, real-time monitoring, and dosimetry, thereby accelerating simulations, reducing errors, and enhancing treatment precision. In the field of interventions, AI is guiding robotic-assisted surgery and intraoperative procedures, enhancing both accuracy and safety. Moreover, AI is streamlining hospital workflows, automating reporting, and enabling operational intelligence. Collectively, these advancements are improving efficiency, accuracy, and patient outcomes, while safeguarding the indispensable role of human care in medicine. This review tries to explore the key advancements enabled by AI in medical physics following the pathway from data acquisition to diagnosis, therapy, and intervention. Looking ahead, personalized care, enabled by digital twins, will make treatments more precise and less invasive. At the same time, generative AI will support healthcare professionals by automating routine tasks, allowing them to focus more on patient relationships and the human side of care.

## 1 Introduction

Medical Physics represents a vast and diverse research and professional field \[[^1],[^2],[^3],[^4],[^5]\], and providing an in-depth review of all topics and areas where artificial intelligence (AI) finds application would inevitably risk being incomplete. In this review, the focus will be on three key domains, namely imaging\, diagnostics, and intervention, following the typical clinical pathway that progresses from data acquisition for diagnostic purposes to therapeutic evaluation and interventional procedures, all within the framework of subject-specific, i.e., personalized healthcare. Medical imaging is, in fact, the first area where typical physics methodologies have found flourishing application \[[^6],[^7],[^8],[^9]\]. MRI, in particular, represents a notable example of how these methodologies have been successfully applied, not only in signal formation but also in sophisticated data pre-processing techniques such as filtering, cleaning, and denoising, as well as in advanced modeling for signal processing and knowledge extraction \[[^10],[^11],[^12],[^13],[^14]\]. Beyond MRI, medical physics plays a central role in the development and refinement of other imaging techniques, including computed tomography (CT) \[[^15],[^16],[^17]\], positron emission tomography (PET) \[[^18], [^19]\], and ultrasound \[[^20],[^21],[^22]\], each of which relies on physics-based principles for image acquisition, processing, and interpretation.

The use of AI has led to unprecedented innovations, bringing accuracy, precision, and reliability to levels that were unimaginable just a few decades ago, opening the way to new diagnostic and therapeutic possibilities. The precision and accuracy of AI-driven methodologies, combined with their computational advantages—such as increased processing speed, workflow automation, and enhanced robustness—are of critical importance in contemporary medical practice \[[^23],[^24],[^25],[^26],[^27],[^28]\]. These innovations not only improve efficiency but also support clinical decision-making with greater consistency and reliability. Moreover, the frontiers of personalized medicine \[[^29],[^30],[^31]\] place new demands on these tools, requiring them to integrate broader and more complex datasets that extend beyond traditional clinical parameters. This includes contextual information, such as genetic profiles and environmental factors \[[^32],[^33],[^34],[^35]\], enabling more tailored diagnostic and therapeutic strategies. Additionally, the integration of AI into emerging technologies like robotics and virtual reality is reshaping surgical and interventional practices. These advancements are enabling the development of intelligent, supportive systems for clinicians, including applications, such as patient-specific digital twins for preoperative planning and intraoperative navigation \[[^36],[^37],[^38],[^39],[^40]\].

To explore these transformative developments in greater depth, this review is organized into three major sections, namely imaging\, diagnostics, and intervention, each corresponding to a key stage in the clinical workflow where AI is reshaping practice through enhanced precision, integration, and decision support.

## 2 Imaging

### 2.1 Denoising medical images

The enhancement of image quality in medical imaging has become a highly innovative field, largely driven by the integration of AI. Traditional denoising methods, such as spatial filters \[[^41], [^42]\], Fourier and Wavelet analyses \[[^43], [^44]\], and statistical approaches like Bayesian models \[[^45],[^46],[^47]\], have laid a strong foundation for these advancements. However, these techniques often suffer from limitations, such as loss of structural information\, decreased contrast, and reduced resolution \[[^48]\].

In contrast, AI-based methods, especially those employing deep learning models, have demonstrated considerable promise \[[^14], [^49],[^50],[^51],[^52],[^53],[^54],[^55]\]. Unlike classical approaches, which perform well in removing simple, unstructured noise (e.g., Gaussian noise), AI models excel in handling complex, context-dependent noise patterns. This makes them especially effective in addressing artifacts commonly found in medical imaging, caused by patient movement during data acquisition, or resulting from intrinsic limitations of the imaging device.

For example, in CT scans, common artifacts include streaks or dark bands between dense structures and low-dose noise, both of which can significantly degrade image quality\[[^56],[^57],[^58],[^59],[^60],[^61],[^62]\]. Similarly, in PET imaging\, dense structures such as bones or metal implants can influence signal distribution, leading to artifacts that alter image reconstruction. In ultrasound imaging, it is common to encounter reverberation artifacts, typically caused by ultrasound reflections between highly reflective surfaces, or acoustic shadowing, which occurs when particularly dense anatomical structures, such as bones, block the passage of ultrasound waves; additionally, speckle noise, a granular interference pattern, is a pervasive artifact that reduces contrast and obscures fine details speckle noise in ultrasound imaging \[[^63]\]. In MRI, artifacts, such as image distortion and signal loss, are commonly caused by patient movement or magnetic field inhomogeneities \[[^14], [^64], [^65]\].

**Fig. 1**

![Fig. 1](https://media.springernature.com/lw685/springer-static/image/art%3A10.1007%2Fs40766-025-00073-4/MediaObjects/40766_2025_73_Fig1_HTML.png?as=webp)

[Full size image](https://link.springer.com/article/10.1007/s40766-025-00073-4/figures/1)

Autoencoder-based denoising consists of three phases: (i) data are encoded (ii) to learn a compact representation of data in the so-called latent space where (iii) noise is removed. Noise is intended here as redundant or unnecessary information which can be safely removed from latent space without impairing the data representation

Thanks to their inherently data-driven nature, AI techniques can learn directly from imaging data, allowing them to adapt to a broader and more diverse array of noise types and artifacts than traditional approaches. In this regard, autoencoders deserve a special mention. Autoencoders are a type of neural network specifically designed for unsupervised learning. Fundamentally, autoencoders operate through a two-phase process: first, they compress the input data by learning a representation (encoder), then they reconstruct it by removing noise and preserving essential features (decoder), see Fig. [1](https://link.springer.com/article/10.1007/s40766-025-00073-4#Fig1) for a schematic overview. The encoder reduces the dimensionality of the input data trying to extract its most relevant features, then relies on this reduced representation to remove unwanted noise while minimizing the loss of details and structural information \[[^66], [^67]\]. Among the most commonly used autoencoders in the medical field are Variational Autoencoders (VAE) and Denoising Autoencoders (DAE) \[[^68],[^69],[^70],[^71],[^72]\]. Their use has become essential for CT, MRI, and PET. Valid alternatives to autoencoders leverage well-established deep learning architectures, such as convolutional neural networks (CNNs) or U-NET and its variants, for purely denoising purposes \[[^73],[^74],[^75],[^76]\].

Finally, extremely popular tools, such as transformers, generative adversarial networks (GANS), and recurrent neural networks, have been successfully applied to to medical image denoising\, demonstrating strong performance across various modalities \[[^77],[^78],[^79],[^80],[^81],[^82]\]. In addition, semi-supervised methods, such as Noise2Void and Noise2Self, have gained traction due to their ability to produce clean images without requiring clean data during training. This characteristic makes them particularly well-suited for clinical settings, where obtaining high-quality reference images is often difficult or impractical \[[^83],[^84],[^85]\].

### 2.2 Super-resolution for enhanced diagnostic detail

AI offers powerful tools for enhancing imaging data, particularly in terms of resolution. Among these, AI-based super-resolution stands out as a transformative advancement in medical imaging, enabling the reconstruction of high-resolution images from low-resolution acquisitions, a common scenario in clinical settings. \[[^52], [^86], [^87]\]. These advances are particularly beneficial in the diagnostic field as they allow radiologists to analyze more detailed and accurate images and reduce the risk of interpretation errors, and increase the precision in detecting anomalies or pathologies. In particular, the integration of AI into super-resolution techniques has a significant impact in low-dose imaging contexts; to this aim, the ALARA principle (patient dose As Low As Reasonably Achievable) deserves a particular mention \[[^88]\]. A notable example concerns low-dose CT, which is often used for cancer screening or cardiologic applications \[[^89], [^90]\]. In these situations, AI helps compensate for reduced image quality caused by lower radiation exposure, improving readability and ensuring high-quality results while optimizing the use of available resources without compromising patient safety.

Among the most popular and well-established approaches is the Super-Resolution Convolutional Neural Network (SRCNN) \[[^91]\], which is based on a convolutional architecture, and GANs \[[^92], [^93]\], which combine two neural networks (a generator and a discriminator) to progressively enhance the quality of the reconstructed image, see Fig. [2](https://link.springer.com/article/10.1007/s40766-025-00073-4#Fig2) as an example.

**Fig. 2**

![Fig. 2](https://media.springernature.com/lw685/springer-static/image/art%3A10.1007%2Fs40766-025-00073-4/MediaObjects/40766_2025_73_Fig2_HTML.png?as=webp)

[Full size image](https://link.springer.com/article/10.1007/s40766-025-00073-4/figures/2)

GAN twofold architecture can be exploited for super-resolution. First, high-resolution data are used to improve the resolution of low-resolution data with the help of a generator. Then generated images feed a discriminator which tries to distinguish between a super-resolution and high-resolution image and generate the adversarial loss which will be used for learning

Transformers, such as SwinIR (Swin Transformer for Image Restoration) \[[^94]\], are emerging as cutting-edge technologies for super-resolution, offering in some cases superior results compared to CNNs and GANs. Other approaches worth mentioning include VAEs \[[^14], [^95], [^96]\], and Deep Laplacian Pyramid Super-Resolution Networks (LapSRNs) \[[^97]\]. LapSRNs use a pyramid structure to generate progressively higher resolution images, reducing the risk of artifacts and improving anatomical detail. Finally, for cases involving highly correlated image frames, such as ultrasound sequences or MRI scans acquired at different times, neural networks specifically designed for sequential data analysis, such as Recurrent Neural Networks (RNNs) \[[^98],[^99],[^100]\] and Long Short-Term Memory (LSTM) networks \[[^101],[^102],[^103]\], can be adopted. In addition to the techniques mentioned above, one of the most promising and innovative approaches recently introduced is Physics-Informed Neural Networks (PINNs) \[[^104],[^105],[^106]\]. By integrating physical models into learning algorithms, PINNs can offer greater robustness and generalization, also reducing computational times and the number of instances required by learning. Furthermore, PINNs are more interpretable as they are based on physical and biological constraints.

### 2.3 Normalization, standardization, and harmonization for medical purposes

In the medical field, managing and analyzing large volumes of data is often essential. These datasets are frequently marked by substantial heterogeneity, stemming from factors, such as the use of different imaging scanners, variations in acquisition protocols, and other clinical or technical differences. Beyond intrinsic differences in data acquisition, medical imaging must also account for the variability arising from biological differences, which can be further exacerbated by the presence of pathological conditions. Therefore, in addition to data curation techniques aimed at denoising and enhancing the informative content, it is essential to develop dedicated approaches that enable meaningful and fair comparison.

This need becomes particularly critical in context involving multi-center datasets, such as international research initiatives aimed at studying major diseases like Alzheimer’s \[[^107]\] or Parkinson’s \[[^108]\], as well as global challenges designed to benchmark and compare algorithms and strategies for clinical data analysis \[[^109],[^110],[^111],[^112]\]. For this reason, over the past decade, extensive literature has emerged focusing on this topic, a particularly striking example being data harmonization \[[^113], [^114]\]. See TABLE [1](https://link.springer.com/article/10.1007/s40766-025-00073-4#Tab1) for an overview of multi-centric data commonly used in medical imaging.

**Table 1 Some notable examples of multi-centric imaging initiatives**

Primarily, normalization and standardization in medical imaging operate on pixel intensities in 2D images or voxel intensities in 3D volumes. Early normalization approaches largely relied on statistical techniques: by analyzing the intensity distribution of an image, values could be rescaled to fixed ranges, and the distributions adjusted by estimating statistical moments \[[^122], [^123]\]. Clearly, global approaches, such as the statistical methods, fail to account for local effects and may introduce unwanted artifacts as a result.

Similar to normalization techniques, but with a more structured approach, standardization methods modify image intensities to conform images with predefined, universally accepted parameters, thus reducing the arbitrariness inherent in normalization. The establishment of standards in medical imaging has always been a critical focus \[[^124], [^125]\]. For example, this can be particularly relevant in radiomics (see Sect. [3.2](https://link.springer.com/article/10.1007/s40766-025-00073-4#Sec9)), where ensuring the consistency of image features across different scanners is essential for reliable analysis and comparison \[[^126], [^127]\]. Likewise, in oncology, the use of international standards for image annotation and calibration helps guarantee a reproducible assessment of lesions \[[^128]\].

VAEs and GANs, previously highlighted for their effectiveness in denoising and image enhancement, also demonstrate significant versatility in normalization and standardization tasks. A notable example of this is CycleGANs (Cycle-Consistent GANs), which have been successfully applied in these contexts (Cycle-Consistent GANs) \[[^129], [^130]\]. CycleGANs consist of two generative networks ($G: A \rightarrow B$ and $F: B \rightarrow A$) and two discriminators ($D_A$ and $D_B$), which distinguish images from different scanners and exploit a normalization mapping which does not excessively alter the original features; in fact, CycleGANs employ a consistency loss enforcing that an image converted to another domain and then back to the original should remain as similar as possible to the initial input.

Unlike normalization and standardization, which focus solely on image intensity, harmonization expands the perspective by considering the broader context, leading to a true paradigm shift where all available variables are taken into account. Several techniques enable harmonization. Style Transfer allows adaptation of an image’s style (e.g., pixel intensity and texture) to match a reference dataset while preserving anatomical features \[[^131], [^132]\]. Federated Learning enables medical image harmonization without sharing sensitive data between institutions \[[^133], [^134]\]. AI models are trained locally on different datasets and collaboratively updated, enhancing consistency across acquisitions without centralizing data. Of course, VAEs, GANs, Transformers, and CNNs can be adapted for these tasks. For instance, the generative adversarial domain adaptation and domain-adapted U-Nets are used for harmonization \[[^135],[^136],[^137],[^138]\].

### 2.4 Image registration

Another essential type of normalization in medical imaging is spatial normalization, more commonly referred to as image registration. This process is essential for aligning images acquired at different time points, using different modalities or perhaps most importantly from different patients. Accurate registration is fundamental for monitoring disease progression as it ensures that variations in positioning do not obscure clinical assessment, such as tracking the evolution of oncological lesions. Additional key applications include multi-modal analyses, where data from different imaging techniques (e.g., CT, MRI, and PET) must be precisely aligned to support accurate diagnosis, as well as image-guided surgery, where the overlay of preoperative and intraoperative images is essential for improving surgical precision.

Deep neural networks have become the predominant approach in AI-based image registration \[[^139]\]. Despite employing a variety of architectures and learning strategies, both supervised and unsupervised, AI-based registration methods are fundamentally grounded in deep neural networks. For example, CNNs have been used for the registration of abdominal MRI \[[^140]\] or lung CT \[[^141]\]. U-Nets have been used for MRI registration of hepatic vasculature \[[^142]\]. VoxelMorph \[[^143]\] is another important tool for medical image registration adopting a deformable framework. For example, it has been used for kidney \[[^144]\] and cortex registration \[[^145]\]. Other notable examples involve transformers \[[^146]\], VAEs \[[^147]\], and GANs \[[^148]\]. Deep Reinforcement Learning (DRL) has shown promising applications for multi-modal image registration in intraoperative registration \[[^149]\] and ultrasound imaging \[[^150]\]. Finally, Spatial Transformer Networks (STNs) have been integrated for structure-guided image registration or assist in automatic alignment in radiotherapy treatment \[[^151]\].

To this already extensive, though certainly not exhaustive, list of approaches, more recent strategies based on PINNs have also been added \[[^152]\]. Some interesting studies have used PINNs to enhance medical flow magnetic resonance imaging \[[^106]\]. In addition, PINNs have been experimented with myocardial perfusion MRI quantification \[[^153]\] and image-guided neurosurgery \[[^154]\]. Similarly, Graph Neural Networks (GNNs) are increasingly gaining attraction in research \[[^155]\]. GNNs have been used to register with several modalities, e.g., chest X-ray images \[[^156]\], lung CTs \[[^157]\], brain MRI and multi-modal studies \[[^158]\].

## 3 Diagnostics

### 3.1 Image segmentation: a first step toward diagnostics

Segmentation in medical imaging is a critical step, fundamental to quantitative analysis across all imaging modalities. It enables the identification and precise delineation of anatomical or functional structures within an image. Traditionally, this task has been carried out by human experts through manual contouring, a highly labor-intensive and time-consuming process that, in many cases, remains in use today \[[^159],[^160],[^161],[^162],[^163],[^164]\]. With the advent of AI techniques, automated segmentation methods have gained increasing relevance. Of course, human operators still play a crucial role, especially in cases where algorithms require ground truth data, namely segmentation masks. Nonetheless, unsupervised or semi-supervised approaches can significantly speed up the process.

Segmentation is not only required for morphological assessment; it is also a fundamental step for diagnostic purposes. For example, segmented volumes and surfaces can be used to train decision support systems, outline pathological conditions, or stage diseases \[[^165],[^166],[^167]\]. Moreover, segmentation can play a crucial role in patient therapy, especially in radiotherapy applications \[[^168], [^169]\]. In oncology, precise tumor segmentation is a prerequisite for an accurate assessment of its size and response to treatment. More recently, in the field of assisted surgery, automated segmentation strategies paved the way to innovative surgical procedures \[[^170],[^171],[^172]\].

The most widely adopted AI techniques leverage CNN architectures mimicking the decision-making processes of human experts. Fully Convolutional Networks \[[^173], [^174]\], which replace the fully connected layers of CNNs with convolutional layers, enabling pixel-level segmentation\, deserve a particular mention. Attention-based CNNs and Transformers networks offer valid alternatives \[[^175],[^176],[^177],[^178],[^179],[^180]\]. TransUNet, which combines U-Net and Transformer architectures, can be used to segment fine structures such as blood vessels in ocular images \[[^181]\] or thyroid nodules in ultrasound images \[[^182]\]. Trained U-Nets, such as TotalSegmentator \[[^183]\] and TotalSegmentator MRI \[[^184]\], have been employed to segment multiple anatomic structures in CT and MRI images, respectively. In addition to traditional supervised approaches mentioned above, unsupervised methods have also gained traction in various cases. Autoencoders, for instance, have been applied in MRI studies to outline segmentation anomalies \[[^185]\], while self-supervised models, which learn to segment without labeled data using contrastive learning or pre-training on unlabeled datasets, have been employed for organ segmentation of abdominal CT and MRI images \[[^186]\] or multi-view applications such as cardiac segmentation \[[^187]\].

In recent years, physics-informed models have also emerged in the field of segmentation, offering promising advancements, particularly in applications such as brain MRI \[[^188]\]. In the cardiac domain, PINNs have been developed for 3D segmentation of the left ventricle \[[^189]\]. By incorporating physical constraints, these algorithms draw inspiration from active contour models and use cubic splines to provide fast and interpretable segmentation without requiring labeled data. Physics-informed FAS-U-Net (Finite-Analysis-Solving U-Net) networks combine deep learning principles with variational methods and numerical analysis, making them suitable for medical imaging applications \[[^190]\]. Also, PINNs have been adopted for tumor segmentation in PET scans, ensuring greater precision in delineating tumor masses, an essential requirement for radiotherapy planning and clinical follow-up \[[^191]\]. Despite their novelty, physics-informed models are a promising research field that will influence novel medical imaging applications.

**Fig. 3**

![Fig. 3](https://media.springernature.com/lw685/springer-static/image/art%3A10.1007%2Fs40766-025-00073-4/MediaObjects/40766_2025_73_Fig3_HTML.png?as=webp)

[Full size image](https://link.springer.com/article/10.1007/s40766-025-00073-4/figures/3)

Radiomics enables the extraction of a wide range of features, such as shape, intensity, and texture, that are highly representative of underlying tissue characteristics. These features are then used to inform a decision support system, which is often integrated with an explainability framework to enhance transparency and clinical interpretability

### 3.2 From radiomics to decision support systems

Segmentation is a critical first step in extracting morphometric features, such as surface areas, shapes, and volumes, which can subsequently be used for diagnostic and prognostic purposes. Through advancements in segmentation techniques, AI has significantly enhanced the ability to access diagnostically relevant information from medical images. This capability forms the foundation of radiomics, a field dedicated to the extraction and analysis of quantitative features from medical imaging modalities, such as CT, MRI, and PET \[[^192], [^193]\]. Radiomics leverages machine learning and deep learning algorithms to uncover patterns and biomarkers that may not be visible to the human eye, thereby supporting a more personalized diagnostic approach, one of the key pillars of precision medicine. A typical radiomics workflow is illustrated in Fig. [3](https://link.springer.com/article/10.1007/s40766-025-00073-4#Fig3). Traditionally, radiomics relies on statistical methods to extract features such as statistical moments or more sophisticated characteristics, such as texture and shape, usually referred to as handcrafted radiomics. For instance, from the Gray-Level Co-occurrence Matrix (GLCM), which quantifies spatial relationships between pixel intensities, texture features such as the Haralick features can be derived \[[^194]\]. Similarly, the Gray Level Run Length Matrix (GLRLM) captures the length and distribution of consecutive pixels with the same intensity, enabling the analysis of texture granularity \[[^195]\]. Mathematical transformations can reveal patterns that would otherwise be difficult to detect. Examples include Gabor filters \[[^196]\], Fourier \[[^197]\] and wavelet filters \[[^198]\]. The application of these techniques involves the extraction of an exponential number of features. Hence, feature selection algorithms, such as LASSO (Least Absolute Shrinkage and Selection Operator) \[[^199]\], ReliefF \[[^200]\], Recursive Feature Elimination \[[^201]\], and Boruta \[[^202]\], have gained increasing attention.

A key limitation of traditional statistical feature extraction is its reliance on subjective choices regarding which features to compute. However, it is important to mention that important efforts have been accomplished, e.g., with the Image Biomarker Standardization Initiative (IBSI) guidelines \[[^203]\], which focus on standardizing radiomics by providing clear definitions for image features and recommending uniform image pre-processing. The most significant innovation introduced by AI in this domain is the ability of algorithms to autonomously learn and extract the most relevant features from medical images for specific tasks. CNNs \[[^204]\] and autoencoders \[[^205]\] are commonly used to learn compact, informative image representations. More advanced architectures, such as 3D ResNets, extensions of the classic ResNet models adapted for volumetric data, are particularly effective for processing CT and MRI scans \[[^206]\]. Additionally, transformer-based models divide images into patches and treat them as sequences of tokens, allowing the model to capture both local and global spatial relationships \[[^207]\].

These advances pave the way for significant improvements in Diagnostic Support Systems (DSSs), which are trained using data as their knowledge base, thus enhancing the possibility of learning increasingly complex patterns from medical images and open novel perspectives in our understanding of pathological processes. DSSs are now ubiquitous in the medical field and represent without doubt the most important field where AI applications have disruptively changed clinical practice. When thinking of a DSS, one typically envisions a diagnostic support tool; in fact, the literature is utterly rich with such applications, often achieving remarkable success.

Although of great impact\, diagnostic support is neither the only nor the most important field where DSS provide a significant contribution. In fact, DSS play a crucial role in applications related to personalized medicine \[[^208]\], such as optimizing radiotherapy treatment \[[^209]\] or supporting pharmacological evaluations \[[^210]\], for example to optimize dosages, reducing side effects and improving therapeutic outcomes. In hospital triage, intelligent algorithms quickly assess symptoms to direct patients to the most appropriate treatment \[[^211]\] while in intensive care units, they monitor vital parameters to predict clinical deterioration and prevent complications \[[^212]\].

Technical advances in feature extraction, representation learning, and model development have enabled a wide range of impactful clinical applications. Radiomics-based pipelines and deep learning architectures now form the core of many Diagnostic Support Systems used in practice. In particular, these systems have been successfully deployed across multiple specialties, from oncology and cardiology to neurology and critical care\, demonstrating how data-driven models can support earlier and more accurate diagnoses, improve patient stratification, and assist in treatment planning. In oncology\, deep learning approaches have been adopted to detect lung nodules \[[^115], [^213]\], enabling earlier and more accurate diagnoses compared to manual analysis; they help accurately identify cardiovascular diseases \[[^214]\], reducing the risk of severe events, or diabetic retinopathy \[[^215]\] and macular degeneration \[[^216]\], facilitating early diagnosis and lowering the risk of progression to blindness. AI-driven MRI analysis is nowadays a standard approach for neurodegenerative diseases, such as Alzheimer’s and Parkinson’s disease \[[^217],[^218],[^219]\]. Additionally, automated systems analyze clinical and laboratory data to detect severe infections like sepsis at an early stage \[[^220]\].

It is worth to underline how these applications highlight that AI is not intended to replace human experts but rather to support their decisions. As a result, over the last decade, research has increasingly focused on making AI models, their decisions, and underlying mechanisms more interpretable and transparent to the users.

### 3.3 Explainable artificial intelligence

EXplainable Artificial Intelligence (XAI) is fundamentally concerned with making the learning process and decisions of AI models understandable \[[^221], [^222]\]. Of course, this is of utterly importance in life science applications and in clinical practice, making the adoption of XAI frameworks extremely popular in medical physics \[[^223],[^224],[^225],[^226]\]. Some models are inherently explainable, for example\, decision trees, where each decision, as well as the entire model, can be translated into a clear set of rules and transparent decision-making processes. Unfortunately, more explainable algorithms tend to be less accurate, whereas model accuracy tends to increase with complexity \[[^227]\].

Although this topic has always been of interest, also in relation to classic algorithms such as Random Forests, Support Vector Machines, etc., leading to a rich body of literature on feature importance \[[^228],[^229],[^230],[^231]\], it is with deep learning that explainability has become crucial. Deep learning models, which have become the benchmark across all sectors and applications, have made the decision-making process highly opaque, often earning the notorious label of “black box” \[[^232], [^233]\].

The most important XAI techniques include post hoc methods, such as LIME (Local Interpretable Model-agnostic Explanations) and SHAP (Shapley Additive Explanations), which provide both global and local interpretations of models \[[^234], [^235]\]. Global explanations refer to importance maps, similar to traditional feature importance techniques, offering an overview of how models act on a dataset as a whole. Local explanations, on the other hand, focus on individual instances, providing a detailed breakdown of how the model assigns a specific score to each instance and reaches a decision, see Fig. [4](https://link.springer.com/article/10.1007/s40766-025-00073-4#Fig4) SHAP explanations.

**Fig. 4**

![Fig. 4](https://media.springernature.com/lw685/springer-static/image/art%3A10.1007%2Fs40766-025-00073-4/MediaObjects/40766_2025_73_Fig4_HTML.png?as=webp)

[Full size image](https://link.springer.com/article/10.1007/s40766-025-00073-4/figures/4)

Global explanations (left panel) provide an overall picture: each point represents a data entry, features are ranked according to their importance from the most important to the least one; the color code denotes the feature values from low values (blue) to high values (red). Local explanations (right panel) are entry-specific explanations; each feature contributes to the classification score according to its specific impact on that data entry

One of the main drawback of these techniques is that they can lack easy interpretability in image analysis. Moreover, while these approaches are extremely useful for models with an explicit feature extraction phase, where each feature is included in the model to convey specific information they can be less effective when feature extraction is embedded, as is common in deep learning. To address this, alternative techniques have been proposed such as Grad-CAM (Gradient-weighted Class Activation Mapping) \[[^236]\], CAM (Class Activation Mapping) \[[^237]\], Layer-wise Relevance Propagation \[[^238]\] and its variant DeepLIFT (Deep Learning Important FeaTures) \[[^239]\], which highlight the most influential image regions in activating a specific class. Integrated Gradients assign importance to input features based on the model predictions by calculating how they act on the gradient \[[^240]\]. The following Fig. [5](https://link.springer.com/article/10.1007/s40766-025-00073-4#Fig5) shows an example of how these methods can highlight the regions of interest within the image.

**Fig. 5**

![Fig. 5](https://media.springernature.com/lw685/springer-static/image/art%3A10.1007%2Fs40766-025-00073-4/MediaObjects/40766_2025_73_Fig5_HTML.jpg?as=webp)

[Full size image](https://link.springer.com/article/10.1007/s40766-025-00073-4/figures/5)

A figurative illustration of gradient based explanations. Gradients computed across the convolutional layers of a deep neural network are averaged to get weights for each feature map. The weighted feature maps are then summed and passed through a rectifying unit to keep only the positive contributions of the feature maps to the target class score. Finally, the feature maps are upsampled to the input image size, highlighting the regions most relevant for the class prediction

When an image goes through a CNN, each convolutional layer consists of filters specifically designed to outline different patterns, such as edges or textures. Each filter produces a corresponding feature map that highlights the presence of a specific pattern in the input. During the backward pass, after the prediction, gradients of the class score with respect to each feature map are computed. These gradients show how sensitive the class score is to changes in the feature maps and, therefore, they can be used to understand which regions of the image contributed most to the prediction for that class.

## 4 Intervention

### 4.1 Radiotherapy

External beam radiotherapy is one of the most common treatments for cancer, using high-energy radiation to destroy cancer cells. Its effectiveness depends on the precision with which the beams are directed at the tumor, while minimizing damage to the surrounding healthy tissue. In recent years, AI has begun to play a key role in improving this treatment, leading to significant advancements in precision, personalization, and speed. As mentioned before, CNNs and transformer-based models are refining the automated segmentation of at-risk organs and lesions, thus improving treatment safety. Transformers have recently been applied to treat difficult at-risk organs and lesions, such as those affecting head and neck \[[^241]\].

Another area where AI provides significant enhancement is real-time monitoring during radiotherapy. Imaging technologies like CT or MRI are used to monitor the tumor’s position and its response to treatment. Artificial intelligence can analyze these images in real-time, adjusting the treatment if the tumor shifts or changes over time, such as due to patient breathing movements. The ability to have precise, immediate monitoring allows doctors to make real-time adjustments, further enhancing precision and reducing the risk of damage to healthy tissues.

Predicting treatment response is crucial in the medical field because it allows for the optimization of therapies for each patient, improving effectiveness and reducing side effects. By analyzing medical images and clinical metadata, it is possible to identify predictive biomarkers for response to radiotherapy\, drugs, and immunotherapy \[[^242],[^243],[^244],[^245]\]. By integrating clinical, genomic, and imaging data, AI models optimize treatment planning, support the development of tailored therapeutic strategies and help predict individual patient responses \[[^246], [^247]\]. These approaches naturally lead to personalization of treatments, trying to recommend the most effective therapies and, therefore, to improve the quality of life. Furthermore, they support the healthcare system as a whole, for example empowering the recruitment in clinical trials \[[^248]\] or accelerating the development of new therapies \[[^249]\].

Finally, it must be kept in mind that, while radiotherapy treatments are fundamentally important, they inherently have toxic effects that must be minimized. For this reason, stringent Quality Assurance (QA) procedures are crucial to ensuring that radiation therapy is delivered with the highest precision, safety, and effectiveness \[[^250]\]. QA includes quality control of linear accelerators, verification of treatment plan accuracy, monitoring of administered doses, and calibration of imaging systems used for tumor localization.

### 4.2 Dosimetry

Dosimetry is the discipline that measures and calculates the dose absorbed by tissues during exposure to ionizing radiation, with the goal of ensuring therapeutic effectiveness and patient safety. Accurately measuring the dose delivered by a therapy, as well as exposure to both natural and artificial radiation, has direct implications for human health.

In radiotherapy\, dosimetry plays a critical role in ensuring that the prescribed dose is accurately delivered to the tumor while minimizing exposure to surrounding healthy tissues and organs at risk. In this case, the primary goal is to minimize errors, optimize therapeutic effectiveness, and reduce the risk of side effects in patients. In the medical field, radiotherapy needs are accompanied by those of nuclear medicine, where patients are exposed to radionuclides. In any case, the primary tool remains the Monte Carlo simulation handle nearly the entire dosimetric chain, from beam simulation to radiation–matter interactions, including trajectory tracking and dose calculation \[[^251], [^252]\]. Advances, particularly in computational power, have made Monte Carlo simulations increasingly affordable, reducing computational and time requirements. The introduction of AI has had an immediate and significant impact on the computational efficiency of Monte Carlo methods \[[^253]\]. Deep learning techniques can be used to approximate particle transport \[[^254]\], significantly reducing computation time, or to generate realistic scenarios both in terms of sources and detector response \[[^255]\]. Monte Carlo methods are known to be computationally intensive, and available computing resources do not always meet their demands. Therefore, AI has played a crucial role in making these techniques more accessible without requiring extremely high computing power.

Furthermore, AI models allow for real-time monitoring and calibration of the administered dose \[[^256]\]. GANs are used for synthesizing high-quality images and improving dose planning by generating more precise distributions \[[^257]\]. Deep learning algorithms can optimize dose distribution \[[^89], [^258], [^259]\], reducing the time required for planning and improving adaptation to anatomical changes in patients. Multi-objective optimization algorithms enable automatic balancing of concurrent goals, such as maximizing the dose to the tumor while minimizing the dose to healthy organs; even in this case\, deep learning seems to provide notable advantages \[[^260], [^261]\].

### 4.3 Assisted surgery and robotics

AI has revolutionized surgery by enhancing precision, efficiency, and safety through the integration of advanced algorithms, robotics, and decision-support systems \[[^262], [^263]\].

One of the most significant contributions is to robotic-assisted surgery \[[^264],[^265],[^266],[^267]\], where these systems allow surgeons to perform minimally invasive procedures with unprecedented precision and control; AESOP® (Automated Endoscopic System for Optimal Positioning) (Computer Motion, Inc., Goleta, CA), ZEUS® system (Computer Motion, Inc., Goleta, CA) and the da Vinci® robotic surgery system (Intuitive Surgical, Sunnyvale, CA) are three notable examples \[[^268]\]. In fact, robotics improve movement stability, reducing the risk of human errors, TABLE [2](https://link.springer.com/article/10.1007/s40766-025-00073-4#Tab2) shows an overview of recent applications \[[^269]\].

**Table 2 An overview of recent robotics-assisted surgery**

AI follows the whole surgical procedure, from preoperative planning, to intervention, and the postoperative phase. In preoperative planning, AI segmentation and registration algorithms analyze medical images and support the identification of anatomical structures, the location of lesions; this also enables the simulation of surgical procedures with augmented reality and intraoperative navigation systems \[[^270],[^271],[^272]\]. AI has also transformed intraoperative monitoring and anesthesia management, with predictive algorithms analyzing vital signs in real time to adjust drug dosages and prevent adverse events \[[^273],[^274],[^275]\]. Finally, in the postoperative phase, AI is used to monitor patient recovery by analyzing data from wearable devices or electronic health records to detect early signs of complications and personalize rehabilitation \[[^276],[^277],[^278]\].

Another field where AI has made significant strides is minimally invasive procedures \[[^279], [^280]\]. Traditionally, minimally invasive surgeries, such as laparoscopy and endoscopic surgery, required exceptional skill and expertise from surgeons, relying on tiny incisions and using remotely controlled instruments, without a direct visualization of the surgical area. A wide variety of AI approaches aim to improve the precision, effectiveness, and safety of these procedures \[[^281]\]. Deep learning algorithms enable real-time analysis of intraoperative images (laparoscopic, ultrasound, endoscopic)\, detecting and highlighting vital anatomical structures, tumors, or lesions \[[^282],[^283],[^284]\]. These algorithms could help surgeons achieve greater precision and reduce the risk of damaging healthy tissues. Moreover, they could be used to optimize surgical trajectories, minimizing collateral damage. In general, while artificial intelligence is undoubtedly revolutionizing the surgical landscape, it should be kept in mind that this transformation would not be possible without a strong synergy with robotics.

Among the most revolutionary innovations in medical robotics is the development of intraoperative radiotherapy (IORT) \[[^285], [^286]\]. This cutting-edge technology uniquely merges robotic-assisted surgery with the real-time delivery of therapeutic radiation during the surgical procedure itself. By enabling radiation to be delivered directly to the tumor bed immediately after tumor resection, IORT maximizes therapeutic precision and efficacy while minimizing damage to surrounding healthy tissues. The integration of robotics further elevates this technique, offering unparalleled accuracy in device positioning, trajectory control, and dose administration. This level of intraoperative control and adaptability is unmatched by conventional radiotherapy techniques. Combined with XAI approaches, this can help surgeons make informed decisions in real time, reducing the risk of human errors and improving treatment outcomes. Besides, AI can support robotics in managing and adapting treatment in response to dynamic patient changes, such as tumor movement or modifications in the surgical field geometry.

### 4.4 Process automation and operational intelligence

In the digital age of Big Data, healthcare is increasingly becoming a field for computer scientists. There is a growing belief that the clinical and healthcare sectors should adopt best practices that have characterized business and industrial management for decades, although carefully considering the unique and specific factors of the healthcare domain. For this reason, in recent years, AI has gained a significant attention in supporting process automation and operational intelligence \[[^287], [^288]\]. Process automation and operational intelligence involve integrating advanced technologies to optimize clinical practices, improving efficiency and the quality of outcomes.

Process automation refers to the use of software and algorithms to perform repetitive tasks, such as data management, image processing, and treatment planning, reducing the need for human intervention and minimizing errors. Operational intelligence, on the other hand, focuses on real-time data analysis, enabling informed and timely decision-making. In a strictly clinical setting, operational intelligence leverages artificial intelligence to monitor and predict patient condition trends, optimize diagnostic and therapeutic pathways, and support clinical teams in treatment management \[[^289]\]. By combining automation with operational intelligence, it is possible to achieve faster, more accurate, and personalized results, reducing costs and increasing patient safety. This approach, which integrates AI with existing technological platforms, is revolutionizing multiple sectors, including healthcare, allowing a more agile and innovative management of resources.

A specific area of interest is hospital workflow management \[[^290], [^291]\]. Artificial intelligence is transforming hospital workflows by enhancing operational efficiency and improving the quality of care. For example, AI algorithms are used to optimize resource scheduling, such as managing operating rooms, to prevent overloads and reduce waiting times \[[^292]\]. Additionally, AI can analyze patient data to predict healthcare workers’ workloads, facilitating shift planning, resource allocation and preventing mental issues \[[^293], [^294]\]. AI-powered systems can also monitor patient flow in real time, suggesting solutions to reduce congestion and improve wait times, positively impacting efficiency and patient satisfaction.

AI-based tools, such as chatbots, are used to collect patient information and answer frequently asked questions, freeing up time for medical staff \[[^295]\]. Finally, forecasting the demand for healthcare services using historical data and predictive analytics helps optimize hospital resource management, reducing operational costs and improving access to care. Furthermore, AI is revolutionizing the automation of medical reporting, enhancing the speed and accuracy of diagnostic reports \[[^296]\]. It should also be considered how AI eases the standardization of reports making them easier to be shared and less subjective to operator style. Globally, these systems save time, improve healthcare professionals’ productivity, and ensure greater consistency in medical reports, ultimately enhancing the quality of patient care.

## 5 Conclusions

Artificial intelligence has profoundly revolutionized medical physics, bringing significant advances in diagnosis, therapy, and intervention.

In imaging, AI innovations have enabled the acquisition of higher-quality images\, directly improving diagnostic accuracy. This progress has enhanced the ability to extract more detailed and informative features from data, facilitating the development of more reliable decision support systems.

The adoption of clinical decision support systems is gradually transforming medical practice, making decision-making processes faster and more accurate. Despite initial concerns, the integration of eXplainable Artificial Intelligence promises to increase transparency and interpretability of AI algorithms, a fundamental requisite for both clinicians and patients. No longer “black boxes”, but tools easy to understand and explain, even for personnel without a computer science background.

In therapy, AI plays a pivotal role in personalizing treatments and improving intervention, especially when integrated with robotics. Looking ahead, the concept of digital twins promises more effective and less invasive therapies. Additionally, generative AI is helping healthcare professionals manage workflows, alleviating administrative burdens and allowing them to focus more on patient care.

Looking to the future, AI will remain central to advancing healthcare\, driving increasingly personalized and efficient approaches while ensuring that human care remains at the core of the system.

## References

## Acknowledgements

The authors were supported by the Italian Ministry of University and Research funding within the “Budget MIUR - Dipartimenti di Eccellenza 2023 - 2027” (Law 232, 11 December 2016) - Quantum Sensing and Modeling for One-Health (QuaSiModO), CUP: H97G23000100001. Authors were supported by the National Recovery and Resilience Plan (NRRP), Mission 4 Component 2 Investment 1.4 - Call for tender No. 3138 of 16 December 2021 of Italian Ministry of University and Research, funded by the European Union - NextGenerationEU; Project code: CN00000013, Concession Decree No. 1031 of 17 February 2022 adopted by the Italian Ministry of University and Research, CUP: H93C22000450007, Project title: National Centre for HPC, Big Data and Quantum Computing.

## Funding

Open access funding provided by Università degli Studi di Bari Aldo Moro within the CRUI-CARE Agreement.

## Rights and permissions

**Open Access** This article is licensed under a Creative Commons Attribution 4.0 International License, which permits use, sharing, adaptation\, distribution and reproduction in any medium or format, as long as you give appropriate credit to the original author(s) and the source, provide a link to the Creative Commons licence, and indicate if changes were made. The images or other third party material in this article are included in the article's Creative Commons licence, unless indicated otherwise in a credit line to the material. If material is not included in the article's Creative Commons licence and your intended use is not permitted by statutory regulation or exceeds the permitted use, you will need to obtain permission directly from the copyright holder. To view a copy of this licence, visit [http://creativecommons.org/licenses/by/4.0/](http://creativecommons.org/licenses/by/4.0/).

[^1]: M. Avanzo et al., Artificial intelligence applications in medical imaging: a review of the medical physics research in Italy. Physica Med. **83**, 221–241 (2021)

[Article](https://doi.org/10.1016%2Fj.ejmp.2021.04.010) [ADS](http://adsabs.harvard.edu/cgi-bin/nph-data_query?link_type=ABSTRACT&bibcode=2021afsj.book.....A) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Artificial%20intelligence%20applications%20in%20medical%20imaging%3A%20a%20review%20of%20the%20medical%20physics%20research%20in%20Italy&journal=Physica%20Med.&doi=10.1016%2Fj.ejmp.2021.04.010&volume=83&pages=221-241&publication_year=2021&author=Avanzo%2CM)

[^2]: O. Diaz et al., Artificial intelligence in the medical physics community: an international survey. Physica Med. **81**, 141–146 (2021)

[Article](https://doi.org/10.1016%2Fj.ejmp.2020.11.037) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Artificial%20intelligence%20in%20the%20medical%20physics%20community%3A%20an%20international%20survey&journal=Physica%20Med.&doi=10.1016%2Fj.ejmp.2020.11.037&volume=81&pages=141-146&publication_year=2021&author=Diaz%2CO)

[^3]: G. Mahadevaiah et al., Artificial intelligence-based clinical decision support in modern medical physics: selection, acceptance, commissioning, and quality assurance. Med. Phys. **47** (5), e228–e235 (2020)

[Article](https://doi.org/10.1002%2Fmp.13562) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Artificial%20intelligence-based%20clinical%20decision%20support%20in%20modern%20medical%20physics%3A%20selection%2C%20acceptance%2C%20commissioning%2C%20and%20quality%20assurance&journal=Med.%20Phys.&doi=10.1002%2Fmp.13562&volume=47&issue=5&pages=e228-e235&publication_year=2020&author=Mahadevaiah%2CG)

[^4]: F. Zanca et al., Focus issue: artificial intelligence in medical physics. Physica Medica: Eur. J. Med. Phys. **83**, 287–291 (2021)

[Article](https://doi.org/10.1016%2Fj.ejmp.2021.05.008) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Focus%20issue%3A%20artificial%20intelligence%20in%20medical%20physics&journal=Physica%20Medica%3A%20Eur.%20J.%20Med.%20Phys.&doi=10.1016%2Fj.ejmp.2021.05.008&volume=83&pages=287-291&publication_year=2021&author=Zanca%2CF)

[^5]: I. El Naqa, S. Das, The role of machine and deep learning in modern medical physics (2020)

[^6]: D.G. Brown, R.F. Wagner, Physics and statistics of medical imaging. J. Digit. Imaging **2**, 194–211 (1989)

[Article](https://link.springer.com/doi/10.1007/BF03170407) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Physics%20and%20statistics%20of%20medical%20imaging&journal=J.%20Digit.%20Imaging&doi=10.1007%2FBF03170407&volume=2&pages=194-211&publication_year=1989&author=Brown%2CDG&author=Wagner%2CRF)

[^7]: W.R. Hendee, Physics and applications of medical imaging. Rev. Mod. Phys. **71** (2), S444 (1999)

[Article](https://doi.org/10.1103%2FRevModPhys.71.S444) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Physics%20and%20applications%20of%20medical%20imaging&journal=Rev.%20Mod.%20Phys.&doi=10.1103%2FRevModPhys.71.S444&volume=71&issue=2&publication_year=1999&author=Hendee%2CWR)

[^8]: W.R. Hendee, E.R. Ritenour, Medical imaging physics. Wiley (2003)

[^9]: J.T. Bushberg, J.M. Boone, The essential physics of medical imaging. Lippincott Williams & Wilkins (2011)

[^10]: K. Hammernik et al., Physics-driven deep learning for computational magnetic resonance imaging: combining physics and machine learning for improved medical imaging. IEEE Signal Process. Mag. **40** (1), 98–114 (2023)

[Article](https://doi.org/10.1109%2FMSP.2022.3215288) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Physics-driven%20deep%20learning%20for%20computational%20magnetic%20resonance%20imaging%3A%20combining%20physics%20and%20machine%20learning%20for%20improved%20medical%20imaging&journal=IEEE%20Signal%20Process.%20Mag.&doi=10.1109%2FMSP.2022.3215288&volume=40&issue=1&pages=98-114&publication_year=2023&author=Hammernik%2CK)

[^11]: R.A. Pooley, Fundamental physics of MR imaging. Radiographics **25** (4), 1087–1099 (2005)

[Article](https://doi.org/10.1148%2Frg.254055027) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Fundamental%20physics%20of%20MR%20imaging&journal=Radiographics&doi=10.1148%2Frg.254055027&volume=25&issue=4&pages=1087-1099&publication_year=2005&author=Pooley%2CRA)

[^12]: Y. Gossuin et al., Physics of magnetic resonance imaging: from spin to pixel. J. Phys. D Appl. Phys. **43** (21), 213001 (2010)

[Article](https://doi.org/10.1088%2F0022-3727%2F43%2F21%2F213001) [ADS](http://adsabs.harvard.edu/cgi-bin/nph-data_query?link_type=ABSTRACT&bibcode=2010JPhD...43u3001G) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Physics%20of%20magnetic%20resonance%20imaging%3A%20from%20spin%20to%20pixel&journal=J.%20Phys.%20D%20Appl.%20Phys.&doi=10.1088%2F0022-3727%2F43%2F21%2F213001&volume=43&issue=21&publication_year=2010&author=Gossuin%2CY)

[^13]: K.. Wei, et al., A physics-based noise formation model for extreme low-light raw denoising. in Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition, 2758–2767 (2020)

[^14]: Z. Chen et al., Deep learning for image enhancement and correction in magnetic resonance imaging-state-of-the-art and challenges. J. Digit. Imaging **36** (1), 204–230 (2023)

[Article](https://link.springer.com/doi/10.1007/s10278-022-00721-9) [ADS](http://adsabs.harvard.edu/cgi-bin/nph-data_query?link_type=ABSTRACT&bibcode=2023spri.book.....C) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Deep%20learning%20for%20image%20enhancement%20and%20correction%20in%20magnetic%20resonance%20imaging-state-of-the-art%20and%20challenges&journal=J.%20Digit.%20Imaging&doi=10.1007%2Fs10278-022-00721-9&volume=36&issue=1&pages=204-230&publication_year=2023&author=Chen%2CZ)

[^15]: W.A. Kalender, X-ray computed tomography. Phys. Med. Biol. **51** (13), R29 (2006)

[Article](https://doi.org/10.1088%2F0031-9155%2F51%2F13%2FR03) [ADS](http://adsabs.harvard.edu/cgi-bin/nph-data_query?link_type=ABSTRACT&bibcode=2006PMB....51R..29K) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=X-ray%20computed%20tomography&journal=Phys.%20Med.%20Biol.&doi=10.1088%2F0031-9155%2F51%2F13%2FR03&volume=51&issue=13&publication_year=2006&author=Kalender%2CWA)

[^16]: J. Nuyts et al., Modelling the physics in the iterative reconstruction for transmission computed tomography. Phys. Med. Biol. **58** (12), R63 (2013)

[Article](https://doi.org/10.1088%2F0031-9155%2F58%2F12%2FR63) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Modelling%20the%20physics%20in%20the%20iterative%20reconstruction%20for%20transmission%20computed%20tomography&journal=Phys.%20Med.%20Biol.&doi=10.1088%2F0031-9155%2F58%2F12%2FR63&volume=58&issue=12&publication_year=2013&author=Nuyts%2CJ)

[^17]: W.Y.R. Fok et al., Deep learning in computed tomography super resolution using multi-modality data training. Med. Phys. **51** (4), 2846–2860 (2024)

[Article](https://doi.org/10.1002%2Fmp.16825) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Deep%20learning%20in%20computed%20tomography%20super%20resolution%20using%20multi-modality%20data%20training&journal=Med.%20Phys.&doi=10.1002%2Fmp.16825&volume=51&issue=4&pages=2846-2860&publication_year=2024&author=Fok%2CWYR)

[^18]: M. Conti, L. Eriksson, Physics of pure and non-pure positron emitters for PET: a review and a discussion. EJNMMI Phys. **3**, 1–17 (2016)

[Article](https://link.springer.com/doi/10.1186/s40658-016-0144-5) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Physics%20of%20pure%20and%20non-pure%20positron%20emitters%20for%20PET%3A%20a%20review%20and%20a%20discussion&journal=EJNMMI%20Phys.&doi=10.1186%2Fs40658-016-0144-5&volume=3&pages=1-17&publication_year=2016&author=Conti%2CM&author=Eriksson%2CL)

[^19]: D.R. Schaart, Physics and technology of time-of-flight PET detectors. Phys. Med. Biol. **66** (9), 09TR01 (2021)

[Article](https://doi.org/10.1088%2F1361-6560%2Fabee56) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Physics%20and%20technology%20of%20time-of-flight%20PET%20detectors&journal=Phys.%20Med.%20Biol.&doi=10.1088%2F1361-6560%2Fabee56&volume=66&issue=9&publication_year=2021&author=Schaart%2CDR)

[^20]: G. Kossoff, Basic physics and imaging characteristics of ultrasound. World J. Surg. **24** (2), 134–142 (2000)

[Article](https://link.springer.com/doi/10.1007/s002689910026) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Basic%20physics%20and%20imaging%20characteristics%20of%20ultrasound&journal=World%20J.%20Surg.&doi=10.1007%2Fs002689910026&volume=24&issue=2&pages=134-142&publication_year=2000&author=Kossoff%2CG)

[^21]: J.E. Aldrich, Basic physics of ultrasound imaging. Crit. Care Med. **35** (5), S131–S137 (2007)

[Article](https://doi.org/10.1097%2F01.CCM.0000260624.99430.22) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Basic%20physics%20of%20ultrasound%20imaging&journal=Crit.%20Care%20Med.&doi=10.1097%2F01.CCM.0000260624.99430.22&volume=35&issue=5&pages=S131-S137&publication_year=2007&author=Aldrich%2CJE)

[^22]: S. Khan, J. Huh, J.C. Ye, Variational formulation of unsupervised deep learning for ultrasound image artifact removal. IEEE Trans. Ultrason. Ferroelectr. Freq. Control **68** (6), 2086–2100 (2021)

[Article](https://doi.org/10.1109%2FTUFFC.2021.3056197) [ADS](http://adsabs.harvard.edu/cgi-bin/nph-data_query?link_type=ABSTRACT&bibcode=2021ITUFF..68.2086K) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Variational%20formulation%20of%20unsupervised%20deep%20learning%20for%20ultrasound%20image%20artifact%20removal&journal=IEEE%20Trans.%20Ultrason.%20Ferroelectr.%20Freq.%20Control&doi=10.1109%2FTUFFC.2021.3056197&volume=68&issue=6&pages=2086-2100&publication_year=2021&author=Khan%2CS&author=Huh%2CJ&author=Ye%2CJC)

[^23]: P. Szolovits, R.S. Patil, W.B. Schwartz, Artificial intelligence in medical diagnosis. Ann. Intern. Med. **108** (1), 80–87 (1988)

[Article](https://doi.org/10.7326%2F0003-4819-108-1-80) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Artificial%20intelligence%20in%20medical%20diagnosis&journal=Ann.%20Intern.%20Med.&doi=10.7326%2F0003-4819-108-1-80&volume=108&issue=1&pages=80-87&publication_year=1988&author=Szolovits%2CP&author=Patil%2CRS&author=Schwartz%2CWB)

[^24]: J. Holmes, L. Sacchi, R. Bellazzi et al., Artificial intelligence in medicine. Ann. R. Coll. Surg. Engl. **86**, 334–8 (2004)

[Article](https://doi.org/10.1308%2F147870804290) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Artificial%20intelligence%20in%20medicine&journal=Ann.%20R.%20Coll.%20Surg.%20Engl.&doi=10.1308%2F147870804290&volume=86&pages=334-8&publication_year=2004&author=Holmes%2CJ&author=Sacchi%2CL&author=Bellazzi%2CR)

[^25]: P. Hamet, J. Tremblay, Artificial intelligence in medicine. Metabolism **69**, S36–S40 (2017)

[Article](https://doi.org/10.1016%2Fj.metabol.2017.01.011) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Artificial%20intelligence%20in%20medicine&journal=Metabolism&doi=10.1016%2Fj.metabol.2017.01.011&volume=69&pages=S36-S40&publication_year=2017&author=Hamet%2CP&author=Tremblay%2CJ)

[^26]: A. Holzinger et al., Causability and explainability of artificial intelligence in medicine. Wiley Interdiscip. Rev.: Data Min. Knowl. Discovery **9** (4), e1312 (2019)

[Google Scholar](http://scholar.google.com/scholar_lookup?&title=Causability%20and%20explainability%20of%20artificial%20intelligence%20in%20medicine&journal=Wiley%20Interdiscip.%20Rev.%3A%20Data%20Min.%20Knowl.%20Discovery&volume=9&issue=4&publication_year=2019&author=Holzinger%2CA)

[^27]: S. Kundu, AI in medicine must be explainable. Nat. Med. **27** (8), 1328–1328 (2021)

[Article](https://doi.org/10.1038%2Fs41591-021-01461-z) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=AI%20in%20medicine%20must%20be%20explainable&journal=Nat.%20Med.&doi=10.1038%2Fs41591-021-01461-z&volume=27&issue=8&pages=1328-1328&publication_year=2021&author=Kundu%2CS)

[^28]: R.J. Chen et al., Algorithmic fairness in artificial intelligence for medicine and healthcare. Nat. Biomed. Eng. **7** (6), 719–742 (2023)

[Article](https://doi.org/10.1038%2Fs41551-023-01056-8) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Algorithmic%20fairness%20in%20artificial%20intelligence%20for%20medicine%20and%20healthcare&journal=Nat.%20Biomed.%20Eng.&doi=10.1038%2Fs41551-023-01056-8&volume=7&issue=6&pages=719-742&publication_year=2023&author=Chen%2CRJ)

[^29]: S.E. Dilsizian, E.L. Siegel, Artificial intelligence in medicine and cardiac imaging: harnessing big data and advanced computing to provide personalized medical diagnosis and treatment. Curr. Cardiol. Rep. **16**, 1–8 (2014)

[Article](https://link.springer.com/doi/10.1007/s11886-013-0441-8) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Artificial%20intelligence%20in%20medicine%20and%20cardiac%20imaging%3A%20harnessing%20big%20data%20and%20advanced%20computing%20to%20provide%20personalized%20medical%20diagnosis%20and%20treatment&journal=Curr.%20Cardiol.%20Rep.&doi=10.1007%2Fs11886-013-0441-8&volume=16&pages=1-8&publication_year=2014&author=Dilsizian%2CSE&author=Siegel%2CEL)

[^30]: N.J. Schork, Artificial intelligence and personalized medicine. in Precision medicine in Cancer therapy, pp. 265–283 (2019)

[^31]: H. Taherdoost, A. Ghofrani, AI and the evolution of personalized medicine in pharmacogenomics. in Intelligent Pharmacy (2024)

[^32]: P. Stone, et al. Artificial Intelligence and life in 2030: the one hundred year study on artificial intelligence, (2016)

[^33]: X. Jia et al., Translating cancer genomics into precision medicine with artificial intelligence: applications, challenges and future perspectives. Hum. Genet. **138** (2), 109–124 (2019)

[Article](https://link.springer.com/doi/10.1007/s00439-019-01970-5) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Translating%20cancer%20genomics%20into%20precision%20medicine%20with%20artificial%20intelligence%3A%20applications%2C%20challenges%20and%20future%20perspectives&journal=Hum.%20Genet.&doi=10.1007%2Fs00439-019-01970-5&volume=138&issue=2&pages=109-124&publication_year=2019&author=Jia%2CX)

[^34]: N. Schwalbe, B. Wahl, Artificial intelligence and the future of global health. Lancet **395** (10236), 1579–1586 (2020)

[Article](https://doi.org/10.1016%2FS0140-6736%2820%2930226-9) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Artificial%20intelligence%20and%20the%20future%20of%20global%20health&journal=Lancet&doi=10.1016%2FS0140-6736%2820%2930226-9&volume=395&issue=10236&pages=1579-1586&publication_year=2020&author=Schwalbe%2CN&author=Wahl%2CB)

[^35]: G. Novakovsky et al., Obtaining genetics insights from deep learning via explainable artificial intelligence. Nat. Rev. Genet. **24** (2), 125–137 (2023)

[Article](https://doi.org/10.1038%2Fs41576-022-00532-2) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Obtaining%20genetics%20insights%20from%20deep%20learning%20via%20explainable%20artificial%20intelligence&journal=Nat.%20Rev.%20Genet.&doi=10.1038%2Fs41576-022-00532-2&volume=24&issue=2&pages=125-137&publication_year=2023&author=Novakovsky%2CG)

[^36]: D.A. Hashimoto et al., Artificial intelligence in surgery: promises and perils. Ann. Surg. **268** (1), 70–76 (2018)

[Article](https://doi.org/10.1097%2FSLA.0000000000002693) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Artificial%20intelligence%20in%20surgery%3A%20promises%20and%20perils&journal=Ann.%20Surg.&doi=10.1097%2FSLA.0000000000002693&volume=268&issue=1&pages=70-76&publication_year=2018&author=Hashimoto%2CDA)

[^37]: X.-Y. Zhou et al., Application of artificial intelligence in surgery. Front. Med. **14**, 417–430 (2020)

[Article](https://link.springer.com/doi/10.1007/s11684-020-0770-0) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Application%20of%20artificial%20intelligence%20in%20surgery&journal=Front.%20Med.&doi=10.1007%2Fs11684-020-0770-0&volume=14&pages=417-430&publication_year=2020&author=Zhou%2CX-Y)

[^38]: S.K. Bakshi et al., The era of artificial intelligence and virtual reality: transforming surgical education in ophthalmology. Br. J. Ophthalmol. **105** (10), 1325–1328 (2021)

[Article](https://doi.org/10.1136%2Fbjophthalmol-2020-316845) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=The%20era%20of%20artificial%20intelligence%20and%20virtual%20reality%3A%20transforming%20surgical%20education%20in%20ophthalmology&journal=Br.%20J.%20Ophthalmol.&doi=10.1136%2Fbjophthalmol-2020-316845&volume=105&issue=10&pages=1325-1328&publication_year=2021&author=Bakshi%2CSK)

[^39]: A.S. Ahuja et al., The digital metaverse: applications in artificial intelligence, medical education, and integrative health. Integr. Med. Res. **12** (1), 100917 (2023)

[Article](https://doi.org/10.1016%2Fj.imr.2022.100917) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=The%20digital%20metaverse%3A%20applications%20in%20artificial%20intelligence%2C%20medical%20education%2C%20and%20integrative%20health&journal=Integr.%20Med.%20Res.&doi=10.1016%2Fj.imr.2022.100917&volume=12&issue=1&publication_year=2023&author=Ahuja%2CAS)

[^40]: A. Guni et al., Artificial intelligence in surgery: the future is now. Eur. Surg. Res. **65** (1), 22–39 (2024)

[Google Scholar](http://scholar.google.com/scholar_lookup?&title=Artificial%20intelligence%20in%20surgery%3A%20the%20future%20is%20now&journal=Eur.%20Surg.%20Res.&volume=65&issue=1&pages=22-39&publication_year=2024&author=Guni%2CA)

[^41]: C.P. Behrenbruch et al., Image filtering techniques for medical image post-processing: an overview. Br. J. Radiol. **77** (suppl–2), S126–S132 (2004)

[Article](https://doi.org/10.1259%2Fbjr%2F17464219) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Image%20filtering%20techniques%20for%20medical%20image%20post-processing%3A%20an%20overview&journal=Br.%20J.%20Radiol.&doi=10.1259%2Fbjr%2F17464219&volume=77&issue=suppl%E2%80%932&pages=S126-S132&publication_year=2004&author=Behrenbruch%2CCP)

[^42]: H.M. Ali, MRI medical image denoising by fundamental filters. High-resolution neuroimaging-basic physical principles and clinical applications **14**, 111–124 (2018)

[^43]: T.M. Lehmann, C. Gonner, K. Spitzer, Survey: Interpolation methods in medical image processing. IEEE Trans. Med. Imaging **18** (11), 1049–1075 (1999)

[Article](https://doi.org/10.1109%2F42.816070) [ADS](http://adsabs.harvard.edu/cgi-bin/nph-data_query?link_type=ABSTRACT&bibcode=1999ITMI...18.1049L) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Survey%3A%20Interpolation%20methods%20in%20medical%20image%20processing&journal=IEEE%20Trans.%20Med.%20Imaging&doi=10.1109%2F42.816070&volume=18&issue=11&pages=1049-1075&publication_year=1999&author=Lehmann%2CTM&author=Gonner%2CC&author=Spitzer%2CK)

[^44]: A. Pizurica et al., A versatile wavelet domain noise filtration technique for medical imaging. IEEE Trans. Med. Imaging **22** (3), 323–331 (2003)

[Article](https://doi.org/10.1109%2FTMI.2003.809588) [ADS](http://adsabs.harvard.edu/cgi-bin/nph-data_query?link_type=ABSTRACT&bibcode=2003ITMI...22..323P) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=A%20versatile%20wavelet%20domain%20noise%20filtration%20technique%20for%20medical%20imaging&journal=IEEE%20Trans.%20Med.%20Imaging&doi=10.1109%2FTMI.2003.809588&volume=22&issue=3&pages=323-331&publication_year=2003&author=Pizurica%2CA)

[^45]: A. Achim, A. Bezerianos, P. Tsakalides, Novel Bayesian multiscale method for speckle removal in medical ultrasound images. IEEE Trans. Med. Imaging **20** (8), 772–783 (2002)

[Article](https://doi.org/10.1109%2F42.938245) [ADS](http://adsabs.harvard.edu/cgi-bin/nph-data_query?link_type=ABSTRACT&bibcode=2001ITMI...20..772A) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Novel%20Bayesian%20multiscale%20method%20for%20speckle%20removal%20in%20medical%20ultrasound%20images&journal=IEEE%20Trans.%20Med.%20Imaging&doi=10.1109%2F42.938245&volume=20&issue=8&pages=772-783&publication_year=2002&author=Achim%2CA&author=Bezerianos%2CA&author=Tsakalides%2CP)

[^46]: N. Kumar, M. Nachamai, Noise removal and filtering techniques used in medical images. Orient. J. Comput. Sci. Technol **10** (1), 103–113 (2017)

[Article](https://doi.org/10.13005%2Fojcst%2F10.01.14) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Noise%20removal%20and%20filtering%20techniques%20used%20in%20medical%20images&journal=Orient.%20J.%20Comput.%20Sci.%20Technol&doi=10.13005%2Fojcst%2F10.01.14&volume=10&issue=1&pages=103-113&publication_year=2017&author=Kumar%2CN&author=Nachamai%2CM)

[^47]: F. Baselice, G. Ferraioli, V. Pascazio, A 3D MRI denoising algorithm based on Bayesian theory. Biomed. Eng. Online **16**, 1–19 (2017)

[Article](https://link.springer.com/doi/10.1186/s12938-017-0319-x) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=A%203D%20MRI%20denoising%20algorithm%20based%20on%20Bayesian%20theory&journal=Biomed.%20Eng.%20Online&doi=10.1186%2Fs12938-017-0319-x&volume=16&pages=1-19&publication_year=2017&author=Baselice%2CF&author=Ferraioli%2CG&author=Pascazio%2CV)

[^48]: T. Guo et al., A review of wavelet analysis and its applications: challenges and opportunities. IEEe Access **10**, 58869–58903 (2022)

[Article](https://doi.org/10.1109%2FACCESS.2022.3179517) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=A%20review%20of%20wavelet%20analysis%20and%20its%20applications%3A%20challenges%20and%20opportunities&journal=IEEe%20Access&doi=10.1109%2FACCESS.2022.3179517&volume=10&pages=58869-58903&publication_year=2022&author=Guo%2CT)

[^49]: S. Kollem, K.R.L. Reddy, D.S. Rao, A review of image denoising and segmentation methods based on medical images. Int. J. Mach. Learn. Comput. **9** (3), 288–295 (2019)

[Article](https://doi.org/10.18178%2Fijmlc.2019.9.3.800) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=A%20review%20of%20image%20denoising%20and%20segmentation%20methods%20based%20on%20medical%20images&journal=Int.%20J.%20Mach.%20Learn.%20Comput.&doi=10.18178%2Fijmlc.2019.9.3.800&volume=9&issue=3&pages=288-295&publication_year=2019&author=Kollem%2CS&author=Reddy%2CKRL&author=Rao%2CDS)

[^50]: A.S. Brendlin et al., AI denoising improves image quality and radiological workflows in pediatric ultra-low-dose thorax computed tomography scans. Tomography **8** (4), 1678–1689 (2022)

[Article](https://doi.org/10.3390%2Ftomography8040140) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=AI%20denoising%20improves%20image%20quality%20and%20radiological%20workflows%20in%20pediatric%20ultra-low-dose%20thorax%20computed%20tomography%20scans&journal=Tomography&doi=10.3390%2Ftomography8040140&volume=8&issue=4&pages=1678-1689&publication_year=2022&author=Brendlin%2CAS)

[^51]: A. Kaur, G. Dong, A complete review on image denoising techniques for medical images. Neural Process. Lett. **55** (6), 7807–7850 (2023)

[Article](https://link.springer.com/doi/10.1007/s11063-023-11286-1) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=A%20complete%20review%20on%20image%20denoising%20techniques%20for%20medical%20images&journal=Neural%20Process.%20Lett.&doi=10.1007%2Fs11063-023-11286-1&volume=55&issue=6&pages=7807-7850&publication_year=2023&author=Kaur%2CA&author=Dong%2CG)

[^52]: S. Zhang et al., A fast medical image super resolution method based on deep learning network. IEEE Access **7**, 12319–12327 (2018)

[Article](https://doi.org/10.1109%2FACCESS.2018.2871626) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=A%20fast%20medical%20image%20super%20resolution%20method%20based%20on%20deep%20learning%20network&journal=IEEE%20Access&doi=10.1109%2FACCESS.2018.2871626&volume=7&pages=12319-12327&publication_year=2018&author=Zhang%2CS)

[^53]: K.J. Halupka et al., Retinal optical coherence tomography image enhancement via deep learning. Biomed. Opt. Express **9** (12), 6205–6221 (2018)

[Article](https://doi.org/10.1364%2FBOE.9.006205) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Retinal%20optical%20coherence%20tomography%20image%20enhancement%20via%20deep%20learning&journal=Biomed.%20Opt.%20Express&doi=10.1364%2FBOE.9.006205&volume=9&issue=12&pages=6205-6221&publication_year=2018&author=Halupka%2CKJ)

[^54]: K. Munadi et al., Image enhancement for tuberculosis detection using deep learning. IEEE Access **8**, 217897–217907 (2020)

[Article](https://doi.org/10.1109%2FACCESS.2020.3041867) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Image%20enhancement%20for%20tuberculosis%20detection%20using%20deep%20learning&journal=IEEE%20Access&doi=10.1109%2FACCESS.2020.3041867&volume=8&pages=217897-217907&publication_year=2020&author=Munadi%2CK)

[^55]: C. Ghandour, W. El-Shafai, S. El-Rabaie, Medical image enhancement algorithms using deep learning-based convolutional neural network. J. Opt. **52** (4), 1931–1941 (2023)

[Article](https://link.springer.com/doi/10.1007/s12596-022-01078-6) [ADS](http://adsabs.harvard.edu/cgi-bin/nph-data_query?link_type=ABSTRACT&bibcode=2023JOpt...52.1931G) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Medical%20image%20enhancement%20algorithms%20using%20deep%20learning-based%20convolutional%20neural%20network&journal=J.%20Opt.&doi=10.1007%2Fs12596-022-01078-6&volume=52&issue=4&pages=1931-1941&publication_year=2023&author=Ghandour%2CC&author=El-Shafai%2CW&author=El-Rabaie%2CS)

[^56]: A. Kambadakone, Artificial intelligence and CT image reconstruction: potential of a new era in radiation dose reduction. J. Am. Coll. Radiol. **17** (5), 649–651 (2020)

[Article](https://doi.org/10.1016%2Fj.jacr.2019.12.025) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Artificial%20intelligence%20and%20CT%20image%20reconstruction%3A%20potential%20of%20a%20new%20era%20in%20radiation%20dose%20reduction&journal=J.%20Am.%20Coll.%20Radiol.&doi=10.1016%2Fj.jacr.2019.12.025&volume=17&issue=5&pages=649-651&publication_year=2020&author=Kambadakone%2CA)

[^57]: W. Li et al., Image quality assessment of artificial intelligence iterative reconstruction for low dose aortic CTA: a feasibility study of 70 kVp and reduced contrast medium volume. Eur. J. Radiol. **149**, 110221 (2022)

[Article](https://doi.org/10.1016%2Fj.ejrad.2022.110221) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Image%20quality%20assessment%20of%20artificial%20intelligence%20iterative%20reconstruction%20for%20low%20dose%20aortic%20CTA%3A%20a%20feasibility%20study%20of%2070%20kVp%20and%20reduced%20contrast%20medium%20volume&journal=Eur.%20J.%20Radiol.&doi=10.1016%2Fj.ejrad.2022.110221&volume=149&publication_year=2022&author=Li%2CW)

[^58]: J. Hatvani et al., Deep learning-based super-resolution applied to dental computed tomography. IEEE Trans. Radiat. Plasma Med. Sci. **3** (2), 120–128 (2018)

[Article](https://doi.org/10.1109%2FTRPMS.2018.2827239) [MathSciNet](http://www.ams.org/mathscinet-getitem?mr=1025179) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Deep%20learning-based%20super-resolution%20applied%20to%20dental%20computed%20tomography&journal=IEEE%20Trans.%20Radiat.%20Plasma%20Med.%20Sci.&doi=10.1109%2FTRPMS.2018.2827239&volume=3&issue=2&pages=120-128&publication_year=2018&author=Hatvani%2CJ)

[^59]: M. Li, et al., Computed tomography image enhancement using 3D convolutional neural network, in: International Workshop on Deep Learning in Medical Image Analysis. Springer, pp. 291–299 (2018)

[^60]: T. Wang et al., Deep learning-based image quality improvement for low-dose computed tomography simulation in radiation therapy. J. Med. Imag. **6** (4), 043504–043504 (2019)

[Article](https://doi.org/10.1117%2F1.JMI.6.4.043504) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Deep%20learning-based%20image%20quality%20improvement%20for%20low-dose%20computed%20tomography%20simulation%20in%20radiation%20therapy&journal=J.%20Med.%20Imag.&doi=10.1117%2F1.JMI.6.4.043504&volume=6&issue=4&pages=043504-043504&publication_year=2019&author=Wang%2CT)

[^61]: M. Du, K. Liang, Y. Xing, Reduction of metal artefacts in CT with Cycle-GAN, in 2018 IEEE Nuclear Science Symposium and Medical Imaging Conference Proceedings (NSS/MIC). IEEE, 1–3 (2018)

[^62]: S. Xie, H. Xu, H. Li, Artifact removal using GAN network for limited-angle CT reconstruction, in 2019 Ninth International Conference on Image Processing Theory, Tools and Applications (IPTA). IEEE. 1–4 (2019)

[^63]: M. Moinuddin et al., Medical ultrasound image speckle reduction and resolution enhancement using texture compensated multi-resolution convolution neural network. Front. Physiol. **13**, 961571 (2022)

[Article](https://doi.org/10.3389%2Ffphys.2022.961571) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Medical%20ultrasound%20image%20speckle%20reduction%20and%20resolution%20enhancement%20using%20texture%20compensated%20multi-resolution%20convolution%20neural%20network&journal=Front.%20Physiol.&doi=10.3389%2Ffphys.2022.961571&volume=13&publication_year=2022&author=Moinuddin%2CM)

[^64]: B.A. Duffy et al., Retrospective motion artifact correction of structural MRI images using deep learning improves the quality of cortical surface reconstructions. Neuroimage **230**, 117756 (2021)

[Article](https://doi.org/10.1016%2Fj.neuroimage.2021.117756) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Retrospective%20motion%20artifact%20correction%20of%20structural%20MRI%20images%20using%20deep%20learning%20improves%20the%20quality%20of%20cortical%20surface%20reconstructions&journal=Neuroimage&doi=10.1016%2Fj.neuroimage.2021.117756&volume=230&publication_year=2021&author=Duffy%2CBA)

[^65]: R.-E. Yoo, S.H. Choi, Deep learning-based image enhancement techniques for fast MRI in neuroimaging. Magn. Reson. Med. Sci. **23** (3), 341–351 (2024)

[^66]: P. Vincent, et al., Stacked denoising autoencoders: Learning useful representations in a deep network with a local denoising criterion. J. Mach. Learn. Res. 11(12) (2010)

[^67]: M. Nishio, et al., Convolutional auto-encoder for image denoising of ultra-low-dose CT. Heliyon 3(8), (2017)

[^68]: L. Gondara, Medical image denoising using convolutional denoising autoencoders, in 2016 IEEE 16th international conference on data mining workshops (ICDMW). IEEE, 241–246 (2016)

[^69]: F. Fan et al., Quadratic autoencoder (Q-AE) for low-dose CT denoising. IEEE Trans. Med. Imaging **39** (6), 2035–2050 (2019)

[Article](https://doi.org/10.1109%2FTMI.2019.2963248) [ADS](http://adsabs.harvard.edu/cgi-bin/nph-data_query?link_type=ABSTRACT&bibcode=2020ITMI...39.2035F) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Quadratic%20autoencoder%20%28Q-AE%29%20for%20low-dose%20CT%20denoising&journal=IEEE%20Trans.%20Med.%20Imaging&doi=10.1109%2FTMI.2019.2963248&volume=39&issue=6&pages=2035-2050&publication_year=2019&author=Fan%2CF)

[^70]: B. Biswas, S.Kr. Ghosh, A. Ghosh, DVAE: deep variational auto-encoders for denoising retinal fundus image, in Hybrid machine intelligence for medical image analysis, 257–273 (2020)

[^71]: W.-H. Lee et al., Noise learning-based denoising autoencoder. IEEE Commun. Lett. **25** (9), 2983–2987 (2021)

[Article](https://doi.org/10.1109%2FLCOMM.2021.3091800) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Noise%20learning-based%20denoising%20autoencoder&journal=IEEE%20Commun.%20Lett.&doi=10.1109%2FLCOMM.2021.3091800&volume=25&issue=9&pages=2983-2987&publication_year=2021&author=Lee%2CW-H)

[^72]: J. Ehrhardt, M. Wilms, Autoencoders and variational autoencoders in medical image analysis, in Biomedical Image Synthesis and Simulation. Elsevier, 129–162 (2022)

[^73]: S. Rawat, K.P.S. Rana, V. Kumar, A novel complex-valued convolutional neural network for medical image denoising. Biomed. Signal Process. Control **69**, 102859 (2021)

[Article](https://doi.org/10.1016%2Fj.bspc.2021.102859) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=A%20novel%20complex-valued%20convolutional%20neural%20network%20for%20medical%20image%20denoising&journal=Biomed.%20Signal%20Process.%20Control&doi=10.1016%2Fj.bspc.2021.102859&volume=69&publication_year=2021&author=Rawat%2CS&author=Rana%2CKPS&author=Kumar%2CV)

[^74]: A.E. Ilesanmi, T.O. Ilesanmi, Methods for image denoising using convolutional neural network: a review. Complex Intell. Syst. **7** (5), 2179–2198 (2021)

[Article](https://link.springer.com/doi/10.1007/s40747-021-00428-4) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Methods%20for%20image%20denoising%20using%20convolutional%20neural%20network%3A%20a%20review&journal=Complex%20Intell.%20Syst.&doi=10.1007%2Fs40747-021-00428-4&volume=7&issue=5&pages=2179-2198&publication_year=2021&author=Ilesanmi%2CAE&author=Ilesanmi%2CTO)

[^75]: M.N. Shodiq, et al., Ultrasound image segmentation for deep vein thrombosis using UNet-CNN based on denoising filter, in 2022 IEEE international conference on imaging systems and techniques (IST). IEEE, 1–6 (2022)

[^76]: M.S. Hossain, et al., MultiResUNet3+: a full-scale connected multi-residual UNet model to denoise electrooculogram and electromyogram artifacts from corrupted electroencephalogram signals. Bioengineering **10** (5), 579 (2023)

[^77]: Z. Huang et al., DU-GAN: generative adversarial networks with dual-domain U-Net-based discriminators for low-dose CT denoising. IEEE Trans. Instrum. Meas. **71**, 1–12 (2021)

[Google Scholar](http://scholar.google.com/scholar_lookup?&title=DU-GAN%3A%20generative%20adversarial%20networks%20with%20dual-domain%20U-Net-based%20discriminators%20for%20low-dose%20CT%20denoising&journal=IEEE%20Trans.%20Instrum.%20Meas.&volume=71&pages=1-12&publication_year=2021&author=Huang%2CZ)

[^78]: S. Ayub et al., LSTM-based RNN framework to remove motion artifacts in dynamic multicontrast MR images with registration model. Wirel. Commun. Mob. Comput. **2022** (1), 5906877 (2022)

[Article](https://doi.org/10.1155%2F2022%2F5906877) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=LSTM-based%20RNN%20framework%20to%20remove%20motion%20artifacts%20in%20dynamic%20multicontrast%20MR%20images%20with%20registration%20model&journal=Wirel.%20Commun.%20Mob.%20Comput.&doi=10.1155%2F2022%2F5906877&volume=2022&issue=1&publication_year=2022&author=Ayub%2CS)

[^79]: J. Sun et al., Dual gating myocardial perfusion SPECT denoising using a conditional generative adversarial network. Med. Phys. **49** (8), 5093–5106 (2022)

[Article](https://doi.org/10.1002%2Fmp.15707) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Dual%20gating%20myocardial%20perfusion%20SPECT%20denoising%20using%20a%20conditional%20generative%20adversarial%20network&journal=Med.%20Phys.&doi=10.1002%2Fmp.15707&volume=49&issue=8&pages=5093-5106&publication_year=2022&author=Sun%2CJ)

[^80]: S. Pan et al., 2D medical image synthesis using transformer-based denoising diffusion probabilistic model. Phys. Med. Biol. **68** (10), 105004 (2023)

[Article](https://doi.org/10.1088%2F1361-6560%2Facca5c) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=2D%20medical%20image%20synthesis%20using%20transformer-based%20denoising%20diffusion%20probabilistic%20model&journal=Phys.%20Med.%20Biol.&doi=10.1088%2F1361-6560%2Facca5c&volume=68&issue=10&publication_year=2023&author=Pan%2CS)

[^81]: J. Zhang et al., A novel denoising method for low-dose CT images based on transformer and CNN. Comput. Biol. Med. **163**, 107162 (2023)

[Article](https://doi.org/10.1016%2Fj.compbiomed.2023.107162) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=A%20novel%20denoising%20method%20for%20low-dose%20CT%20images%20based%20on%20transformer%20and%20CNN&journal=Comput.%20Biol.%20Med.&doi=10.1016%2Fj.compbiomed.2023.107162&volume=163&publication_year=2023&author=Zhang%2CJ)

[^82]: M. Chen et al., Elimination of random mixed noise in ECG using convolutional denoising autoencoder with transformer encoder. IEEE J. Biomed. Health Inform. **28** (4), 1993–2004 (2024)

[Article](https://doi.org/10.1109%2FJBHI.2024.3355960) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Elimination%20of%20random%20mixed%20noise%20in%20ECG%20using%20convolutional%20denoising%20autoencoder%20with%20transformer%20encoder&journal=IEEE%20J.%20Biomed.%20Health%20Inform.&doi=10.1109%2FJBHI.2024.3355960&volume=28&issue=4&pages=1993-2004&publication_year=2024&author=Chen%2CM)

[^83]: T.-A. Song, F. Yang, J. Dutta, Noise2Void: unsupervised denoising of PET images. Phys. Med. Biol. **66** (21), 214002 (2021)

[Article](https://doi.org/10.1088%2F1361-6560%2Fac30a0) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Noise2Void%3A%20unsupervised%20denoising%20of%20PET%20images&journal=Phys.%20Med.%20Biol.&doi=10.1088%2F1361-6560%2Fac30a0&volume=66&issue=21&publication_year=2021&author=Song%2CT-A&author=Yang%2CF&author=Dutta%2CJ)

[^84]: S. Kojima, T. Ito, T. Hayashi, Denoising using Noise2Void for low-field magnetic resonance imaging: a phantom study. J. Med. Phys. **47** (4), 387–393 (2022)

[Article](https://doi.org/10.4103%2Fjmp.jmp_71_22) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Denoising%20using%20Noise2Void%20for%20low-field%20magnetic%20resonance%20imaging%3A%20a%20phantom%20study&journal=J.%20Med.%20Phys.&doi=10.4103%2Fjmp.jmp_71_22&volume=47&issue=4&pages=387-393&publication_year=2022&author=Kojima%2CS&author=Ito%2CT&author=Hayashi%2CT)

[^85]: Z. Wang, et al., Blind2unblind: Self-supervised image denoising with visible blind spots. in Proceedings of the IEEE/CVF conference on computer vision and pattern recognition, 2027–2036 (2022)

[^86]: S. Kaji, S. Kida, Overview of image-to-image translation by use of deep neural networks: denoising, super-resolution, modality conversion, and reconstruction in medical imaging. Radiol. Phys. Technol. **12** (3), 235–248 (2019)

[Article](https://link.springer.com/doi/10.1007/s12194-019-00520-y) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Overview%20of%20image-to-image%20translation%20by%20use%20of%20deep%20neural%20networks%3A%20denoising%2C%20super-resolution%2C%20modality%20conversion%2C%20and%20reconstruction%20in%20medical%20imaging&journal=Radiol.%20Phys.%20Technol.&doi=10.1007%2Fs12194-019-00520-y&volume=12&issue=3&pages=235-248&publication_year=2019&author=Kaji%2CS&author=Kida%2CS)

[^87]: H. Yang et al., Deep learning in medical image super resolution: a review. Appl. Intell. **53** (18), 20891–20916 (2023)

[Article](https://link.springer.com/doi/10.1007/s10489-023-04566-9) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Deep%20learning%20in%20medical%20image%20super%20resolution%3A%20a%20review&journal=Appl.%20Intell.&doi=10.1007%2Fs10489-023-04566-9&volume=53&issue=18&pages=20891-20916&publication_year=2023&author=Yang%2CH)

[^88]: D.L. Miller, D. Schauer, The ALARA principle in medical imaging. Philosophy **44** (6), 595–600 (1983)

[Google Scholar](http://scholar.google.com/scholar_lookup?&title=The%20ALARA%20principle%20in%20medical%20imaging&journal=Philosophy&volume=44&issue=6&pages=595-600&publication_year=1983&author=Miller%2CDL&author=Schauer%2CD)

[^89]: E. Immonen et al., The use of deep learning towards dose optimization in low-dose computed tomography: a scoping review. Radiography **28** (1), 208–214 (2022)

[Article](https://doi.org/10.1016%2Fj.radi.2021.07.010) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=The%20use%20of%20deep%20learning%20towards%20dose%20optimization%20in%20low-dose%20computed%20tomography%3A%20a%20scoping%20review&journal=Radiography&doi=10.1016%2Fj.radi.2021.07.010&volume=28&issue=1&pages=208-214&publication_year=2022&author=Immonen%2CE)

[^90]: A. Thummerer, et al., Deep learning based super-resolution for CBCT dose reduction in radiotherapy. Med. Phys. (2024)

[^91]: C. Dong, C.C. Loy, X. Tang, Accelerating the super-resolution convolutional neural network. in Computer Vision–ECCV 2016: 14th European Conference, Amsterdam, The Netherlands, October 11–14, 2016, Proceedings, Part II 14. Springer. 391–407 (2016)

[^92]: D. Mahapatra, B. Bozorgtabar, R. Garnavi, Image super-resolution using progressive generative adversarial networks for medical image analysis. Comput. Med. Imaging Graph. **71**, 30–39 (2019)

[Article](https://doi.org/10.1016%2Fj.compmedimag.2018.10.005) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Image%20super-resolution%20using%20progressive%20generative%20adversarial%20networks%20for%20medical%20image%20analysis&journal=Comput.%20Med.%20Imaging%20Graph.&doi=10.1016%2Fj.compmedimag.2018.10.005&volume=71&pages=30-39&publication_year=2019&author=Mahapatra%2CD&author=Bozorgtabar%2CB&author=Garnavi%2CR)

[^93]: W. Ahmad et al., A new generative adversarial network for medical images super resolution. Sci. Rep. **12** (1), 9533 (2022)

[Article](https://doi.org/10.1038%2Fs41598-022-13658-4) [ADS](http://adsabs.harvard.edu/cgi-bin/nph-data_query?link_type=ABSTRACT&bibcode=2022NatSR..12.9533A) [MathSciNet](http://www.ams.org/mathscinet-getitem?mr=603413) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=A%20new%20generative%20adversarial%20network%20for%20medical%20images%20super%20resolution&journal=Sci.%20Rep.&doi=10.1038%2Fs41598-022-13658-4&volume=12&issue=1&publication_year=2022&author=Ahmad%2CW)

[^94]: J. Liang, et al., Swinir: image restoration using swin transformer. in Proceedings of the IEEE/CVF international conference on computer vision. 1833–1844 (2021)

[^95]: D. Chira, et al., Image super-resolution with deep variational autoencoders, in European Conference on Computer Vision. Springer, 395–411 (2022)

[^96]: S. Cackowski et al., ImUnity: a generalizable VAE-GAN solution for multicenter MR image harmonization. Med. Image Anal. **88**, 102799 (2023)

[Article](https://doi.org/10.1016%2Fj.media.2023.102799) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=ImUnity%3A%20a%20generalizable%20VAE-GAN%20solution%20for%20multicenter%20MR%20image%20harmonization&journal=Med.%20Image%20Anal.&doi=10.1016%2Fj.media.2023.102799&volume=88&publication_year=2023&author=Cackowski%2CS)

[^97]: W.-S. Lai, et al., Deep Laplacian pyramid networks for fast and accurate super-resolution, in Proceedings of the IEEE conference on computer vision and pattern recognition. 624–632 (2017)

[^98]: S. Azizi et al., Deep recurrent neural networks for prostate cancer detection: analysis of temporal enhanced ultrasound. IEEE Trans. Med. Imaging **37** (12), 2695–2703 (2018)

[Article](https://doi.org/10.1109%2FTMI.2018.2849959) [ADS](http://adsabs.harvard.edu/cgi-bin/nph-data_query?link_type=ABSTRACT&bibcode=2018ITMI...37.2695A) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Deep%20recurrent%20neural%20networks%20for%20prostate%20cancer%20detection%3A%20analysis%20of%20temporal%20enhanced%20ultrasound&journal=IEEE%20Trans.%20Med.%20Imaging&doi=10.1109%2FTMI.2018.2849959&volume=37&issue=12&pages=2695-2703&publication_year=2018&author=Azizi%2CS)

[^99]: C. Qin et al., Convolutional recurrent neural networks for dynamic MR image reconstruction. IEEE Trans. Med. Imaging **38** (1), 280–290 (2018)

[Article](https://doi.org/10.1109%2FTMI.2018.2863670) [ADS](http://adsabs.harvard.edu/cgi-bin/nph-data_query?link_type=ABSTRACT&bibcode=2019ITMI...38..280Q) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Convolutional%20recurrent%20neural%20networks%20for%20dynamic%20MR%20image%20reconstruction&journal=IEEE%20Trans.%20Med.%20Imaging&doi=10.1109%2FTMI.2018.2863670&volume=38&issue=1&pages=280-290&publication_year=2018&author=Qin%2CC)

[^100]: Z. Lei, et al., Fully complex-valued gated recurrent neural network for ultrasound imaging. IEEE Trans. Neural Netw. Learn. Syst. (2023)

[^101]: C. Zhao, et al., Predicting tongue motion in unlabeled ultrasound videos using convolutional LSTM neural networks, in ICASSP 2019-2019 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP). IEEE, pp. 5926–5930 (2019)

[^102]: M.M. Ghazi et al., Training recurrent neural networks robust to incomplete data: application to Alzheimer’s disease progression modeling. Med. Image Anal. **53**, 39–46 (2019)

[Article](https://doi.org/10.1016%2Fj.media.2019.01.004) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Training%20recurrent%20neural%20networks%20robust%20to%20incomplete%20data%3A%20application%20to%20Alzheimer%E2%80%99s%20disease%20progression%20modeling&journal=Med.%20Image%20Anal.&doi=10.1016%2Fj.media.2019.01.004&volume=53&pages=39-46&publication_year=2019&author=Ghazi%2CMM)

[^103]: P. Pan et al., Tumor segmentation in automated whole breast ultrasound using bidirectional LSTM neural network and attention mechanism. Ultrasonics **110**, 106271 (2021)

[Article](https://doi.org/10.1016%2Fj.ultras.2020.106271) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Tumor%20segmentation%20in%20automated%20whole%20breast%20ultrasound%20using%20bidirectional%20LSTM%20neural%20network%20and%20attention%20mechanism&journal=Ultrasonics&doi=10.1016%2Fj.ultras.2020.106271&volume=110&publication_year=2021&author=Pan%2CP)

[^104]: A.J.G. Inda, et al., Physics informed neural network (PINN) for noise-robust phase-based magnetic resonance electrical properties tomography, in 2022 3rd URSI Atlantic and Asia Pacific Radio Science Meeting (AT-AP-RASC). IEEE, pp. 1–4 (2022)

[^105]: J. Oldenburg, et al., Augmentation of experimentally obtained flow fields by means of Physics Informed Neural Networks (PINN) demonstrated on aneurysm flow, in Current Directions in Biomedical Engineering. Vol. 9. 1. De Gruyter, 519–523 (2023)

[^106]: A. Villié, et al., Physics-informed neural networks for enhancing medical flow magnetic resonance imaging: artifact correction and mean pressure and Reynolds stresses assimilation. Phys. Fluids **37** (2), (2025)

[^107]: S.G. Mueller et al., Ways toward an early diagnosis in Alzheimer’s disease: the Alzheimer’s Disease Neuroimaging Initiative (ADNI). Alzheimer’s Dementia **1** (1), 55–66 (2005)

[Article](https://doi.org/10.1016%2Fj.jalz.2005.06.003) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Ways%20toward%20an%20early%20diagnosis%20in%20Alzheimer%E2%80%99s%20disease%3A%20the%20Alzheimer%E2%80%99s%20Disease%20Neuroimaging%20Initiative%20%28ADNI%29&journal=Alzheimer%E2%80%99s%20Dementia&doi=10.1016%2Fj.jalz.2005.06.003&volume=1&issue=1&pages=55-66&publication_year=2005&author=Mueller%2CSG)

[^108]: K. Marek et al., The Parkinson progression marker initiative (PPMI). Prog. Neurobiol. **95** (4), 629–635 (2011)

[Article](https://doi.org/10.1016%2Fj.pneurobio.2011.09.005) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=The%20Parkinson%20progression%20marker%20initiative%20%28PPMI%29&journal=Prog.%20Neurobiol.&doi=10.1016%2Fj.pneurobio.2011.09.005&volume=95&issue=4&pages=629-635&publication_year=2011&author=Marek%2CK)

[^109]: E.E. Bron et al., Standardized evaluation of algorithms for computer-aided diagnosis of dementia based on structural MRI: the CADDementia challenge. Neuroimage **111**, 562–579 (2015)

[Article](https://doi.org/10.1016%2Fj.neuroimage.2015.01.048) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Standardized%20evaluation%20of%20algorithms%20for%20computer-aided%20diagnosis%20of%20dementia%20based%20on%20structural%20MRI%3A%20the%20CADDementia%20challenge&journal=Neuroimage&doi=10.1016%2Fj.neuroimage.2015.01.048&volume=111&pages=562-579&publication_year=2015&author=Bron%2CEE)

[^110]: N. Amoroso et al., Deep learning reveals Alzheimer’s disease onset in MCI subjects: results from an international challenge. J. Neurosci. Methods **302**, 3–9 (2018)

[Article](https://doi.org/10.1016%2Fj.jneumeth.2017.12.011) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Deep%20learning%20reveals%20Alzheimer%E2%80%99s%20disease%20onset%20in%20MCI%20subjects%3A%20results%20from%20an%20international%20challenge&journal=J.%20Neurosci.%20Methods&doi=10.1016%2Fj.jneumeth.2017.12.011&volume=302&pages=3-9&publication_year=2018&author=Amoroso%2CN)

[^111]: M. Hatt et al., The first MICCAI challenge on PET tumor segmentation. Med. Image Anal. **44**, 177–195 (2018)

[Article](https://doi.org/10.1016%2Fj.media.2017.12.007) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=The%20first%20MICCAI%20challenge%20on%20PET%20tumor%20segmentation&journal=Med.%20Image%20Anal.&doi=10.1016%2Fj.media.2017.12.007&volume=44&pages=177-195&publication_year=2018&author=Hatt%2CM)

[^112]: O. Commowick et al., Multiple sclerosis lesions segmentation from multiple experts: the MICCAI 2016 challenge dataset. Neuroimage **244**, 118589 (2021)

[Article](https://doi.org/10.1016%2Fj.neuroimage.2021.118589) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Multiple%20sclerosis%20lesions%20segmentation%20from%20multiple%20experts%3A%20the%20MICCAI%202016%20challenge%20dataset&journal=Neuroimage&doi=10.1016%2Fj.neuroimage.2021.118589&volume=244&publication_year=2021&author=Commowick%2CO)

[^113]: P. Papadimitroulas et al., Artificial intelligence: Deep learning in oncological radiomics and challenges of interpretability and data harmonization. Physica Medica: Eur. J. Med. Phys. **83**, 108–121 (2021)

[Article](https://doi.org/10.1016%2Fj.ejmp.2021.03.009) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Artificial%20intelligence%3A%20Deep%20learning%20in%20oncological%20radiomics%20and%20challenges%20of%20interpretability%20and%20data%20harmonization&journal=Physica%20Medica%3A%20Eur.%20J.%20Med.%20Phys.&doi=10.1016%2Fj.ejmp.2021.03.009&volume=83&pages=108-121&publication_year=2021&author=Papadimitroulas%2CP)

[^114]: S. Seoni, et al., All you need is data preparation: a systematic review of image harmonization techniques in Multi-center/device studies for medical support systems. in Computer Methods and Programs in Biomedicine, 108200 (2024)

[^115]: L.M. Pehrson, M.B. Nielsen, C.A. Lauridsen, Automatic pulmonary nodule detection applying deep learning or machine learning algorithms to the LIDC-IDRI database: a systematic review. Diagnostics **9** (1), 29 (2019)

[Article](https://doi.org/10.3390%2Fdiagnostics9010029) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Automatic%20pulmonary%20nodule%20detection%20applying%20deep%20learning%20or%20machine%20learning%20algorithms%20to%20the%20LIDC-IDRI%20database%3A%20a%20systematic%20review&journal=Diagnostics&doi=10.3390%2Fdiagnostics9010029&volume=9&issue=1&publication_year=2019&author=Pehrson%2CLM&author=Nielsen%2CMB&author=Lauridsen%2CCA)

[^116]: R.S. Lee et al., A curated mammography data set for use in computer-aided detection and diagnosis research. Sci. Data **4** (1), 1–9 (2017)

[Article](https://doi.org/10.1038%2Fsdata.2017.177) [MathSciNet](http://www.ams.org/mathscinet-getitem?mr=3331838) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=A%20curated%20mammography%20data%20set%20for%20use%20in%20computer-aided%20detection%20and%20diagnosis%20research&journal=Sci.%20Data&doi=10.1038%2Fsdata.2017.177&volume=4&issue=1&pages=1-9&publication_year=2017&author=Lee%2CRS)

[^117]: D.C. Moura, M.A.G. López, An evaluation of image descriptors combined with clinical data for breast cancer diagnosis. Int. J. Comput. Assist. Radiol. Surg. **8**, 561–574 (2013)

[Article](https://link.springer.com/doi/10.1007/s11548-013-0838-2) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=An%20evaluation%20of%20image%20descriptors%20combined%20with%20clinical%20data%20for%20breast%20cancer%20diagnosis&journal=Int.%20J.%20Comput.%20Assist.%20Radiol.%20Surg.&doi=10.1007%2Fs11548-013-0838-2&volume=8&pages=561-574&publication_year=2013&author=Moura%2CDC&author=L%C3%B3pez%2CMAG)

[^118]: V. Rotemberg et al., A patient-centric dataset of images and metadata for identifying melanomas using clinical context. Sci. Data **8** (1), 34 (2021)

[Article](https://doi.org/10.1038%2Fs41597-021-00815-z) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=A%20patient-centric%20dataset%20of%20images%20and%20metadata%20for%20identifying%20melanomas%20using%20clinical%20context&journal=Sci.%20Data&doi=10.1038%2Fs41597-021-00815-z&volume=8&issue=1&publication_year=2021&author=Rotemberg%2CV)

[^119]: C.E. Bearden, P.M. Thompson, Emerging global initiatives in neurogenetics: the enhancing neuroimaging genetics through meta-analysis (ENIGMA) consortium. Neuron **94** (2), 232–236 (2017)

[Article](https://doi.org/10.1016%2Fj.neuron.2017.03.033) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Emerging%20global%20initiatives%20in%20neurogenetics%3A%20the%20enhancing%20neuroimaging%20genetics%20through%20meta-analysis%20%28ENIGMA%29%20consortium&journal=Neuron&doi=10.1016%2Fj.neuron.2017.03.033&volume=94&issue=2&pages=232-236&publication_year=2017&author=Bearden%2CCE&author=Thompson%2CPM)

[^120]: C. Bycroft et al., The UK Biobank resource with deep phenotyping and genomic data. Nature **562** (7726), 203–209 (2018)

[Article](https://doi.org/10.1038%2Fs41586-018-0579-z) [ADS](http://adsabs.harvard.edu/cgi-bin/nph-data_query?link_type=ABSTRACT&bibcode=2018Natur.562..203B) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=The%20UK%20Biobank%20resource%20with%20deep%20phenotyping%20and%20genomic%20data&journal=Nature&doi=10.1038%2Fs41586-018-0579-z&volume=562&issue=7726&pages=203-209&publication_year=2018&author=Bycroft%2CC)

[^121]: A. Di Martino et al., The autism brain imaging data exchange: towards a large-scale evaluation of the intrinsic brain architecture in autism. Mol. Psychiatry **19** (6), 659–667 (2014)

[Article](https://doi.org/10.1038%2Fmp.2013.78) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=The%20autism%20brain%20imaging%20data%20exchange%3A%20towards%20a%20large-scale%20evaluation%20of%20the%20intrinsic%20brain%20architecture%20in%20autism&journal=Mol.%20Psychiatry&doi=10.1038%2Fmp.2013.78&volume=19&issue=6&pages=659-667&publication_year=2014&author=Martino%2CA)

[^122]: N.L. Weisenfeld, S.K. Warfteld, Normalization of joint image-intensity statistics in MRI using the Kullback-Leibler divergence, in 2004 2nd IEEE International Symposium on Biomedical Imaging: Nano to Macro (IEEE Cat No. 04EX821). IEEE, 101–104 (2004)

[^123]: R.T. Shinohara et al., Statistical normalization techniques for magnetic resonance imaging. NeuroImage: Clinical **6**, 9–19 (2014)

[Article](https://doi.org/10.1016%2Fj.nicl.2014.08.008) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Statistical%20normalization%20techniques%20for%20magnetic%20resonance%20imaging&journal=NeuroImage%3A%20Clinical&doi=10.1016%2Fj.nicl.2014.08.008&volume=6&pages=9-19&publication_year=2014&author=Shinohara%2CRT)

[^124]: M. Eichelberg, et al., Ten years of medical imaging standardization and prototypical implementation: the DICOM standard and the OFFIS DICOM toolkit (DCMTK), in Medical Imaging 2004: PACS and Imaging Informatics. Vol. 5371. SPIE, 57–68 (2004)

[^125]: B. Gibaud, The quest for standards in medical imaging. Eur. J. Radiol. **78** (2), 190–198 (2011)

[Article](https://doi.org/10.1016%2Fj.ejrad.2010.05.003) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=The%20quest%20for%20standards%20in%20medical%20imaging&journal=Eur.%20J.%20Radiol.&doi=10.1016%2Fj.ejrad.2010.05.003&volume=78&issue=2&pages=190-198&publication_year=2011&author=Gibaud%2CB)

[^126]: A. Haga et al., Standardization of imaging features for radiomics analysis. J. Med. Invest. **66** (1.2), 35–37 (2019)

[Article](https://doi.org/10.2152%2Fjmi.66.35) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Standardization%20of%20imaging%20features%20for%20radiomics%20analysis&journal=J.%20Med.%20Invest.&doi=10.2152%2Fjmi.66.35&volume=66&issue=1.2&pages=35-37&publication_year=2019&author=Haga%2CA)

[^127]: M. Cobo et al., Enhancing radiomics and deep learning systems through the standardization of medical imaging workflows. Sci. Data **10** (1), 732 (2023)

[Article](https://doi.org/10.1038%2Fs41597-023-02641-x) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Enhancing%20radiomics%20and%20deep%20learning%20systems%20through%20the%20standardization%20of%20medical%20imaging%20workflows&journal=Sci.%20Data&doi=10.1038%2Fs41597-023-02641-x&volume=10&issue=1&publication_year=2023&author=Cobo%2CM)

[^128]: B.M. Ellingson et al., Consensus recommendations for a standardized brain tumor imaging protocol in clinical trials. Neuro Oncol. **17** (9), 1188–1198 (2015)

[Google Scholar](http://scholar.google.com/scholar_lookup?&title=Consensus%20recommendations%20for%20a%20standardized%20brain%20tumor%20imaging%20protocol%20in%20clinical%20trials&journal=Neuro%20Oncol.&volume=17&issue=9&pages=1188-1198&publication_year=2015&author=Ellingson%2CBM)

[^129]: N. Zhou, et al., Enhanced cycle-consistent generative adversarial network for color normalization of H &E stained images, in International Conference on Medical Image Computing and Computer-Assisted Intervention. Springer. 694–702 (2019)

[^130]: G. Modanwal, A. Vellal, M.A. Mazurowski, Normalization of breast MRIs using cycle-consistent generative adversarial networks. Comput. Methods Programs Biomed. **208**, 106225 (2021)

[Article](https://doi.org/10.1016%2Fj.cmpb.2021.106225) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Normalization%20of%20breast%20MRIs%20using%20cycle-consistent%20generative%20adversarial%20networks&journal=Comput.%20Methods%20Programs%20Biomed.&doi=10.1016%2Fj.cmpb.2021.106225&volume=208&publication_year=2021&author=Modanwal%2CG&author=Vellal%2CA&author=Mazurowski%2CMA)

[^131]: M. Liu, et al., Style transfer using generative adversarial networks for multi-site mri harmonization. in Medical Image Computing and Computer Assisted Intervention–MICCAI 2021: 24th International Conference, Strasbourg, France, September 27–October 1, 2021, Proceedings, Part III 24. Springer. 313–322 (2021)

[^132]: H.J. Jeong et al., MR image harmonization based on cross-center style transfer using deep generative adversarial network. Alzheimer’s Dementia **19**, e066262 (2023)

[Article](https://doi.org/10.1002%2Falz.066262) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=MR%20image%20harmonization%20based%20on%20cross-center%20style%20transfer%20using%20deep%20generative%20adversarial%20network&journal=Alzheimer%E2%80%99s%20Dementia&doi=10.1002%2Falz.066262&volume=19&publication_year=2023&author=Jeong%2CHJ)

[^133]: G.A. Kaissis et al., Secure, privacy-preserving and federated machine learning in medical imaging. Nature Mach. Intell. **2** (6), 305–311 (2020)

[Article](https://doi.org/10.1038%2Fs42256-020-0186-1) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Secure%2C%20privacy-preserving%20and%20federated%20machine%20learning%20in%20medical%20imaging&journal=Nature%20Mach.%20Intell.&doi=10.1038%2Fs42256-020-0186-1&volume=2&issue=6&pages=305-311&publication_year=2020&author=Kaissis%2CGA)

[^134]: M. Jiang, Z. Wang, Q. Dou, Harmofl: harmonizing local and global drifts in federated learning on heterogeneous medical images. Proc. AAAI Conf. Artif. Intell. **36** (1), 1087–1095 (2022)

[Google Scholar](http://scholar.google.com/scholar_lookup?&title=Harmofl%3A%20harmonizing%20local%20and%20global%20drifts%20in%20federated%20learning%20on%20heterogeneous%20medical%20images&journal=Proc.%20AAAI%20Conf.%20Artif.%20Intell.&volume=36&issue=1&pages=1087-1095&publication_year=2022&author=Jiang%2CM&author=Wang%2CZ&author=Dou%2CQ)

[^135]: Q. Zhu, D. Bo, P. Yan, Boundary-weighted domain adaptive neural network for prostate MR image segmentation. IEEE Trans. Med. Imaging **39** (3), 753–763 (2019)

[Article](https://doi.org/10.1109%2FTMI.2019.2935018) [ADS](http://adsabs.harvard.edu/cgi-bin/nph-data_query?link_type=ABSTRACT&bibcode=2020ITMI...39..753Z) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Boundary-weighted%20domain%20adaptive%20neural%20network%20for%20prostate%20MR%20image%20segmentation&journal=IEEE%20Trans.%20Med.%20Imaging&doi=10.1109%2FTMI.2019.2935018&volume=39&issue=3&pages=753-763&publication_year=2019&author=Zhu%2CQ&author=Bo%2CD&author=Yan%2CP)

[^136]: Y. He, et al., Self domain adapted network. in Medical Image Computing and Computer Assisted Intervention–MICCAI 2020: 23rd International Conference, Lima, Peru, October 4–8, 2020, Proceedings, Part I 23. Springer. 437–446 (2020)

[^137]: H. Guan, M. Liu, Domain adaptation for medical image analysis: a survey. IEEE Trans. Biomed. Eng. **69** (3), 1173–1185 (2021)

[Article](https://doi.org/10.1109%2FTBME.2021.3117407) [ADS](http://adsabs.harvard.edu/cgi-bin/nph-data_query?link_type=ABSTRACT&bibcode=2021ITAP...69.1179G) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Domain%20adaptation%20for%20medical%20image%20analysis%3A%20a%20survey&journal=IEEE%20Trans.%20Biomed.%20Eng.&doi=10.1109%2FTBME.2021.3117407&volume=69&issue=3&pages=1173-1185&publication_year=2021&author=Guan%2CH&author=Liu%2CM)

[^138]: Z. Zhang, Y. Li, B.-S. Shin, C2-GAN: content-consistent generative adversarial networks for unsupervised domain adaptation in medical image segmentation. Med. Phys. **49** (10), 6491–6504 (2022)

[Article](https://doi.org/10.1002%2Fmp.15944) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=C2-GAN%3A%20content-consistent%20generative%20adversarial%20networks%20for%20unsupervised%20domain%20adaptation%20in%20medical%20image%20segmentation&journal=Med.%20Phys.&doi=10.1002%2Fmp.15944&volume=49&issue=10&pages=6491-6504&publication_year=2022&author=Zhang%2CZ&author=Li%2CY&author=Shin%2CB-S)

[^139]: H.R. Boveiri et al., Medical image registration using deep neural networks: a comprehensive review. Comput. Electr. Eng. **87**, 106767 (2020)

[Article](https://doi.org/10.1016%2Fj.compeleceng.2020.106767) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Medical%20image%20registration%20using%20deep%20neural%20networks%3A%20a%20comprehensive%20review&journal=Comput.%20Electr.%20Eng.&doi=10.1016%2Fj.compeleceng.2020.106767&volume=87&publication_year=2020&author=Boveiri%2CHR)

[^140]: J. Lv et al., Respiratory motion correction for free-breathing 3D abdominal MRI using CNN-based image registration: a feasibility study. Br. J. Radiol. **91** (1083), 20170788 (2018)

[Article](https://doi.org/10.1259%2Fbjr.20170788) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Respiratory%20motion%20correction%20for%20free-breathing%203D%20abdominal%20MRI%20using%20CNN-based%20image%20registration%3A%20a%20feasibility%20study&journal=Br.%20J.%20Radiol.&doi=10.1259%2Fbjr.20170788&volume=91&issue=1083&publication_year=2018&author=Lv%2CJ)

[^141]: H. Xiaokun, J. Yang, J. Yang, A CNN-based approach for lung 3D-CT registration. IEEE Access **8**, 192835–192843 (2020)

[Article](https://doi.org/10.1109%2FACCESS.2020.3032612) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=A%20CNN-based%20approach%20for%20lung%203D-CT%20registration&journal=IEEE%20Access&doi=10.1109%2FACCESS.2020.3032612&volume=8&pages=192835-192843&publication_year=2020&author=Xiaokun%2CH&author=Yang%2CJ&author=Yang%2CJ)

[^142]: B.R. Thomson, et al., MR-to-US registration using multiclass segmentation of hepatic vasculature with a reduced 3D U-Net, in International Conference on Medical Image Computing and Computer-Assisted Intervention. Springer. 275–284 (2020)

[^143]: G. Balakrishnan et al., Voxelmorph: a learning framework for deformable medical image registration. IEEE Trans. Med. Imaging **38** (8), 1788–1800 (2019)

[Article](https://doi.org/10.1109%2FTMI.2019.2897538) [ADS](http://adsabs.harvard.edu/cgi-bin/nph-data_query?link_type=ABSTRACT&bibcode=2019ITMI...38.1788B) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Voxelmorph%3A%20a%20learning%20framework%20for%20deformable%20medical%20image%20registration&journal=IEEE%20Trans.%20Med.%20Imaging&doi=10.1109%2FTMI.2019.2897538&volume=38&issue=8&pages=1788-1800&publication_year=2019&author=Balakrishnan%2CG)

[^144]: A. Oyarzun-Domeño, et al., Advancing ASL kidney image registration: a tailored pipeline with VoxelMorph. in Neural Computing and Applications, 1–23 (2025)

[^145]: R. McKinley, C. Rummel, CortexMorph: fast cortical thickness estimation via diffeomorphic registration using VoxelMorph, in International Conference on Medical Image Computing and Computer-Assisted Intervention. Springer, 730–739 (2023)

[^146]: H. Ramadan, et al., Medical image registration in the era of Transformers: a recent review. in Informatics in Medicine Unlocked, 101540 (2024)

[^147]: Y. Hua, X. Kangrong, X. Yang, Variational image registration with learned prior using multi-stage VAEs. Comput. Biol. Med. **178**, 108785 (2024)

[Article](https://doi.org/10.1016%2Fj.compbiomed.2024.108785) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Variational%20image%20registration%20with%20learned%20prior%20using%20multi-stage%20VAEs&journal=Comput.%20Biol.%20Med.&doi=10.1016%2Fj.compbiomed.2024.108785&volume=178&publication_year=2024&author=Hua%2CY&author=Kangrong%2CX&author=Yang%2CX)

[^148]: Y. Zheng et al., SymReg-GAN: symmetric image registration with generative adversarial networks. IEEE Trans. Pattern Anal. Mach. Intell. **44** (9), 5631–5646 (2021)

[ADS](http://adsabs.harvard.edu/cgi-bin/nph-data_query?link_type=ABSTRACT&bibcode=2022ITPAM..44.5631Z) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=SymReg-GAN%3A%20symmetric%20image%20registration%20with%20generative%20adversarial%20networks&journal=IEEE%20Trans.%20Pattern%20Anal.%20Mach.%20Intell.&volume=44&issue=9&pages=5631-5646&publication_year=2021&author=Zheng%2CY)

[^149]: K. Ma, et al., Multimodal image registration with deep context reinforcement learning. in Medical Image Computing and Computer Assisted Intervention- MICCAI 2017: 20th International Conference, Quebec City, QC, Canada, September 11–13, 2017, Proceedings, Part I 20. Springer, 240–248 (2017)

[^150]: A. Li, et al., RL-USRegi: autonomous ultrasound registration for radiation-free spinal surgical navigation using reinforcement learning. IEEE Trans. Autom. Sci. Eng. (2025)

[^151]: L.V. Romaguera et al., Prediction of in-plane organ deformation during free-breathing radiotherapy via discriminative spatial transformer networks. Med. Image Anal. **64**, 101754 (2020)

[Article](https://doi.org/10.1016%2Fj.media.2020.101754) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Prediction%20of%20in-plane%20organ%20deformation%20during%20free-breathing%20radiotherapy%20via%20discriminative%20spatial%20transformer%20networks&journal=Med.%20Image%20Anal.&doi=10.1016%2Fj.media.2020.101754&volume=64&publication_year=2020&author=Romaguera%2CLV)

[^152]: Z. Min, et al., Non-rigid medical image registration using physics-informed neural networks, in International Conference on Information Processing in Medical Imaging. Springer, 601–613 (2023)

[^153]: R.L.M. van Herten et al., Physics-informed neural networks for myocardial perfusion MRI quantification. Med. Image Anal. **78**, 102399 (2022)

[Article](https://doi.org/10.1016%2Fj.media.2022.102399) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Physics-informed%20neural%20networks%20for%20myocardial%20perfusion%20MRI%20quantification&journal=Med.%20Image%20Anal.&doi=10.1016%2Fj.media.2022.102399&volume=78&publication_year=2022&author=Herten%2CRLM)

[^154]: Y. Salehi, D. Giannacopoulos, PhysGNN: a physics-driven graph neural network based model for predicting soft tissue deformation in image-guided neurosurgery. Adv. Neural. Inf. Process. Syst. **35**, 37282–37296 (2022)

[Google Scholar](http://scholar.google.com/scholar_lookup?&title=PhysGNN%3A%20a%20physics-driven%20graph%20neural%20network%20based%20model%20for%20predicting%20soft%20tissue%20deformation%20in%20image-guided%20neurosurgery&journal=Adv.%20Neural.%20Inf.%20Process.%20Syst.&volume=35&pages=37282-37296&publication_year=2022&author=Salehi%2CY&author=Giannacopoulos%2CD)

[^155]: Z. Dong, Research on medical image registration based on graphic neural network reinforcement learning. J. Phys.: Conf. Ser. Vol. 1693. 1. IOP Publishing. 012131 (2020)

[^156]: N. Gaggion et al., Improving anatomical plausibility in medical image segmentation via hybrid graph neural networks: applications to chest x-ray analysis. IEEE Trans. Med. Imaging **42** (2), 546–556 (2022)

[Article](https://doi.org/10.1109%2FTMI.2022.3224660) [ADS](http://adsabs.harvard.edu/cgi-bin/nph-data_query?link_type=ABSTRACT&bibcode=2023ITMI...42..546G) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Improving%20anatomical%20plausibility%20in%20medical%20image%20segmentation%20via%20hybrid%20graph%20neural%20networks%3A%20applications%20to%20chest%20x-ray%20analysis&journal=IEEE%20Trans.%20Med.%20Imaging&doi=10.1109%2FTMI.2022.3224660&volume=42&issue=2&pages=546-556&publication_year=2022&author=Gaggion%2CN)

[^157]: L. Hansen, M.P. Heinrich, GraphRegNet: deep graph regularisation networks on sparse keypoints for dense registration of 3D lung CTs. IEEE Trans. Med. Imaging **40** (9), 2246–2257 (2021)

[Article](https://doi.org/10.1109%2FTMI.2021.3073986) [ADS](http://adsabs.harvard.edu/cgi-bin/nph-data_query?link_type=ABSTRACT&bibcode=2021ITMI...40.2246H) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=GraphRegNet%3A%20deep%20graph%20regularisation%20networks%20on%20sparse%20keypoints%20for%20dense%20registration%20of%203D%20lung%20CTs&journal=IEEE%20Trans.%20Med.%20Imaging&doi=10.1109%2FTMI.2021.3073986&volume=40&issue=9&pages=2246-2257&publication_year=2021&author=Hansen%2CL&author=Heinrich%2CMP)

[^158]: Y. Zhang et al., Multi-modal graph neural network for early diagnosis of Alzheimer’s disease from sMRI and PET scans. Comput. Biol. Med. **164**, 107328 (2023)

[Article](https://doi.org/10.1016%2Fj.compbiomed.2023.107328) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Multi-modal%20graph%20neural%20network%20for%20early%20diagnosis%20of%20Alzheimer%E2%80%99s%20disease%20from%20sMRI%20and%20PET%20scans&journal=Comput.%20Biol.%20Med.&doi=10.1016%2Fj.compbiomed.2023.107328&volume=164&publication_year=2023&author=Zhang%2CY)

[^159]: W.M. Wells et al., Adaptive segmentation of MRI data. IEEE Trans. Med. Imaging **15** (4), 429–442 (1996)

[Article](https://doi.org/10.1109%2F42.511747) [ADS](http://adsabs.harvard.edu/cgi-bin/nph-data_query?link_type=ABSTRACT&bibcode=1996ITMI...15..429W) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Adaptive%20segmentation%20of%20MRI%20data&journal=IEEE%20Trans.%20Med.%20Imaging&doi=10.1109%2F42.511747&volume=15&issue=4&pages=429-442&publication_year=1996&author=Wells%2CWM)

[^160]: I. Sluimer, M. Prokop, B. Van Ginneken, Toward automated segmentation of the pathological lung in CT. IEEE Trans. Med. Imaging **24** (8), 1025–1038 (2005)

[Article](https://doi.org/10.1109%2FTMI.2005.851757) [ADS](http://adsabs.harvard.edu/cgi-bin/nph-data_query?link_type=ABSTRACT&bibcode=2005ITMI...24.1025S) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Toward%20automated%20segmentation%20of%20the%20pathological%20lung%20in%20CT&journal=IEEE%20Trans.%20Med.%20Imaging&doi=10.1109%2FTMI.2005.851757&volume=24&issue=8&pages=1025-1038&publication_year=2005&author=Sluimer%2CI&author=Prokop%2CM&author=Ginneken%2CB)

[^161]: S. Pirner et al., CT-based manual segmentation and evaluation of paranasal sinuses. Eur. Arch. Otorhinolaryngol. **266**, 507–518 (2009)

[Article](https://link.springer.com/doi/10.1007/s00405-008-0777-7) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=CT-based%20manual%20segmentation%20and%20evaluation%20of%20paranasal%20sinuses&journal=Eur.%20Arch.%20Otorhinolaryngol.&doi=10.1007%2Fs00405-008-0777-7&volume=266&pages=507-518&publication_year=2009&author=Pirner%2CS)

[^162]: C. Petitjean, J.-N. Dacher, A review of segmentation methods in short axis cardiac MR images. Med. Image Anal. **15** (2), 169–184 (2011)

[Article](https://doi.org/10.1016%2Fj.media.2010.12.004) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=A%20review%20of%20segmentation%20methods%20in%20short%20axis%20cardiac%20MR%20images&journal=Med.%20Image%20Anal.&doi=10.1016%2Fj.media.2010.12.004&volume=15&issue=2&pages=169-184&publication_year=2011&author=Petitjean%2CC&author=Dacher%2CJ-N)

[^163]: I. Despotović, B. Goossens, W. Philips, MRI segmentation of the human brain: challenges, methods, and applications. Comput. Math. Methods Med. **2015** (1), 450341 (2015)

[Google Scholar](http://scholar.google.com/scholar_lookup?&title=MRI%20segmentation%20of%20the%20human%20brain%3A%20challenges%2C%20methods%2C%20and%20applications&journal=Comput.%20Math.%20Methods%20Med.&volume=2015&issue=1&publication_year=2015&author=Despotovi%C4%87%2CI&author=Goossens%2CB&author=Philips%2CW)

[^164]: D. Berron et al., A protocol for manual segmentation of medial temporal lobe subregions in 7 Tesla MRI. NeuroImage: Clin. **15**, 466–482 (2017)

[Article](https://doi.org/10.1016%2Fj.nicl.2017.05.022) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=A%20protocol%20for%20manual%20segmentation%20of%20medial%20temporal%20lobe%20subregions%20in%207%20Tesla%20MRI&journal=NeuroImage%3A%20Clin.&doi=10.1016%2Fj.nicl.2017.05.022&volume=15&pages=466-482&publication_year=2017&author=Berron%2CD)

[^165]: S. Timp, N. Karssemeijer, A new 2D segmentation method based on dynamic programming applied to computer aided detection in mammography. Med. Phys. **31** (5), 958–971 (2004)

[Article](https://doi.org/10.1118%2F1.1688039) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=A%20new%202D%20segmentation%20method%20based%20on%20dynamic%20programming%20applied%20to%20computer%20aided%20detection%20in%20mammography&journal=Med.%20Phys.&doi=10.1118%2F1.1688039&volume=31&issue=5&pages=958-971&publication_year=2004&author=Timp%2CS&author=Karssemeijer%2CN)

[^166]: Y. Wang et al., A two-step convolutional neural network based computer-aided detection scheme for automatically segmenting adipose tissue volume depicting on CT images. Comput. Methods Programs Biomed. **144**, 97–104 (2017)

[Article](https://doi.org/10.1016%2Fj.cmpb.2017.03.017) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=A%20two-step%20convolutional%20neural%20network%20based%20computer-aided%20detection%20scheme%20for%20automatically%20segmenting%20adipose%20tissue%20volume%20depicting%20on%20CT%20images&journal=Comput.%20Methods%20Programs%20Biomed.&doi=10.1016%2Fj.cmpb.2017.03.017&volume=144&pages=97-104&publication_year=2017&author=Wang%2CY)

[^167]: M. Liu et al., A multi-model deep convolutional neural network for automatic hippocampus segmentation and classification in Alzheimer’s disease. Neuroimage **208**, 116459 (2020)

[Article](https://doi.org/10.1016%2Fj.neuroimage.2019.116459) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=A%20multi-model%20deep%20convolutional%20neural%20network%20for%20automatic%20hippocampus%20segmentation%20and%20classification%20in%20Alzheimer%E2%80%99s%20disease&journal=Neuroimage&doi=10.1016%2Fj.neuroimage.2019.116459&volume=208&publication_year=2020&author=Liu%2CM)

[^168]: G. Sharp et al., Vision 20/20: perspectives on automated image segmentation for radiotherapy. Med. Phys. **41** (5), 050902 (2014)

[Article](https://doi.org/10.1118%2F1.4871620) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Vision%2020%2F20%3A%20perspectives%20on%20automated%20image%20segmentation%20for%20radiotherapy&journal=Med.%20Phys.&doi=10.1118%2F1.4871620&volume=41&issue=5&publication_year=2014&author=Sharp%2CG)

[^169]: L.J. Isaksson et al., Automatic segmentation with deep learning in radiotherapy. Cancers **15** (17), 4389 (2023)

[Article](https://doi.org/10.3390%2Fcancers15174389) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Automatic%20segmentation%20with%20deep%20learning%20in%20radiotherapy&journal=Cancers&doi=10.3390%2Fcancers15174389&volume=15&issue=17&publication_year=2023&author=Isaksson%2CLJ)

[^170]: J. Pan et al., Real-time segmentation and tracking of excised corneal contour by deep neural networks for DALK surgical navigation. Comput. Methods Programs Biomed. **197**, 105679 (2020)

[Article](https://doi.org/10.1016%2Fj.cmpb.2020.105679) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Real-time%20segmentation%20and%20tracking%20of%20excised%20corneal%20contour%20by%20deep%20neural%20networks%20for%20DALK%20surgical%20navigation&journal=Comput.%20Methods%20Programs%20Biomed.&doi=10.1016%2Fj.cmpb.2020.105679&volume=197&publication_year=2020&author=Pan%2CJ)

[^171]: A. Madani et al., Artificial intelligence for intraoperative guidance: using semantic segmentation to identify surgical anatomy during laparoscopic cholecystectomy. Ann. Surg. **276** (2), 363–369 (2022)

[Article](https://doi.org/10.1097%2FSLA.0000000000004594) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Artificial%20intelligence%20for%20intraoperative%20guidance%3A%20using%20semantic%20segmentation%20to%20identify%20surgical%20anatomy%20during%20laparoscopic%20cholecystectomy&journal=Ann.%20Surg.&doi=10.1097%2FSLA.0000000000004594&volume=276&issue=2&pages=363-369&publication_year=2022&author=Madani%2CA)

[^172]: H. Zoe et al., Real-time automatic tumor segmentation for ultrasound-guided breast-conserving surgery navigation. Int. J. Comput. Assist. Radiol. Surg. **17** (9), 1663–1672 (2022)

[Article](https://link.springer.com/doi/10.1007/s11548-022-02658-4) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Real-time%20automatic%20tumor%20segmentation%20for%20ultrasound-guided%20breast-conserving%20surgery%20navigation&journal=Int.%20J.%20Comput.%20Assist.%20Radiol.%20Surg.&doi=10.1007%2Fs11548-022-02658-4&volume=17&issue=9&pages=1663-1672&publication_year=2022&author=Zoe%2CH)

[^173]: T.M. Quan, D.G.C. Hildebrand, W.-K. Jeong, Fusionnet: a deep fully residual convolutional neural network for image segmentation in connectomics. Front. Comput. Sci. **3**, 613981 (2021)

[Article](https://doi.org/10.3389%2Ffcomp.2021.613981) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Fusionnet%3A%20a%20deep%20fully%20residual%20convolutional%20neural%20network%20for%20image%20segmentation%20in%20connectomics&journal=Front.%20Comput.%20Sci.&doi=10.3389%2Ffcomp.2021.613981&volume=3&publication_year=2021&author=Quan%2CTM&author=Hildebrand%2CDGC&author=Jeong%2CW-K)

[^174]: A. Tragakis, et al., The fully convolutional transformer for medical image segmentation, in Proceedings of the IEEE/CVF winter conference on applications of computer vision, 3660–3669 (2023)

[^175]: M. Yeung et al., Focus U-Net: a novel dual attention-gated CNN for polyp segmentation during colonoscopy. Comput. Biol. Med. **137**, 104815 (2021)

[Article](https://doi.org/10.1016%2Fj.compbiomed.2021.104815) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Focus%20U-Net%3A%20a%20novel%20dual%20attention-gated%20CNN%20for%20polyp%20segmentation%20during%20colonoscopy&journal=Comput.%20Biol.%20Med.&doi=10.1016%2Fj.compbiomed.2021.104815&volume=137&publication_year=2021&author=Yeung%2CM)

[^176]: A. Hatamizadeh, et al., Unetr: transformers for 3d medical image segmentation. in Proceedings of the IEEE/CVF winter conference on applications of computer vision, 574–584 (2022)

[^177]: R. Azad, et al., Transdeeplab: convolution-free transformer-based deeplab v3+ for medical image segmentation, in International Workshop on PRedictive Intelligence In MEdicine. Springer, 91–102 (2022)

[^178]: R. Karthik et al., Contour-enhanced attention CNN for CT-based COVID-19 segmentation. Pattern Recogn. **125**, 108538 (2022)

[Article](https://doi.org/10.1016%2Fj.patcog.2022.108538) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Contour-enhanced%20attention%20CNN%20for%20CT-based%20COVID-19%20segmentation&journal=Pattern%20Recogn.&doi=10.1016%2Fj.patcog.2022.108538&volume=125&publication_year=2022&author=Karthik%2CR)

[^179]: N.T. Duc et al., Colonformer: an efficient transformer based method for colon polyp segmentation. IEEE Access **10**, 80575–80586 (2022)

[Article](https://doi.org/10.1109%2FACCESS.2022.3195241) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Colonformer%3A%20an%20efficient%20transformer%20based%20method%20for%20colon%20polyp%20segmentation&journal=IEEE%20Access&doi=10.1109%2FACCESS.2022.3195241&volume=10&pages=80575-80586&publication_year=2022&author=Duc%2CNT)

[^180]: H.-Y. Zhou et al., nnFormer: volumetric medical image segmentation via a 3D transformer. IEEE Trans. Image Process. **32**, 4036–4045 (2023)

[Article](https://doi.org/10.1109%2FTIP.2023.3293771) [ADS](http://adsabs.harvard.edu/cgi-bin/nph-data_query?link_type=ABSTRACT&bibcode=2023ITIP...32.4036Z) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=nnFormer%3A%20volumetric%20medical%20image%20segmentation%20via%20a%203D%20transformer&journal=IEEE%20Trans.%20Image%20Process.&doi=10.1109%2FTIP.2023.3293771&volume=32&pages=4036-4045&publication_year=2023&author=Zhou%2CH-Y)

[^181]: Y. Qiu, et al., GKE-TUNet: geometry-knowledge embedded TransUNet model for retinal vessel segmentation considering anatomical topology. IEEE J. Biomed. Health Inform. (2024)

[^182]: A. Ozcan et al., Enhanced-TransUNet for ultrasound segmentation of thyroid nodules. Biomed. Signal Process. Control **95**, 106472 (2024)

[Article](https://doi.org/10.1016%2Fj.bspc.2024.106472) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Enhanced-TransUNet%20for%20ultrasound%20segmentation%20of%20thyroid%20nodules&journal=Biomed.%20Signal%20Process.%20Control&doi=10.1016%2Fj.bspc.2024.106472&volume=95&publication_year=2024&author=Ozcan%2CA)

[^183]: J. Wasserthal et al., TotalSegmentator: robust segmentation of 104 anatomic structures in CT images. Radiology: Artif. Intell. **5** (5), e230024 (2023)

[Google Scholar](http://scholar.google.com/scholar_lookup?&title=TotalSegmentator%3A%20robust%20segmentation%20of%20104%20anatomic%20structures%20in%20CT%20images&journal=Radiology%3A%20Artif.%20Intell.&volume=5&issue=5&publication_year=2023&author=Wasserthal%2CJ)

[^184]: T.A. D’Antonoli et al., Totalsegmentator mri: robust sequence-independent segmentation of multiple anatomic structures in mri. Radiology **314** (2), e241613 (2025)

[Article](https://doi.org/10.1148%2Fradiol.241613) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Totalsegmentator%20mri%3A%20robust%20sequence-independent%20segmentation%20of%20multiple%20anatomic%20structures%20in%20mri&journal=Radiology&doi=10.1148%2Fradiol.241613&volume=314&issue=2&publication_year=2025&author=D%E2%80%99Antonoli%2CTA)

[^185]: C. Baur et al., Autoencoders for unsupervised anomaly segmentation in brain MR images: a comparative study. Med. Image Anal. **69**, 101952 (2021)

[Article](https://doi.org/10.1016%2Fj.media.2020.101952) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Autoencoders%20for%20unsupervised%20anomaly%20segmentation%20in%20brain%20MR%20images%3A%20a%20comparative%20study&journal=Med.%20Image%20Anal.&doi=10.1016%2Fj.media.2020.101952&volume=69&publication_year=2021&author=Baur%2CC)

[^186]: C. Ouyang et al., Self-supervised learning for few-shot medical image segmentation. IEEE Trans. Med. Imaging **41** (7), 1837–1848 (2022)

[Article](https://doi.org/10.1109%2FTMI.2022.3150682) [ADS](http://adsabs.harvard.edu/cgi-bin/nph-data_query?link_type=ABSTRACT&bibcode=2022ITMI...41.1837O) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Self-supervised%20learning%20for%20few-shot%20medical%20image%20segmentation&journal=IEEE%20Trans.%20Med.%20Imaging&doi=10.1109%2FTMI.2022.3150682&volume=41&issue=7&pages=1837-1848&publication_year=2022&author=Ouyang%2CC)

[^187]: M. Mazher et al., Self-supervised spatial-temporal transformer fusion based federated framework for 4D cardiovascular image segmentation. Inf. Fusion **106**, 102256 (2024)

[Article](https://doi.org/10.1016%2Fj.inffus.2024.102256) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Self-supervised%20spatial-temporal%20transformer%20fusion%20based%20federated%20framework%20for%204D%20cardiovascular%20image%20segmentation&journal=Inf.%20Fusion&doi=10.1016%2Fj.inffus.2024.102256&volume=106&publication_year=2024&author=Mazher%2CM)

[^188]: P. Borges, et al., Physics-informed brain MRI segmentation, in Simulation and Synthesis in Medical Imaging: 4th International Workshop, SASHIMI 2019, Held in Conjunction with MICCAI 2019, Shenzhen, China, October 13, 2019, Proceedings 4. Springer, 100–109 (2019)

[^189]: V. Dwivedi, B. Srinivasan, G. Krishnamurthi, Physics informed contour selection for rapid image segmentation. Sci. Rep. **14** (1), 6996 (2024)

[Article](https://doi.org/10.1038%2Fs41598-024-57281-x) [ADS](http://adsabs.harvard.edu/cgi-bin/nph-data_query?link_type=ABSTRACT&bibcode=2024NatSR..14.6996D) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Physics%20informed%20contour%20selection%20for%20rapid%20image%20segmentation&journal=Sci.%20Rep.&doi=10.1038%2Fs41598-024-57281-x&volume=14&issue=1&publication_year=2024&author=Dwivedi%2CV&author=Srinivasan%2CB&author=Krishnamurthi%2CG)

[^190]: H. Zhu, S. Shu, J. Zhang, FAS-UNet: a novel FAS-driven UNet to learn variational image segmentation. Mathematics **10** (21), 4055 (2022)

[Article](https://doi.org/10.3390%2Fmath10214055) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=FAS-UNet%3A%20a%20novel%20FAS-driven%20UNet%20to%20learn%20variational%20image%20segmentation&journal=Mathematics&doi=10.3390%2Fmath10214055&volume=10&issue=21&publication_year=2022&author=Zhu%2CH&author=Shu%2CS&author=Zhang%2CJ)

[^191]: K.H. Leung et al., A physics-guided modular deep-learning based automated framework for tumor segmentation in PET. Phys. Med. Biol. **65** (24), 245032 (2020)

[Article](https://doi.org/10.1088%2F1361-6560%2Fab8535) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=A%20physics-guided%20modular%20deep-learning%20based%20automated%20framework%20for%20tumor%20segmentation%20in%20PET&journal=Phys.%20Med.%20Biol.&doi=10.1088%2F1361-6560%2Fab8535&volume=65&issue=24&publication_year=2020&author=Leung%2CKH)

[^192]: P. Lambin et al., Radiomics: extracting more information from medical images using advanced feature analysis. Eur. J. Cancer **48** (4), 441–446 (2012)

[Article](https://doi.org/10.1016%2Fj.ejca.2011.11.036) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Radiomics%3A%20extracting%20more%20information%20from%20medical%20images%20using%20advanced%20feature%20analysis&journal=Eur.%20J.%20Cancer&doi=10.1016%2Fj.ejca.2011.11.036&volume=48&issue=4&pages=441-446&publication_year=2012&author=Lambin%2CP)

[^193]: M. Avanzo et al., Machine and deep learning methods for radiomics. Med. Phys. **47** (5), e185–e202 (2020)

[Article](https://doi.org/10.1002%2Fmp.13678) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Machine%20and%20deep%20learning%20methods%20for%20radiomics&journal=Med.%20Phys.&doi=10.1002%2Fmp.13678&volume=47&issue=5&pages=e185-e202&publication_year=2020&author=Avanzo%2CM)

[^194]: R.M. Haralick, K. Shanmugam, I.H. Dinstein, Textural features for image classification. IEEE Trans. Syst. Man Cybern. **6**, 610–621 (1973)

[Article](https://doi.org/10.1109%2FTSMC.1973.4309314) [ADS](http://adsabs.harvard.edu/cgi-bin/nph-data_query?link_type=ABSTRACT&bibcode=1973ITSMC...3..610H) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Textural%20features%20for%20image%20classification&journal=IEEE%20Trans.%20Syst.%20Man%20Cybern.&doi=10.1109%2FTSMC.1973.4309314&volume=6&pages=610-621&publication_year=1973&author=Haralick%2CRM&author=Shanmugam%2CK&author=Dinstein%2CIH)

[^195]: X. Tang, Texture information in run-length matrices. IEEE Trans. Image Process. **7** (11), 1602–1609 (1998)

[Article](https://doi.org/10.1109%2F83.725367) [ADS](http://adsabs.harvard.edu/cgi-bin/nph-data_query?link_type=ABSTRACT&bibcode=1998ITIP....7.1602T) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Texture%20information%20in%20run-length%20matrices&journal=IEEE%20Trans.%20Image%20Process.&doi=10.1109%2F83.725367&volume=7&issue=11&pages=1602-1609&publication_year=1998&author=Tang%2CX)

[^196]: I. Buciu, A. Gacsadi, Gabor wavelet based features for medical image analysis and classification, in 2009 2nd International Symposium on Applied Sciences in Biomedical and Communication Technologies. IEEE. 1–4 (2009)

[^197]: C.-C. Chen, J.S. DaPonte, M.D. Fox, Fractal feature analysis and classification in medical imaging. IEEE Trans. Med. Imaging **8** (2), 133–142 (1989)

[Article](https://doi.org/10.1109%2F42.24861) [ADS](http://adsabs.harvard.edu/cgi-bin/nph-data_query?link_type=ABSTRACT&bibcode=1989ITMI....8..133C) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Fractal%20feature%20analysis%20and%20classification%20in%20medical%20imaging&journal=IEEE%20Trans.%20Med.%20Imaging&doi=10.1109%2F42.24861&volume=8&issue=2&pages=133-142&publication_year=1989&author=Chen%2CC-C&author=DaPonte%2CJS&author=Fox%2CMD)

[^198]: T. Mita, T. Kaneko, O. Hori, Joint haar-like features for face detection, in Tenth IEEE International Conference on Computer Vision (ICCV’05) Volume 1. Vol. 2. IEEE, 1619–1626 (2005)

[^199]: R. Muthukrishnan, R. Rohini, LASSO: a feature selection technique in predictive modeling for machine learning, in 2016 IEEE international conference on advances in computer applications (ICACA). IEEE, 18–20 (2016)

[^200]: Z. Pang et al., A computer-aided diagnosis system for dynamic contrast-enhanced MR images based on level set segmentation and ReliefF feature selection. Comput. Math. Methods Med. **2015** (1), 450531 (2015)

[Google Scholar](http://scholar.google.com/scholar_lookup?&title=A%20computer-aided%20diagnosis%20system%20for%20dynamic%20contrast-enhanced%20MR%20images%20based%20on%20level%20set%20segmentation%20and%20ReliefF%20feature%20selection&journal=Comput.%20Math.%20Methods%20Med.&volume=2015&issue=1&publication_year=2015&author=Pang%2CZ)

[^201]: L. Xiaobing et al., Discriminative analysis of schizophrenia using support vector machine and recursive feature elimination on structural MRI images. Medicine **95** (30), e3973 (2016)

[Article](https://doi.org/10.1097%2FMD.0000000000003973) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Discriminative%20analysis%20of%20schizophrenia%20using%20support%20vector%20machine%20and%20recursive%20feature%20elimination%20on%20structural%20MRI%20images&journal=Medicine&doi=10.1097%2FMD.0000000000003973&volume=95&issue=30&publication_year=2016&author=Xiaobing%2CL)

[^202]: L.K. Leong, A.A. Abdullah, Prediction of Alzheimer’s disease (AD) using machine learning techniques with Boruta algorithm as feature selection method. J. Phys.: Conf. Ser. **1372**. 1. IOP Publishing, 012065 (2019)

[^203]: A. Zwanenburg et al., The image biomarker standardization initiative: standardized quantitative radiomics for high-throughput image-based phenotyping. Radiology **295** (2), 328–338 (2020)

[Article](https://doi.org/10.1148%2Fradiol.2020191145) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=The%20image%20biomarker%20standardization%20initiative%3A%20standardized%20quantitative%20radiomics%20for%20high-throughput%20image-based%20phenotyping&journal=Radiology&doi=10.1148%2Fradiol.2020191145&volume=295&issue=2&pages=328-338&publication_year=2020&author=Zwanenburg%2CA)

[^204]: D. Varshni, et al., Pneumonia detection using CNN based feature extraction, in 2019 IEEE international conference on electrical, computer and communication technologies (ICECCT). IEEE. 1–7 (2019)

[^205]: J. Masci, et al., Stacked convolutional auto-encoders for hierarchical feature extraction. in Artificial neural networks and machine learning–ICANN 2011: 21st international conference on artificial neural networks, Espoo, Finland, June 14–17, 2011, proceedings, part i 21. Springer. 52–59 (2011)

[^206]: X. Wanni, F. You-Lei, D. Zhu, ResNet and its application to medical image processing: research progress and challenges. Comput. Methods Programs Biomed. **240**, 107660 (2023)

[Article](https://doi.org/10.1016%2Fj.cmpb.2023.107660) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=ResNet%20and%20its%20application%20to%20medical%20image%20processing%3A%20research%20progress%20and%20challenges&journal=Comput.%20Methods%20Programs%20Biomed.&doi=10.1016%2Fj.cmpb.2023.107660&volume=240&publication_year=2023&author=Wanni%2CX&author=You-Lei%2CF&author=Zhu%2CD)

[^207]: F. Shamshad et al., Transformers in medical imaging: a survey. Med. Image Anal. **88**, 102802 (2023)

[Article](https://doi.org/10.1016%2Fj.media.2023.102802) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Transformers%20in%20medical%20imaging%3A%20a%20survey&journal=Med.%20Image%20Anal.&doi=10.1016%2Fj.media.2023.102802&volume=88&publication_year=2023&author=Shamshad%2CF)

[^208]: D. Cirillo, A. Valencia, Big data analytics for personalized medicine. Curr. Opin. Biotechnol. **58**, 161–167 (2019)

[Article](https://doi.org/10.1016%2Fj.copbio.2019.03.004) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Big%20data%20analytics%20for%20personalized%20medicine&journal=Curr.%20Opin.%20Biotechnol.&doi=10.1016%2Fj.copbio.2019.03.004&volume=58&pages=161-167&publication_year=2019&author=Cirillo%2CD&author=Valencia%2CA)

[^209]: J. Fan et al., Automatic treatment planning based on three-dimensional dose distribution predicted from deep learning technique. Med. Phys. **46** (1), 370–381 (2019)

[Article](https://doi.org/10.1002%2Fmp.13271) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Automatic%20treatment%20planning%20based%20on%20three-dimensional%20dose%20distribution%20predicted%20from%20deep%20learning%20technique&journal=Med.%20Phys.&doi=10.1002%2Fmp.13271&volume=46&issue=1&pages=370-381&publication_year=2019&author=Fan%2CJ)

[^210]: A. Aliper et al., Deep learning applications for predicting pharmacological properties of drugs and drug repurposing using transcriptomic data. Mol. Pharm. **13** (7), 2524–2530 (2016)

[Article](https://doi.org/10.1021%2Facs.molpharmaceut.6b00248) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Deep%20learning%20applications%20for%20predicting%20pharmacological%20properties%20of%20drugs%20and%20drug%20repurposing%20using%20transcriptomic%20data&journal=Mol.%20Pharm.&doi=10.1021%2Facs.molpharmaceut.6b00248&volume=13&issue=7&pages=2524-2530&publication_year=2016&author=Aliper%2CA)

[^211]: W.S. Hong, A.D. Haimovich, R. Andrew Taylor, Predicting hospital admission at emergency department triage using machine learning. PLoS ONE **13** (7), e0201016 (2018)

[Article](https://doi.org/10.1371%2Fjournal.pone.0201016) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Predicting%20hospital%20admission%20at%20emergency%20department%20triage%20using%20machine%20learning&journal=PLoS%20ONE&doi=10.1371%2Fjournal.pone.0201016&volume=13&issue=7&publication_year=2018&author=Hong%2CWS&author=Haimovich%2CAD&author=Andrew%20Taylor%2CR)

[^212]: A. Davoudi et al., Intelligent ICU for autonomous patient monitoring using pervasive sensing and deep learning. Sci. Rep. **9** (1), 8020 (2019)

[Article](https://doi.org/10.1038%2Fs41598-019-44004-w) [ADS](http://adsabs.harvard.edu/cgi-bin/nph-data_query?link_type=ABSTRACT&bibcode=2019NatSR...9.8020D) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Intelligent%20ICU%20for%20autonomous%20patient%20monitoring%20using%20pervasive%20sensing%20and%20deep%20learning&journal=Sci.%20Rep.&doi=10.1038%2Fs41598-019-44004-w&volume=9&issue=1&publication_year=2019&author=Davoudi%2CA)

[^213]: N. Nasrullah et al., Automated lung nodule detection and classification using deep learning combined with multiple strategies. Sensors **19** (17), 3722 (2019)

[Article](https://doi.org/10.3390%2Fs19173722) [ADS](http://adsabs.harvard.edu/cgi-bin/nph-data_query?link_type=ABSTRACT&bibcode=2019Senso..19.3722N) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Automated%20lung%20nodule%20detection%20and%20classification%20using%20deep%20learning%20combined%20with%20multiple%20strategies&journal=Sensors&doi=10.3390%2Fs19173722&volume=19&issue=17&publication_year=2019&author=Nasrullah%2CN)

[^214]: J. Wang et al., Detecting cardiovascular disease from mammograms with deep learning. IEEE Trans. Med. Imaging **36** (5), 1172–1181 (2017)

[Article](https://doi.org/10.1109%2FTMI.2017.2655486) [ADS](http://adsabs.harvard.edu/cgi-bin/nph-data_query?link_type=ABSTRACT&bibcode=2017ITMI...36.1172W) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Detecting%20cardiovascular%20disease%20from%20mammograms%20with%20deep%20learning&journal=IEEE%20Trans.%20Med.%20Imaging&doi=10.1109%2FTMI.2017.2655486&volume=36&issue=5&pages=1172-1181&publication_year=2017&author=Wang%2CJ)

[^215]: R. Gargeya, T. Leng, Automated identification of diabetic retinopathy using deep learning. Ophthalmology **124** (7), 962–969 (2017)

[Article](https://doi.org/10.1016%2Fj.ophtha.2017.02.008) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Automated%20identification%20of%20diabetic%20retinopathy%20using%20deep%20learning&journal=Ophthalmology&doi=10.1016%2Fj.ophtha.2017.02.008&volume=124&issue=7&pages=962-969&publication_year=2017&author=Gargeya%2CR&author=Leng%2CT)

[^216]: Q. Yan et al., Deep-learning-based prediction of late age-related macular degeneration progression. Nature Mach. Intell. **2** (2), 141–150 (2020)

[Article](https://doi.org/10.1038%2Fs42256-020-0154-9) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Deep-learning-based%20prediction%20of%20late%20age-related%20macular%20degeneration%20progression&journal=Nature%20Mach.%20Intell.&doi=10.1038%2Fs42256-020-0154-9&volume=2&issue=2&pages=141-150&publication_year=2020&author=Yan%2CQ)

[^217]: S. Sivaranjini, C.M. Sujatha, Deep learning based diagnosis of Parkinson’s disease using convolutional neural network. Multimedia Tools Appl. **79** (21), 15467–15479 (2020)

[Article](https://link.springer.com/doi/10.1007/s11042-019-7469-8) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Deep%20learning%20based%20diagnosis%20of%20Parkinson%E2%80%99s%20disease%20using%20convolutional%20neural%20network&journal=Multimedia%20Tools%20Appl.&doi=10.1007%2Fs11042-019-7469-8&volume=79&issue=21&pages=15467-15479&publication_year=2020&author=Sivaranjini%2CS&author=Sujatha%2CCM)

[^218]: M.B.T. Noor et al., Application of deep learning in detecting neurological disorders from magnetic resonance images: a survey on the detection of Alzheimer’s disease. Parkinson’s disease and schizophrenia. Brain Inform. **7**, 1–21 (2020)

[Article](https://link.springer.com/doi/10.1186/s40708-020-00112-2) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Application%20of%20deep%20learning%20in%20detecting%20neurological%20disorders%20from%20magnetic%20resonance%20images%3A%20a%20survey%20on%20the%20detection%20of%20Alzheimer%E2%80%99s%20disease.%20Parkinson%E2%80%99s%20disease%20and%20schizophrenia&journal=Brain%20Inform.&doi=10.1186%2Fs40708-020-00112-2&volume=7&pages=1-21&publication_year=2020&author=Noor%2CMBT)

[^219]: S. Murugan et al., DEMNET: a deep learning model for early diagnosis of Alzheimer diseases and dementia from MR images. IEEE Access **9**, 90319–90329 (2021)

[Article](https://doi.org/10.1109%2FACCESS.2021.3090474) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=DEMNET%3A%20a%20deep%20learning%20model%20for%20early%20diagnosis%20of%20Alzheimer%20diseases%20and%20dementia%20from%20MR%20images&journal=IEEE%20Access&doi=10.1109%2FACCESS.2021.3090474&volume=9&pages=90319-90329&publication_year=2021&author=Murugan%2CS)

[^220]: H.J. Kam, H.Y. Kim, Learning representations for the early detection of sepsis with deep neural networks. Comput. Biol. Med. **89**, 248–255 (2017)

[^221]: D. Gunning et al., XAI—explainable artificial intelligence. Sci. Robot. **4** (37), eaay7120 (2019)

[Article](https://doi.org/10.1126%2Fscirobotics.aay7120) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=XAI%E2%80%94explainable%20artificial%20intelligence&journal=Sci.%20Robot.&doi=10.1126%2Fscirobotics.aay7120&volume=4&issue=37&publication_year=2019&author=Gunning%2CD)

[^222]: D. Gunning, D. Aha, DARPA’s explainable artificial intelligence (XAI) program. AI Mag. **40** (2), 44–58 (2019)

[Google Scholar](http://scholar.google.com/scholar_lookup?&title=DARPA%E2%80%99s%20explainable%20artificial%20intelligence%20%28XAI%29%20program&journal=AI%20Mag.&volume=40&issue=2&pages=44-58&publication_year=2019&author=Gunning%2CD&author=Aha%2CD)

[^223]: E. Tjoa, C. Guan, A survey on explainable artificial intelligence (xai): toward medical xai. IEEE Trans. Neural Netw. Learn. Syst. **32** (11), 4793–4813 (2020)

[Article](https://doi.org/10.1109%2FTNNLS.2020.3027314) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=A%20survey%20on%20explainable%20artificial%20intelligence%20%28xai%29%3A%20toward%20medical%20xai&journal=IEEE%20Trans.%20Neural%20Netw.%20Learn.%20Syst.&doi=10.1109%2FTNNLS.2020.3027314&volume=32&issue=11&pages=4793-4813&publication_year=2020&author=Tjoa%2CE&author=Guan%2CC)

[^224]: B.H.M. Van der Velden et al., Explainable artificial intelligence (XAI) in deep learning-based medical image analysis. Med. Image Anal. **79**, 102470 (2022)

[Article](https://doi.org/10.1016%2Fj.media.2022.102470) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Explainable%20artificial%20intelligence%20%28XAI%29%20in%20deep%20learning-based%20medical%20image%20analysis&journal=Med.%20Image%20Anal.&doi=10.1016%2Fj.media.2022.102470&volume=79&publication_year=2022&author=Velden%2CBHM)

[^225]: B.M. De Vries et al., Explainable artificial intelligence (XAI) in radiology and nuclear medicine: a literature review. Front. Med. **10**, 1180773 (2023)

[Article](https://doi.org/10.3389%2Ffmed.2023.1180773) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Explainable%20artificial%20intelligence%20%28XAI%29%20in%20radiology%20and%20nuclear%20medicine%3A%20a%20literature%20review&journal=Front.%20Med.&doi=10.3389%2Ffmed.2023.1180773&volume=10&publication_year=2023&author=Vries%2CBM)

[^226]: C.A. Hamm et al., Interactive explainable deep learning model informs prostate cancer diagnosis at MRI. Radiology **307** (4), e222276 (2023)

[Article](https://doi.org/10.1148%2Fradiol.222276) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Interactive%20explainable%20deep%20learning%20model%20informs%20prostate%20cancer%20diagnosis%20at%20MRI&journal=Radiology&doi=10.1148%2Fradiol.222276&volume=307&issue=4&publication_year=2023&author=Hamm%2CCA)

[^227]: A.B. Arrieta et al., Explainable artificial intelligence (XAI): concepts, taxonomies, opportunities and challenges toward responsible AI. Inf. Fusion **58**, 82–115 (2020)

[Article](https://doi.org/10.1016%2Fj.inffus.2019.12.012) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Explainable%20artificial%20intelligence%20%28XAI%29%3A%20concepts%2C%20taxonomies%2C%20opportunities%20and%20challenges%20toward%20responsible%20AI&journal=Inf.%20Fusion&doi=10.1016%2Fj.inffus.2019.12.012&volume=58&pages=82-115&publication_year=2020&author=Arrieta%2CAB)

[^228]: K. Kira, L.A. Rendell, A practical approach to feature selection. Machine learning proceedings 1992. Elsevier, 249–256 (1992)

[^229]: B.H. Menze et al., A comparison of random forest and its Gini importance with standard chemometric methods for the feature selection and classification of spectral data. BMC Bioinform. **10**, 1–16 (2009)

[Article](https://link.springer.com/doi/10.1186/1471-2105-10-213) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=A%20comparison%20of%20random%20forest%20and%20its%20Gini%20importance%20with%20standard%20chemometric%20methods%20for%20the%20feature%20selection%20and%20classification%20of%20spectral%20data&journal=BMC%20Bioinform.&doi=10.1186%2F1471-2105-10-213&volume=10&pages=1-16&publication_year=2009&author=Menze%2CBH)

[^230]: A. Altmann et al., Permutation importance: a corrected feature importance measure. Bioinformatics **26** (10), 1340–1347 (2010)

[Article](https://doi.org/10.1093%2Fbioinformatics%2Fbtq134) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Permutation%20importance%3A%20a%20corrected%20feature%20importance%20measure&journal=Bioinformatics&doi=10.1093%2Fbioinformatics%2Fbtq134&volume=26&issue=10&pages=1340-1347&publication_year=2010&author=Altmann%2CA)

[^231]: H. Zheng, J. Yuan, L. Chen, Short-term load forecasting using EMD-LSTM neural networks with a Xgboost algorithm for feature importance evaluation. Energies **10** (8), 1168 (2017)

[Article](https://doi.org/10.3390%2Fen10081168) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Short-term%20load%20forecasting%20using%20EMD-LSTM%20neural%20networks%20with%20a%20Xgboost%20algorithm%20for%20feature%20importance%20evaluation&journal=Energies&doi=10.3390%2Fen10081168&volume=10&issue=8&publication_year=2017&author=Zheng%2CH&author=Yuan%2CJ&author=Chen%2CL)

[^232]: D. Castelvecchi, Can we open the black box of AI? Nature News **538** (7623), 20 (2016)

[Article](https://doi.org/10.1038%2F538020a) [ADS](http://adsabs.harvard.edu/cgi-bin/nph-data_query?link_type=ABSTRACT&bibcode=2016Natur.538...20C) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Can%20we%20open%20the%20black%20box%20of%20AI%3F&journal=Nature%20News&doi=10.1038%2F538020a&volume=538&issue=7623&publication_year=2016&author=Castelvecchi%2CD)

[^233]: R. Shwartz-Ziv, N. Tishby, Opening the black box of deep neural networks via information. arXiv preprint [arXiv:1703.00810](http://arxiv.org/abs/1703.00810) (2017)

[^234]: V. Vimbi, N. Shaffi, M. Mahmud, Interpreting artificial intelligence models: a systematic review on the application of LIME and SHAP in Alzheimer’s disease detection. Brain Inform. **11** (1), 10 (2024)

[Article](https://link.springer.com/doi/10.1186/s40708-024-00222-1) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Interpreting%20artificial%20intelligence%20models%3A%20a%20systematic%20review%20on%20the%20application%20of%20LIME%20and%20SHAP%20in%20Alzheimer%E2%80%99s%20disease%20detection&journal=Brain%20Inform.&doi=10.1186%2Fs40708-024-00222-1&volume=11&issue=1&publication_year=2024&author=Vimbi%2CV&author=Shaffi%2CN&author=Mahmud%2CM)

[^235]: A.M. Salih et al., A perspective on explainable artificial intelligence methods: SHAP and LIME. Adv. Intell. Syst. **7** (1), 2400304 (2025)

[Article](https://doi.org/10.1002%2Faisy.202400304) [MathSciNet](http://www.ams.org/mathscinet-getitem?mr=4887954) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=A%20perspective%20on%20explainable%20artificial%20intelligence%20methods%3A%20SHAP%20and%20LIME&journal=Adv.%20Intell.%20Syst.&doi=10.1002%2Faisy.202400304&volume=7&issue=1&publication_year=2025&author=Salih%2CAM)

[^236]: R.R. Selvaraju et al., Grad-CAM: visual explanations from deep networks via gradient-based localization. Int. J. Comput. Vision **128**, 336–359 (2020)

[Article](https://link.springer.com/doi/10.1007/s11263-019-01228-7) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Grad-CAM%3A%20visual%20explanations%20from%20deep%20networks%20via%20gradient-based%20localization&journal=Int.%20J.%20Comput.%20Vision&doi=10.1007%2Fs11263-019-01228-7&volume=128&pages=336-359&publication_year=2020&author=Selvaraju%2CRR)

[^237]: P.-T. Jiang et al., Layercam: exploring hierarchical class activation maps for localization. IEEE Trans. Image Process. **30**, 5875–5888 (2021)

[Article](https://doi.org/10.1109%2FTIP.2021.3089943) [ADS](http://adsabs.harvard.edu/cgi-bin/nph-data_query?link_type=ABSTRACT&bibcode=2021ITIP...30.5875J) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Layercam%3A%20exploring%20hierarchical%20class%20activation%20maps%20for%20localization&journal=IEEE%20Trans.%20Image%20Process.&doi=10.1109%2FTIP.2021.3089943&volume=30&pages=5875-5888&publication_year=2021&author=Jiang%2CP-T)

[^238]: S. Bach et al., On pixel-wise explanations for non-linear classifier decisions by layer-wise relevance propagation. PLoS ONE **10** (7), e0130140 (2015)

[Article](https://doi.org/10.1371%2Fjournal.pone.0130140) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=On%20pixel-wise%20explanations%20for%20non-linear%20classifier%20decisions%20by%20layer-wise%20relevance%20propagation&journal=PLoS%20ONE&doi=10.1371%2Fjournal.pone.0130140&volume=10&issue=7&publication_year=2015&author=Bach%2CS)

[^239]: J. Li et al., Deep-LIFT: deep label-specific feature learning for image annotation. IEEE Trans. Cybern. **52** (8), 7732–7741 (2021)

[Article](https://doi.org/10.1109%2FTCYB.2021.3049630) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Deep-LIFT%3A%20deep%20label-specific%20feature%20learning%20for%20image%20annotation&journal=IEEE%20Trans.%20Cybern.&doi=10.1109%2FTCYB.2021.3049630&volume=52&issue=8&pages=7732-7741&publication_year=2021&author=Li%2CJ)

[^240]: M. Sundararajan, A. Taly, Q. Yan, Axiomatic attribution for deep networks. in International conference on machine learning. PMLR. 3319–3328 (2017)

[^241]: H. Chenchen et al., TrDosePred: a deep learning dose prediction algorithm based on transformers for head and neck cancer radiotherapy. J. Appl. Clin. Med. Phys. **24** (7), e13942 (2023)

[Article](https://doi.org/10.1002%2Facm2.13942) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=TrDosePred%3A%20a%20deep%20learning%20dose%20prediction%20algorithm%20based%20on%20transformers%20for%20head%20and%20neck%20cancer%20radiotherapy&journal=J.%20Appl.%20Clin.%20Med.%20Phys.&doi=10.1002%2Facm2.13942&volume=24&issue=7&publication_year=2023&author=Chenchen%2CH)

[^242]: B. Lou et al., An image-based deep learning framework for individualising radiotherapy dose: a retrospective analysis of outcome prediction. Lancet Digital Health **1** (3), e136–e147 (2019)

[Article](https://doi.org/10.1016%2FS2589-7500%2819%2930058-5) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=An%20image-based%20deep%20learning%20framework%20for%20individualising%20radiotherapy%20dose%3A%20a%20retrospective%20analysis%20of%20outcome%20prediction&journal=Lancet%20Digital%20Health&doi=10.1016%2FS2589-7500%2819%2930058-5&volume=1&issue=3&pages=e136-e147&publication_year=2019&author=Lou%2CB)

[^243]: X. Yiwen et al., Deep learning predicts lung cancer treatment response from serial medical imaging. Clin. Cancer Res. **25** (11), 3266–3275 (2019)

[Article](https://doi.org/10.1158%2F1078-0432.CCR-18-2495) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Deep%20learning%20predicts%20lung%20cancer%20treatment%20response%20from%20serial%20medical%20imaging&journal=Clin.%20Cancer%20Res.&doi=10.1158%2F1078-0432.CCR-18-2495&volume=25&issue=11&pages=3266-3275&publication_year=2019&author=Yiwen%2CX)

[^244]: X. Wang et al., Cancer immunotherapy response prediction from multi-modal clinical and image data using semi-supervised deep learning. Radiother. Oncol. **186**, 109793 (2023)

[Article](https://doi.org/10.1016%2Fj.radonc.2023.109793) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Cancer%20immunotherapy%20response%20prediction%20from%20multi-modal%20clinical%20and%20image%20data%20using%20semi-supervised%20deep%20learning&journal=Radiother.%20Oncol.&doi=10.1016%2Fj.radonc.2023.109793&volume=186&publication_year=2023&author=Wang%2CX)

[^245]: C.-Y. Liao et al., Personalized prediction of immunotherapy response in lung cancer patients using advanced radiomics and deep learning. Cancer Imaging **24** (1), 129 (2024)

[Article](https://link.springer.com/doi/10.1186/s40644-024-00779-4) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Personalized%20prediction%20of%20immunotherapy%20response%20in%20lung%20cancer%20patients%20using%20advanced%20radiomics%20and%20deep%20learning&journal=Cancer%20Imaging&doi=10.1186%2Fs40644-024-00779-4&volume=24&issue=1&publication_year=2024&author=Liao%2CC-Y)

[^246]: H.-H. Tseng et al., Deep reinforcement learning for automated radiation adaptation in lung cancer. Med. Phys. **44** (12), 6690–6705 (2017)

[Article](https://doi.org/10.1002%2Fmp.12625) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Deep%20reinforcement%20learning%20for%20automated%20radiation%20adaptation%20in%20lung%20cancer&journal=Med.%20Phys.&doi=10.1002%2Fmp.12625&volume=44&issue=12&pages=6690-6705&publication_year=2017&author=Tseng%2CH-H)

[^247]: A. Jalalimanesh et al., Simulation-based optimization of radiotherapy: agent-based modeling and reinforcement learning. Math. Comput. Simul. **133**, 235–248 (2017)

[Article](https://doi.org/10.1016%2Fj.matcom.2016.05.008) [MathSciNet](http://www.ams.org/mathscinet-getitem?mr=3575279) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Simulation-based%20optimization%20of%20radiotherapy%3A%20agent-based%20modeling%20and%20reinforcement%20learning&journal=Math.%20Comput.%20Simul.&doi=10.1016%2Fj.matcom.2016.05.008&volume=133&pages=235-248&publication_year=2017&author=Jalalimanesh%2CA)

[^248]: J. Gligorijevic et al., Optimizing clinical trials recruitment via deep learning. J. Am. Med. Inform. Assoc. **26** (11), 1195–1202 (2019)

[Article](https://doi.org/10.1093%2Fjamia%2Focz064) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Optimizing%20clinical%20trials%20recruitment%20via%20deep%20learning&journal=J.%20Am.%20Med.%20Inform.%20Assoc.&doi=10.1093%2Fjamia%2Focz064&volume=26&issue=11&pages=1195-1202&publication_year=2019&author=Gligorijevic%2CJ)

[^249]: D. Dana et al., Deep learning in drug discovery and medicine; scratching the surface. Molecules **23** (9), 2384 (2018)

[Article](https://doi.org/10.3390%2Fmolecules23092384) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Deep%20learning%20in%20drug%20discovery%20and%20medicine%3B%20scratching%20the%20surface&journal=Molecules&doi=10.3390%2Fmolecules23092384&volume=23&issue=9&publication_year=2018&author=Dana%2CD)

[^250]: T.K. Yeung et al., Quality assurance in radiotherapy: evaluation of errors and incidents recorded over a 10 year period. Radiother. Oncol. **74** (3), 283–291 (2005)

[Article](https://doi.org/10.1016%2Fj.radonc.2004.12.003) [ADS](http://adsabs.harvard.edu/cgi-bin/nph-data_query?link_type=ABSTRACT&bibcode=2005IAUS..226..283Y) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Quality%20assurance%20in%20radiotherapy%3A%20evaluation%20of%20errors%20and%20incidents%20recorded%20over%20a%2010%20year%20period&journal=Radiother.%20Oncol.&doi=10.1016%2Fj.radonc.2004.12.003&volume=74&issue=3&pages=283-291&publication_year=2005&author=Yeung%2CTK)

[^251]: D. Sarrut et al., A review of the use and potential of the GATE Monte Carlo simulation code for radiation therapy and dosimetry applications. Med. Phys. **41** (6Part1), 064301 (2014)

[Article](https://doi.org/10.1118%2F1.4871617) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=A%20review%20of%20the%20use%20and%20potential%20of%20the%20GATE%20Monte%20Carlo%20simulation%20code%20for%20radiation%20therapy%20and%20dosimetry%20applications&journal=Med.%20Phys.&doi=10.1118%2F1.4871617&volume=41&issue=6Part1&publication_year=2014&author=Sarrut%2CD)

[^252]: P. Andreo, Monte Carlo simulations in radiotherapy dosimetry. Radiat. Oncol. **13**, 1–15 (2018)

[Article](https://link.springer.com/doi/10.1186/s13014-018-1065-3) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Monte%20Carlo%20simulations%20in%20radiotherapy%20dosimetry&journal=Radiat.%20Oncol.&doi=10.1186%2Fs13014-018-1065-3&volume=13&pages=1-15&publication_year=2018&author=Andreo%2CP)

[^253]: H. Shen, J. Liu, F. Liang, Self-learning Monte Carlo with deep neural networks. Phys. Rev. B **97** (20), 205140 (2018)

[Article](https://doi.org/10.1103%2FPhysRevB.97.205140) [ADS](http://adsabs.harvard.edu/cgi-bin/nph-data_query?link_type=ABSTRACT&bibcode=2018PhRvB..97t5140S) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Self-learning%20Monte%20Carlo%20with%20deep%20neural%20networks&journal=Phys.%20Rev.%20B&doi=10.1103%2FPhysRevB.97.205140&volume=97&issue=20&publication_year=2018&author=Shen%2CH&author=Liu%2CJ&author=Liang%2CF)

[^254]: O. Pastor-Serrano, Z. Perkó, Millisecond speed deep learning based proton dose calculation with Monte Carlo accuracy. Phys. Med. Biol. **67** (10), 105006 (2022)

[Article](https://doi.org/10.1088%2F1361-6560%2Fac692e) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Millisecond%20speed%20deep%20learning%20based%20proton%20dose%20calculation%20with%20Monte%20Carlo%20accuracy&journal=Phys.%20Med.%20Biol.&doi=10.1088%2F1361-6560%2Fac692e&volume=67&issue=10&publication_year=2022&author=Pastor-Serrano%2CO&author=Perk%C3%B3%2CZ)

[^255]: D. Sarrut et al., Artificial intelligence for Monte Carlo simulation in medical physics. Front. Phys. **9**, 738112 (2021)

[Article](https://doi.org/10.3389%2Ffphy.2021.738112) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Artificial%20intelligence%20for%20Monte%20Carlo%20simulation%20in%20medical%20physics&journal=Front.%20Phys.&doi=10.3389%2Ffphy.2021.738112&volume=9&publication_year=2021&author=Sarrut%2CD)

[^256]: J. Maier et al., Real-time estimation of patient-specific dose distributions for medical CT using the deep dose estimation. Med. Phys. **49** (4), 2259–2269 (2022)

[Article](https://doi.org/10.1002%2Fmp.15488) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Real-time%20estimation%20of%20patient-specific%20dose%20distributions%20for%20medical%20CT%20using%20the%20deep%20dose%20estimation&journal=Med.%20Phys.&doi=10.1002%2Fmp.15488&volume=49&issue=4&pages=2259-2269&publication_year=2022&author=Maier%2CJ)

[^257]: L. Gao et al., Generating synthetic CT from low-dose cone-beam CT by using generative adversarial networks for adaptive radiotherapy. Radiat. Oncol. **16**, 1–16 (2021)

[Article](https://link.springer.com/doi/10.1186/s13014-021-01928-w) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Generating%20synthetic%20CT%20from%20low-dose%20cone-beam%20CT%20by%20using%20generative%20adversarial%20networks%20for%20adaptive%20radiotherapy&journal=Radiat.%20Oncol.&doi=10.1186%2Fs13014-021-01928-w&volume=16&pages=1-16&publication_year=2021&author=Gao%2CL)

[^258]: B. Rigaud et al., Automatic segmentation using deep learning to enable online dose optimization during adaptive radiation therapy of cervical cancer. Int. J. Radiat. Oncol.\* Biol.\* Phys. **109** (4), 1096–1110 (2021)

[Article](https://doi.org/10.1016%2Fj.ijrobp.2020.10.038) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Automatic%20segmentation%20using%20deep%20learning%20to%20enable%20online%20dose%20optimization%20during%20adaptive%20radiation%20therapy%20of%20cervical%20cancer&journal=Int.%20J.%20Radiat.%20Oncol.%2A%20Biol.%2A%20Phys.&doi=10.1016%2Fj.ijrobp.2020.10.038&volume=109&issue=4&pages=1096-1110&publication_year=2021&author=Rigaud%2CB)

[^259]: Y. Nagayama et al., Radiation dose optimization potential of deep learning-based reconstruction for multiphase hepatic CT: a clinical and phantom study. Eur. J. Radiol. **151**, 110280 (2022)

[Article](https://doi.org/10.1016%2Fj.ejrad.2022.110280) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Radiation%20dose%20optimization%20potential%20of%20deep%20learning-based%20reconstruction%20for%20multiphase%20hepatic%20CT%3A%20a%20clinical%20and%20phantom%20study&journal=Eur.%20J.%20Radiol.&doi=10.1016%2Fj.ejrad.2022.110280&volume=151&publication_year=2022&author=Nagayama%2CY)

[^260]: R. Wang et al., Multi-objective ensemble deep learning using electronic health records to predict outcomes after lung cancer radiotherapy. Phys. Med. Biol. **64** (24), 245005 (2019)

[Article](https://doi.org/10.1088%2F1361-6560%2Fab555e) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Multi-objective%20ensemble%20deep%20learning%20using%20electronic%20health%20records%20to%20predict%20outcomes%20after%20lung%20cancer%20radiotherapy&journal=Phys.%20Med.%20Biol.&doi=10.1088%2F1361-6560%2Fab555e&volume=64&issue=24&publication_year=2019&author=Wang%2CR)

[^261]: K. Wang et al., A multi-objective radiomics model for the prediction of locoregional recurrence in head and neck squamous cell cancer. Med. Phys. **47** (10), 5392–5400 (2020)

[Article](https://doi.org/10.1002%2Fmp.14388) [ADS](http://adsabs.harvard.edu/cgi-bin/nph-data_query?link_type=ABSTRACT&bibcode=2020QBS.....4...28W) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=A%20multi-objective%20radiomics%20model%20for%20the%20prediction%20of%20locoregional%20recurrence%20in%20head%20and%20neck%20squamous%20cell%20cancer&journal=Med.%20Phys.&doi=10.1002%2Fmp.14388&volume=47&issue=10&pages=5392-5400&publication_year=2020&author=Wang%2CK)

[^262]: B.S. Peters et al., Review of emerging surgical robotic technology. Surg. Endosc. **32**, 1636–1655 (2018)

[Article](https://link.springer.com/doi/10.1007/s00464-018-6079-2) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Review%20of%20emerging%20surgical%20robotic%20technology&journal=Surg.%20Endosc.&doi=10.1007%2Fs00464-018-6079-2&volume=32&pages=1636-1655&publication_year=2018&author=Peters%2CBS)

[^263]: A. Moglia et al., A systematic review on artificial intelligence in robot-assisted surgery. Int. J. Surg. **95**, 106151 (2021)

[Article](https://doi.org/10.1016%2Fj.ijsu.2021.106151) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=A%20systematic%20review%20on%20artificial%20intelligence%20in%20robot-assisted%20surgery&journal=Int.%20J.%20Surg.&doi=10.1016%2Fj.ijsu.2021.106151&volume=95&publication_year=2021&author=Moglia%2CA)

[^264]: G. Veronesi et al., Robot-assisted surgery for lung cancer: State of the art and perspectives. Lung Cancer **101**, 28–34 (2016)

[Article](https://doi.org/10.1016%2Fj.lungcan.2016.09.004) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Robot-assisted%20surgery%20for%20lung%20cancer%3A%20State%20of%20the%20art%20and%20perspectives&journal=Lung%20Cancer&doi=10.1016%2Fj.lungcan.2016.09.004&volume=101&pages=28-34&publication_year=2016&author=Veronesi%2CG)

[^265]: V. Zanagnolo et al., Robot-assisted surgery in gynecologic cancers. J. Minim. Invasive Gynecol. **24** (3), 379–396 (2017)

[Article](https://doi.org/10.1016%2Fj.jmig.2017.01.006) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Robot-assisted%20surgery%20in%20gynecologic%20cancers&journal=J.%20Minim.%20Invasive%20Gynecol.&doi=10.1016%2Fj.jmig.2017.01.006&volume=24&issue=3&pages=379-396&publication_year=2017&author=Zanagnolo%2CV)

[^266]: T. Matsuyama et al., Robotic-assisted surgery for rectal cancer: current state and future perspective. Ann. Gastroenterological Surg. **2** (6), 406–412 (2018)

[Article](https://doi.org/10.1002%2Fags3.12202) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Robotic-assisted%20surgery%20for%20rectal%20cancer%3A%20current%20state%20and%20future%20perspective&journal=Ann.%20Gastroenterological%20Surg.&doi=10.1002%2Fags3.12202&volume=2&issue=6&pages=406-412&publication_year=2018&author=Matsuyama%2CT)

[^267]: U. Falagario et al., Robotic-assisted surgery for the treatment of urologic cancers: recent advances. Expert Rev. Med. Devices **17** (6), 579–590 (2020)

[Article](https://doi.org/10.1080%2F17434440.2020.1762487) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Robotic-assisted%20surgery%20for%20the%20treatment%20of%20urologic%20cancers%3A%20recent%20advances&journal=Expert%20Rev.%20Med.%20Devices&doi=10.1080%2F17434440.2020.1762487&volume=17&issue=6&pages=579-590&publication_year=2020&author=Falagario%2CU)

[^268]: F. Pugin, P. Bucher, P. Morel, History of robotic surgery: from AESOP® and ZEUS® to da Vinci®. J. Visc. Surg. **148** (5), e3–e8 (2011)

[Article](https://doi.org/10.1016%2Fj.jviscsurg.2011.04.007) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=History%20of%20robotic%20surgery%3A%20from%20AESOP%C2%AE%20and%20ZEUS%C2%AE%20to%20da%20Vinci%C2%AE&journal=J.%20Visc.%20Surg.&doi=10.1016%2Fj.jviscsurg.2011.04.007&volume=148&issue=5&pages=e3-e8&publication_year=2011&author=Pugin%2CF&author=Bucher%2CP&author=Morel%2CP)

[^269]: M. Iftikhar et al., Artificial intelligence: revolutionizing robotic surgery. Ann. Med. Surg. **86** (9), 5401–5409 (2024)

[Article](https://doi.org/10.1097%2FMS9.0000000000002426) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Artificial%20intelligence%3A%20revolutionizing%20robotic%20surgery&journal=Ann.%20Med.%20Surg.&doi=10.1097%2FMS9.0000000000002426&volume=86&issue=9&pages=5401-5409&publication_year=2024&author=Iftikhar%2CM)

[^270]: A. Winkler-Schwartz et al., Artificial intelligence in medical education: best practices using machine learning to assess surgical expertise in virtual reality simulation. J. Surg. Educ. **76** (6), 1681–1690 (2019)

[Article](https://doi.org/10.1016%2Fj.jsurg.2019.05.015) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Artificial%20intelligence%20in%20medical%20education%3A%20best%20practices%20using%20machine%20learning%20to%20assess%20surgical%20expertise%20in%20virtual%20reality%20simulation&journal=J.%20Surg.%20Educ.&doi=10.1016%2Fj.jsurg.2019.05.015&volume=76&issue=6&pages=1681-1690&publication_year=2019&author=Winkler-Schwartz%2CA)

[^271]: J. Varas et al., Innovations in surgical training: exploring the role of artificial intelligence and large language models (LLM). Rev. do Col é gio Brasileiro de Cirurgi õ es **50**, e20233605 (2023)

[Google Scholar](http://scholar.google.com/scholar_lookup?&title=Innovations%20in%20surgical%20training%3A%20exploring%20the%20role%20of%20artificial%20intelligence%20and%20large%20language%20models%20%28LLM%29&journal=Rev.%20do%20Col%20%C3%A9%20gio%20Brasileiro%20de%20Cirurgi%20%C3%B5%20es&volume=50&publication_year=2023&author=Varas%2CJ)

[^272]: D.T. Guerrero et al., Advancing surgical education: the use of artificial intelligence in surgical training. Am. Surg. **89** (1), 49–54 (2023)

[Article](https://doi.org/10.1177%2F00031348221101503) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Advancing%20surgical%20education%3A%20the%20use%20of%20artificial%20intelligence%20in%20surgical%20training&journal=Am.%20Surg.&doi=10.1177%2F00031348221101503&volume=89&issue=1&pages=49-54&publication_year=2023&author=Guerrero%2CDT)

[^273]: L. Gordon, T. Grantcharov, F. Rudzicz, Explainable artificial intelligence for safe intraoperative decision support. JAMA Surg. **154** (11), 1064–1065 (2019)

[Article](https://doi.org/10.1001%2Fjamasurg.2019.2821) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Explainable%20artificial%20intelligence%20for%20safe%20intraoperative%20decision%20support&journal=JAMA%20Surg.&doi=10.1001%2Fjamasurg.2019.2821&volume=154&issue=11&pages=1064-1065&publication_year=2019&author=Gordon%2CL&author=Grantcharov%2CT&author=Rudzicz%2CF)

[^274]: L. Tanzi, P. Piazzolla, E. Vezzetti, Intraoperative surgery room management: a deep learning perspective. Int. J. Med. Robotics Comput. Assisted Surg. **16** (5), 1–12 (2020)

[Article](https://doi.org/10.1002%2Frcs.2136) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Intraoperative%20surgery%20room%20management%3A%20a%20deep%20learning%20perspective&journal=Int.%20J.%20Med.%20Robotics%20Comput.%20Assisted%20Surg.&doi=10.1002%2Frcs.2136&volume=16&issue=5&pages=1-12&publication_year=2020&author=Tanzi%2CL&author=Piazzolla%2CP&author=Vezzetti%2CE)

[^275]: D.C. Birkhoff, A.S.H.M. van Dalen, M.P. Schijven, A review on the current applications of artificial intelligence in the operating room. Surg. Innov. **28** (5), 611–619 (2021)

[^276]: Y. Liu et al., Evaluation of a wearable wireless device with artificial intelligence, iThermonitor WT705, for continuous temperature monitoring for patients in surgical wards: a prospective comparative study. BMJ Open **10** (11), e039474 (2020)

[Article](https://doi.org/10.1136%2Fbmjopen-2020-039474) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Evaluation%20of%20a%20wearable%20wireless%20device%20with%20artificial%20intelligence%2C%20iThermonitor%20WT705%2C%20for%20continuous%20temperature%20monitoring%20for%20patients%20in%20surgical%20wards%3A%20a%20prospective%20comparative%20study&journal=BMJ%20Open&doi=10.1136%2Fbmjopen-2020-039474&volume=10&issue=11&publication_year=2020&author=Liu%2CY)

[^277]: F. Michard, Postoperative surveillance: the rise of wireless sensors, pocket ultrasound devices and AI-enabled tools, in Hemodynamic Monitoring and Fluid Therapy During Surgery, 289 (2024)

[^278]: I. Park et al., Artificial intelligence model predicting postoperative pain using facial expressions: a pilot study. J. Clin. Monit. Comput. **38** (2), 261–270 (2024)

[Article](https://link.springer.com/doi/10.1007/s10877-023-01100-7) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Artificial%20intelligence%20model%20predicting%20postoperative%20pain%20using%20facial%20expressions%3A%20a%20pilot%20study&journal=J.%20Clin.%20Monit.%20Comput.&doi=10.1007%2Fs10877-023-01100-7&volume=38&issue=2&pages=261-270&publication_year=2024&author=Park%2CI)

[^279]: B. Johansson et al., Robotic surgery: review on minimally invasive techniques. Fusion Multidiscip. Res. Int. J. **2** (2), 201–210 (2021)

[Article](https://doi.org/10.63995%2FGQNC2594) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Robotic%20surgery%3A%20review%20on%20minimally%20invasive%20techniques&journal=Fusion%20Multidiscip.%20Res.%20Int.%20J.&doi=10.63995%2FGQNC2594&volume=2&issue=2&pages=201-210&publication_year=2021&author=Johansson%2CB)

[^280]: M. Takeuchi et al., Automated surgical-phase recognition for robot-assisted minimally invasive esophagectomy using artificial intelligence. Ann. Surg. Oncol. **29** (11), 6847–6855 (2022)

[Article](https://doi.org/10.1245%2Fs10434-022-11996-1) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Automated%20surgical-phase%20recognition%20for%20robot-assisted%20minimally%20invasive%20esophagectomy%20using%20artificial%20intelligence&journal=Ann.%20Surg.%20Oncol.&doi=10.1245%2Fs10434-022-11996-1&volume=29&issue=11&pages=6847-6855&publication_year=2022&author=Takeuchi%2CM)

[^281]: R. Anteby et al., Deep learning visual analysis in laparoscopic surgery: a systematic review and diagnostic test accuracy meta-analysis. Surg. Endosc. **35**, 1521–1533 (2021)

[Article](https://link.springer.com/doi/10.1007/s00464-020-08168-1) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Deep%20learning%20visual%20analysis%20in%20laparoscopic%20surgery%3A%20a%20systematic%20review%20and%20diagnostic%20test%20accuracy%20meta-analysis&journal=Surg.%20Endosc.&doi=10.1007%2Fs00464-020-08168-1&volume=35&pages=1521-1533&publication_year=2021&author=Anteby%2CR)

[^282]: I.S. Alam et al., Emerging intraoperative imaging modalities to improve surgical precision. Mol. Imag. Biol. **20**, 705–715 (2018)

[Article](https://link.springer.com/doi/10.1007/s11307-018-1227-6) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Emerging%20intraoperative%20imaging%20modalities%20to%20improve%20surgical%20precision&journal=Mol.%20Imag.%20Biol.&doi=10.1007%2Fs11307-018-1227-6&volume=20&pages=705-715&publication_year=2018&author=Alam%2CIS)

[^283]: S.M. Hussain et al., Deep learning based image processing for robot assisted surgery: a systematic literature survey. IEEE Access **10**, 122627–122657 (2022)

[Article](https://doi.org/10.1109%2FACCESS.2022.3223704) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Deep%20learning%20based%20image%20processing%20for%20robot%20assisted%20surgery%3A%20a%20systematic%20literature%20survey&journal=IEEE%20Access&doi=10.1109%2FACCESS.2022.3223704&volume=10&pages=122627-122657&publication_year=2022&author=Hussain%2CSM)

[^284]: R. Levendovics, et al., Surgical data science: Emerging trends and future pathways. in Recent Advances in Intelligent Engineering: Volume Dedicated to Imre J. Rudas’ Seventy-Fifth Birthday, 65–84 (2024)

[^285]: S. Gerlach, A. Schlaefer, Robotic systems in radiotherapy and radiosurgery. Curr. Robot. Rep. **3** (1), 9–19 (2022)

[Article](https://link.springer.com/doi/10.1007/s43154-021-00072-3) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Robotic%20systems%20in%20radiotherapy%20and%20radiosurgery&journal=Curr.%20Robot.%20Rep.&doi=10.1007%2Fs43154-021-00072-3&volume=3&issue=1&pages=9-19&publication_year=2022&author=Gerlach%2CS&author=Schlaefer%2CA)

[^286]: F.Á.C. Manuel et al., Clinical feasibility of combining intraoperative electron radiation therapy with minimally invasive surgery: a potential for electron-FLASH clinical development. Clin. Transl. Oncol. **25** (2), 429–439 (2023)

[Article](https://link.springer.com/doi/10.1007/s12094-022-02955-z) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Clinical%20feasibility%20of%20combining%20intraoperative%20electron%20radiation%20therapy%20with%20minimally%20invasive%20surgery%3A%20a%20potential%20for%20electron-FLASH%20clinical%20development&journal=Clin.%20Transl.%20Oncol.&doi=10.1007%2Fs12094-022-02955-z&volume=25&issue=2&pages=429-439&publication_year=2023&author=Manuel%2CF%C3%81C)

[^287]: R. Fitriana, T.D. Eriyatno, T. Djatna, Progress in business intelligence system research: a literature review. Int. J. Basic Appl. Sci. IJBAS-IJENS **11** (03), 118503–6464 (2011)

[Google Scholar](http://scholar.google.com/scholar_lookup?&title=Progress%20in%20business%20intelligence%20system%20research%3A%20a%20literature%20review&journal=Int.%20J.%20Basic%20Appl.%20Sci.%20IJBAS-IJENS&volume=11&issue=03&pages=118503-6464&publication_year=2011&author=Fitriana%2CR&author=Eriyatno%2CTD&author=Djatna%2CT)

[^288]: E.O. Eboigbe et al., Business intelligence transformation through AI and data analytics. Eng. Sci. Technol. J. **4** (5), 285–307 (2023)

[Article](https://doi.org/10.51594%2Festj.v4i5.616) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Business%20intelligence%20transformation%20through%20AI%20and%20data%20analytics&journal=Eng.%20Sci.%20Technol.%20J.&doi=10.51594%2Festj.v4i5.616&volume=4&issue=5&pages=285-307&publication_year=2023&author=Eboigbe%2CEO)

[^289]: F. Berns et al., Medical operational AI: artificial intelligence in routine medical operations. J. Lab. Med. **47** (4), 171–179 (2023)

[Article](https://doi.org/10.1515%2Flabmed-2023-0011) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Medical%20operational%20AI%3A%20artificial%20intelligence%20in%20routine%20medical%20operations&journal=J.%20Lab.%20Med.&doi=10.1515%2Flabmed-2023-0011&volume=47&issue=4&pages=171-179&publication_year=2023&author=Berns%2CF)

[^290]: E. Ranschaert, L. Topff, O. Pianykh, Optimization of radiology workflow with artificial intelligence. Radiol. Clin. **59** (6), 955–966 (2021)

[Article](https://doi.org/10.1016%2Fj.rcl.2021.06.006) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Optimization%20of%20radiology%20workflow%20with%20artificial%20intelligence&journal=Radiol.%20Clin.&doi=10.1016%2Fj.rcl.2021.06.006&volume=59&issue=6&pages=955-966&publication_year=2021&author=Ranschaert%2CE&author=Topff%2CL&author=Pianykh%2CO)

[^291]: D.S. Rammal, M. Alomar, S. Palaian et al., AI-Driven pharmacy practice: unleashing the revolutionary potential in medication management, pharmacy workflow, and patient care. Pharm. Pract. **22** (2), 1–11 (2024)

[Google Scholar](http://scholar.google.com/scholar_lookup?&title=AI-Driven%20pharmacy%20practice%3A%20unleashing%20the%20revolutionary%20potential%20in%20medication%20management%2C%20pharmacy%20workflow%2C%20and%20patient%20care&journal=Pharm.%20Pract.&volume=22&issue=2&pages=1-11&publication_year=2024&author=Rammal%2CDS&author=Alomar%2CM&author=Palaian%2CS)

[^292]: Y. Alnsour et al., Predicting patient length of stay using artificial intelligence to assist healthcare professionals in resource planning and scheduling decisions. J. Global Inf. Manag. **31** (1), 1–14 (2023)

[Article](https://doi.org/10.4018%2FJGIM.323059) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Predicting%20patient%20length%20of%20stay%20using%20artificial%20intelligence%20to%20assist%20healthcare%20professionals%20in%20resource%20planning%20and%20scheduling%20decisions&journal=J.%20Global%20Inf.%20Manag.&doi=10.4018%2FJGIM.323059&volume=31&issue=1&pages=1-14&publication_year=2023&author=Alnsour%2CY)

[^293]: H. Shamszare, A. Choudhury, Clinicians’ perceptions of artificial intelligence: focus on workload, risk, trust, clinical decision making, and clinical integration. Healthcare. **11** (16), 2308 (2023) MDPI

[^294]: C. Levin, E. Naimi, M. Saban, Evaluating AI systems to combat mental health issues in healthcare workers: An integrative literature review, Int. J. Med. Inform., 105566 (2024)

[^295]: M.R. King, The future of AI in medicine: a perspective from a Chatbot. Ann. Biomed. Eng. **51** (2), 291–295 (2023)

[Article](https://link.springer.com/doi/10.1007/s10439-022-03121-w) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=The%20future%20of%20AI%20in%20medicine%3A%20a%20perspective%20from%20a%20Chatbot&journal=Ann.%20Biomed.%20Eng.&doi=10.1007%2Fs10439-022-03121-w&volume=51&issue=2&pages=291-295&publication_year=2023&author=King%2CMR)

[^296]: J. Park et al., Patient-centered radiology reports with generative artificial intelligence: adding value to radiology reporting. Sci. Rep. **14** (1), 13218 (2024)

[Article](https://doi.org/10.1038%2Fs41598-024-63824-z) [ADS](http://adsabs.harvard.edu/cgi-bin/nph-data_query?link_type=ABSTRACT&bibcode=2024NatSR..1413218P) [MathSciNet](http://www.ams.org/mathscinet-getitem?mr=1143693) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Patient-centered%20radiology%20reports%20with%20generative%20artificial%20intelligence%3A%20adding%20value%20to%20radiology%20reporting&journal=Sci.%20Rep.&doi=10.1038%2Fs41598-024-63824-z&volume=14&issue=1&publication_year=2024&author=Park%2CJ)