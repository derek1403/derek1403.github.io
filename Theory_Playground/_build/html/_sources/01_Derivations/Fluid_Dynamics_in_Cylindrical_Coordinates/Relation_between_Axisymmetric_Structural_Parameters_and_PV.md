# 圓柱座標次環流結構參數與位渦關係 (Relation between Axisymmetric Structural Parameters and Ertel PV)

+++


## 證明目標:

證明在圓柱座標系下，結構參數的行列式等同於大氣慣性參數與 Ertel PV 的乘積：

$$(\rho A)(\rho C) - (\rho B)^2 = \left(f+\frac{2v}{r}\right)  PV_b$$



+++


## 假設與已知 (Assumptions & Preliminaries)

* **【假設 1】 軸對稱假設 (Axisymmetric Assumption)：**
  
  $$\frac{\partial}{\partial\lambda} = 0$$

  * 系統在切線方向（方位角 $\lambda$）上沒有變化，這是一個成熟熱帶氣旋的標準假設。
  

* **【已知 1】 [次環流結構參數](https://derek1403.github.io/Theory_Playground/_build/html/01_Derivations/Fluid_Dynamics_in_Cylindrical_Coordinates/Eliassen_Secondary_Circulation_Coefficients.html)：**
  
  * 垂直穩定度 (Static Stability) $\rho A \overset{\text{def}}{=} \frac{g}{\theta_0}\frac{\partial\theta}{\partial z}$ 
  * 熱力風 (Thermal wind)： $\rho B_{\text{thermal}} \overset{\text{def}}{=} -\frac{g}{\theta_0}\frac{\partial\theta}{\partial r}$
  * 斜壓性(Baroclinicity)：$\rho B_{\text{momentum}} \overset{\text{def}}{=} -\left(f+\frac{2v}{r}\right)\frac{\partial v}{\partial z}$
  * 慣性穩定度 (Inertial Stability)：$\rho C \overset{\text{def}}{=} \left(f+\frac{2v}{r}\right)(f+\zeta)$
  * 熱力與動力強迫項 (Forcing Terms)：
    * $J \overset{\text{def}}{=} \frac{g}{\theta_0}\frac{\theta}{T}\frac{Q}{c_p}$
    * $F \overset{\text{def}}{=} \left(f+\frac{2v}{r}\right)X$




* **【定義 1】 浮力 (Buoyancy) 與位溫的簡化代換：**
    為了公式推導的簡潔，我們將含有 $\frac{g}{\theta_0}$ 的項統一定義為浮力 $b$

    $$b \overset{\text{def}}{=} \frac{g}{\theta_0}\theta$$
    
    * $\rho A = \frac{\partial b}{\partial z}$ 
    * $\rho B_{\text{thermal}} = -\frac{\partial b}{\partial r}$ 
    * $\rho B_{\text{momentum}} = -\left(f+\frac{2v}{r}\right)\frac{\partial v}{\partial z}$
    * $\rho C = \left(f+\frac{2v}{r}\right)(f+\zeta)$ 

* **【已知 2】 [熱力風平衡的 B 參數等價性](https://derek1403.github.io/Theory_Playground/_build/html/01_Derivations/Fluid_Dynamics_in_Cylindrical_Coordinates/Eliassen_Secondary_Circulation_Coefficients.html)：**
  
    
    $$\begin{gather*}
    &\rho B_{\text{thermal}} &=& \rho B_{\text{momentum}} \\
    \implies& -\frac{\partial b}{\partial r} &=& -\left(f+\frac{2v}{r}\right)\frac{\partial v}{\partial z}
    \end{gather*}$$
    
    * 熱力型態的 $B$ 必須等於動力型態的 $B$

* **【已知 3】 軸對稱的[浮力位渦 (Buoyancy Potential Vorticity)](https://derek1403.github.io/Theory_Playground/_build/html/01_Derivations/Fluid_Dynamics_Variable_Coordinate_Physics/PV_Representations_and_Mappings/Relation_Between_PV_and_PVb.html)：**
  
    * 位渦 $PV_b$ 定義為絕對渦度向量 $\boldsymbol{\eta}_a$ 與浮力梯度向量 $\nabla b$ 的內積
    * **【已知 3-假設a】只有切線主環流計算渦度**
      *  $\vec{V} = v\hat{\lambda}$
    * **【已知 3-假設b】考慮科氏力**
      *  $f\hat{k}$  
    * **浮力梯度向量**： $\nabla b \overset{\text{假設 1}}{=} \frac{\partial b}{\partial r}\hat{r} + \frac{\partial b}{\partial z}\hat{k}$
    * **絕對渦度向量**：

    $$\begin{gather*}
    PV_b &\overset{\text{def}}{=}& \boldsymbol{\eta}_a &\cdot& \nabla b \\
    PV_b &\overset{\text{假設 1}}{=}& \boldsymbol{\eta}_a &\cdot& \left( \frac{\partial b}{\partial r}\hat{r} + \frac{\partial b}{\partial z}\hat{k} \right)\\
    PV_b &\overset{\text{已知 3-假設a,b}}{=}& \left( \nabla \times (v\hat{\lambda}) + f\hat{k} \right) &\cdot& \left( \frac{\partial b}{\partial r}\hat{r} + \frac{\partial b}{\partial z}\hat{k} \right)\\
    PV_b &=& \left( -\frac{\partial v}{\partial z}\hat{r} + \left(f + \frac{\partial[rv]}{r\partial r}\right)\hat{k} \right) &\cdot& \left( \frac{\partial b}{\partial r}\hat{r} + \frac{\partial b}{\partial z}\hat{k} \right)\\
    PV_b &=& \left( -\frac{\partial v}{\partial z}\hat{r} + (f+\zeta)\hat{k} \right) &\cdot& \left( \frac{\partial b}{\partial r}\hat{r} + \frac{\partial b}{\partial z}\hat{k} \right)\\
    PV_b &=& -\frac{\partial v}{\partial z}\frac{\partial b}{\partial r} &+& (f+\zeta)\frac{\partial b}{\partial z}
    \end{gather*}$$


+++




## 證明:

在計算 $(\rho B)^2$ **把熱力版與動力版的 $\rho B$ 乘在一起** ，提取共同的慣性係數 $\left(f+\frac{2v}{r}\right)$

$$\begin{gather*}
(\rho A)(\rho C) - (\rho B)^2 &\overset{\text{已知 2}}{=}& (\rho A)(\rho C) - (\rho B_{\text{thermal}})(\rho B_{\text{momentum}}) \\
&\overset{\text{已知 1}}{=}& \left( \frac{\partial b}{\partial z} \right) \left( \left(f+\frac{2v}{r}\right)(f+\zeta) \right) - \left( -\frac{\partial b}{\partial r} \right) \left( -\left(f+\frac{2v}{r}\right)\frac{\partial v}{\partial z} \right) \\
&=& \left(f+\frac{2v}{r}\right)(f+\zeta)\frac{\partial b}{\partial z} - \left(f+\frac{2v}{r}\right)\frac{\partial b}{\partial r}\frac{\partial v}{\partial z} \\
&=& \left(f+\frac{2v}{r}\right) \left( (f+\zeta)\frac{\partial b}{\partial z} - \frac{\partial v}{\partial z}\frac{\partial b}{\partial r} \right)\\
&\overset{\text{已知 3}}{=}& \left(f+\frac{2v}{r}\right)  PV_b \\
\end{gather*}$$



+++


---

## 物理解釋

如果我們直接在圓柱座標系推導，物理圖象會比直角座標更加豐富，因為我們多出了一個係數 $\left(f+\frac{2v}{r}\right)$，我們稱之為 **「絕對慣性參數（Absolute Inertial Parameter）」**

1. **神聖的守恆性：** 無論是在直角座標還是圓柱座標，系統的「對稱穩定度（由 $AC-B^2$ 決定）」都嚴格正比於「位渦（PV）」。
2. **圓柱座標的獨特效應：** 在強烈颱風中，切線風速 $v$ 很大，且曲率半徑 $r$ 很小，這導致離心力項 $\frac{2v}{r}$ 遠大於科氏力 $f$。因此，颱風眼牆的「絕對慣性參數」非常巨大。
3. **穩定度的倍增：** 這個公式告訴我們，在同樣的位渦 $PV_b$ 結構下，**颱風（圓柱系統）會比鋒面（直角系統）擁有大得多的抵抗對稱不穩定的能力**，因為它被強大的離心曲率 $\left(\frac{2v}{r}\right)$ 給放大了。這就是為什麼颱風眼牆可以維持如此直挺挺的極端結構，而不容易崩潰的原因！

+++
