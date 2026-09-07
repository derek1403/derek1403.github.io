# Separation into the Horizontal Structure System (垂直結構的分離與水平結構方程組)

+++

## 證明目標:

把 [線性化原始方程組](Log_Pressure_Linearized_Primitive_Equations.md) 的**三維**問題，
用 [垂直結構函數](Vertical_Structure_Equation_in_Log_Pressure.md) 壓成一組**二維**的水平結構方程組。

* (a) 分離變數的形式**不是自由選的** —— $u, v, \phi$ 掛在 $Z(z)$ 上，而 $T, w, Q$ 必須掛在 $Z'(z)$ 上：

$$\begin{pmatrix} u \cr v \cr \phi \end{pmatrix}(x,y,z,t) = \begin{pmatrix} \hat{u} \cr \hat{v} \cr \hat{\phi} \end{pmatrix}(x,y,t)\,Z(z),
\qquad
\begin{pmatrix} T \cr w \cr Q \end{pmatrix}(x,y,z,t) = \begin{pmatrix} \hat{T} \cr \hat{w} \cr \hat{Q} \end{pmatrix}(x,y,t)\,Z'(z)$$

* (b) 代回原方程組後，垂直依賴整個約掉，只剩五條**二維**方程式：

$$\frac{\partial \hat{u}}{\partial t} - \beta y\,\hat{v} + \frac{\partial \hat{\phi}}{\partial x} = -\alpha\hat{u}$$

$$\frac{\partial \hat{v}}{\partial t} + \beta y\,\hat{u} + \frac{\partial \hat{\phi}}{\partial y} = -\alpha\hat{v}$$

$$\hat{\phi} = R\hat{T}$$

$$\frac{\partial \hat{u}}{\partial x} + \frac{\partial \hat{v}}{\partial y} - \left(\frac{\pi^{2}}{z_T^{2}} + \frac{1}{4}\right)\hat{w} = 0$$

$$\frac{\partial \hat{T}}{\partial t} + \Gamma\hat{w} = -\alpha\hat{T} + \frac{\hat{Q}}{c_p}$$

其中

* $u,\ v$ : 擾動緯向、經向風速 (Perturbation zonal and meridional velocities) $[\text{m}\cdot\text{s}^{-1}]$
* $\phi$ : 擾動位勢 (Perturbation geopotential) $[\text{m}^{2}\cdot\text{s}^{-2}]$
* $T$ : 擾動溫度 (Perturbation temperature) $[\text{K}]$
* $w$ : 擾動對數氣壓垂直速度 (Perturbation log-pressure vertical velocity) $[\text{s}^{-1}]$
* $Q$ : 非絕熱加熱率 (Diabatic heating rate) $[\text{J}\cdot\text{kg}^{-1}\cdot\text{s}^{-1}]$
* $\hat{u},\ \hat{v}$ : 緯向、經向風的水平結構函數 (Horizontal structure functions of the velocities) $[\text{m}\cdot\text{s}^{-1}]$
* $\hat{\phi}$ : 擾動位勢的水平結構函數 (Horizontal structure function of the perturbation geopotential) $[\text{m}^{2}\cdot\text{s}^{-2}]$
* $\hat{T}$ : 擾動溫度的水平結構函數 (Horizontal structure function of the perturbation temperature) $[\text{K}]$
* $\hat{w}$ : 擾動對數氣壓垂直速度的水平結構函數 (Horizontal structure function of the perturbation log-pressure vertical velocity) $[\text{s}^{-1}]$
* $\hat{Q}$ : 加熱率的水平結構函數 (Horizontal structure function of the heating rate) $[\text{J}\cdot\text{kg}^{-1}\cdot\text{s}^{-1}]$
* $Z(z)$ : 垂直結構函數 (Vertical structure function) $[\text{無單位}]$
* $Z'$ : 垂直結構函數 $Z$ 對 $z$ 的一階微分 (First derivative of the vertical structure function with respect to $z$) $[\text{無單位}]$，$Z' = \dfrac{dZ}{dz}$
* $x,\ y$ : 緯向、經向座標 (Zonal and meridional coordinates) $[\text{m}]$
* $z$ : 對數氣壓垂直座標 (Log-pressure vertical coordinate) $[\text{無單位}]$
* $t$ : 時間 (Time) $[\text{s}]$
* $\alpha$ : 常數阻尼率 (Constant damping rate) $[\text{s}^{-1}]$
* $\beta$ : 赤道 $\beta$ 參數 (Equatorial beta parameter) $[\text{m}^{-1}\cdot\text{s}^{-1}]$
* $\Gamma$ : 靜力穩定度 (Static stability) $[\text{K}]$
* $R$ : 乾空氣氣體常數 (Gas constant for dry air) $[\text{J}\cdot\text{kg}^{-1}\cdot\text{K}^{-1}]$
* $c_p$ : 定壓比熱 (Specific heat at constant pressure) $[\text{J}\cdot\text{kg}^{-1}\cdot\text{K}^{-1}]$
* $z_T$ : 對流層頂的對數氣壓高度 (Log-pressure height of the tropopause) $[\text{無單位}]$，$z_T \approx 1.619$
* 註：(a)(b) 就是 [Schubert & Masarik (2006)](../../06_References/Tropical_wave_dynamics/Schubert2006-Potential_vorticity_aspects_of_the_MJO/Potential_vorticity_aspects_of_the_MJO.ipynb) 的 $(3.4)$ 與 $(3.5)$。
* 註：本篇的重點**不是**「代進去約掉」這件苦力，而是**證明 (a) 的配對是被逼出來的**：靜力方程式逼出 $T \propto Z'$，連續方程式與垂直結構方程式一起逼出 $w \propto Z'$。若隨手把 $T$ 也掛在 $Z$ 上，方程組**不會閉合**。
* 註：$(3.5)$ 在形式上就是一組**淺水方程式**。$\hat{\phi}$ 扮演位勢高度、$\left(\dfrac{\pi^{2}}{z_T^{2}} + \dfrac{1}{4}\right)^{-1}$ 扮演等效深度的角色，這一點在 [傅立葉轉換至淺水系統](Fourier_Transform_to_Shallow_Water_System.md) 會寫成標準形式。

