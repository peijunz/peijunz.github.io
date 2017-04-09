Research Experience
###################

:date: 2015-10-09
:slug: research-ustc
:tags: reasearch, ustc

Partial Coherent Light
-------------------------------------
:Cooperators: Zhonghua Qian, Zijiao Yang, Jingsong Shang
:Advisor: Anting Wang, Quan Zhang
:Time: Sep. 2014---Jan. 2015

We studied the spatial coherent properties of partial coherent light by experiments, which was later awarded the First Grade Prize in Physical Experiment Contest. Our equipment was based on the partial coherent light source and the modified Michelson’s inter-ferometer. 

Noise reduction
``````````````````````
In the beginning, we could not get stable interference fringes because of the small but crucial vibration of the optical platform. To overcome this problem, we improved the insulation of rotating ground glass and designed more flexible devices to control the glass. The original data were a series of photos taken by the CCD. Realizing that the noise in the photos would render the results unreliable, I used wavelet transformation to filter the noise of high frequency. After that, we were able to compute the contrast in different lines which are parallel to the central line.

.. .. figure:: /res/origin.png
..     :alt: original photo with noise
..     :align: left
..     :scale: 50%
..     
..     Original photo with noise
..     
.. .. figure:: /res/nonoise.png
..     :alt: Noise reduced 
..     :align: left
..     :scale: 50%
..     
..     Processed picture with reduced noise

Data fitting
```````````````````
Unlike what was claimed to be Gaussian in the bibliography, we noticed a sharp peak in the middle of the curve of contrast distribution, for most photos. Then, I proposed a crude statistical model to explain the properties of the contrast curve, which fits the trend and shape of the curve quite well. 

.. figure:: {attach}/res/fit.png
    :alt: fit
    :align: center
    :width: 500px
    
    Use the new model to fit the data

During the research of our group, I not only undertook some experimental work, but also completed more than half of the work after experiments---data analysis and statistical theory of contrast curve. I have learnt to be patient and meticulous during the process of building the equipment to get fine data. 

.. Members of our group often discuss together to solve many knotty problems.

-----------------------

NPT Width of Band Matrices
-------------------------------
:Cooperators:  Yuchen Ma, Yijian Zou
:Advisor: Wenge Wang
:Time: Apr. 2015---Jun. 2015
:Dissertation: `arXiv:1512.02701 <http://arxiv.org/abs/1512.02701>`_

Studies have shown close relationship among width of non-perturbative parts (NPT), half width of local spectral density of states (LDOS), and half width of eigenfunctions (EFs). We predicted behaviors of NPT width in the limits of strong and weak perturbation with some approximation. The prediction fit very well with the results from Monte Carlo Simulation. We also developed iteration algorithms based on matrix transformation and path summation to numerically calculate NPT width with less time complexity. Furthermore, similarities between behavious of NPT width and half width of eigenstates are studied by new algorithms. In this project, I contributed mainly in two aspects: the prediction in the limit of strong perturbation and development of an effective method of computing NPT width. That is, I contributed to Section III. (B, C), IV. A, Appendix. (A, B) in the dissertation above.

The limit of strong perturbation
`````````````````````````````````
Yijian used truncated matrices to get an accurate enough approximate solution in the weak perturbation. Then I delved into strong perturbation analysis, doubting about one unproved assertion we made before. It seems to be obvious and trivial that the behaviour of NPT width under strong perturbation should be linear. The false illusion comes from a normal mistake of scale transformation. Provided that we have a tiny flea which is able to jump 1m from the ground, and another flea as large as humans, made up of the same material, then the latter one will still jump about the same height rather than much higher than 1m (here we do not consider the possibility of the collapse of the flea because of its own weight). 

To estimate the increasing trend when perturbation increase, I used some techniques learnt in the Statistical Mechanics course and many other approximation methods. The estimation can be completed with a little information about the distribution, which can be easily calculated by MC simulation of eigenvalues of small random matrices. I also absorbed the truncation method from Yijian in my derivation. Then I proved the trend of NPT width :math:`w`, when the :math:`\lambda` increase, should be about :math:`w\propto\lambda\sqrt{\ln\lambda}`, with a slight deviation term :math:`\sqrt{\ln\lambda}` from the former unsubstantial assertion :math:`w\propto\lambda`. 

.. figure:: {attach}/res/large.png
    :alt:   large
    :align: center
    :width: 500
    
    The linearity between :math:`w/\lambda` and :math:`\sqrt{\ln\lambda}` hold true when :math:`\lambda` is large
..    :scale: 40%
    
Iteration Algorithms
````````````````````
Yuchen developed his path summation approach to calculate the NPT width of special tri-diagonal. The method gave a simple iteration method to calculate the NPT width, while the derivation of this method is very complicated. This has impressed me and I decide to find a simpler derivation in a totally different way. Inspired by the similarity between a theorem in the Linear Algebra and the iteration method, I finally used the theorem and proved the method with simplicity. The proof mainly used an equivalent criterion of the positive definiteness of a matrix, as well as the famous Gaussian Elimination. 

However, my derivation was not superfluous. When we moved on to the general (2n+1)-diagonal condition, some unbridgeable variance emerged. My method can be neatly generalized to the new condition. Later, Yuchen also developed his generalization independently. The two results are not equivalent. Under the examination of several specific instances, mine hold true whereas even simple penta-diagonal condition disproved his. But the method of Yuchen is very inspiring---the method is novel and it has inspired me a lot. 

------------------------------

Soft Matter
---------------------------
:Advisor: Xiaoming Mao
:Time: July. 2015--Sep. 2015
:Location: University of Michigan, Ann Arbor

I have learned much experience of programming, knowledge of soft matter and self-assembly, and meet with many new friends in Umich.

Self-assembly of colloidal particles
``````````````````````````````````````
There are many interactions between colloidal particles, such as DLVO interaction, depletion interaction, capillary interaction, etc.. I researched about the probable self-assembly of 2D colloidal particles dominated by depletion interaction. The aim is to find a structure to assemble the kagome lattice. The kagome lattice can exhibit sub-extensive numbers of zero-frequency floppy modes when it is of finite size, such as the property shown in the `video <http://www-personal.umich.edu/~maox/research/TTMM/TTMM.html>`_. I developed a program written in SciPy to calculate the potential between two colloidal particles. The source code can be downloaded `here <https://bitbucket.org/zpj/kagome-lattice/downloads>`_

