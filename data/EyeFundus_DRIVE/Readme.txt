# DRIVE
#######


# http://www.isi.uu.nl/Research/Databases/DRIVE/process_download.php


DRIVE: Digital Retinal Images for Vessel Extraction
Introduction

The DRIVE database has been established to enable comparative studies on segmentation of blood vessels in retinal images. The research community is invited to test their algorithms on this database and share the results with other researchers through this web site. On this page, instructions can be found on downloading the database and uploading results, and the results of various methods can be inspected.
Using the database

The data included in this database can be used, free of charge, for research and educational purposes. Copying, redistribution, and any unauthorized commercial use is prohibited. The use of this database is restricted to those individuals or organizations that obtained the database directly from this website. Any researcher reporting results which use this database must acknowledge the DRIVE database. We request you to do so by citing this publication:

    J.J. Staal, M.D. Abramoff, M. Niemeijer, M.A. Viergever, B. van Ginneken, "Ridge based vessel segmentation in color images of the retina", IEEE Transactions on Medical Imaging, 2004, vol. 23, pp. 501-509.

In addition, we appreciate to hear about any publications that use the DRIVE database. Feedback on the database and this website is also welcome. The person to contact is Bram van Ginneken.
Data description

The photographs for the DRIVE database were obtained from a diabetic retinopathy screening program in The Netherlands. The screening population consisted of 400 diabetic subjects between 25-90 years of age. Forty photographs have been randomly selected, 33 do not show any sign of diabetic retinopathy and 7 show signs of mild early diabetic retinopathy. Each image has been JPEG compressed.

The images were acquired using a Canon CR5 non-mydriatic 3CCD camera with a 45 degree field of view (FOV). Each image was captured using 8 bits per color plane at 768 by 584 pixels. The FOV of each image is circular with a diameter of approximately 540 pixels. For this database, the images have been cropped around the FOV. For each image, a mask image is provided that delineates the FOV.

The set of 40 images has been divided into a training and a test set, both containing 20 images. For the training images, a single manual segmentation of the vasculature is available. For the test cases, two manual segmentations are available; one is used as gold standard, the other one can be used to compare computer generated segmentations with those of an independent human observer. All human observers that manually segmented the vasculature were instructed and trained by an experienced ophthalmologist. They were asked to mark all pixels for which they were for at least 70% certain that they were vessel.

All of the images contained in the database were actually used for making clinical diagnoses. To ensure the utmost protection of patient privacy, information that might allow the identity of a patient to be reconstructed has been removed, and we have no actual knowledge that the images could be used alone or in combination to identify any subject. To minimize any further risk of breach of privacy, the use of this database is restricted to those individuals or organizations that obtained the database directly from this website.

For more background information on the database, consult [1] or [2].
Download

The download page gives instructions on downloading the DRIVE database.
Results of segmentation algorithms

Since its original publication in 2004, a wide range of segmentation algorithms has been applied to the DRIVE database. At the end of this page we list papers that cite the database. On this site we provide a results page that lists results from some algorithms in tabular format and shows ROC curves. The result browser allows interactive viewing of images and segmentations for a small set of methods that we have implemented. The result browser is also a useful way to explore the database.
Links

    Another database with retinal images in which the vasculature has been segmented is available on Adam Hoover's Stare web site.
    The REVIEW database, containing a set of retinal images with accurate width measurements can be found here.

References

The following papers describe the DRIVE database:

[1] J.J. Staal, M.D. Abramoff, M. Niemeijer, M.A. Viergever, B. van Ginneken, "Ridge based vessel segmentation in color images of the retina", IEEE Transactions on Medical Imaging, 2004, vol. 23, pp. 501-509.

[2] M. Niemeijer, J.J. Staal, B. van Ginneken, M. Loog, M.D. Abramoff, "Comparative study of retinal vessel segmentation methods on a new publicly available database", in: SPIE Medical Imaging, Editor(s): J. Michael Fitzpatrick, M. Sonka, SPIE, 2004, vol. 5370, pp. 648-656.

