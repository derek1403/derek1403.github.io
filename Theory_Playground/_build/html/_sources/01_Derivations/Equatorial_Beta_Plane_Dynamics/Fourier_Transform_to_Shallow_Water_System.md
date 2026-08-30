# Fourier Transform to the Shallow Water System (隨波座標、緯向傅立葉轉換與淺水系統的算符形式)

+++

## 證明目標:

把 [水平結構方程組](Separation_into_Horizontal_Structure_System.md) 的**偏微分方程組**，
經「隨波定常化 → 緯向傅立葉轉換」兩步，壓成每個緯向波數各自獨立的**常微分方程組**，
再收進一個線性算符裡。

* (a) 隨波座標下的時間與空間導數替換：

$$\frac{\partial}{\partial t} \to -c\frac{\partial}{\partial \xi}, \qquad \frac{\partial}{\partial x} \to \frac{\partial}{\partial \xi}$$

* (b) 緯向傅立葉轉換對：

$$\hat{u}_m(y) = \frac{1}{2\pi a}\int_{-\pi a}^{\pi a}\hat{u}(\xi, y)\,e^{-im\xi/a}\,d\xi, \qquad \hat{u}(\xi, y) = \sum_{m = -\infty}^{\infty}\hat{u}_m(y)\,e^{im\xi/a}$$

* (c) 轉換後的常微分方程組（「淺水系統」）：

$$\left(\alpha - \frac{imc}{a}\right)\hat{u}_m - \beta y\,\hat{v}_m + \frac{im}{a}\hat{\phi}_m = 0$$

$$\left(\alpha - \frac{imc}{a}\right)\hat{v}_m + \beta y\,\hat{u}_m + \frac{d\hat{\phi}_m}{dy} = 0$$

$$\left(\alpha - \frac{imc}{a}\right)\hat{\phi}_m + \bar{c}^{2}\left(\frac{im}{a}\hat{u}_m + \frac{d\hat{v}_m}{dy}\right) = \kappa\hat{Q}_m$$

* (d) 垂直速度的診斷還原式：

$$\hat{w}_m = \left(\frac{\pi^{2}}{z_T^{2}} + \frac{1}{4}\right)^{-1}\left(\frac{im}{a}\hat{u}_m + \frac{d\hat{v}_m}{dy}\right)$$

* (e) 收進算符後的向量形式：

$$\left(\alpha - \frac{imc}{a}\right)\hat{\boldsymbol{\eta}}_m + \mathcal{L}\hat{\boldsymbol{\eta}}_m = \kappa\hat{\mathbf{Q}}_m$$

  其中

$$\mathcal{L} = \begin{pmatrix} 0 & -\beta y & im/a \cr \beta y & 0 & d/dy \cr \bar{c}^{2}im/a & \bar{c}^{2}d/dy & 0 \end{pmatrix},
\qquad
\hat{\boldsymbol{\eta}}_m = \begin{pmatrix}\hat{u}_m \cr \hat{v}_m \cr \hat{\phi}_m\end{pmatrix},
\qquad
\hat{\mathbf{Q}}_m = \begin{pmatrix}0 \cr 0 \cr \hat{Q}_m\end{pmatrix}$$

* (f) 等效重力波速的數值：

$$\bar{c} \approx 41.25 \ \text{m}\cdot\text{s}^{-1}$$

