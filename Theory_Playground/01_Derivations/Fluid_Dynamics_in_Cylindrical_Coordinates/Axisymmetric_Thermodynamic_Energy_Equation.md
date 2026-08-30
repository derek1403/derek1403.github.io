# Axisymmetric Thermodynamic Energy Equation (軸對稱熱力學能量方程式)

+++


## 證明目標:

$$\frac{\partial\theta}{\partial t}+u\frac{\partial\theta}{\partial r}+w\frac{\partial\theta}{\partial z}=\frac{\theta}{T}\frac{Q}{c_{p}}$$


+++


## 假設與已知 (Assumptions & Preliminaries)

* **【已知 1】 熱力學第一定律 (First Law of Thermodynamics)：**
* 
  空氣塊吸收的熱量，會轉化為內能的增加（溫度上升）與對外作功（體積膨脹），寫成單位質量的隨時間變化率：

  $$Q = c_p \frac{DT}{Dt} - \alpha \frac{DP}{Dt}$$

  * $Q$: 非絕熱加熱率 (Diabatic heating rate)，例如輻射加熱、潛熱釋放 $[\text{J} \cdot \text{kg}^{-1} \cdot \text{s}^{-1}]$
  * $c_p$: 乾空氣定壓比熱 $c_p \sim 1004 \text{J} \cdot \text{kg}^{-1} \cdot \text{K}^{-1}$
  * $\alpha$: 比容 (Specific volume, 即密度的倒數 $\alpha = \frac{1}{\rho}$) $[\text{m}^3 \cdot \text{kg}^{-1}]$
  * 

* **【已知 2】 理想氣體方程式 (Ideal Gas Law)：**
  
  $$P = \rho R_d T \implies \frac{1}{\rho} = \alpha = \frac{R_d T}{P}$$

* **【已知 3】 位溫的定義 (Definition of Potential Temperature)：**
  
  $$\theta \overset{\text{def}}{=} T \left(\frac{P_s}{P}\right)^{R_d/c_p}$$

  * 乾空氣的氣體常數：$R_d \approx 287 \text{J}\cdot \text{kg}^{-1}\cdot \text{K}^{-1} $
  * 乾空氣的定壓比熱：$C_p \approx 1004 \text{J}\cdot \text{kg}^{-1}\cdot \text{K}^{-1}$
  * $P_s$: 參考氣壓 (通常為 $1000 \text{ hPa}$)，是一個**常數**。

* **【已知 4】 全導數 (Material Derivative) 的圓柱座標展開：**
  
  $$\frac{D\theta}{Dt} = \frac{\partial\theta}{\partial t} + u\frac{\partial\theta}{\partial r} + \frac{v}{r}\frac{\partial\theta}{\partial\lambda} + w\frac{\partial\theta}{\partial z}$$

* **【假設 1】 軸對稱假設 (Axisymmetric Assumption)：**
  
  $$\frac{\partial}{\partial\lambda} = 0$$

+++


## 證明:

這條證明的核心思路是：**先對位溫取自然對數，然後對時間求全導數 $\frac{D}{Dt}$，最後把熱力學第一定律塞進去，對整個方程式取全導數 $\frac{D}{Dt}$ ，等號左右兩邊同時乘上 $c_p T$ ，把全導數依照座標系展開，並套用軸對稱假設**

