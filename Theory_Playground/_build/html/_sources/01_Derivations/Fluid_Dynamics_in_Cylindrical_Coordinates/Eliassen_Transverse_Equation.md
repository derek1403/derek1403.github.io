# Eliassen Transverse Equation (次環流方程式)

+++


## 證明目標

證明在軸對稱、滿足質量連續的前提下，熱帶氣旋的次環流（徑向與垂直運動）可由以下橢圓型偏微分方程式描述：

$$\frac{\partial}{\partial r}\left[ \frac{A}{r}\frac{\partial \psi}{\partial r} + \frac{B}{r}\frac{\partial \psi}{\partial z} \right] + \frac{\partial}{\partial z}\left[ \frac{B}{r}\frac{\partial \psi}{\partial r} + \frac{C}{r}\frac{\partial \psi}{\partial z} \right] = \frac{\partial J}{\partial r} - \frac{\partial F}{\partial z}$$

+++



## 假設與已知 (Assumptions & Preliminaries)


* **【已知 1】 切線動量方程式 (Tangential Momentum Equation)：**
  
  $$\frac{\partial v}{\partial t} + u(f+\zeta) + w\frac{\partial v}{\partial z} = X$$

* **【已知 2】 梯度風平衡 (Gradient Wind Balance)：**
 
    $$\frac{v^2}{r} + fv = \frac{\partial\phi}{\partial r}$$

    * 徑向的力學平衡關係 
  
* **【已知 3】 流體靜力平衡 (Hydrostatic Balance)：**
  
    $$\frac{\partial\phi}{\partial z} = \frac{g}{\theta_0}\theta'$$

    * 垂直的力學平衡關係
  
* **【已知 4】 熱力學能量方程式 (Thermodynamic Equation)：**
  
  $$\frac{\partial\theta}{\partial t} + u\frac{\partial\theta}{\partial r} + w\frac{\partial\theta}{\partial z} = \frac{\theta}{T}\frac{Q}{c_p}$$

* **【已知 5】 軸對稱連續方程式 (Continuity Equation)：**
  
  $$\frac{1}{r}\frac{\partial(\rho ru)}{\partial r} + \frac{\partial(\rho w)}{\partial z} = 0$$

