# Axisymmetric Tangential Momentum Equation (軸對稱切線動量方程式)

+++

## 證明目標:

$$\frac{\partial v}{\partial t}+u(f+\zeta)+w\frac{\partial v}{\partial z}=X$$


1. $- u(\zeta + f)$：絕對渦度的徑向平流
    * $(\zeta + f)$ 是「絕對渦度」（颱風自己的旋轉 + 地球給的旋轉）。
    * 當颱風底層有強烈的向內氣流（$u < 0$）時，它會把外圍的絕對渦度往中心「擠壓」集中，因為 $u<0 \implies - u >0$ ，這會導致當地的切線風速狂飆（$\frac{\partial v}{\partial t} > 0$）
    * 這就像花式溜冰選手把手收攏 ($u < 0$)，旋轉速度就會變快！
2. $- w\frac{\partial v}{\partial z}$：垂直動量的平流
    * 如果底層的風比較強，高空的風比較弱（$\frac{\partial v}{\partial z} < 0$），當上升氣流（$w > 0$）把底層強大的旋轉動能往上帶時，就會讓上面原本轉得慢的地方加速。
3. $X$：外力破壞
    * 例如地表摩擦力，它通常與風向相反，所以會不斷消耗切線風速。

+++

## 假設與已知 (Assumptions & Preliminaries)

* **【已知 1】 [圓柱座標的 $\hat{\lambda}$ 動量方程式](https://derek1403.github.io/Theory_Playground/_build/html/01_Derivations/Coordinate_System/cylindrical_coordinate_transformation_momentum_equation.html)：** 

  $$\frac{Dv}{Dt} + \frac{uv}{r} + fu = -\frac{1}{\rho r} \frac{\partial P}{\partial \lambda} + \text{RHS}_{\hat{\lambda}}$$

* **【假設 1】 僅考慮科氏力、壓力梯度力、動量強迫、摩擦力：** 

  * 切向風速 $v$ 的改變（颱風的增強或減弱）深刻依賴於 **海表面的摩擦力消耗** ，或是對流雲系內部未被網格解析出來的小尺度動量交換，我們不能將其忽略必須將其參數化
  * 自由大氣是 **無黏滯性 (Inviscid)** 的
  * 在圓柱座標的 $\hat{\lambda}$ 動量方程式中 $\text{RHS}_{\hat{\lambda}} = X$ 是除了科氏力、壓力梯度力以外的力，在這裡我們多考慮**動量強迫、摩擦力**

* **【假設 2】 軸對稱假設：**
  
  $$\frac{\partial}{\partial\lambda} = 0$$

  * $-\frac{1}{\rho r} \frac{\partial P}{\partial \lambda} =0$


* **【已知 2】 $\frac{Du}{Dt}$ 的展開 ：** 

  $$\frac{Dv}{Dt} = \frac{\partial v}{\partial t} + u\frac{\partial v}{\partial r}  +  w\frac{\partial v}{\partial z}$$

  * $\frac{Dv}{Dt} = \frac{\partial v}{\partial t} + u\frac{\partial v}{\partial r} + v\frac{\partial v}{\partial\lambda} +  w\frac{\partial v}{\partial z}$ 但是【假設 2】可以知道 $\frac{\partial}{\partial\lambda} = 0$

* **【已知 3】 [$\hat{z}$ 相對渦度 $\zeta$](https://derek1403.github.io/Theory_Playground/_build/html/01_Derivations/Coordinate_System/cylindrical_coordinate_transformation_Relative_Vorticity.html)：** 
  
  $$\begin{gather*}
  \vec{\zeta} \cdot  \hat{z} =&\zeta &=& \frac{1}{r}\left( \frac{\partial [rv]}{\partial r} - \frac{\partial u}{\partial \lambda} \right)\\
  &&\overset{\text{假設 2}}{=}& \frac{1}{r} \frac{\partial [rv]}{\partial r}\\
  &&=& \frac{1}{r} \left( r\frac{\partial v}{\partial r} + v \right) \\
  &&=& \frac{\partial v}{\partial r} + \frac{v}{r}
  \end{gather*}$$

+++

## 證明:

$$\begin{gather*}
\frac{Dv}{Dt} + \frac{uv}{r} + fu &\overset{\text{已知 1}}{=}&  -\frac{1}{\rho r} \frac{\partial P}{\partial \lambda} + \text{RHS}_{\hat{\lambda}}  \\
\frac{Dv}{Dt} + \frac{uv}{r} + fu &\overset{\text{假設 1}}{=}&  -\frac{1}{\rho r} \frac{\partial P}{\partial \lambda} + X  \\
\frac{Dv}{Dt} + \frac{uv}{r} + fu &\overset{\text{假設 2}}{=}&  X  \\
\left( \frac{\partial v}{\partial t} + u\frac{\partial v}{\partial r} + w\frac{\partial v}{\partial z} \right) + \frac{uv}{r} + fu &\overset{\text{已知 2}}{=}&   X\\
\frac{\partial v}{\partial t} + u\left( \frac{\partial v}{\partial r} + \frac{v}{r} + f \right) + w\frac{\partial v}{\partial z} &=& X\\
\frac{\partial v}{\partial t} + u(\zeta + f) + w\frac{\partial v}{\partial z} &\overset{\text{已知 3}}{=}& X
\end{gather*}$$

+++