$$\begin{gather*}
\theta &\overset{\text{已知 3}}{=}& T \left(\frac{P_s}{P}\right)^{R_d/c_p} \\
\ln \theta &=& \ln \left( T \left(\frac{P_s}{P}\right)^{R_d/c_p} \right) \\
\ln \theta &=& \ln T + \frac{R_d}{c_p}\ln P_s - \frac{R_d}{c_p}\ln P \\
\frac{D}{Dt} \left[ \ln \theta  \right] &=& \frac{D}{Dt} \left[ \ln T  \right] + \frac{D}{Dt} \left[  \frac{R_d}{c_p}\ln P_s  \right] - \frac{D}{Dt} \left[ \frac{R_d}{c_p}\ln P \right]\\
\frac{1}{\theta}\frac{D\theta}{Dt} &=& \frac{1}{T}\frac{DT}{Dt} + \frac{R_d}{c_p}0 - \frac{R_d}{c_p}\frac{1}{P}\frac{DP}{Dt} \\
\frac{c_p T}{\theta}\frac{D\theta}{Dt} &=& c_p\frac{DT}{Dt} - \frac{R_d T}{P}\frac{DP}{Dt} \\
\frac{c_p T}{\theta}\frac{D\theta}{Dt} &\overset{\text{已知 2}}{=}& c_p\frac{DT}{Dt} - \alpha\frac{DP}{Dt} \\
\frac{c_p T}{\theta}\frac{D\theta}{Dt} &\overset{\text{已知 1}}{=}& Q \\
\frac{D\theta}{Dt} &=& \frac{\theta}{T}\frac{Q}{c_p} \\
\frac{\partial\theta}{\partial t} + u\frac{\partial\theta}{\partial r} + \frac{v}{r}\frac{\partial\theta}{\partial\lambda} + w\frac{\partial\theta}{\partial z} &\overset{\text{已知 4}}{=}& \frac{\theta}{T}\frac{Q}{c_p} \\
\frac{\partial\theta}{\partial t} + u\frac{\partial\theta}{\partial r} + \frac{v}{r}0 + w\frac{\partial\theta}{\partial z} &\overset{\text{假設 1}}{=}& \frac{\theta}{T}\frac{Q}{c_p} \\
\frac{\partial\theta}{\partial t} + u\frac{\partial\theta}{\partial r} + w\frac{\partial\theta}{\partial z} &=& \frac{\theta}{T}\frac{Q}{c_p}
\end{gather*}$$


+++




### 💡 直觀比喻：財富與購買力

這個方程式的物理意義非常漂亮，我們把它拆成兩邊來看：

**1. 等號右邊：真正的「財富增加」($\frac{\theta}{T}\frac{Q}{c_p}$)**
你可以把空氣塊的「絕對溫度 $T$」想像成「帳戶裡的存款數字」，而「氣壓 $P$」是「當地的物價」。
如果今天你只是因為物價下跌而覺得自己變有錢了（絕熱膨脹），你的「實質購買力（位溫 $\theta$）」其實是**沒有改變的**。
要讓你的實質購買力 $\theta$ 真正增加，唯一的辦法就是**有外部資金匯入你的帳戶（非絕熱加熱 $Q > 0$）**！例如：水氣凝結釋放潛熱（颱風增強的火力來源），或是太陽輻射加熱。如果 $Q=0$（絕熱過程），等號右邊就是 0，你的購買力 $\theta$ 就永遠守恆。

**2. 等號左邊：追蹤你某銀行的財富變化 ($\frac{\partial\theta}{\partial t} + u\frac{\partial\theta}{\partial r} + w\frac{\partial\theta}{\partial z}$)**
這三項代表我們站在一個固定的觀測站，看著周遭空氣的位溫變化：
* $\frac{\partial\theta}{\partial t}$：本地位溫隨時間的實際變化。 華南的錢💰
* $u\frac{\partial\theta}{\partial r} + w\frac{\partial\theta}{\partial z}$：**平流項 (Advection)**。意思是，即使沒有外部加熱 ($Q=0$)，如果遠方有一團「原本就很富有（高位溫）」的空氣，被水平風 $u$ 或垂直風 $w$ 吹到你的觀測站，你這個地方的平均位溫還是會上升。 **從郵局匯錢💸到華南**

**總結來說：** 這個方程式告訴我們，一個固定地點的位溫會改變，只有兩個原因：一是**外面有不同溫度的空氣被風吹過來了（平流）**，二是**空氣本身正在被加熱或冷卻（非絕熱過程 $Q$）**！

+++