+++

## 假設與已知 (Assumptions & Preliminaries)

* **【已知 1】 [對數氣壓座標下的線性化原始方程組 (Log-pressure linearized primitive equations)](https://derek1403.github.io/Theory_Playground/_build/html/01_Derivations/Equatorial_Beta_Plane_Dynamics/Log_Pressure_Linearized_Primitive_Equations.html#assumptions-preliminaries)：** 對數氣壓座標下、繞靜止基本態線性化後的五條方程式：兩條水平動量方程、靜力方程、連續方程式與熱力學方程式，未知場為 $u,\ v,\ \phi,\ T,\ w$。整篇的工作就是把這五條的垂直依賴分離出去。（已於本庫 Log-Pressure Linearized Primitive Equations 完整證明，此處直接引用。）

  * (a) 緯向動量方程式：

    $$\frac{\partial u}{\partial t} - \beta y\,v + \frac{\partial \phi}{\partial x} = -\alpha u$$

  * (b) 經向動量方程式：

    $$\frac{\partial v}{\partial t} + \beta y\,u + \frac{\partial \phi}{\partial y} = -\alpha v$$

  * (c) 靜力方程式：

    $$\frac{\partial \phi}{\partial z} = RT$$

  * (d) 連續方程式：

    $$\frac{\partial u}{\partial x} + \frac{\partial v}{\partial y} + \frac{\partial w}{\partial z} - w = 0$$

  * (e) 熱力學方程式：

    $$\frac{\partial T}{\partial t} + \Gamma w = -\alpha T + \frac{Q}{c_p}$$

  * $u,\ v$ : 擾動緯向、經向風速 (Perturbation zonal and meridional velocities) $[\text{m}\cdot\text{s}^{-1}]$
  * $w$ : 擾動對數氣壓垂直速度 (Perturbation log-pressure vertical velocity) $[\text{s}^{-1}]$
  * $\phi$ : 擾動位勢 (Perturbation geopotential) $[\text{m}^{2}\cdot\text{s}^{-2}]$
  * $T$ : 擾動溫度 (Perturbation temperature) $[\text{K}]$
  * $Q$ : 非絕熱加熱率 (Diabatic heating rate) $[\text{J}\cdot\text{kg}^{-1}\cdot\text{s}^{-1}]$
  * $\beta$ : 赤道 $\beta$ 參數 (Equatorial beta parameter) $[\text{m}^{-1}\cdot\text{s}^{-1}]$
  * $\alpha$ : 常數阻尼率 (Constant damping rate) $[\text{s}^{-1}]$
  * $\Gamma$ : 靜力穩定度 (Static stability) $[\text{K}]$
  * $R$ : 乾空氣氣體常數 (Gas constant for dry air) $[\text{J}\cdot\text{kg}^{-1}\cdot\text{K}^{-1}]$
  * $c_p$ : 定壓比熱 (Specific heat at constant pressure) $[\text{J}\cdot\text{kg}^{-1}\cdot\text{K}^{-1}]$
  * $t$ : 時間 (Time) $[\text{s}]$
  * $y$ : 經向座標，以赤道為原點 (Meridional coordinate) $[\text{m}]$
  * $x,\ y$ : 緯向、經向座標 (Zonal and meridional coordinates) $[\text{m}]$
  * $z$ : 對數氣壓垂直座標 (Log-pressure vertical coordinate) $[\text{無單位}]$

* **【已知 2】 [垂直結構方程式 (Vertical structure equation)](https://derek1403.github.io/Theory_Playground/_build/html/01_Derivations/Equatorial_Beta_Plane_Dynamics/Vertical_Structure_Equation_in_Log_Pressure.html#a-proof-eigenvalue-of-the-first-vertical-internal-mode)：** 垂直結構函數所滿足的本徵方程：算符 $\left(\frac{d}{dz} - 1\right)\frac{d}{dz}$ 作用在 $Z$ 上會還原成 $Z$ 本身乘一個常數，該常數即分離常數 $\lambda$，並由剛蓋條件量子化成 $\frac{\pi^{2}}{z_T^{2}} + \frac{1}{4}$。（已於本庫 Vertical Structure Equation in Log-Pressure【證明 (a)】完整證明，此處直接引用。）

  $$\left(\frac{d}{dz} - 1\right)\frac{dZ}{dz} = -\left(\frac{\pi^{2}}{z_T^{2}} + \frac{1}{4}\right)Z$$

  * $Z(z)$ : 垂直結構函數 (Vertical structure function) $[\text{無單位}]$
  * $z$ : 對數氣壓垂直座標 (Log-pressure vertical coordinate) $[\text{無單位}]$
  * $z_T$ : 對流層頂的對數氣壓高度 (Log-pressure height of the tropopause) $[\text{無單位}]$，$z_T \approx 1.619$

* **【定義 1】 第一內模態的分離常數 (Separation constant of the first internal mode)：** 【已知 2】右端的常數，之後會反覆出現

  $$\lambda \overset{\text{def}}{=} \frac{\pi^{2}}{z_T^{2}} + \frac{1}{4}$$

  * $\lambda$ : 第一內模態的分離常數 (Separation constant) $[\text{無單位}]$，$\lambda \approx 4.014$
  * $z$ : 對數氣壓垂直座標 (Log-pressure vertical coordinate) $[\text{無單位}]$
  * $z_T$ : 對流層頂的對數氣壓高度 (Log-pressure height of the tropopause) $[\text{無單位}]$，$z_T \approx 1.619$

* **【定義 2】 水平結構函數 (Horizontal structure functions)：** 把三維場的垂直依賴抽出來，剩下的二維部分加帽子

  * (a) 掛在 $Z$ 上的三個場：

    $$\begin{pmatrix} u(x,y,z,t) \cr v(x,y,z,t) \cr \phi(x,y,z,t) \end{pmatrix} \overset{\text{def}}{=} \begin{pmatrix} \hat{u}(x,y,t) \cr \hat{v}(x,y,t) \cr \hat{\phi}(x,y,t) \end{pmatrix} Z(z)$$

  * (b) 掛在 $Z'$ 上的三個場：

    $$\begin{pmatrix} T(x,y,z,t) \cr w(x,y,z,t) \cr Q(x,y,z,t) \end{pmatrix} \overset{\text{def}}{=} \begin{pmatrix} \hat{T}(x,y,t) \cr \hat{w}(x,y,t) \cr \hat{Q}(x,y,t) \end{pmatrix} Z'(z)$$

  * $\hat{u},\ \hat{v}$ : 緯向、經向風的水平結構函數 (Horizontal structure functions of the velocities) $[\text{m}\cdot\text{s}^{-1}]$
  * $\hat{\phi}$ : 擾動位勢的水平結構函數 (Horizontal structure function of the perturbation geopotential) $[\text{m}^{2}\cdot\text{s}^{-2}]$
  * $\hat{T}$ : 擾動溫度的水平結構函數 (Horizontal structure function of the perturbation temperature) $[\text{K}]$
  * $\hat{w}$ : 擾動對數氣壓垂直速度的水平結構函數 (Horizontal structure function of the perturbation log-pressure vertical velocity) $[\text{s}^{-1}]$
  * $\hat{Q}$ : 加熱率的水平結構函數 (Horizontal structure function of the heating rate) $[\text{J}\cdot\text{kg}^{-1}\cdot\text{s}^{-1}]$
  * $u,\ v$ : 擾動緯向、經向風速 (Perturbation zonal and meridional velocities) $[\text{m}\cdot\text{s}^{-1}]$
  * $x,\ y$ : 緯向、經向座標 (Zonal and meridional coordinates) $[\text{m}]$
  * $y$ : 經向座標，以赤道為原點 (Meridional coordinate) $[\text{m}]$
  * $z$ : 對數氣壓垂直座標 (Log-pressure vertical coordinate) $[\text{無單位}]$
  * $t$ : 時間 (Time) $[\text{s}]$
  * $\phi$ : 擾動位勢 (Perturbation geopotential) $[\text{m}^{2}\cdot\text{s}^{-2}]$
  * $Z(z)$ : 垂直結構函數 (Vertical structure function) $[\text{無單位}]$
  * $Z'$ : 垂直結構函數 $Z$ 對 $z$ 的一階微分 (First derivative of the vertical structure function with respect to $z$) $[\text{無單位}]$，$Z' = \dfrac{dZ}{dz}$
  * $T$ : 擾動溫度 (Perturbation temperature) $[\text{K}]$
  * $w$ : 擾動對數氣壓垂直速度 (Perturbation log-pressure vertical velocity) $[\text{s}^{-1}]$
  * $Q$ : 非絕熱加熱率 (Diabatic heating rate) $[\text{J}\cdot\text{kg}^{-1}\cdot\text{s}^{-1}]$
  * 註：(b) 用 $Z'$ 而非 $Z$ **不是選擇，是被迫的**，理由見【推導 1】【推導 2】。

* **【假設 1】 只激發第一垂直內模態 (Only the first vertical internal mode is excited)：** 非絕熱強迫的垂直剖面完全落在【已知 2】的第一內模態上，其餘模態的振幅為零

  $$\hat{Q}_n = 0 \qquad \left(n \ge 2\right)$$

  * $\hat{Q}_n$ : 加熱在第 $n$ 垂直模態上的投影 (Projection of the heating onto the $n$-th vertical mode) $[\text{J}\cdot\text{kg}^{-1}\cdot\text{s}^{-1}]$
  * $Z'$ : 垂直結構函數 $Z$ 對 $z$ 的一階微分 (First derivative of the vertical structure function with respect to $z$) $[\text{無單位}]$，$Z' = \dfrac{dZ}{dz}$
  * 註：這是本篇最強的一條假設，也是【定義 2】**能只寫單一個 $Z(z)$ 的唯一理由** —— 一般情形下每個場都該寫成 $\sum_n(\cdot)Z_n(z)$ 的級數。它在下方的【證明】中不以 `\overset` 形式出現（它不是等號的依據，而是整個分離變數設定的前提），故列於此處備查。
  * 註：論文對這條假設的辯護是觀測 —— Johnson and Ciesielski (2000) 的西太平洋暖池加熱剖面，形狀與 $Z'(z)$ 幾乎重合。

* **【假設 2】 垂直結構函數不恆為零 (The structure function is non-trivial)：** 垂直結構函數及其導數都不是恆等於零的平凡解 ─ 這排除了「整個擾動場為零」這個沒有物理內容的解，也讓【證明】中兩側同除 $Z$ 或 $Z'$ 的動作合法

  $$Z(z) \not\equiv 0, \qquad Z'(z) \not\equiv 0$$

  * $Z(z)$ : 垂直結構函數 (Vertical structure function) $[\text{無單位}]$
  * $Z'$ : 垂直結構函數 $Z$ 對 $z$ 的一階微分 (First derivative of the vertical structure function with respect to $z$) $[\text{無單位}]$，$Z' = \dfrac{dZ}{dz}$
  * $z$ : 對數氣壓垂直座標 (Log-pressure vertical coordinate) $[\text{無單位}]$

* **【推導 1】 靜力方程式逼出 $T \propto Z'$ (Hydrostatic balance forces $T \propto Z'$)：** 一旦把 $\phi$ 掛在 $Z$ 上，$T$ 的垂直結構就沒有選擇餘地

  $$\begin{gather*}
  RT &\overset{\text{已知 1(c)}}{=}& \frac{\partial \phi}{\partial z} \\
  RT &\overset{\text{定義 2(a)}}{=}& \frac{\partial}{\partial z}\left[\hat{\phi}(x,y,t)\,Z(z)\right] \\
  RT &=& \hat{\phi}(x,y,t)\,Z'(z) \\
  T &=& \frac{\hat{\phi}}{R}\,Z'(z)
  \end{gather*}$$

  * $R$ : 乾空氣氣體常數 (Gas constant for dry air) $[\text{J}\cdot\text{kg}^{-1}\cdot\text{K}^{-1}]$
  * $T$ : 擾動溫度 (Perturbation temperature) $[\text{K}]$
  * $\phi$ : 擾動位勢 (Perturbation geopotential) $[\text{m}^{2}\cdot\text{s}^{-2}]$
  * $z$ : 對數氣壓垂直座標 (Log-pressure vertical coordinate) $[\text{無單位}]$
  * $\hat{\phi}$ : 擾動位勢的水平結構函數 (Horizontal structure function of the perturbation geopotential) $[\text{m}^{2}\cdot\text{s}^{-2}]$
  * $x,\ y$ : 緯向、經向座標 (Zonal and meridional coordinates) $[\text{m}]$
  * $y$ : 經向座標，以赤道為原點 (Meridional coordinate) $[\text{m}]$
  * $t$ : 時間 (Time) $[\text{s}]$
  * $Z(z)$ : 垂直結構函數 (Vertical structure function) $[\text{無單位}]$
  * $Z'$ : 垂直結構函數 $Z$ 對 $z$ 的一階微分 (First derivative of the vertical structure function with respect to $z$) $[\text{無單位}]$，$Z' = \dfrac{dZ}{dz}$
  * 註：右端的垂直依賴**只能是 $Z'$**。這就是【定義 2】(b) 為什麼非得用 $Z'$ 不可 —— 把 $\hat{T} = \hat{\phi}/R$ 對照【定義 2】(b) 即得【證明 (c)】。

* **【推導 2】 連續方程式逼出 $w \propto Z'$ (Continuity forces $w \propto Z'$)：** 【已知 1】(d) 中 $u, v$ 的水平輻散帶著 $Z$，因此 $\left(\dfrac{\partial}{\partial z} - 1\right)w$ 也必須正比於 $Z$；而【已知 2】說**恰好是 $Z'$ 有這個性質**

  $$\begin{gather*}
  \left(\frac{d}{dz} - 1\right)Z'(z) &\overset{\text{已知 2}}{=}& -\lambda\,Z(z) \\
  \end{gather*}$$

  * $z$ : 對數氣壓垂直座標 (Log-pressure vertical coordinate) $[\text{無單位}]$
  * $Z(z)$ : 垂直結構函數 (Vertical structure function) $[\text{無單位}]$
  * $Z'$ : 垂直結構函數 $Z$ 對 $z$ 的一階微分 (First derivative of the vertical structure function with respect to $z$) $[\text{無單位}]$，$Z' = \dfrac{dZ}{dz}$
  * $\lambda$ : 第一內模態的分離常數 (Separation constant) $[\text{無單位}]$，$\lambda \approx 4.014$
  * $u,\ v$ : 擾動緯向、經向風速 (Perturbation zonal and meridional velocities) $[\text{m}\cdot\text{s}^{-1}]$
  * $w$ : 擾動對數氣壓垂直速度 (Perturbation log-pressure vertical velocity) $[\text{s}^{-1}]$
  * 註：這一條是整篇的樞紐。它說：**$Z'$ 經過 $\left(\dfrac{\partial}{\partial z} - 1\right)$ 加工後會變回 $Z$**。若把 $w$ 掛在 $Z$ 上，$\left(\dfrac{d}{dz} - 1\right)Z$ 一般不會正比於 $Z$，連續方程式的垂直依賴就約不掉，方程組**不閉合**。