Below are papers that refer to the 2004 TMI paper in which the DRIVE database was first described. If you have published a paper that uses the DRIVE database and is not listed here, please contact Bram van Ginneken. Some conference papers have been omitted from the list when a later journal paper has been published. This list was last updated in april 2007.

    Jelinek HF, Cree MJ, Leandro JJG, Soares JVB, Cesar RM, and Luckie A, "Automated segmentation of retinal blood vessels and identification of proliferative diabetic retinopathy", JOSA A 24(5): 1448-1456, 2007.
    Adjeroh DA, Kandaswamy U, Vernon Odom J, "Texton-based segmentation of retinal vessels", JOSA A 24(5): 1384-1393, 2007.
    Wu CH, Agam G, "Probabilistic retinal vessel segmentation", in Proceedings of SPIE, vol. 6512, Medical Imaging 2007.
    Staal J, van Ginneken B, Viergever MA, "Automatic rib segmentation and labeling in computed tomography scans using a general framework for detection, recognition and segmentation of objects in volumetric data", Medical Image Analysis 11(1): 35-46, 2007.
    Martinez-Perez ME, Hughes AD, Thom SA, et al., "Segmentation of blood vessels from red-free and fluorescein retinal images", Medical Image Analysis 11(1): 47-61, 2007.
    Perfetti R, Ricci E, Casali D, et al., "Cellular neural networks with virtual template expansion for retinal vessel segmentation", IEEE Transactions on Circuits and Systems II 54(2): 141-145, 2007.
    Wang L, Bhalerao A, Wilson R, "Analysis of retinal vasculature using a multiresolution Hermite model", IEEE Transactions on Medical Imaging 26(2): 137-152, 2007.
    Salem SA, Salem NM, Nandi AK, "Segmentation of retinal blood vessels using a novel clustering algorithm (RACAL) with a partial supervision strategy", Medical and Biological Engineering and Computing 45(3): 261-273, 2007.
    Al-Rawi M, Qutaishat M, Arrar M, "An improved matched filter for blood vessel detection of digital retinal images", Computers in Biology and Medicine 37(2): 262-267, 2007.
    Garg S, Sivaswamy J, Chandra S, "Unsupervised curvature-based retinal vessel segmentation", in International Symposium on Biomedical Imaging, pp. 344-347, 2007.
    Wu CH, Agam G, Stanchev P, "A hybrid filtering approach to retinal vessel segmentation", in International Symposium on Biomedical Imaging, pp. 604-607, 2007.
    Sofka M, Stewart CV, "Retinal vessel centerline extraction using multiscale matched filters, confidence and edge measures", IEEE Transactions on Medical Imaging 25(12): 1531-1546, 2006.
    Cai WC, Chung ACS, "Multi-resolution vessel segmentation using normalized cuts in retinal images", in Lecture Notes in Computer Science 4191:928-936, 2006.
    Mendonca AM, Campilho A, "Segmentation of retinal blood vessels by combining the detection of centerlines and morphological reconstruction", IEEE Transactions on Medical Imaging 25(9): 1200-1213, 2006.
    Soares JVB, Leandro JJG, Cesar RM, et al., "Retinal vessel segmentation using the 2-D Gabor wavelet and supervised classification", IEEE Transactions on Medical Imaging 25(9): 1214-1222, 2006.
    Sapuppo F, Bucolo M, Intaglietta M, et al., "Cellular non-linear networks for microcirculation applications" International Journal of Circuit Theory and Applications 34(4): 471-488, 2006.
    Narasimha-Lyer H, Can A, Roysam B, et al.,"Robust detection and classification of longitudinal changes in color retinal fundus images for monitoring diabetic retinopathy", IEEE Transactions on Biomedical Engineering 53(6): 1084-1098, 2006.
    Chanwimaluang T, Fan GL, Fransen SR, "Hybrid retinal image registration", IEEE Transactions on Information Technology in Biomedicine 10(1): 129-142, 2006.
    Condurache AP, Aach T, "Vessel Segmentation in 2D-Projection Images Using a Supervised Linear Hysteresis Classifier", in 18th International Conference on Pattern Recognition, vol 1, pp. 343-346, 2006.
    Sun C, Vallotton P, "Fast Linear Feature Detection Using Multiple Directional Non-Maximum Suppression", in 18th International Conference on Pattern Recognition, vol.2, pp. 288-291, 2006.
    Sheng K, Kameyama K, Katagishi K, and Toraichi K, "Matched filter design by fluency analysis for a more accurate fundus image blood-vessel extraction", in Proceedings of the 24th IASTED International Conference on Biomedical Engineering, p. 350-355, 2006.
    Jung E, Hong K, "Automatic Retinal Vasculature Structure Tracing and Vascular Landmark Extraction from Human Eye Image", in International Conference on Hybrid Information Technology, pp. 161-167, 2006.
    Van Staalduinen M, Backer E, Van der Lubbe JCA, "Robust Feature Detection for Computer Vision", in ASCI, pp. 406-413, 2006.
    Abramoff MD, Suttorp-Schulten MSA, "Web-based screening for diabetic retinopathy in a primary care population: The EyeCheck project", Telemedicine Journal and E-health 11(6): 668-674, 2005.
    Aho E, Vanne J, Hamalainen TD, et al., "Block-level parallel processing for scaling evenly divisible images", IEEE Transactions on circuits and systems I 52(12): 2717-2725, 2005.
    Stewart CV, "Computer vision algorithms for retinal image analysis: Current results and future directions", in Lecture Notes in Computer Science 3765: 31-50, 2005.
    Abdul-Karim MA, Roysam B, Dowell-Mesfin NM, et al., "Automatic selection of parameters for vessel/neurite segmentation algorithms", IEEE Transactions on Image Processing 14(9): 1338-1350, 2005.
    Niemeijer M, van Ginneken B, Staal J, et al., "Automatic detection of red lesions in digital color fundus photographs", IEEE Transactions on Medical Imaging 24(5): 584-592, 2005.
    Condurache AP, Aach T, "Vessel segmentation in angiograms using hysteresis thresholding", in Proceedings of MVA, 2005.
    HF Jelinek, C Depardieu, C Lucas, DJ Cornforth, et al., "Towards Vessel Characterisation in the Vicinity of the Optic Disc in Digital Retinal Images", in Image and Vision Computing New Zealand, 2005.
    Cree M, Cornforth D, Jelinek HF, "Vessel Segmentation and Tracking Using a Two-Dimensional Model", in Image and Vision Computing New Zealand, 2005.
    Petrie TC, Boult TE, "Separable Features as a Basis for Adaptive Multi-Thresholding and Segmentation", listed by Google Scholar. 