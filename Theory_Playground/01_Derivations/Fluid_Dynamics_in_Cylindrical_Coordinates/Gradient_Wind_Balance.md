# Gradient Wind Balance

+++

## 證明目標:

$$\frac{v^{2}}{r} + fv = \frac{\partial\phi}{\partial r}$$

* $\frac{v^2}{r}$ (離心力)： 空氣塊旋轉時被往外甩的力
* $fv$ (科氏力)： 地球自轉造成的偏向力（$f$ 是科氏參數），在北半球也是向外拉扯空氣塊
* $\frac{\partial\phi}{\partial r} $ ( Anelastic Approximation的 $\frac{1}{\rho} \frac{\partial p}{\partial r}$ 氣壓梯度力)： 颱風中心是低壓，外圍是高壓，所以這是一股強大的「向內吸力」

+++

## 假設與已知 (Assumptions & Preliminaries)

* **【已知 1】 [圓柱座標的 $\hat{r}$ 動量方程式](https://derek1403.github.io/Theory_Playground/_build/html/01_Derivations/Coordinate_System/cylindrical_coordinate_transformation_momentum_equation.html)：** 

  $$\frac{Du}{Dt} - \frac{v^2}{r} - fv = -\frac{1}{\rho} \frac{\partial P}{\partial r} + \text{RHS}_{\hat{r}}$$

* **【假設 1】 僅考慮科氏力、壓力梯度力：** 

  * 忽略摩擦力或其他未解析的小尺度亂流外力
  * 自由大氣是 **無黏滯性 (Inviscid)** 的
  * 在圓柱座標的 $\hat{r}$ 動量方程式中 $\text{RHS}_{\hat{r}} = 0$ 

* **【假設 2】 軸對稱假設：**
  
  $$\frac{\partial}{\partial\lambda} = 0$$

* **【已知 2】 $\frac{Du}{Dt}$ 的展開 ：** 

  $$\frac{Du}{Dt} = \frac{\partial u}{\partial t} + u\frac{\partial u}{\partial r}  +  w\frac{\partial u}{\partial z}$$

  * $\frac{Du}{Dt} = \frac{\partial u}{\partial t} + u\frac{\partial u}{\partial r} + v\frac{\partial u}{\partial\lambda} +  w\frac{\partial u}{\partial z}$ 但是【假設 2】可以知道 $\frac{\partial}{\partial\lambda} = 0$

* **【假設 3】 尺度分析與主環流假設：** 
  
  $$\frac{Du}{Dt} \ll \frac{v^2}{r}$$

  * 對於一個成熟的颱風中
    * 水平長度尺度 (半徑)：$L \sim 10^5 \text{ m}$ ($100 \text{ km}$)
    * 垂直高度尺度 (對流層)：$H \sim 10^4 \text{ m}$ ($10 \text{ km}$)
    * 切線風速 (繞圈的主環流)：$V \sim 50 \text{m} \cdot \text{s}^{-1}$
    * 徑向風速 (向內輻合的次環流)：$U \sim 5 \text{m} \cdot \text{s}^{-1}$ 
    * 垂直風速 (上升氣流)：$W \sim 1 \text{m} \cdot \text{s}^{-1}$
    * 科氏參數 (中低緯度)：$f \sim 10^{-4} \text{ s}^{-1}$
  1. 離心力項： $\frac{V^2}{L} \sim \frac{50^2}{100,000} = \frac{2500}{10^5} = \mathbf{0.025 }$ $[\text{m} \cdot \text{s}^{-2}]$
  2. 科氏力項： $fV \sim (10^{-4}) \times 50 = \mathbf{0.005 }$ $[\text{m} \cdot \text{s}^{-2}]$
  3. 徑向平流加速度 ($u\frac{\partial u}{\partial r}$):這代表風往內吹時，因為地形或結構改變導致的速度空間變化。$\frac{U^2}{L} \sim \frac{5^2}{100,000} = \frac{25}{10^5} = \mathbf{0.00025 }$ $[\text{m} \cdot \text{s}^{-2}]$
  4. 垂直平流加速度 ($w\frac{\partial u}{\partial z}$):這代表上升氣流把不同高度的徑向風帶上來造成的加速度。$\frac{W \cdot U}{H} \sim \frac{1 \times 5}{10,000} = \mathbf{0.0005 }$ $[\text{m} \cdot \text{s}^{-2}]$
  5. 局部時間變化 ($\frac{\partial u}{\partial t}$):對於一個已經發展成熟的颱風，系統處於「準穩定態 (Quasi-steady)」，風速隨時間的變化非常緩慢所以這項通常比平流項還要小，我們大略估計它也是 $\sim 10^{-4}$ 量級。

* **【假設 4】 Anelastic Approximation：**
  
  * 氣壓：$P(r, \lambda, z, t) = \bar{P}(z) + P'(r, \lambda, z, t)$
  * 密度：$\rho(r, \lambda, z, t) = \bar{\rho}(z) + \rho'(r, \lambda, z, t)$

* **【假設 5】 尺度分析：**
  
  $$\rho'(r, \lambda, z, t) \ll \bar{\rho}(z)$$

  * $\rho'(r, \lambda, z, t) \sim $ 
  * 背景密度是隨著高度遞減的。大氣層越往上，空氣越稀薄 ：
    * 在近地表（海平面）： $\bar{\rho} \sim 1.2 \text{kg} \cdot \text{m}^{-3}$ 
    * 在 5 公里高空： $\bar{\rho} \sim 0.7 \text{kg} \cdot \text{m}^{-3}$ 
    * 在 10 公里高空： $\bar{\rho} \sim 0.4 \text{kg} \cdot \text{m}^{-3}$ 
  * 擾動密度 $\rho'$ 可以從理想氣體狀態方程式 $\frac{\rho'}{\bar{\rho}} \approx -\frac{\theta'}{\bar{\theta}}$ 估計
    * 在近地表： $\rho' \approx 1.2 \times 0.016 \sim 0.019 \text{kg} \cdot \text{m}^{-3}$ 
    * 在 10 公里高空： $\rho' \approx 0.4 \times 0.016 \sim 0.006 \text{kg} \cdot \text{m}^{-3}$ 


* **【定義 1】 擾動位勢 $\phi$：** 
  
  $$\phi(r, \lambda, z, t) \overset{\text{def}}{=} \frac{P'(r, \lambda, z, t)}{\bar{\rho}(z)}$$

+++

## 證明:

$$\begin{gather*}
\frac{Du}{Dt} - \frac{v^2}{r} - fv &\overset{\text{已知 1}}{=}& -\frac{1}{\rho} \frac{\partial P}{\partial r} + \text{RHS}_{\hat{r}}   \\
\frac{Du}{Dt} - \frac{v^2}{r} - fv &\overset{\text{假設 1}}{=}& -\frac{1}{\rho} \frac{\partial P}{\partial r} \\
- \frac{v^2}{r} - fv &\overset{\text{假設 3}}{=}& -\frac{1}{\rho} \frac{\partial P}{\partial r} \\
- \frac{v^2}{r} - fv &\overset{\text{假設 4}}{=}& -\frac{1}{\bar{\rho}(z) + \rho'(r, \lambda, z, t)} \frac{\partial }{\partial r} \left[ \bar{P}(z) + P'(r, \lambda, z, t) \right] \\
- \frac{v^2}{r} - fv &=& -\frac{1}{\bar{\rho}(z) + \rho'(r, \lambda, z, t)} \frac{\partial }{\partial r} \left[  P'(r, \lambda, z, t) \right] \\
- \frac{v^2}{r} - fv &\overset{\text{假設 5}}{=}& -\frac{1}{\bar{\rho}(z)} \frac{\partial }{\partial r} \left[  P'(r, \lambda, z, t) \right] \\
- \frac{v^2}{r} - fv &=& -\frac{\partial }{\partial r} \left[ \frac{P'(r, \lambda, z, t)}{\bar{\rho}(z)}  \right] \\
- \frac{v^2}{r} - fv &\overset{\text{定義 1}}{=}& -\frac{\partial }{\partial r} \left[ \phi(r, \lambda, z, t)  \right] \\
- \frac{v^2}{r} - fv &=& -\frac{\partial \phi}{\partial r}  \\
\frac{v^2}{r} + fv &=& \frac{\partial \phi}{\partial r}  \\
\end{gather*}$$


+++