+++

## 證明:

### (a) proof 緯向動量方程式的分離 (Separation of the zonal momentum equation)

三項都掛著同一個 $Z(z)$，直接提出來約掉。

$$\begin{gather*}
-\alpha u &\overset{\text{已知 1(a)}}{=}& \frac{\partial u}{\partial t} - \beta y\,v + \frac{\partial \phi}{\partial x} \\
-\alpha\hat{u}Z &\overset{\text{定義 2(a)}}{=}& \frac{\partial \hat{u}}{\partial t}Z - \beta y\,\hat{v}Z + \frac{\partial \hat{\phi}}{\partial x}Z \\
-\alpha\hat{u} &\overset{\text{假設 2}}{=}& \frac{\partial \hat{u}}{\partial t} - \beta y\,\hat{v} + \frac{\partial \hat{\phi}}{\partial x} \\
\frac{\partial \hat{u}}{\partial t} - \beta y\,\hat{v} + \frac{\partial \hat{\phi}}{\partial x} &=& -\alpha\hat{u}
\end{gather*}$$

### (b) proof 經向動量方程式的分離 (Separation of the meridional momentum equation)

與【證明 (a)】逐步平行。

$$\begin{gather*}
-\alpha v &\overset{\text{已知 1(b)}}{=}& \frac{\partial v}{\partial t} + \beta y\,u + \frac{\partial \phi}{\partial y} \\
-\alpha\hat{v}Z &\overset{\text{定義 2(a)}}{=}& \frac{\partial \hat{v}}{\partial t}Z + \beta y\,\hat{u}Z + \frac{\partial \hat{\phi}}{\partial y}Z \\
-\alpha\hat{v} &\overset{\text{假設 2}}{=}& \frac{\partial \hat{v}}{\partial t} + \beta y\,\hat{u} + \frac{\partial \hat{\phi}}{\partial y} \\
\frac{\partial \hat{v}}{\partial t} + \beta y\,\hat{u} + \frac{\partial \hat{\phi}}{\partial y} &=& -\alpha\hat{v}
\end{gather*}$$