The hinge of calculating the depletion potential is to calculate the intersection area of extended borders. One of the difficulties is to **find extended borders** for given borders. To make the problem simpler, I supposed the border consists of several arcs. The efficiency of the program is inversely proportional to the number of segments of each colloid. Another difficulty is to **get the intersection area** of two extended borders. To solve the problem, we first consider two borders as a unity. Then we split the unity into several groups of closed curves without intersection with any other loop. The area of each region can be calculated by Green's Theorem. Among these loops we suppose the areas of :math:`C_1, C_2,\ldots C_m` are all positive. If :math:`C_k` is the one with the largest area, we can prove that the area of intersection should be :math:`A_{\mathrm{inter}}=\sum_{i=0}^m A(C_i)-A(C_k)`. In this way, we are able to compute the potential at **arbitrary** accuracy! We can find the contacting point for given angles by bisection method and later calculate the potential at that point for combinations of rotation angle and revolution angle :math:`(x, y)`. Using the contour plot of the contacting potential energy in the coordinate (x,y), we can easily analyse the stability of tip-to-tip, side-to-side and other assembly. I tried many kinds of shapes, like I, III, VII and etc.. There are some slides_ showing the potential plot of shape VII.

.. figure:: {attach}/res/shape1.svg
    :alt:   shape
    :width: 400px
    :align: left
    
    Shape I
    
.. figure:: {attach}/res/shape3.svg
    :alt:   shape
    :width: 400px
    :align: left
    
    Shape III

.. figure:: {attach}/res/shape7.svg
    :alt:   shape
    :width: 400px
    :align: left
    
    Shape VII


Molecular dynamic simulation is needed for further verification. I suppose that the potential should be calculated by interpolation of the values calculated in some near points to save time, at the price of memory. However, as the experiment seems to have not reached the scale in which the depletion interaction becomes dominant, I did not continue to do the dynamic simulation. There are also other ways of self-assembly driven by capillary interaction. This interaction can be implemented more easily in experiments. However it is more complicated and the calculation is more difficult than the depletion interaction.

.. _slides:

.. note:: Left/Right Click to go forward/backward. Mouse wheel move forward/backward to zoom in/out. Shift+Mouse wheel to rotate. Or you can read more about `how to play <http://sozi.baierouge.fr/pages/40-play.html>`_

.. raw:: html

    <div class="figure align-center">
      <iframe style="width: 480px;height: 320px;max-width: 100%;" src="/colloid/shape-show.sozi.html"></iframe>
    </div>

Mechanical diode
`````````````````````````````````````````
I developed a program to calculate the resonance of a mechanical chain. The source code can be downloaded in my `here <https://bitbucket.org/zpj/kagome-lattice/downloads>`_. The aim is to make the signal easy to propagate in one direction but hard in another direction, like the motion of a kink in a spiral wire. The model is a single chain made up of many particles with some friction and potential between near particles. We drive one end at a period of :math:`T` to see the resonance of the other end and the energy dissipation. Even though the band width will not be significantly broadened, increase the number of particles will make the resonance curve more smooth. There is a critical friction :math:`\mu_n` to make the bandwidth wide and the resonance smooth. I calculated the resonance under dry friction or double-well potential. The first disposition of dry friction can be analytically solved by slicing time into pieces, and in each piece it is a harmonic oscillator of many degrees of freedom. But the process is also difficult to be done by humans, so we need simulation to see the behaviour. For the second disposition of double-well potential, the behaviour is much more difficult. The behaviour may diverge at some point thus the period of resonance turns out to be :math:`nT`, which is very interesting. 

To calculate transmission rate of energy, it is very important to judge whether the system has reached a stable state with fluctuation little enough. For the resonance of period :math:`T`, it is straight forward; but if the period has changed to several times of that, it is much more difficult. The program is versatile to handle these conditions to give an accurate judgement of the stability. This way the mean energy can be computed reliably with less time.