* **【已知 6】 偏導數可交換性 (Schwarz's Theorem)：**
  對於連續可微的重力位高度場 $\phi(r,z)$，先對空間微分再對時間微分可交換，且對 $r$ 與 $z$ 的偏微分亦可交換：

  $$\frac{\partial}{\partial r}\left[ \frac{\partial^2\phi}{\partial t\partial z} \right] = \frac{\partial}{\partial z}\left[ \frac{\partial^2\phi}{\partial t\partial r} \right]$$

* **【定義 1】 次環流流線函數 (Streamfunction, $\psi$)：**
  
  為了自動滿足【已知 5】的質量連續方程式，我們定義一個Streamfunction $\psi(r,z)$，使得：

  $$\rho u \overset{\text{def}}{=} -\frac{1}{r}\frac{\partial\psi}{\partial z} \quad , \quad \rho w \overset{\text{def}}{=} \frac{1}{r}\frac{\partial\psi}{\partial r}$$
  
  * 驗證：代入【已知 5】會得到 $\frac{1}{r}\frac{\partial}{\partial r}(-\frac{\partial\psi}{\partial z}) + \frac{\partial}{\partial z}(\frac{1}{r}\frac{\partial\psi}{\partial r}) = -\frac{1}{r}\psi_{rz} + \frac{1}{r}\psi_{rz} = 0$，完美守恆
  
* **【定義 2】 穩定度結構參數 ($A, B, C$)：**
  
  $$\rho A \overset{\text{def}}{=} \frac{g}{\theta_0}\frac{\partial\theta}{\partial z}$$
  
  $$\rho B \overset{\text{def}}{=} -\frac{g}{\theta_0}\frac{\partial\theta}{\partial r} = -\left(f+\frac{2v}{r}\right)\frac{\partial v}{\partial z}$$
  
  $$\rho C \overset{\text{def}}{=} \left(f+\frac{2v}{r}\right)(f+\zeta)$$

* **【定義 3】 動力與熱力強迫項 (Forcing Terms, $F, J$)：**
  
  $$F \overset{\text{def}}{=} \left(f+\frac{2v}{r}\right)X$$
  
  $$J \overset{\text{def}}{=} \frac{g}{\theta_0}\frac{\theta}{T}\frac{Q}{c_p}$$


* **【已知 7】 熱力演變 (Thermal Tendency)：** 
  
  $$\begin{gather*}
  \frac{\partial\phi}{\partial z} &\overset{\text{已知 3}}{=}&  \frac{g}{\theta_0}\theta'\\
  \frac{\partial}{\partial t}\left[ \frac{\partial\phi}{\partial z} \right] &=& \frac{\partial}{\partial t}\left[ \frac{g}{\theta_0}\theta' \right] \\
  \frac{\partial^2\phi}{\partial t\partial z} &=& \frac{g}{\theta_0}\frac{\partial\theta'}{\partial t} \\
  \frac{\partial^2\phi}{\partial t\partial z} &=& \frac{g}{\theta_0}\frac{\partial\theta}{\partial t} \\
  \frac{\partial^2\phi}{\partial t\partial z} &\overset{\text{已知 4}}{=}& \frac{g}{\theta_0} \left( -u\frac{\partial\theta}{\partial r} - w\frac{\partial\theta}{\partial z} + \frac{\theta}{T}\frac{Q}{c_p} \right) \\
  \frac{\partial^2\phi}{\partial t\partial z} &=& -u\left( \frac{g}{\theta_0}\frac{\partial\theta}{\partial r} \right) - w\left( \frac{g}{\theta_0}\frac{\partial\theta}{\partial z} \right) + \left( \frac{g}{\theta_0}\frac{\theta}{T}\frac{Q}{c_p} \right) \\
  \frac{\partial^2\phi}{\partial t\partial z} &\overset{\text{定義 2,3}}{=}& -u(-\rho B) - w(\rho A) + J \\
  \frac{\partial^2\phi}{\partial t\partial z} &=& u\rho B - w\rho A + J 
  \end{gather*}$$


* **【已知 8】 動力演變 (Momentum Tendency)：** 
  
  $$\begin{gather*}
  \frac{\partial\phi}{\partial r}  &\overset{\text{已知 2}}{=}&  \frac{v^2}{r} + fv  \\
  \frac{\partial}{\partial t}\left[ \frac{\partial\phi}{\partial r} \right] &=& \frac{\partial}{\partial t}\left[ \frac{v^2}{r} + fv \right] \\
  \frac{\partial^2\phi}{\partial t\partial r} &=& \left( \frac{2v}{r} + f \right)\frac{\partial v}{\partial t} \\
  \frac{\partial^2\phi}{\partial t\partial r} &\overset{\text{已知 1}}{=}& \left( f + \frac{2v}{r} \right) \left[ -u(f+\zeta) - w\frac{\partial v}{\partial z} + X \right] \\
  \frac{\partial^2\phi}{\partial t\partial r} &=& -u\left( f + \frac{2v}{r} \right)(f+\zeta) - w\left( f + \frac{2v}{r} \right)\frac{\partial v}{\partial z} + \left( f + \frac{2v}{r} \right)X \\
  \frac{\partial^2\phi}{\partial t\partial r} &\overset{\text{定義 2,3}}{=}& -u(\rho C) - w(-\rho B) + F \\
  \frac{\partial^2\phi}{\partial t\partial r} &=& -u\rho C + w\rho B + F 
  \end{gather*}$$

* **【定義 4】 notation of Eliassen Transverse Equation in Cylindrical Corordnate ：** 

  $$\mathcal{L_{\text{cyl}}}[\cdot]=\frac{\partial}{\partial r}\left[ \frac{A}{r}\frac{\partial r[\cdot]}{\partial r}+\frac{B}{r}\frac{\partial[\cdot]}{\partial z} \right]+\frac{\partial}{\partial z}\left[ \frac{B}{r}\frac{\partial r[\cdot]}{\partial r}+\frac{C}{r}\frac{\partial[\cdot]}{\partial z}\right]$$

+++



## 證明

$$\begin{gather*}
\frac{\partial}{\partial r}\left[ \frac{\partial^2\phi}{\partial t\partial z} \right] &\overset{\text{已知 6}}{=}& \frac{\partial}{\partial z}\left[ \frac{\partial^2\phi}{\partial t\partial r} \right] \\
\frac{\partial}{\partial r}\left[ u\rho B - w\rho A + J \right] &\overset{\text{已知 7,8}}{=}& \frac{\partial}{\partial z}\left[ -u\rho C + w\rho B + F \right] \\
\frac{\partial}{\partial r}\left[ u\rho B - w\rho A \right] + \frac{\partial J}{\partial r} &=& \frac{\partial}{\partial z}\left[ -u\rho C + w\rho B \right] + \frac{\partial F}{\partial z} \\
\frac{\partial}{\partial r}\left[ u\rho B - w\rho A \right] - \frac{\partial}{\partial z}\left[ -u\rho C + w\rho B \right] &=& \frac{\partial F}{\partial z} - \frac{\partial J}{\partial r} \\
\frac{\partial}{\partial r}\left[ u\rho B - w\rho A \right] + \frac{\partial}{\partial z}\left[ u\rho C - w\rho B \right] &=& \frac{\partial F}{\partial z} - \frac{\partial J}{\partial r} \\
\frac{\partial}{\partial r}\left[ -\frac{1}{r}\frac{\partial\psi}{\partial z} B -\frac{1}{r}\frac{\partial\psi}{\partial r} A \right] + \frac{\partial}{\partial z}\left[ -\frac{1}{r}\frac{\partial\psi}{\partial z} C - \frac{1}{r}\frac{\partial\psi}{\partial r} B \right] &\overset{\text{定義 1}}{=}&  \frac{\partial F}{\partial z} - \frac{\partial J}{\partial r} \\
\frac{\partial}{\partial r}\left[ -\left( \frac{A}{r}\frac{\partial\psi}{\partial r} + \frac{B}{r}\frac{\partial\psi}{\partial z} \right) \right] + \frac{\partial}{\partial z}\left[ -\left( \frac{B}{r}\frac{\partial\psi}{\partial r} + \frac{C}{r}\frac{\partial\psi}{\partial z} \right) \right] &=& \frac{\partial F}{\partial z} - \frac{\partial J}{\partial r} \\
\frac{\partial}{\partial r}\left[ \frac{A}{r}\frac{\partial\psi}{\partial r} + \frac{B}{r}\frac{\partial\psi}{\partial z} \right] + \frac{\partial}{\partial z}\left[ \frac{B}{r}\frac{\partial\psi}{\partial r} + \frac{C}{r}\frac{\partial\psi}{\partial z} \right] &=& \frac{\partial J}{\partial r} - \frac{\partial F}{\partial z}\\
\mathcal{L_{\text{cyl}}}[\psi] &\overset{\text{定義 4}}{=}& \frac{\partial J}{\partial r} - \frac{\partial F}{\partial z}
\end{gather*}$$





+++


## 💡 直觀比喻：系統的「彈簧床」與「重量」



這個方程式的結構非常具有物理直覺，我們可以把它看成是一個**「彈簧床受力變形」**的模型：

1. **等號左邊 $\mathcal{L_{\text{cyl}}}[\psi]$ (大氣的彈簧床)：**
   算子內部的 $A, B, C$ 矩陣就是我們前面討論過的「穩定度結構」，它代表這張彈簧床的剛性與傾斜程度。當 $AC - B^2 > 0$ 時，這是一張緊繃且完好的彈簧床（橢圓型方程式）。
2. **等號右邊 $\frac{\partial J}{\partial r} - \frac{\partial F}{\partial z}$ (放上去的重量)：**
   這代表 **「強迫力的空間不均勻性（梯度）」** ，單純的加熱 $J$ 或摩擦 $F$ 不會產生次環流，必須要有「差異」才會！例如眼牆加熱極強，外圍加熱弱（$\frac{\partial J}{\partial r} < 0$），這就像在彈簧床的中心放了一顆重重的保齡球。
3. **流線函數 $\psi$ (變形的結果)：**
   當右邊的重量壓在左邊的彈簧床上時，彈簧床被迫凹陷（$\psi$ 產生非零的解），大氣為了解除這個不平衡狀態，就會沿著阻力最小的路徑，擠壓出我們看到的次環流（徑向輻合 $u$ 與強烈垂直上升 $w$）！

+++