### (c) proof 靜力方程式的分離 (Separation of the hydrostatic equation)

【推導 1】已經把式子整成 $T = \left(\hat{\phi}/R\right)Z'$，對照【定義 2】(b) 即得 —— 微分方程退化成**代數關係**。

$$\begin{gather*}
\hat{T}Z' &\overset{\text{定義 2(b)}}{=}& T \\
\hat{T}Z' &\overset{\text{推導 1}}{=}& \frac{\hat{\phi}}{R}Z' \\
\hat{T} &\overset{\text{假設 2}}{=}& \frac{\hat{\phi}}{R} \\
\hat{\phi} &=& R\hat{T}
\end{gather*}$$

### (d) proof 連續方程式的分離 (Separation of the continuity equation)

$u, v$ 帶 $Z$，$w$ 帶 $Z'$；後者經過 $\left(\dfrac{\partial}{\partial z} - 1\right)$ 之後被【推導 2】換回 $-\lambda Z$，於是兩邊的垂直依賴一致，可以約掉。

$$\begin{gather*}
0 &\overset{\text{已知 1(d)}}{=}& \frac{\partial u}{\partial x} + \frac{\partial v}{\partial y} + \left(\frac{\partial}{\partial z} - 1\right)w \\
&\overset{\text{定義 2(a)(b)}}{=}& \frac{\partial \hat{u}}{\partial x}Z + \frac{\partial \hat{v}}{\partial y}Z + \hat{w}\left(\frac{d}{dz} - 1\right)Z' \\
&\overset{\text{推導 2}}{=}& \frac{\partial \hat{u}}{\partial x}Z + \frac{\partial \hat{v}}{\partial y}Z - \lambda\hat{w}Z \\
&\overset{\text{假設 2}}{=}& \frac{\partial \hat{u}}{\partial x} + \frac{\partial \hat{v}}{\partial y} - \lambda\hat{w} \\
&\overset{\text{定義 1}}{=}& \frac{\partial \hat{u}}{\partial x} + \frac{\partial \hat{v}}{\partial y} - \left(\frac{\pi^{2}}{z_T^{2}} + \frac{1}{4}\right)\hat{w}
\end{gather*}$$

