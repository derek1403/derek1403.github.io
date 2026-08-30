# Axisymmetric Continuity Equation (軸對稱連續方程式)

+++


## 證明目標:

$$\frac{1}{r}\frac{\partial(\rho ru)}{\partial r}+\frac{\partial(\rho w)}{\partial z}=0$$

+++


## 假設與已知 (Assumptions & Preliminaries)

* **【已知 1】 [三維連續方程式 (質量守恆)](https://derek1403.github.io/PC-NTU/Advanced-Atmospheric-Dynamics/_build/html/lecture/week1/week1.html#continuity-equation)：**
  
  $$\frac{\partial \rho}{\partial t } + \nabla \cdot (\rho \mathbf{u}) = 0$$

* **【已知 2】 [圓柱座標的散度 (Divergence in Cylindrical Coordinates)](https://derek1403.github.io/Theory_Playground/_build/html/01_Derivations/Coordinate_System/Divergence_Operator_in_Cylindrical_Coordinates.html)：** 對於任意向量場 $\mathbf{A} = (A_r, A_\lambda, A_z)$，其散度展開為：
  
  $$\nabla \cdot \mathbf{A} = \frac{1}{r}\frac{\partial (r A_r)}{\partial r} + \frac{1}{r}\frac{\partial A_\lambda}{\partial \lambda} + \frac{\partial A_z}{\partial z}$$

  * 徑向要乘上 $r$ 因為在圓柱座標中一個微小體積單元 (Volume Element) 不是完美的方塊而是一塊「扇形蛋糕」，它的內側面積是 $r d\lambda dz$，外側面積是 $(r+dr) d\lambda dz$，當流體沿著徑向 ($\hat{r}$) 流動即使速度 $u$ 不變，因為「外側的開口面積比內側大」使流出去的總量還是會變多，這就是在微分裡面必須把 $r$ 塞進括號裡跟著一起微分的原因：我們看的是「通量 (Flux = 密度 $\times$ 速度 $\times$ 面積比例 $r$)」的變化。

* **【假設 1】 軸對稱假設 (Axisymmetric Assumption)：**
  
  $$\frac{\partial}{\partial\lambda} = 0$$

  * 系統在切線方向（方位角 $\lambda$）上沒有變化，這是一個成熟熱帶氣旋的標準假設。

* **【假設 2】 準穩定態假設 (Quasi-steady State Assumption)：**
  
  $$\frac{\partial \rho}{\partial t} \approx 0$$

  * 對於一個發展成熟的颱風在我們觀測的短時間區間內，空間中某個固定點的空氣「密度」幾乎不會隨時間有劇烈改變。
  * **尺度分析**：
    * 徑向質量通量散度：$\frac{1}{r}\frac{\partial (\rho r u)}{\partial r} \sim \frac{\rho U}{L} \sim \frac{1 \times 5}{100,000} = \mathbf{5 \times 10^{-5} } [\text{kg} \cdot \text{m}^{-3} \cdot \text{s}^{-1}]$
    * 密度的局部時間變化：假設颱風中心氣壓在 3 小時 ($10^4$ 秒) 內下降了 3 hPa，對應的密度變化大約只有 $\frac{\Delta P}{R_d T} = \Delta \rho \sim 0.003 \text{ kg} \cdot \text{m}^{-3}$。則 $\frac{\partial \rho}{\partial t} \sim \frac{0.003}{10^4} = \mathbf{3 \times 10^{-7} } [\text{kg} \cdot \text{m}^{-3} \cdot \text{s}^{-1}]$
  * 因為 $3 \times 10^{-7} \ll 5 \times 10^{-5}$，密度的局部時間變化項（相比於空間的通量變化）可以忽略不計。
  * *如果套用 Anelastic Approximation，這裡的 $\rho$ 會直接被替換為只隨高度變化的背景密度 $\bar{\rho}(z)$，此時 $\frac{\partial \bar{\rho}}{\partial t}$ 數學上就嚴格等於 $0$*

+++


## 證明:

$$\begin{gather*}
\frac{\partial \rho}{\partial t } + \nabla \cdot (\rho \mathbf{u}) &\overset{\text{已知 1}}{=}& 0 \\
\frac{\partial \rho}{\partial t } + \nabla \cdot (\rho u, \rho v, \rho w) &=& 0 \\
\frac{\partial \rho}{\partial t } + \frac{1}{r}\frac{\partial (r \rho u)}{\partial r} + \frac{1}{r}\frac{\partial (\rho v)}{\partial \lambda} + \frac{\partial (\rho w)}{\partial z} &\overset{\text{已知 2}}{=}& 0 \\
\frac{\partial \rho}{\partial t } + \frac{1}{r}\frac{\partial (\rho r u)}{\partial r} + 0 + \frac{\partial (\rho w)}{\partial z} &\overset{\text{假設 1}}{=}& 0 \\
0 + \frac{1}{r}\frac{\partial (\rho r u)}{\partial r} + \frac{\partial (\rho w)}{\partial z} &\overset{\text{假設 2}}{=}& 0 \\
\frac{1}{r}\frac{\partial (\rho r u)}{\partial r} + \frac{\partial (\rho w)}{\partial z} &=& 0 \\
\end{gather*}$$

+++

## 物理解釋
### 💡 直觀比喻：甜甜圈形狀的房間

想像在颱風的某個高度，我們用紅龍柱圍出一個「甜甜圈形狀（環狀）的隱形房間」。
這個房間有兩扇門：
1. **側門（徑向，$r$ 方向）**：外圈的牆壁和內圈的牆壁，空氣可以橫向穿過。
2. **天窗與地板（垂直向，$z$ 方向）**：房間的屋頂和地板，空氣可以上下穿過。

因為我們假設了「準穩定態（密度不隨時間改變）」，這意味著這個房間裡**不能無限期地塞滿空氣，也不能被抽成真空**。也就是說：**「每秒鐘擠進房間的空氣總質量，必須剛好等於跑出去的空氣總質量。」**

我們來看看方程式的每一項是如何描述這個過程的：

---

### 第一部分： $\frac{1}{r}\frac{\partial(\rho r u)}{\partial r}$ —— 從「側門」擠進來的空氣 (徑向質量散度)

這項描述的是空氣在水平方向（往圓心或背離圓心）流動時，造成的質量累積或流失。

* **為什麼要綁在一起看 $\rho r u$？**
  * $\rho u$ 是「質量通量」，代表每秒鐘穿過每 $1 \text{ m}^2$ 面積的空氣公斤數。
  * 但在圓柱座標裡，越靠近圓心，圓的周長（$2\pi r$）就越小。也就是說，外圈的「側門」很大，內圈的「側門」很小。
  * 所以我們必須把 $\rho u$ 乘上 $r$（代表總面積的比例），$\rho r u$ 才是真正代表「總共有多少質量的空氣穿過這道環形牆壁」。
* **$\frac{\partial}{\partial r}(\rho r u)$ 的物理意義：**
  * 它是「外圈流進來的量」與「內圈流出去的量」的**差值**。
  * 如果 $\frac{\partial(\rho r u)}{\partial r} < 0$（也就是徑向質量通量往外遞減，或者說往內猛烈灌入），這代表外圈進來的車多，內圈出去的車少。這時空氣就會在這個環形房間裡**嚴重塞車（輻合，Convergence）**。

### 第二部分： $\frac{\partial(\rho w)}{\partial z}$ —— 從「天窗」跑出去的空氣 (垂直質量散度)

這項相對單純很多，因為垂直方向的面積不會隨高度改變（不像圓柱的側面積會隨半徑縮水）。

* **$\rho w$**：垂直的質量通量（每秒鐘有多少空氣往上或往下升降）。
* **$\frac{\partial(\rho w)}{\partial z}$ 的物理意義：**
  * 它是「從地板進來的量」與「從天花板出去的量」的**差值**。
  * 如果 $\frac{\partial(\rho w)}{\partial z} > 0$，這代表從天花板跑出去的空氣，比從地板進來的還要多。也就是空氣正在**往上抽離（輻散，Divergence）**。



### 第三部分： 等號 $= 0$ —— 大自然的完美配合 (次環流的誕生)

現在我們把它們加起來看：

$$\underbrace{\frac{1}{r}\frac{\partial(\rho ru)}{\partial r}}_{\text{側門的淨進出}} + \underbrace{\frac{\partial(\rho w)}{\partial z}}_{\text{上下的淨進出}} = 0$$

這條方程式強制規定了一種大自然的「連動機制」。我們以**颱風的底層眼牆 (Eyewall)** 為例來推演：

1. **底層強烈輻合**：在颱風底層，因為摩擦力和其他動力機制的關係，大量的空氣會朝著颱風中心狂飆（$u < 0$ 且向內急遽增加）。這會導致強烈的「徑向質量輻合」，也就是第一項變成一個**極大的負值**。
2. **尋找出口**：房間裡的空氣快被擠爆了，但因為 $=0$ 的鐵律，這些空氣不能憑空消失。既然第一項是負的，**第二項就必須被強迫變成正的**，來抵消它！
3. **被迫向上拔起**：也就是說，$\frac{\partial(\rho w)}{\partial z}$ 必須大於 $0$。在地面，垂直風速是零（$w=0$），所以唯一的解決辦法，就是**在眼牆區域強迫產生極其猛烈的上升氣流（$w > 0$ 且隨高度急遽增加）**，把剛剛從四周擠進來的空氣全部往上抽走！

**總結來說：**
這條方程式的物理靈魂就是大氣中的 **「質量連續性」** ，水平方向的風（徑向風 $u$）和垂直方向的風（上升氣流 $w$）絕對不是各自獨立的， **底層水平方向的「擠壓（輻合）」必然會直接轉換成垂直方向的「噴發（上升氣流）」**，這正是維持熱帶氣旋生命週期中最關鍵的「次環流 (Secondary Circulation)」機制！🎆

+++