* 註：(a)–(f) 就是 [Schubert & Masarik (2006)](../../06_References/Tropical_wave_dynamics/Schubert2006-Potential_vorticity_aspects_of_the_MJO/Potential_vorticity_aspects_of_the_MJO.ipynb) 的 $(4.2)$–$(4.4)$、$(4.6)$、$(4.7)$。加熱項本身的緯向傅立葉係數 $(4.5)$ 留到 [移動熱源的模態投影](Projection_of_a_Moving_Heat_Source.md)，因為它需要先給定加熱的具體形式 $(4.1)$。
* 註：「把流體力學偏微分方程組轉成線性代數的矩陣方程式」這個手法，已在 Advanced Atmospheric Dynamics 的 [project1_2](https://derek1403.github.io/PC-NTU/Advanced-Atmospheric-Dynamics/_build/html/project/project1/project1_2.html) 完整示範過。本篇只是把同一套手法套在 Schubert 的方程組上。

+++

## 假設與已知 (Assumptions & Preliminaries)

* **【已知 1】 [水平結構方程組 (Horizontal structure system)](https://derek1403.github.io/Theory_Playground/_build/html/01_Derivations/Equatorial_Beta_Plane_Dynamics/Separation_into_Horizontal_Structure_System.html#assumptions-preliminaries)：** 把垂直依賴分離掉之後剩下的五條純水平方程式：形式與原始方程組相同，但垂直速度只透過連續方程式裡的 $-\lambda\hat{w}$ 出現，靜力關係也退化成代數式 $\hat{\phi} = R\hat{T}$ ─ 這使整組方程得以收成淺水系統。（已於本庫 Separation into the Horizontal Structure System 完整證明，此處直接引用。）

  * (a) 緯向動量方程式：

    $$\frac{\partial \hat{u}}{\partial t} - \beta y\,\hat{v} + \frac{\partial \hat{\phi}}{\partial x} = -\alpha\hat{u}$$

  * (b) 經向動量方程式：

    $$\frac{\partial \hat{v}}{\partial t} + \beta y\,\hat{u} + \frac{\partial \hat{\phi}}{\partial y} = -\alpha\hat{v}$$

  * (c) 靜力關係：

    $$\hat{\phi} = R\hat{T}$$

  * (d) 連續方程式：

    $$\frac{\partial \hat{u}}{\partial x} + \frac{\partial \hat{v}}{\partial y} - \lambda\hat{w} = 0$$

  * (e) 熱力學方程式：

    $$\frac{\partial \hat{T}}{\partial t} + \Gamma\hat{w} = -\alpha\hat{T} + \frac{\hat{Q}}{c_p}$$

  * $\hat{u},\ \hat{v}$ : 緯向、經向風的水平結構函數 (Horizontal structure functions of the velocities) $[\text{m}\cdot\text{s}^{-1}]$
  * $\hat{\phi}$ : 擾動位勢的水平結構函數 (Horizontal structure function of the perturbation geopotential) $[\text{m}^{2}\cdot\text{s}^{-2}]$
  * $\hat{T}$ : 擾動溫度的水平結構函數 (Horizontal structure function of the perturbation temperature) $[\text{K}]$
  * $\hat{w}$ : 擾動對數氣壓垂直速度的水平結構函數 (Horizontal structure function of the perturbation log-pressure vertical velocity) $[\text{s}^{-1}]$
  * $\hat{Q}$ : 加熱率的水平結構函數 (Horizontal structure function of the heating rate) $[\text{J}\cdot\text{kg}^{-1}\cdot\text{s}^{-1}]$
  * $\lambda$ : 第一內模態的分離常數 (Separation constant) $[\text{無單位}]$，$\lambda = \dfrac{\pi^{2}}{z_T^{2}} + \dfrac{1}{4} \approx 4.014$
  * $\beta$ : 赤道 $\beta$ 參數 (Equatorial beta parameter) $[\text{m}^{-1}\cdot\text{s}^{-1}]$，$\beta = 2\Omega/a$
  * $\alpha$ : 常數阻尼率 (Constant damping rate) $[\text{s}^{-1}]$
  * $\Gamma$ : 靜力穩定度 (Static stability) $[\text{K}]$，$\Gamma = 23.79 \ \text{K}$
  * $R$ : 乾空氣氣體常數 (Gas constant for dry air) $[\text{J}\cdot\text{kg}^{-1}\cdot\text{K}^{-1}]$，$R = 287 \ \text{J}\cdot\text{kg}^{-1}\cdot\text{K}^{-1}$
  * $c_p$ : 定壓比熱 (Specific heat at constant pressure) $[\text{J}\cdot\text{kg}^{-1}\cdot\text{K}^{-1}]$
  * $a$ : 地球半徑 (Earth's radius) $[\text{m}]$，$a = 6370 \ \text{km}$
  * $\Omega$ : 地球自轉角速度 (Earth's angular velocity) $[\text{s}^{-1}]$，$\Omega = 7.292\times10^{-5} \ \text{s}^{-1}$
  * $t$ : 時間 (Time) $[\text{s}]$
  * $y$ : 經向座標，以赤道為原點 (Meridional coordinate) $[\text{m}]$
  * $x,\ y$ : 緯向、經向座標 (Zonal and meridional coordinates) $[\text{m}]$

* **【已知 2】 [複數傅立葉級數 (Complex Fourier series)](https://dlmf.nist.gov/1.8#i)：** 週期為 $2\pi a$ 的函數可展開成緯向波數 $m$ 的級數，係數由積分取出。（標準結果，此處直接引用。）

  $$F(\xi) = \sum_{m = -\infty}^{\infty}F_m\,e^{im\xi/a}, \qquad F_m = \frac{1}{2\pi a}\int_{-\pi a}^{\pi a}F(\xi)\,e^{-im\xi/a}\,d\xi$$

  * $F(\xi)$ : 待展開的週期函數 (Periodic function) $[\text{依應用而定}]$
  * $F_m$ : 第 $m$ 個傅立葉係數 (The $m$-th Fourier coefficient) $[\text{依應用而定}]$
  * $m$ : 緯向波數 (Zonal wavenumber) $[\text{無單位}]$，整數
  * $\xi$ : 隨波緯向座標 (Translating zonal coordinate) $[\text{m}]$
  * $a$ : 地球半徑 (Earth's radius) $[\text{m}]$，$a = 6370 \ \text{km}$

* **【假設 1】 隨波定常 (Steadiness in the translating frame)：** 解在以速度 $c$ 東移的參考系中是定常的，因此所有場只依賴 $\xi = x - ct$ 與 $y$

  * (a) 隨波座標：

    $$\xi \overset{\text{def}}{=} x - ct$$

  * (b) 在該座標下場對時間的顯式依賴消失：

    $$\hat{u}(x, y, t) = \hat{u}(\xi, y)$$

  * $\xi$ : 隨波緯向座標 (Translating zonal coordinate) $[\text{m}]$
  * $c$ : 對流包絡的東移速度 (Eastward propagation speed) $[\text{m}\cdot\text{s}^{-1}]$，$c = 5 \ \text{m}\cdot\text{s}^{-1}$
  * $x,\ y$ : 緯向、經向座標 (Zonal and meridional coordinates) $[\text{m}]$
  * $t$ : 時間 (Time) $[\text{s}]$
  * $\hat{u},\ \hat{v}$ : 緯向、經向風的水平結構函數 (Horizontal structure functions of the velocities) $[\text{m}\cdot\text{s}^{-1}]$
  * $y$ : 經向座標，以赤道為原點 (Meridional coordinate) $[\text{m}]$
  * 註：這是把「時間」這個維度換成「相位」的標準操作。代價是**只能描述已達成定常的成熟階段**，無法描述 MJO 的起始與衰減。

* **【假設 2】 緯向週期性 (Zonal periodicity)：** 求解區域繞地球一圈，故所有場對 $\xi$ 是週期為 $2\pi a$ 的週期函數，【已知 2】適用

  $$\hat{u}(\xi + 2\pi a, y) = \hat{u}(\xi, y)$$

  * $\hat{u},\ \hat{v}$ : 緯向、經向風的水平結構函數 (Horizontal structure functions of the velocities) $[\text{m}\cdot\text{s}^{-1}]$
  * $\xi$ : 隨波緯向座標 (Translating zonal coordinate) $[\text{m}]$
  * $a$ : 地球半徑 (Earth's radius) $[\text{m}]$，$a = 6370 \ \text{km}$
  * $y$ : 經向座標，以赤道為原點 (Meridional coordinate) $[\text{m}]$

* **【定義 1】 等效重力波速 (Equivalent gravity wave speed)：** 第一垂直內模態對應的淺水重力波速

  $$\begin{gather*}
  \bar{c}^{2} &\overset{\text{def}}{=}& \frac{R\Gamma}{\lambda} \\
  &\overset{\text{已知 1}}{=}& R\Gamma\left[\left(\frac{\pi}{z_T}\right)^{2} + \frac{1}{4}\right]^{-1}
  \end{gather*}$$

  * $\bar{c}$ : 等效重力波速 (Equivalent gravity wave speed) $[\text{m}\cdot\text{s}^{-1}]$
  * $R$ : 乾空氣氣體常數 (Gas constant for dry air) $[\text{J}\cdot\text{kg}^{-1}\cdot\text{K}^{-1}]$，$R = 287 \ \text{J}\cdot\text{kg}^{-1}\cdot\text{K}^{-1}$
  * $\Gamma$ : 靜力穩定度 (Static stability) $[\text{K}]$，$\Gamma = 23.79 \ \text{K}$
  * $\lambda$ : 第一內模態的分離常數 (Separation constant) $[\text{無單位}]$，$\lambda = \dfrac{\pi^{2}}{z_T^{2}} + \dfrac{1}{4} \approx 4.014$
  * $z$ : 對數氣壓垂直座標 (Log-pressure vertical coordinate) $[\text{無單位}]$
  * $z_T$ : 對流層頂的對數氣壓高度 (Log-pressure height of the tropopause) $[\text{無單位}]$

* **【定義 2】 Poisson 常數 (Poisson constant)：** 氣體常數與定壓比熱之比，量度乾空氣在絕熱過程中溫度對氣壓變化的敏感度；它是把熱力學第一定律換成對數氣壓座標時自然收攏出來的組合。

  $$\kappa \overset{\text{def}}{=} \frac{R}{c_p}$$

  * $\kappa$ : Poisson 常數 (Poisson constant) $[\text{無單位}]$，$\kappa \approx 0.286$
  * $R$ : 乾空氣氣體常數 (Gas constant for dry air) $[\text{J}\cdot\text{kg}^{-1}\cdot\text{K}^{-1}]$，$R = 287 \ \text{J}\cdot\text{kg}^{-1}\cdot\text{K}^{-1}$
  * $c_p$ : 定壓比熱 (Specific heat at constant pressure) $[\text{J}\cdot\text{kg}^{-1}\cdot\text{K}^{-1}]$

* **【定義 3】 狀態向量與強迫向量 (State and forcing vectors)：** 把三個未知場與強迫收成三分量向量

  * (a) 狀態向量：

    $$\hat{\boldsymbol{\eta}}_m(y) \overset{\text{def}}{=} \begin{pmatrix}\hat{u}_m(y) \cr \hat{v}_m(y) \cr \hat{\phi}_m(y)\end{pmatrix}$$

  * (b) 強迫向量（加熱只出現在第三分量）：

    $$\hat{\mathbf{Q}}_m(y) \overset{\text{def}}{=} \begin{pmatrix}0 \cr 0 \cr \hat{Q}_m(y)\end{pmatrix}$$

  * $\hat{\boldsymbol{\eta}}_m$ : 第 $m$ 個緯向波數的狀態向量 (State vector) $[\text{依分量而定}]$
  * $\hat{\mathbf{Q}}_m$ : 第 $m$ 個緯向波數的強迫向量 (Forcing vector) $[\text{依分量而定}]$
  * $y$ : 經向座標，以赤道為原點 (Meridional coordinate) $[\text{m}]$
  * $\hat{u},\ \hat{v}$ : 緯向、經向風的水平結構函數 (Horizontal structure functions of the velocities) $[\text{m}\cdot\text{s}^{-1}]$
  * $\hat{\phi}$ : 擾動位勢的水平結構函數 (Horizontal structure function of the perturbation geopotential) $[\text{m}^{2}\cdot\text{s}^{-2}]$
  * $\hat{Q}$ : 加熱率的水平結構函數 (Horizontal structure function of the heating rate) $[\text{J}\cdot\text{kg}^{-1}\cdot\text{s}^{-1}]$

* **【定義 4】 線性算符 $\mathcal{L}$ (Linear operator $\mathcal{L}$)：** 把【證明 (c)】三條式子的係數收成一個 $3 \times 3$ 的算符矩陣

  $$\mathcal{L} \overset{\text{def}}{=} \begin{pmatrix} 0 & -\beta y & \dfrac{im}{a} \cr \beta y & 0 & \dfrac{d}{dy} \cr \bar{c}^{2}\dfrac{im}{a} & \bar{c}^{2}\dfrac{d}{dy} & 0 \end{pmatrix}$$

  * $\mathcal{L}$ : 水平結構的線性算符 (Linear operator of the horizontal structure) $[\text{s}^{-1}]$
  * $\beta$ : 赤道 $\beta$ 參數 (Equatorial beta parameter) $[\text{m}^{-1}\cdot\text{s}^{-1}]$，$\beta = 2\Omega/a$
  * $y$ : 經向座標，以赤道為原點 (Meridional coordinate) $[\text{m}]$
  * $m$ : 緯向波數 (Zonal wavenumber) $[\text{無單位}]$，整數
  * $a$ : 地球半徑 (Earth's radius) $[\text{m}]$，$a = 6370 \ \text{km}$
  * $\bar{c}$ : 等效重力波速 (Equivalent gravity wave speed) $[\text{m}\cdot\text{s}^{-1}]$
  * 註：矩陣元素含微分算子 $d/dy$，因此 $\mathcal{L}$ 是**算符**而非普通矩陣。它作用在 $\hat{\boldsymbol{\eta}}_m(y)$ 這個向量函數上。

* **【推導 1】 隨波座標下的導數替換 (Derivative replacements in the translating frame)：** 由【假設 1】的連鎖律

  * (a) 時間導數：

    $$\begin{gather*}
    \left.\frac{\partial}{\partial t}\right|_{x} &\overset{\text{假設 1(b)}}{=}& \frac{\partial \xi}{\partial t}\frac{\partial}{\partial \xi} \\
    &\overset{\text{假設 1(a)}}{=}& -c\frac{\partial}{\partial \xi}
    \end{gather*}$$

  * (b) 緯向導數：

    $$\begin{gather*}
    \left.\frac{\partial}{\partial x}\right|_{t} &\overset{\text{假設 1(b)}}{=}& \frac{\partial \xi}{\partial x}\frac{\partial}{\partial \xi} \\
    &\overset{\text{假設 1(a)}}{=}& \frac{\partial}{\partial \xi}
    \end{gather*}$$

  * $t$ : 時間 (Time) $[\text{s}]$
  * $\xi$ : 隨波緯向座標 (Translating zonal coordinate) $[\text{m}]$
  * $c_p$ : 定壓比熱 (Specific heat at constant pressure) $[\text{J}\cdot\text{kg}^{-1}\cdot\text{K}^{-1}]$
  * $x,\ y$ : 緯向、經向座標 (Zonal and meridional coordinates) $[\text{m}]$

* **【推導 2】 傅立葉轉換下的導數 (Derivatives under the Fourier transform)：** 對【已知 2】的展開式逐項微分

  * (a) 對 $\xi$ 的導數變成乘以 $im/a$：

    $$\begin{gather*}
    \frac{\partial}{\partial \xi}\left[\sum_{m}F_m(y)\,e^{im\xi/a}\right] &\overset{\text{已知 2}}{=}& \sum_{m}F_m(y)\frac{im}{a}e^{im\xi/a} \\
    \frac{\partial}{\partial \xi} &\to& \frac{im}{a}
    \end{gather*}$$

  * (b) 對 $y$ 的導數只落在係數上：

    $$\frac{\partial}{\partial y}\left[\sum_{m}F_m(y)\,e^{im\xi/a}\right] = \sum_{m}\frac{dF_m}{dy}e^{im\xi/a}$$

  * $\xi$ : 隨波緯向座標 (Translating zonal coordinate) $[\text{m}]$
  * $m$ : 緯向波數 (Zonal wavenumber) $[\text{無單位}]$，整數
  * $F(\xi)$ : 待展開的週期函數 (Periodic function) $[\text{依應用而定}]$
  * $y$ : 經向座標，以赤道為原點 (Meridional coordinate) $[\text{m}]$
  * $a$ : 地球半徑 (Earth's radius) $[\text{m}]$，$a = 6370 \ \text{km}$
  * $F_m$ : 第 $m$ 個傅立葉係數 (The $m$-th Fourier coefficient) $[\text{依應用而定}]$
  * 註：因為 $e^{im\xi/a}$ 對不同的 $m$ 線性獨立（【已知 2】的正交性），代入方程式後**每個 $m$ 各自成立一條方程式**，$m$ 之間完全不耦合。

* **【推導 3】 加熱項的合併 (Combining the diabatic terms)：** 把【已知 1】(c)(d)(e) 三條合成一條只含 $\hat{\phi}$ 與水平輻散的方程式

  $$\begin{gather*}
  \frac{\hat{Q}}{c_p} &\overset{\text{已知 1(e)}}{=}& \frac{\partial \hat{T}}{\partial t} + \alpha\hat{T} + \Gamma\hat{w} \\
  \frac{\hat{Q}}{c_p} &\overset{\text{已知 1(c)}}{=}& \frac{1}{R}\left[\frac{\partial \hat{\phi}}{\partial t} + \alpha\hat{\phi}\right] + \Gamma\hat{w} \\
  \frac{\hat{Q}}{c_p} &\overset{\text{已知 1(d)}}{=}& \frac{1}{R}\left[\frac{\partial \hat{\phi}}{\partial t} + \alpha\hat{\phi}\right] + \frac{\Gamma}{\lambda}\left[\frac{\partial \hat{u}}{\partial x} + \frac{\partial \hat{v}}{\partial y}\right] \\
  \frac{R\hat{Q}}{c_p} &=& \frac{\partial \hat{\phi}}{\partial t} + \alpha\hat{\phi} + \frac{R\Gamma}{\lambda}\left[\frac{\partial \hat{u}}{\partial x} + \frac{\partial \hat{v}}{\partial y}\right] \\
  \kappa\hat{Q} &\overset{\text{定義 1,定義 2}}{=}& \frac{\partial \hat{\phi}}{\partial t} + \alpha\hat{\phi} + \bar{c}^{2}\left[\frac{\partial \hat{u}}{\partial x} + \frac{\partial \hat{v}}{\partial y}\right]
  \end{gather*}$$

  * $\hat{Q}$ : 加熱率的水平結構函數 (Horizontal structure function of the heating rate) $[\text{J}\cdot\text{kg}^{-1}\cdot\text{s}^{-1}]$
  * $c_p$ : 定壓比熱 (Specific heat at constant pressure) $[\text{J}\cdot\text{kg}^{-1}\cdot\text{K}^{-1}]$
  * $\hat{T}$ : 擾動溫度的水平結構函數 (Horizontal structure function of the perturbation temperature) $[\text{K}]$
  * $t$ : 時間 (Time) $[\text{s}]$
  * $\alpha$ : 常數阻尼率 (Constant damping rate) $[\text{s}^{-1}]$
  * $\Gamma$ : 靜力穩定度 (Static stability) $[\text{K}]$，$\Gamma = 23.79 \ \text{K}$
  * $\hat{w}$ : 擾動對數氣壓垂直速度的水平結構函數 (Horizontal structure function of the perturbation log-pressure vertical velocity) $[\text{s}^{-1}]$
  * $R$ : 乾空氣氣體常數 (Gas constant for dry air) $[\text{J}\cdot\text{kg}^{-1}\cdot\text{K}^{-1}]$，$R = 287 \ \text{J}\cdot\text{kg}^{-1}\cdot\text{K}^{-1}$
  * $\hat{\phi}$ : 擾動位勢的水平結構函數 (Horizontal structure function of the perturbation geopotential) $[\text{m}^{2}\cdot\text{s}^{-2}]$
  * $\lambda$ : 第一內模態的分離常數 (Separation constant) $[\text{無單位}]$，$\lambda = \dfrac{\pi^{2}}{z_T^{2}} + \dfrac{1}{4} \approx 4.014$
  * $\hat{u},\ \hat{v}$ : 緯向、經向風的水平結構函數 (Horizontal structure functions of the velocities) $[\text{m}\cdot\text{s}^{-1}]$
  * $x,\ y$ : 緯向、經向座標 (Zonal and meridional coordinates) $[\text{m}]$
  * $y$ : 經向座標，以赤道為原點 (Meridional coordinate) $[\text{m}]$
  * $\kappa$ : Poisson 常數 (Poisson constant) $[\text{無單位}]$，$\kappa \approx 0.286$
  * $\bar{c}$ : 等效重力波速 (Equivalent gravity wave speed) $[\text{m}\cdot\text{s}^{-1}]$

+++

## 證明:

### (a) proof 隨波座標的導數替換 (Derivative replacement in the translating frame)

【推導 1】已經把兩條替換算完，此處只是把它們並列成論文的形式。

$$\begin{gather*}
\left.\frac{\partial}{\partial t}\right|_{x} &\overset{\text{推導 1(a)}}{=}& -c\frac{\partial}{\partial \xi} \\
\left.\frac{\partial}{\partial x}\right|_{t} &\overset{\text{推導 1(b)}}{=}& \frac{\partial}{\partial \xi}
\end{gather*}$$

### (b) proof 緯向傅立葉轉換對 (Zonal Fourier transform pair)

【假設 2】保證週期性，直接套用【已知 2】並把 $F$ 取為 $\hat{u}$。

$$\begin{gather*}
\hat{u}(\xi, y) &\overset{\text{假設 2,已知 2}}{=}& \sum_{m = -\infty}^{\infty}\hat{u}_m(y)\,e^{im\xi/a} \\
\hat{u}_m(y) &\overset{\text{已知 2}}{=}& \frac{1}{2\pi a}\int_{-\pi a}^{\pi a}\hat{u}(\xi, y)\,e^{-im\xi/a}\,d\xi
\end{gather*}$$

### (c) proof 淺水系統 (Shallow water system)

三條方程式各自代入【推導 1】的座標替換與【推導 2】的導數規則。第三條先經過【推導 3】的合併。

* **緯向動量方程式：**

$$\begin{gather*}
-\alpha\hat{u}_m &\overset{\text{已知 1(a)}}{=}& \frac{\partial \hat{u}_m}{\partial t} - \beta y\,\hat{v}_m + \frac{\partial \hat{\phi}_m}{\partial x} \\
-\alpha\hat{u}_m &\overset{\text{推導 1(a)(b)}}{=}& -c\frac{\partial \hat{u}_m}{\partial \xi} - \beta y\,\hat{v}_m + \frac{\partial \hat{\phi}_m}{\partial \xi} \\
-\alpha\hat{u}_m &\overset{\text{推導 2(a)}}{=}& -\frac{imc}{a}\hat{u}_m - \beta y\,\hat{v}_m + \frac{im}{a}\hat{\phi}_m \\
0 &=& \left(\alpha - \frac{imc}{a}\right)\hat{u}_m - \beta y\,\hat{v}_m + \frac{im}{a}\hat{\phi}_m
\end{gather*}$$

* **經向動量方程式：**

$$\begin{gather*}
-\alpha\hat{v}_m &\overset{\text{已知 1(b)}}{=}& \frac{\partial \hat{v}_m}{\partial t} + \beta y\,\hat{u}_m + \frac{\partial \hat{\phi}_m}{\partial y} \\
-\alpha\hat{v}_m &\overset{\text{推導 1(a),推導 2(b)}}{=}& -\frac{imc}{a}\hat{v}_m + \beta y\,\hat{u}_m + \frac{d\hat{\phi}_m}{dy} \\
0 &=& \left(\alpha - \frac{imc}{a}\right)\hat{v}_m + \beta y\,\hat{u}_m + \frac{d\hat{\phi}_m}{dy}
\end{gather*}$$

* **位勢方程式：**

$$\begin{gather*}
\kappa\hat{Q}_m &\overset{\text{推導 3}}{=}& \frac{\partial \hat{\phi}_m}{\partial t} + \alpha\hat{\phi}_m + \bar{c}^{2}\left[\frac{\partial \hat{u}_m}{\partial x} + \frac{\partial \hat{v}_m}{\partial y}\right] \\
&\overset{\text{推導 1(a)(b),推導 2(a)(b)}}{=}& -\frac{imc}{a}\hat{\phi}_m + \alpha\hat{\phi}_m + \bar{c}^{2}\left[\frac{im}{a}\hat{u}_m + \frac{d\hat{v}_m}{dy}\right] \\
&=& \left(\alpha - \frac{imc}{a}\right)\hat{\phi}_m + \bar{c}^{2}\left(\frac{im}{a}\hat{u}_m + \frac{d\hat{v}_m}{dy}\right)
\end{gather*}$$

### (d) proof 垂直速度的診斷還原 (Diagnostic recovery of the vertical velocity)

連續方程式對 $\hat{w}$ 而言是純代數式，直接移項並代入傅立葉導數。

$$\begin{gather*}
0 &\overset{\text{已知 1(d)}}{=}& \frac{\partial \hat{u}_m}{\partial x} + \frac{\partial \hat{v}_m}{\partial y} - \lambda\hat{w}_m \\
0 &\overset{\text{推導 1(b),推導 2(a)(b)}}{=}& \frac{im}{a}\hat{u}_m + \frac{d\hat{v}_m}{dy} - \lambda\hat{w}_m \\
\hat{w}_m &=& \frac{1}{\lambda}\left(\frac{im}{a}\hat{u}_m + \frac{d\hat{v}_m}{dy}\right) \\
\hat{w}_m &\overset{\text{已知 1}}{=}& \left(\frac{\pi^{2}}{z_T^{2}} + \frac{1}{4}\right)^{-1}\left(\frac{im}{a}\hat{u}_m + \frac{d\hat{v}_m}{dy}\right)
\end{gather*}$$

### (e) proof 向量形式 (Vector form)

把【證明 (c)】的三條依【定義 4】拆成「對角的 $\left(\alpha - imc/a\right)$」與「其餘全部收進 $\mathcal{L}$」兩部分。

$$\begin{gather*}
\mathcal{L}\hat{\boldsymbol{\eta}}_m &\overset{\text{定義 3(a),定義 4}}{=}& \begin{pmatrix} -\beta y\,\hat{v}_m + \dfrac{im}{a}\hat{\phi}_m \cr \beta y\,\hat{u}_m + \dfrac{d\hat{\phi}_m}{dy} \cr \bar{c}^{2}\dfrac{im}{a}\hat{u}_m + \bar{c}^{2}\dfrac{d\hat{v}_m}{dy} \end{pmatrix} \\
\mathcal{L}\hat{\boldsymbol{\eta}}_m &\overset{\text{證明 (c)}}{=}& \begin{pmatrix} -\left(\alpha - \dfrac{imc}{a}\right)\hat{u}_m \cr -\left(\alpha - \dfrac{imc}{a}\right)\hat{v}_m \cr \kappa\hat{Q}_m - \left(\alpha - \dfrac{imc}{a}\right)\hat{\phi}_m \end{pmatrix} \\
\mathcal{L}\hat{\boldsymbol{\eta}}_m &\overset{\text{定義 3(a)(b)}}{=}& \kappa\hat{\mathbf{Q}}_m - \left(\alpha - \frac{imc}{a}\right)\hat{\boldsymbol{\eta}}_m \\
\left(\alpha - \frac{imc}{a}\right)\hat{\boldsymbol{\eta}}_m + \mathcal{L}\hat{\boldsymbol{\eta}}_m &=& \kappa\hat{\mathbf{Q}}_m
\end{gather*}$$

### (f) solve 等效重力波速的數值 (Numerical value of the equivalent gravity wave speed)

把【已知 1】的常數代進【定義 1】。

$$\begin{gather*}
\lambda &\overset{\text{已知 1}}{\approx}& \frac{9.8696}{1.6194^{2}} + 0.25 \\
\lambda &\approx& 3.7636 + 0.25 \\
\lambda &\approx& 4.0136 \\
\bar{c}^{2} &\overset{\text{定義 1}}{\approx}& \frac{287 \times 23.79}{4.0136} \\
\bar{c}^{2} &\approx& 1701 \ \text{m}^{2}\cdot\text{s}^{-2} \\
\bar{c} &\approx& 41.25 \ \text{m}\cdot\text{s}^{-1}
\end{gather*}$$

+++

## 結構解釋

### 三步化簡各自買到了什麼

| 步驟 | 出處 | 消掉了什麼 | 代價 |
|---|---|---|---|
| 隨波定常 | 【假設 1】 | **時間維度** $t$ | 只能描述成熟、定常的階段 |
| 緯向傅立葉 | 【假設 2】+【已知 2】 | **緯向維度** $\xi$（每個 $m$ 獨立） | 需要緯向週期性 |
| 垂直分離（前一篇） | — | **垂直維度** $z$ | 只保留第一內模態 |

三步做完，原本 $(x, y, z, t)$ 四維的偏微分方程組，只剩下**對 $y$ 的常微分方程組**（【證明 (c)】）。
剩下那一維會在 [赤道波本徵函數](Equatorial_Wave_Eigenfunctions.md) 被正規模態轉換吃掉，屆時方程式會塌縮成純代數。

### 阻尼與移動速度為什麼會合成同一個複數

【證明 (c)】三條式子的對角項都是 $\left(\alpha - \dfrac{imc}{a}\right)$ —— **實部是阻尼、虛部是強迫的移動頻率**。

這個組合之所以能收得這麼乾淨，靠的是 [線性化原始方程組](Log_Pressure_Linearized_Primitive_Equations.md)【假設 4】那條「Rayleigh 摩擦與 Newtonian 冷卻取同一個 $\alpha$」。若兩者取不同的阻尼率（例如輻射阻尼 $10$–$20$ 天、摩擦阻尼 $3$–$5$ 天），對角項就會變成三個不同的複數，後面的正規模態轉換仍然做得下去，只是式子變醜。

這個複數分母正是 [受迫解](Forced_Response_of_Equatorial_Modes.md) 中「受迫阻尼振子響應函數」的來源。

### 為什麼 $\mathcal{L}$ 值得單獨取名

【定義 4】把三條方程式的**所有空間結構**塞進一個算符。這一步的意義是：原本的問題「解一組耦合的常微分方程」被翻譯成線性代數的標準問題

$$\left(\text{對角項}\right)\hat{\boldsymbol{\eta}}_m + \mathcal{L}\hat{\boldsymbol{\eta}}_m = \text{強迫}$$

只要能找到 $\mathcal{L}$ 的**本徵函數**，上式在該基底下就會對角化，每個模態各自變成一行除法。

而 $\mathcal{L}$ 的本徵函數之所以能構成一組完備正交基底，靠的是它相對於某個內積是**反厄米**的 —— 那正是 [能量內積與反厄米算符](Energy_Inner_Product_and_Skew_Hermitian_Operator.md) 要證的事。同樣的邏輯鏈在 Advanced Atmospheric Dynamics 的 [project1_3](https://derek1403.github.io/PC-NTU/Advanced-Atmospheric-Dynamics/_build/html/project/project1/project1_3.html) 已對另一個算符走過一遍。

### 等效深度的讀法

【定義 1】的 $\bar{c}^{2} = R\Gamma/\lambda$ 在淺水系統中扮演 $gH$ 的角色，因此**等效深度**為

$$H_{\text{eq}} = \frac{\bar{c}^{2}}{g} \approx \frac{1701}{9.81} \approx 173 \ \text{m}$$

也就是說：這個三維層結大氣中的第一斜壓模態，動力上完全等價於一層**深約 $173 \ \text{m}$ 的淺水**。分離常數 $\lambda$ 裡那個來自密度遞減的 $\dfrac{1}{4}$（見 [垂直結構方程式](Vertical_Structure_Equation_in_Log_Pressure.md) 的結構解釋）讓 $\bar{c}$ 比忽略它時小了約 $3\%$。