### (e) proof 熱力學方程式的分離 (Separation of the thermodynamic equation)

四項都掛著同一個 $Z'(z)$，直接約掉。

$$\begin{gather*}
\frac{Q}{c_p} &\overset{\text{已知 1(e)}}{=}& \frac{\partial T}{\partial t} + \alpha T + \Gamma w \\
\frac{\hat{Q}}{c_p}Z' &\overset{\text{定義 2(b)}}{=}& \frac{\partial \hat{T}}{\partial t}Z' + \alpha\hat{T}Z' + \Gamma\hat{w}Z' \\
\frac{\hat{Q}}{c_p} &\overset{\text{假設 2}}{=}& \frac{\partial \hat{T}}{\partial t} + \alpha\hat{T} + \Gamma\hat{w} \\
\frac{\partial \hat{T}}{\partial t} + \Gamma\hat{w} &=& -\alpha\hat{T} + \frac{\hat{Q}}{c_p}
\end{gather*}$$

+++

## 結構解釋

### 「$Z$ 與 $Z'$ 的配對」是被逼出來的，不是湊出來的

這是本篇最值得記住的一句話。整個配對只靠**兩條約束**：

1. **靜力方程式 $\dfrac{\partial\phi}{\partial z} = RT$（【推導 1】）** —— $T$ 是 $\phi$ 的垂直導數，所以 $\phi \propto Z$ 就強迫 $T \propto Z'$。
2. **連續方程式 ＋ 垂直結構方程式（【推導 2】）** —— 連續方程式要求 $\left(\dfrac{\partial}{\partial z} - 1\right)w \propto Z$，而垂直結構方程式**就是**在說 $\left(\dfrac{d}{dz} - 1\right)Z' = -\lambda Z$。

