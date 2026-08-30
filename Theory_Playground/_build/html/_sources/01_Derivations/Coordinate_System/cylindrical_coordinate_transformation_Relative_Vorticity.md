# Cylindrical Coordinate Transformation : Relative Vorticity

+++

## 目標

**將相對渦度**

$$
\vec{\zeta} \overset{\text{def}}{=} \nabla \times \vec{V}
$$

**寫在圓柱座標系 $(r, \lambda, z)$**，對應速度 $([u\text{ 徑向}],[v\text{ 切向}],[w\text{ 垂直}])$

$$\begin{aligned}
\left[\hat{r} \text{ 徑向}\right] \quad &\vec{\zeta} \cdot  \hat{r} =  \frac{1}{r}\frac{\partial w}{\partial \lambda} - \frac{\partial v}{\partial z}   \\
[\hat{\lambda} \text{ 切向}] \quad &\vec{\zeta} \cdot  \hat{\lambda} =  \frac{\partial u}{\partial z} - \frac{\partial w}{\partial r}  \\
\left[\hat{z} \text{ 垂直}\right] \quad &\vec{\zeta} \cdot  \hat{z} = \frac{1}{r}\left( \frac{\partial (rv)}{\partial r} - \frac{\partial u}{\partial \lambda} \right)
\end{aligned}$$


+++

## 假設與已知 (Assumptions & Preliminaries)

* **【已知 1】速度向量 $\vec{V}$ ：** 

  $$\vec{V} = u\hat{r} + v\hat{\lambda} + w\hat{z}$$

* **【已知 2】 圓柱座標的 $\nabla$ 算子 ：** 

  $$\nabla = \hat{r}\frac{\partial}{\partial r} + \hat{\lambda}\frac{1}{r}\frac{\partial}{\partial \lambda} + \hat{z}\frac{\partial}{\partial z}$$

+++

## 證明

$$\begin{gather*}
\vec{\zeta} & =& \nabla \times \vec{V} \\
& \overset{\text{已知1,已知2}}{=}& \left(\hat{r}\frac{\partial}{\partial r} + \hat{\lambda}\frac{1}{r}\frac{\partial}{\partial \lambda} + \hat{z}\frac{\partial}{\partial z} \right) \times \left(u\hat{r} + v\hat{\lambda} + w\hat{z} \right) \\
& =& \begin{vmatrix} \hat{r} & \hat{\lambda} & \hat{z} \\ \frac{\partial}{\partial r} & \frac{1}{r}\frac{\partial}{\partial \lambda} & \frac{\partial}{\partial z} \\ u & v & w \end{vmatrix} \\
& =&\left( \frac{1}{r}\frac{\partial w}{\partial \lambda} - \frac{\partial v}{\partial z} \right) \hat{r} + 
\left( \frac{\partial u}{\partial z} - \frac{\partial w}{\partial r} \right) \hat{\lambda} +
\frac{1}{r}\left( \frac{\partial (rv)}{\partial r} - \frac{\partial u}{\partial \lambda} \right)\hat{z} \\
\end{gather*}$$

+++