換句話說：[垂直結構方程式](Vertical_Structure_Equation_in_Log_Pressure.md)【定義 2】那個看似隨手寫下的
$\left(\dfrac{d}{dz} - 1\right)\dfrac{dZ}{dz} = -\lambda Z$，**它存在的唯一理由就是讓這裡的【證明 (d)】能約掉 $Z$**。

熱力學方程式（【證明 (e)】）沒有提供新的約束 —— 它同時含 $T$ 與 $w$，兩者都已是 $Z'$，自動相容。**這個自動相容正是分離變數成立的驗證**：若配對錯了，(e) 會在這裡爆掉。

### 三維問題塌縮成什麼

【證明 (a)】–【證明 (e)】的五條式子裡，$z$ **完全消失了**。剩下的是一組只含 $(x, y, t)$ 的方程組，其結構與**淺水方程式**完全同構：

| 淺水系統 | 本系統 | 對應關係 |
|---|---|---|
| 水深擾動 $g h'$ | $\hat{\phi}$ | 位勢即「有效水深」 |
| 重力波速平方 $gH$ | $R\Gamma/\lambda$ | 等效重力波速 $\bar{c}^{2}$ |
| $\dfrac{\partial h'}{\partial t} + H\nabla\cdot\mathbf{u} = 0$ | 【證明 (c)(d)(e)】三式合併 | 見下 |

把【證明 (c)】的 $\hat{T} = \hat\phi/R$ 代進【證明 (e)】，再用【證明 (d)】把 $\hat{w}$ 換掉：

$$\frac{1}{R}\frac{\partial \hat{\phi}}{\partial t} + \frac{\Gamma}{\lambda}\left[\frac{\partial \hat{u}}{\partial x} + \frac{\partial \hat{v}}{\partial y}\right] = -\frac{\alpha}{R}\hat{\phi} + \frac{\hat{Q}}{c_p}$$

兩側乘 $R$，$\dfrac{R\Gamma}{\lambda}$ 就是等效重力波速的平方 $\bar{c}^{2} \approx \left(41.25 \ \text{m}\cdot\text{s}^{-1}\right)^{2}$。這一步的正式版本見 [傅立葉轉換至淺水系統](Fourier_Transform_to_Shallow_Water_System.md)。

### 「只留第一模態」這條假設有多貴

【假設 1】是本篇唯一沒有數學辯護的一條。它的代價是：

* 模式**無法**描述加熱剖面形狀改變所帶來的響應變化（例如淺對流 vs. 深對流的差別）；
* 也無法描述垂直模態之間的能量交換。

論文付得起這個代價，是因為它處理的是 **MJO 對流包絡通過時對流最旺盛的時刻** —— 那個時候的加熱剖面確實非常接近單一的深對流剖面。但如果要研究 MJO 的**起始**或**衰減**階段（淺對流、層狀降水各佔一定比例），這條假設就會成為主要的模式誤差來源。

本庫 [垂直模態分解](../../02_Concepts/Atmospheric_Dynamics/Normal_Mode_Decomposition.ipynb) 對「保留多個模態」的一般情形有概念層面的討論。
