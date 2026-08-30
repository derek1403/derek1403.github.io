# Physical Field Recovery and Zero Kelvin PV (物理場的還原與 Kelvin 波的零位渦)

+++

## 證明目標:

**端點①的收尾。** 把 [受迫解](Forced_Response_of_Equatorial_Modes.md) 的譜係數 $\hat{\eta}_{mnr}$
轉回物理空間的 $u, v, \phi, q, w$，並證明本文後半段最關鍵的一個事實。

* (a) 風場與質量場的還原：

$$\begin{pmatrix}u \cr v \cr \phi\end{pmatrix}\left(\xi, y, z\right) = Z(z)\sum_{m = -\infty}^{\infty}\sum_{n = -1}^{\infty}\sum_{r}\hat{\eta}_{mnr}\begin{pmatrix}U_{mnr}(\hat{y}) \cr V_{mnr}(\hat{y}) \cr \Phi_{mnr}(\hat{y})\end{pmatrix}e^{im\xi/a}$$

* (b) 位渦場的還原 —— 每個模態的 PV **只含單一個 $\mathcal{H}_n$**：

$$q\left(\xi, y, z\right) = Z(z)\sum_{m = -\infty}^{\infty}\sum_{n = -1}^{\infty}\sum_{r}\hat{q}_{mnr}\,\mathcal{H}_n(\hat{y})\,e^{im\xi/a}$$

* (c) 位渦的譜係數：

$$\hat{q}_{mnr} = A_{mnr}\left(\frac{m^{2} - \epsilon\hat{\nu}_{mnr}^{2}}{a\,\hat{\nu}_{mnr}}\right)\hat{\eta}_{mnr}$$

* (d) **★ Kelvin 波的位渦恰好為零：**

$$\hat{q}_{m,-1,2} = 0$$

* (e) 垂直速度的還原：

$$w\left(\xi, y, z\right) = \frac{Z'(z)}{R\Gamma}\sum_{m = -\infty}^{\infty}\sum_{n = -1}^{\infty}\sum_{r}i\nu_{mnr}\,\hat{\eta}_{mnr}\,\Phi_{mnr}(\hat{y})\,e^{im\xi/a}$$

* 註：(a)–(e) 就是 [Schubert & Masarik (2006)](../../06_References/Tropical_wave_dynamics/Schubert2006-Potential_vorticity_aspects_of_the_MJO/Potential_vorticity_aspects_of_the_MJO.ipynb) 的 $(4.24)$–$(4.27)$。
* 註：**(d) 是全文最重要的一條負面結果。** 它說 Kelvin 波把它所有的資訊都藏在 PV **以外**的地方。這直接導致 [可逆性原理](Equatorial_PV_Invertibility_Principle.md)（端點③）救不回對流**東側**的流場 —— 那不是近似不夠好，而是**資訊在 $q$ 這個變數裡根本不存在**。

+++

## 假設與已知 (Assumptions & Preliminaries)

* **【已知 1】 [正規模態展開與傅立葉逆轉換 (Normal mode expansion and inverse Fourier transform)](https://derek1403.github.io/Theory_Playground/_build/html/01_Derivations/Equatorial_Beta_Plane_Dynamics/Forced_Response_of_Equatorial_Modes.html#a-proof-normal-mode-expansion)：** 把譜空間的解還原成物理場所需的三步：先用正規模態把 $\hat{\boldsymbol{\eta}}_m$ 組回來，再對緯向波數做逆傅立葉轉換，最後乘上垂直結構函數（$u,\ v,\ \phi$ 用 $Z$；$T,\ w,\ Q$ 用 $Z'$）。（已於本庫 [Forced Response of Equatorial Modes](Forced_Response_of_Equatorial_Modes.md)【證明 (a)】與 [Fourier Transform to the Shallow Water System](Fourier_Transform_to_Shallow_Water_System.md)【證明 (b)】完整證明，此處直接引用。）

  * (a) 正規模態展開：

    $$\hat{\boldsymbol{\eta}}_m(\hat{y}) = \sum_{n = -1}^{\infty}\sum_{r}\hat{\eta}_{mnr}\mathbf{K}_{mnr}(\hat{y})$$

  * (b) 緯向傅立葉逆轉換：

    $$\hat{\boldsymbol{\eta}}\left(\xi, y\right) = \sum_{m = -\infty}^{\infty}\hat{\boldsymbol{\eta}}_m(y)\,e^{im\xi/a}$$

  * (c) 垂直分離：

    $$\left(u,\ v,\ \phi\right) = \left(\hat{u},\ \hat{v},\ \hat{\phi}\right)Z(z), \qquad \left(T,\ w,\ Q\right) = \left(\hat{T},\ \hat{w},\ \hat{Q}\right)Z'(z)$$

  * $\hat{\eta}_{mnr}$ : 正規模態展開係數 (Expansion coefficient) $[\text{m}\cdot\text{s}^{-1}]$
  * $\mathbf{K}_{mnr} = \left(U_{mnr},\ V_{mnr},\ \Phi_{mnr}\right)^{\mathsf{T}}$ : 本徵函數 (Eigenfunction) $[\text{依分量而定}]$
  * $Z(z)$ : 垂直結構函數 (Vertical structure function) $[\text{無單位}]$
  * $Z'$ : 垂直結構函數 $Z$ 對 $z$ 的一階微分 (First derivative of the vertical structure function with respect to $z$) $[\text{無單位}]$，$Z' = \dfrac{dZ}{dz}$
  * $\hat{\boldsymbol{\eta}}_m$ : 第 $m$ 個緯向波數的狀態向量 (State vector) $[\text{依分量而定}]$
  * $\hat{y}$ : 無因次經向座標 (Dimensionless meridional coordinate) $[\text{無單位}]$
  * $\xi$ : 隨波緯向座標 (Translating zonal coordinate) $[\text{m}]$
  * $y$ : 經向座標，以赤道為原點 (Meridional coordinate) $[\text{m}]$
  * $a$ : 地球半徑 (Earth's radius) $[\text{m}]$
  * $u,\ v$ : 擾動緯向、經向風速 (Perturbation velocities) $[\text{m}\cdot\text{s}^{-1}]$
  * $v$ : 擾動經向風速 (Perturbation meridional velocity) $[\text{m}\cdot\text{s}^{-1}]$
  * $\phi$ : 擾動位勢 (Perturbation geopotential) $[\text{m}^{2}\cdot\text{s}^{-2}]$
  * $\hat{u},\ \hat{v}$ : 緯向、經向風的水平結構函數 (Horizontal structure functions of the velocities) $[\text{m}\cdot\text{s}^{-1}]$
  * $\hat{\phi}$ : 擾動位勢的水平結構函數 (Horizontal structure function of the perturbation geopotential) $[\text{m}^{2}\cdot\text{s}^{-2}]$
  * $z$ : 對數氣壓垂直座標 (Log-pressure vertical coordinate) $[\text{無單位}]$
  * $w$ : 擾動對數氣壓垂直速度 (Perturbation log-pressure vertical velocity) $[\text{s}^{-1}]$
  * $Q$ : 非絕熱加熱率 (Diabatic heating rate) $[\text{J}\cdot\text{kg}^{-1}\cdot\text{s}^{-1}]$
  * $\hat{T}$ : 擾動溫度的水平結構函數 (Horizontal structure function of the perturbation temperature) $[\text{K}]$
  * $\hat{w}$ : 擾動對數氣壓垂直速度的水平結構函數 (Horizontal structure function of the perturbation log-pressure vertical velocity) $[\text{s}^{-1}]$
  * $\hat{Q}$ : 加熱率的水平結構函數 (Horizontal structure function of the heating rate) $[\text{J}\cdot\text{kg}^{-1}\cdot\text{s}^{-1}]$
  * $\mathbf{K}_{mnr}$ : 本徵函數 (Eigenfunction) $[\text{依分量而定}]$
  * $n$ : 經向模態指標 (Meridional mode index) $[\text{無單位}]$
  * $r$ : 波型指標 (Wave-type index) $[\text{無單位}]$

* **【已知 2】 [位渦距平的定義與垂直結構方程式 (PV anomaly and the vertical structure equation)](https://derek1403.github.io/Theory_Playground/_build/html/01_Derivations/Equatorial_Beta_Plane_Dynamics/Equatorial_PV_Equation_and_Beta_y_Source.html#assumptions-preliminaries)：** 還原位渦所需的三件事：位渦距平的定義（相對渦度加上 $\beta y$ 加權的層結項）、垂直結構的本徵方程，以及由分離常數定出的等效重力波速 $\bar{c}^{2} = R\Gamma/\lambda$。（已於本庫 [Equatorial PV Equation and the Beta-y Source](Equatorial_PV_Equation_and_Beta_y_Source.md)【定義 1】與 [Vertical Structure Equation in Log-Pressure](Vertical_Structure_Equation_in_Log_Pressure.md)【證明 (a)】完整證明，此處直接引用。）

  * (a) 位渦距平：

    $$q = \frac{\partial v}{\partial x} - \frac{\partial u}{\partial y} + \frac{\beta y}{R\Gamma}\left(\frac{\partial}{\partial z} - 1\right)\frac{\partial \phi}{\partial z}$$

  * (b) 垂直結構方程式：

    $$\left(\frac{d}{dz} - 1\right)\frac{dZ}{dz} = -\lambda Z, \qquad \lambda = \frac{\pi^{2}}{z_T^{2}} + \frac{1}{4}$$

  * (c) 等效重力波速：

    $$\bar{c}^{2} = \frac{R\Gamma}{\lambda}$$

  * $q$ : 位渦距平 (PV anomaly) $[\text{s}^{-1}]$
  * $\lambda$ : 第一內模態的分離常數 (Separation constant) $[\text{無單位}]$
  * $\bar{c}$ : 等效重力波速 (Equivalent gravity wave speed) $[\text{m}\cdot\text{s}^{-1}]$
  * $v$ : 擾動經向風速 (Perturbation meridional velocity) $[\text{m}\cdot\text{s}^{-1}]$
  * $x,\ y$ : 緯向、經向座標 (Zonal and meridional coordinates) $[\text{m}]$
  * $u,\ v$ : 擾動緯向、經向風速 (Perturbation velocities) $[\text{m}\cdot\text{s}^{-1}]$
  * $y$ : 經向座標，以赤道為原點 (Meridional coordinate) $[\text{m}]$
  * $\beta$ : 赤道 $\beta$ 參數 (Equatorial beta parameter) $[\text{m}^{-1}\cdot\text{s}^{-1}]$
  * $R$ : 乾空氣氣體常數 (Gas constant for dry air) $[\text{J}\cdot\text{kg}^{-1}\cdot\text{K}^{-1}]$
  * $\Gamma$ : 靜力穩定度 (Static stability) $[\text{K}]$
  * $z$ : 對數氣壓垂直座標 (Log-pressure vertical coordinate) $[\text{無單位}]$
  * $\phi$ : 擾動位勢 (Perturbation geopotential) $[\text{m}^{2}\cdot\text{s}^{-2}]$
  * $Z(z)$ : 垂直結構函數 (Vertical structure function) $[\text{無單位}]$
  * $z_T$ : 對流層頂的對數氣壓高度 (Log-pressure height of the tropopause) $[\text{無單位}]$

* **【已知 3】 [本徵值問題的三條分量式 (The three component equations of the eigenvalue problem)](https://derek1403.github.io/Theory_Playground/_build/html/01_Derivations/Equatorial_Beta_Plane_Dynamics/Fourier_Transform_to_Shallow_Water_System.html#e-proof-vector-form)：** 由本庫 [Fourier Transform to the Shallow Water System](Fourier_Transform_to_Shallow_Water_System.md)【定義 4】的算符與本徵值方程 $\mathcal{L}\mathbf{K}_{mnr} = i\nu_{mnr}\mathbf{K}_{mnr}$ 逐列讀出

  * (a) 第一列：

    $$-\beta y\,V_{mnr} + \frac{im}{a}\Phi_{mnr} = i\nu_{mnr}U_{mnr}$$

  * (b) 第二列：

    $$\beta y\,U_{mnr} + \frac{d\Phi_{mnr}}{dy} = i\nu_{mnr}V_{mnr}$$

  * (c) 第三列：

    $$\bar{c}^{2}\left(\frac{im}{a}U_{mnr} + \frac{dV_{mnr}}{dy}\right) = i\nu_{mnr}\Phi_{mnr}$$

  * $\nu_{mnr}$ : 本徵頻率 (Eigenfrequency) $[\text{s}^{-1}]$，實數
  * $\beta$ : 赤道 $\beta$ 參數 (Equatorial beta parameter) $[\text{m}^{-1}\cdot\text{s}^{-1}]$
  * $y$ : 經向座標，以赤道為原點 (Meridional coordinate) $[\text{m}]$
  * $\mathbf{K}_{mnr} = \left(U_{mnr},\ V_{mnr},\ \Phi_{mnr}\right)^{\mathsf{T}}$ : 本徵函數 (Eigenfunction) $[\text{依分量而定}]$
  * $a$ : 地球半徑 (Earth's radius) $[\text{m}]$
  * $U,\ V$ : 本徵函數的速度分量 (Velocity components of the eigenfunction) $[\text{無單位}]$
  * $\bar{c}$ : 等效重力波速 (Equivalent gravity wave speed) $[\text{m}\cdot\text{s}^{-1}]$
  * $i$ : 虛數單位 (Imaginary unit) $[\text{無單位}]$，$i^{2} = -1$

* **【已知 4】 [本徵函數的第二分量與 Kelvin 波的本徵值 (Second component of the eigenfunction and the Kelvin eigenvalue)](https://derek1403.github.io/Theory_Playground/_build/html/01_Derivations/Equatorial_Beta_Plane_Dynamics/Equatorial_Wave_Eigenfunctions.html#a-proof-explicit-form-of-the-eigenfunctions)：** 本徵函數的第二分量正比於 $\left(\epsilon\hat{\nu}_{mnr}^{2} - m^{2}\right)\mathcal{H}_n$；而 Kelvin 波滿足 $\epsilon^{1/2}\hat{\nu}_{m,-1,2} = m$，恰好讓這個係數為零 ─ 這就是 Kelvin 波經向速度恆為零、位渦也為零的代數根源。（已於本庫 [Equatorial Wave Eigenfunctions](Equatorial_Wave_Eigenfunctions.md) 與 [Matsuno Dispersion Relation](Matsuno_Dispersion_Relation.md) 完整證明，此處直接引用。）

  * (a) 第二分量：

    $$V_{mnr}(\hat{y}) = -i\,A_{mnr}\left(\epsilon\hat{\nu}_{mnr}^{2} - m^{2}\right)\mathcal{H}_n(\hat{y})$$

  * (b) Kelvin 波的本徵值：

    $$\epsilon^{1/2}\hat{\nu}_{m,-1,2} = m$$

  * $A_{mnr}$ : 歸一化常數 (Normalization constant) $[\text{無單位}]$
  * $\epsilon$ : Lamb 參數 (Lamb's parameter) $[\text{無單位}]$
  * $\hat{\nu}_{mnr}$ : 無因次本徵頻率 (Dimensionless eigenfrequency) $[\text{無單位}]$，$\hat{\nu}_{mnr} = \nu_{mnr}/\left(2\Omega\right)$
  * $\mathbf{K}_{mnr} = \left(U_{mnr},\ V_{mnr},\ \Phi_{mnr}\right)^{\mathsf{T}}$ : 本徵函數 (Eigenfunction) $[\text{依分量而定}]$
  * $\hat{y}$ : 無因次經向座標 (Dimensionless meridional coordinate) $[\text{無單位}]$
  * $\mathcal{H}_n$ : 歸一化 Hermite 函數 (Normalized Hermite function) $[\text{無單位}]$
  * $i$ : 虛數單位 (Imaginary unit) $[\text{無單位}]$，$i^{2} = -1$
  * $m$ : 緯向波數 (Zonal wavenumber) $[\text{無單位}]$，整數

* **【已知 5】 [垂直速度的診斷關係 (Diagnostic relation for the vertical velocity)](https://derek1403.github.io/Theory_Playground/_build/html/01_Derivations/Equatorial_Beta_Plane_Dynamics/Fourier_Transform_to_Shallow_Water_System.html#d-proof-diagnostic-recovery-of-the-vertical-velocity)：** 垂直速度不是預報量而是診斷量：它由水平輻散除以分離常數 $\lambda$ 直接給出，因此只要 $\hat{u}_m$ 與 $\hat{v}_m$ 定了，$\hat{w}_m$ 就跟著定了。（已於本庫 [Fourier Transform to the Shallow Water System](Fourier_Transform_to_Shallow_Water_System.md)【證明 (d)】完整證明，此處直接引用。）

  $$\hat{w}_m = \frac{1}{\lambda}\left(\frac{im}{a}\hat{u}_m + \frac{d\hat{v}_m}{dy}\right)$$

  * $\hat{w}$ : 擾動對數氣壓垂直速度的水平結構函數 (Horizontal structure function of the perturbation log-pressure vertical velocity) $[\text{s}^{-1}]$
  * $m$ : 緯向波數 (Zonal wavenumber) $[\text{無單位}]$，整數
  * $\lambda$ : 第一內模態的分離常數 (Separation constant) $[\text{無單位}]$
  * $a$ : 地球半徑 (Earth's radius) $[\text{m}]$
  * $\hat{u},\ \hat{v}$ : 緯向、經向風的水平結構函數 (Horizontal structure functions of the velocities) $[\text{m}\cdot\text{s}^{-1}]$
  * $y$ : 經向座標，以赤道為原點 (Meridional coordinate) $[\text{m}]$

* **【假設 1】 級數可逐項微分 (Term-by-term differentiation of the series)：** 展開式在物理空間收斂夠好，微分算子可與兩層求和交換

  $$\frac{\partial}{\partial s}\left[\sum_{m}\sum_{n,r}\left(\cdot\right)\right] = \sum_{m}\sum_{n,r}\frac{\partial}{\partial s}\left(\cdot\right) \qquad \left(s = \xi,\ y,\ z\right)$$

  * $s$ : 積分變數 (Integration variable) $[\text{依應用而定}]$
  * $m$ : 緯向波數 (Zonal wavenumber) $[\text{無單位}]$，整數
  * $\xi$ : 隨波緯向座標 (Translating zonal coordinate) $[\text{m}]$
  * $y$ : 經向座標，以赤道為原點 (Meridional coordinate) $[\text{m}]$
  * $z$ : 對數氣壓垂直座標 (Log-pressure vertical coordinate) $[\text{無單位}]$
  * $n$ : 經向模態指標 (Meridional mode index) $[\text{無單位}]$
  * $r$ : 波型指標 (Wave-type index) $[\text{無單位}]$

* **【假設 2】 頻率不為零 (Nonzero eigenfrequency)：** 【推導 2】要除以 $\nu_{mnr}$

  $$\nu_{mnr} \neq 0$$

  * $\nu_{mnr}$ : 本徵頻率 (Eigenfrequency) $[\text{s}^{-1}]$，實數
  * $m$ : 緯向波數 (Zonal wavenumber) $[\text{無單位}]$，整數
  * $n$ : 經向模態指標 (Meridional mode index) $[\text{無單位}]$
  * $r$ : 波型指標 (Wave-type index) $[\text{無單位}]$
  * 註：唯一的例外是緯向對稱的羅斯貝模態（$m = 0$、$n > 0$、$r = 0$）。那些模態由 [赤道波本徵函數](Equatorial_Wave_Eigenfunctions.md)【證明 (f)】可知是地轉平衡的定常緯向流，其 PV 需另外由【已知 2】(a) 直接計算。

* **【定義 1】 位渦的譜係數 (Spectral coefficient of the PV)：** 位渦場在 $\left(m, n, r\right)$ 模態上的振幅

  $$\hat{q}_{mnr} \overset{\text{def}}{=} \text{位渦場中對應於 } \mathcal{H}_n(\hat{y})e^{im\xi/a}Z(z) \text{ 的係數}$$

  * $\hat{q}_{mnr}$ : 位渦的譜係數 (Spectral PV coefficient) $[\text{s}^{-1}]$
  * $\mathcal{H}_n$ : 歸一化 Hermite 函數 (Normalized Hermite function) $[\text{無單位}]$
  * $\hat{y}$ : 無因次經向座標 (Dimensionless meridional coordinate) $[\text{無單位}]$
  * $\xi$ : 隨波緯向座標 (Translating zonal coordinate) $[\text{m}]$
  * $a$ : 地球半徑 (Earth's radius) $[\text{m}]$
  * $Z(z)$ : 垂直結構函數 (Vertical structure function) $[\text{無單位}]$
  * $z$ : 對數氣壓垂直座標 (Log-pressure vertical coordinate) $[\text{無單位}]$

* **【推導 1】 位渦在垂直分離後的形式 (PV after the vertical separation)：** $\left(\dfrac{\partial}{\partial z} - 1\right)\dfrac{\partial\phi}{\partial z}$ 這一串被垂直結構方程式換成 $-\lambda\hat{\phi}Z$

  $$\begin{gather*}
  q &\overset{\text{已知 2(a)}}{=}& \frac{\partial v}{\partial x} - \frac{\partial u}{\partial y} + \frac{\beta y}{R\Gamma}\left(\frac{\partial}{\partial z} - 1\right)\frac{\partial \phi}{\partial z} \\
  &\overset{\text{已知 1(c)}}{=}& \left[\frac{\partial \hat{v}}{\partial x} - \frac{\partial \hat{u}}{\partial y}\right]Z + \frac{\beta y}{R\Gamma}\hat{\phi}\left(\frac{d}{dz} - 1\right)\frac{dZ}{dz} \\
  &\overset{\text{已知 2(b)}}{=}& \left[\frac{\partial \hat{v}}{\partial x} - \frac{\partial \hat{u}}{\partial y}\right]Z - \frac{\lambda\,\beta y}{R\Gamma}\hat{\phi}\,Z \\
  &\overset{\text{已知 2(c)}}{=}& \left[\frac{\partial \hat{v}}{\partial x} - \frac{\partial \hat{u}}{\partial y} - \frac{\beta y}{\bar{c}^{2}}\hat{\phi}\right]Z
  \end{gather*}$$

  * $q$ : 位渦距平 (PV anomaly) $[\text{s}^{-1}]$
  * $v$ : 擾動經向風速 (Perturbation meridional velocity) $[\text{m}\cdot\text{s}^{-1}]$
  * $x,\ y$ : 緯向、經向座標 (Zonal and meridional coordinates) $[\text{m}]$
  * $u,\ v$ : 擾動緯向、經向風速 (Perturbation velocities) $[\text{m}\cdot\text{s}^{-1}]$
  * $y$ : 經向座標，以赤道為原點 (Meridional coordinate) $[\text{m}]$
  * $\beta$ : 赤道 $\beta$ 參數 (Equatorial beta parameter) $[\text{m}^{-1}\cdot\text{s}^{-1}]$
  * $R$ : 乾空氣氣體常數 (Gas constant for dry air) $[\text{J}\cdot\text{kg}^{-1}\cdot\text{K}^{-1}]$
  * $\Gamma$ : 靜力穩定度 (Static stability) $[\text{K}]$
  * $z$ : 對數氣壓垂直座標 (Log-pressure vertical coordinate) $[\text{無單位}]$
  * $\phi$ : 擾動位勢 (Perturbation geopotential) $[\text{m}^{2}\cdot\text{s}^{-2}]$
  * $\hat{u},\ \hat{v}$ : 緯向、經向風的水平結構函數 (Horizontal structure functions of the velocities) $[\text{m}\cdot\text{s}^{-1}]$
  * $Z(z)$ : 垂直結構函數 (Vertical structure function) $[\text{無單位}]$
  * $Z'$ : 垂直結構函數 $Z$ 對 $z$ 的一階微分 (First derivative of the vertical structure function with respect to $z$) $[\text{無單位}]$，$Z' = \dfrac{dZ}{dz}$
  * $\hat{\phi}$ : 擾動位勢的水平結構函數 (Horizontal structure function of the perturbation geopotential) $[\text{m}^{2}\cdot\text{s}^{-2}]$
  * $\lambda$ : 第一內模態的分離常數 (Separation constant) $[\text{無單位}]$
  * $\bar{c}$ : 等效重力波速 (Equivalent gravity wave speed) $[\text{m}\cdot\text{s}^{-1}]$
  * 註：**位渦與 $u, v, \phi$ 掛在同一個 $Z(z)$ 上**（不是 $Z'$）。這就是【證明 (b)】的 $q$ 也帶著 $Z(z)$ 的原因，也是 $q$ 在對流層上下層反號的原因。

* **【推導 2】 單一模態的位渦（關鍵恆等式）(PV of a single mode — the key identity)：** 把三條本徵方程式組合起來，$\Phi$ 與 $\dfrac{dV}{dy}$ 全部對消，只剩 $\beta V$

  * (a) 令 $\mathcal{Q}_{mnr}$ 為單一模態的位渦結構函數：

    $$\mathcal{Q}_{mnr} \overset{\text{let}}{=} \frac{im}{a}V_{mnr} - \frac{dU_{mnr}}{dy} - \frac{\beta y}{\bar{c}^{2}}\Phi_{mnr}$$

  * (b) 三項各自乘上 $i\nu_{mnr}$ 後用【已知 3】換掉：

    $$\begin{gather*}
    i\nu_{mnr}\,\frac{im}{a}V_{mnr} &\overset{\text{已知 3(b)}}{=}& \frac{im}{a}\left[\beta y\,U_{mnr} + \frac{d\Phi_{mnr}}{dy}\right] \\
    i\nu_{mnr}\,\frac{dU_{mnr}}{dy} &\overset{\text{已知 3(a)}}{=}& \frac{d}{dy}\left[-\beta y\,V_{mnr} + \frac{im}{a}\Phi_{mnr}\right] \\
    i\nu_{mnr}\,\frac{dU_{mnr}}{dy} &=& -\beta V_{mnr} - \beta y\frac{dV_{mnr}}{dy} + \frac{im}{a}\frac{d\Phi_{mnr}}{dy} \\
    i\nu_{mnr}\,\frac{\beta y}{\bar{c}^{2}}\Phi_{mnr} &\overset{\text{已知 3(c)}}{=}& \beta y\left[\frac{im}{a}U_{mnr} + \frac{dV_{mnr}}{dy}\right]
    \end{gather*}$$

  * (c) 三項相減，除了 $\beta V_{mnr}$ 之外全數對消：

    $$\begin{gather*}
    i\nu_{mnr}\,\mathcal{Q}_{mnr} &\overset{\text{推導 2(a)(b)}}{=}& \frac{im}{a}\beta y\,U_{mnr} + \frac{im}{a}\frac{d\Phi_{mnr}}{dy} + \beta V_{mnr} + \beta y\frac{dV_{mnr}}{dy} - \frac{im}{a}\frac{d\Phi_{mnr}}{dy} - \frac{im}{a}\beta y\,U_{mnr} - \beta y\frac{dV_{mnr}}{dy} \\
    i\nu_{mnr}\,\mathcal{Q}_{mnr} &=& \beta V_{mnr} \\
    \mathcal{Q}_{mnr} &\overset{\text{假設 2}}{=}& \frac{\beta V_{mnr}}{i\nu_{mnr}}
    \end{gather*}$$

  * $\mathcal{Q}_{mnr}$ : 單一模態的位渦結構函數 (PV structure function of a single mode) $[\text{s}^{-1}]$
  * $m$ : 緯向波數 (Zonal wavenumber) $[\text{無單位}]$，整數
  * $n$ : 經向模態指標 (Meridional mode index) $[\text{無單位}]$
  * $r$ : 波型指標 (Wave-type index) $[\text{無單位}]$
  * $a$ : 地球半徑 (Earth's radius) $[\text{m}]$
  * $\mathbf{K}_{mnr} = \left(U_{mnr},\ V_{mnr},\ \Phi_{mnr}\right)^{\mathsf{T}}$ : 本徵函數 (Eigenfunction) $[\text{依分量而定}]$
  * $U,\ V$ : 本徵函數的速度分量 (Velocity components of the eigenfunction) $[\text{無單位}]$
  * $y$ : 經向座標，以赤道為原點 (Meridional coordinate) $[\text{m}]$
  * $\beta$ : 赤道 $\beta$ 參數 (Equatorial beta parameter) $[\text{m}^{-1}\cdot\text{s}^{-1}]$
  * $\bar{c}$ : 等效重力波速 (Equivalent gravity wave speed) $[\text{m}\cdot\text{s}^{-1}]$
  * $\nu_{mnr}$ : 本徵頻率 (Eigenfrequency) $[\text{s}^{-1}]$，實數
  * $i$ : 虛數單位 (Imaginary unit) $[\text{無單位}]$，$i^{2} = -1$

* **【推導 3】 位渦結構函數的顯式 (Explicit form of the PV structure function)：** 把【已知 4】(a) 代進【推導 2】(c)

  $$\begin{gather*}
  \mathcal{Q}_{mnr} &\overset{\text{推導 2(c)}}{=}& \frac{\beta}{i\nu_{mnr}}V_{mnr} \\
  &\overset{\text{已知 4(a)}}{=}& \frac{\beta}{i\nu_{mnr}}\left(-i\right)A_{mnr}\left(\epsilon\hat{\nu}_{mnr}^{2} - m^{2}\right)\mathcal{H}_n \\
  &=& \frac{\beta}{\nu_{mnr}}A_{mnr}\left(m^{2} - \epsilon\hat{\nu}_{mnr}^{2}\right)\mathcal{H}_n \\
  &\overset{\text{已知 4}}{=}& \frac{2\Omega/a}{2\Omega\hat{\nu}_{mnr}}A_{mnr}\left(m^{2} - \epsilon\hat{\nu}_{mnr}^{2}\right)\mathcal{H}_n \\
  &=& A_{mnr}\left(\frac{m^{2} - \epsilon\hat{\nu}_{mnr}^{2}}{a\,\hat{\nu}_{mnr}}\right)\mathcal{H}_n
  \end{gather*}$$

  * $\mathcal{Q}_{mnr}$ : 單一模態的位渦結構函數 (PV structure function of a single mode) $[\text{s}^{-1}]$
  * $m$ : 緯向波數 (Zonal wavenumber) $[\text{無單位}]$，整數
  * $n$ : 經向模態指標 (Meridional mode index) $[\text{無單位}]$
  * $r$ : 波型指標 (Wave-type index) $[\text{無單位}]$
  * $\beta$ : 赤道 $\beta$ 參數 (Equatorial beta parameter) $[\text{m}^{-1}\cdot\text{s}^{-1}]$
  * $\nu_{mnr}$ : 本徵頻率 (Eigenfrequency) $[\text{s}^{-1}]$，實數
  * $\mathbf{K}_{mnr} = \left(U_{mnr},\ V_{mnr},\ \Phi_{mnr}\right)^{\mathsf{T}}$ : 本徵函數 (Eigenfunction) $[\text{依分量而定}]$
  * $A_{mnr}$ : 歸一化常數 (Normalization constant) $[\text{無單位}]$
  * $\epsilon$ : Lamb 參數 (Lamb's parameter) $[\text{無單位}]$
  * $\hat{\nu}_{mnr}$ : 無因次本徵頻率 (Dimensionless eigenfrequency) $[\text{無單位}]$，$\hat{\nu}_{mnr} = \nu_{mnr}/\left(2\Omega\right)$
  * $\mathcal{H}_n$ : 歸一化 Hermite 函數 (Normalized Hermite function) $[\text{無單位}]$
  * $\Omega$ : 地球自轉角速度 (Earth's angular velocity) $[\text{s}^{-1}]$
  * $a$ : 地球半徑 (Earth's radius) $[\text{m}]$
  * $i$ : 虛數單位 (Imaginary unit) $[\text{無單位}]$，$i^{2} = -1$

+++

## 證明:

### (a) proof 風場與質量場的還原 (Recovery of the wind and mass fields)

三層轉換各自反轉：正規模態、緯向傅立葉、垂直結構。

$$\begin{gather*}
\begin{pmatrix}u \cr v \cr \phi\end{pmatrix} &\overset{\text{已知 1(c)}}{=}& \hat{\boldsymbol{\eta}}\left(\xi, y\right)Z(z) \\
&\overset{\text{已知 1(b)}}{=}& Z(z)\sum_{m = -\infty}^{\infty}\hat{\boldsymbol{\eta}}_m(\hat{y})\,e^{im\xi/a} \\
&\overset{\text{已知 1(a)}}{=}& Z(z)\sum_{m = -\infty}^{\infty}\sum_{n = -1}^{\infty}\sum_{r}\hat{\eta}_{mnr}\begin{pmatrix}U_{mnr}(\hat{y}) \cr V_{mnr}(\hat{y}) \cr \Phi_{mnr}(\hat{y})\end{pmatrix}e^{im\xi/a}
\end{gather*}$$

### (b) proof 位渦場的還原 (Recovery of the potential vorticity field)

把【證明 (a)】代進【推導 1】的括號裡，每個模態的貢獻由【推導 2】(a) 的 $\mathcal{Q}_{mnr}$ 給出，再由【推導 3】換成 $\mathcal{H}_n$。

$$\begin{gather*}
q &\overset{\text{推導 1}}{=}& \left[\frac{\partial \hat{v}}{\partial x} - \frac{\partial \hat{u}}{\partial y} - \frac{\beta y}{\bar{c}^{2}}\hat{\phi}\right]Z(z) \\
&\overset{\text{證明 (a),假設 1}}{=}& Z(z)\sum_{m}\sum_{n, r}\hat{\eta}_{mnr}\left[\frac{im}{a}V_{mnr} - \frac{dU_{mnr}}{dy} - \frac{\beta y}{\bar{c}^{2}}\Phi_{mnr}\right]e^{im\xi/a} \\
&\overset{\text{推導 2(a)}}{=}& Z(z)\sum_{m}\sum_{n, r}\hat{\eta}_{mnr}\,\mathcal{Q}_{mnr}\,e^{im\xi/a} \\
&\overset{\text{推導 3}}{=}& Z(z)\sum_{m}\sum_{n, r}\hat{\eta}_{mnr}A_{mnr}\left(\frac{m^{2} - \epsilon\hat{\nu}_{mnr}^{2}}{a\,\hat{\nu}_{mnr}}\right)\mathcal{H}_n(\hat{y})\,e^{im\xi/a}
\end{gather*}$$

### (c) proof 位渦的譜係數 (Spectral coefficient of the PV)

對照【證明 (b)】與【定義 1】即得。

$$\hat{q}_{mnr} \overset{\text{定義 1,證明 (b)}}{=} A_{mnr}\left(\frac{m^{2} - \epsilon\hat{\nu}_{mnr}^{2}}{a\,\hat{\nu}_{mnr}}\right)\hat{\eta}_{mnr}$$

### (d) proof Kelvin 波的位渦為零 (Zero potential vorticity of the Kelvin wave)

Kelvin 波的頻散關係讓【證明 (c)】分子的括號**精確**歸零。

$$\begin{gather*}
m^{2} - \epsilon\hat{\nu}_{m,-1,2}^{2} &\overset{\text{已知 4(b)}}{=}& m^{2} - \epsilon\left(\frac{m}{\epsilon^{1/2}}\right)^{2} \\
m^{2} - \epsilon\hat{\nu}_{m,-1,2}^{2} &=& m^{2} - m^{2} \\
m^{2} - \epsilon\hat{\nu}_{m,-1,2}^{2} &=& 0 \\
\hat{q}_{m,-1,2} &\overset{\text{證明 (c)}}{=}& A_{m,-1,2}\cdot\frac{0}{a\,\hat{\nu}_{m,-1,2}}\cdot\hat{\eta}_{m,-1,2} \\
\hat{q}_{m,-1,2} &=& 0
\end{gather*}$$

### (e) proof 垂直速度的還原 (Recovery of the vertical velocity)

診斷關係中的括號恰好是【已知 3】(c) 的左端，可直接換成 $i\nu\Phi/\bar{c}^{2}$；再用 $\lambda\bar{c}^{2} = R\Gamma$ 收尾。

$$\begin{gather*}
w &\overset{\text{已知 1(c)}}{=}& \hat{w}\left(\xi, y\right)Z'(z) \\
&\overset{\text{已知 1(b),已知 5}}{=}& Z'(z)\sum_{m}\frac{1}{\lambda}\left[\frac{im}{a}\hat{u}_m + \frac{d\hat{v}_m}{dy}\right]e^{im\xi/a} \\
&\overset{\text{已知 1(a),假設 1}}{=}& \frac{Z'(z)}{\lambda}\sum_{m}\sum_{n, r}\hat{\eta}_{mnr}\left[\frac{im}{a}U_{mnr} + \frac{dV_{mnr}}{dy}\right]e^{im\xi/a} \\
&\overset{\text{已知 3(c)}}{=}& \frac{Z'(z)}{\lambda\bar{c}^{2}}\sum_{m}\sum_{n, r}i\nu_{mnr}\hat{\eta}_{mnr}\,\Phi_{mnr}(\hat{y})\,e^{im\xi/a} \\
&\overset{\text{已知 2(c)}}{=}& \frac{Z'(z)}{R\Gamma}\sum_{m}\sum_{n, r}i\nu_{mnr}\hat{\eta}_{mnr}\,\Phi_{mnr}(\hat{y})\,e^{im\xi/a}
\end{gather*}$$

+++

## 物理解釋

### 為什麼 PV 只剩單一個 $\mathcal{H}_n$

$u, v, \phi$ 每一個模態都是 $\mathcal{H}_{n+1}$、$\mathcal{H}_n$、$\mathcal{H}_{n-1}$ 三個函數的混合（見 [赤道波本徵函數](Equatorial_Wave_Eigenfunctions.md)【證明 (a)】）。但【證明 (b)】說 **PV 只剩中間那一個 $\mathcal{H}_n$**。

原因藏在【推導 2】：三條本徵方程式組合之後，$\Phi_{mnr}$ 與 $\dfrac{dV_{mnr}}{dy}$ 全部對消，只剩 $\beta V_{mnr}$ —— 而 $V_{mnr}$ 本來就只含 $\mathcal{H}_n$。

**PV 是一個「乾淨」的變數**：它把每個模態的三重結構壓成單一階。這正是它適合當診斷量、也適合當可逆性原理的輸入的原因。

### 那個「精確為零」有多硬

【證明 (d)】不是「很小」，是**代數恆等式**。Kelvin 波的頻散關係 $\epsilon^{1/2}\hat{\nu} = m$ 一代進去，$m^{2} - \epsilon\hat{\nu}^{2}$ 就是零，沒有任何近似。

它的物理意義是：**Kelvin 波在赤道 $\beta$ 平面上是純重力波，不攜帶任何位渦。** 這件事的後果非常嚴重：

| 場 | Kelvin 波有沒有貢獻？ |
|---|---|
| $u,\ \phi$（對流**東側**的主要流型） | **有**（而且是主導） |
| $q$ | **完全沒有** |

於是任何「從 $q$ 出發反演流場」的方法 —— 也就是 [可逆性原理](Equatorial_PV_Invertibility_Principle.md) —— **註定救不回對流東側的流場**。論文在 §6 誠實地記錄了這一點：反演解與原始方程解最明顯的差異，就是「赤道上的緯向氣壓梯度力沒有被重現」。

**這不是近似不夠好，而是資訊在 $q$ 這個變數裡根本不存在。**

### 慣性重力波的 PV：赤道與中緯度的差別

中緯度 $f$ 平面上，慣性重力波的 PV **嚴格為零**。赤道 $\beta$ 平面上**不是** —— 由【證明 (c)】，只要 $m^{2} \neq \epsilon\hat{\nu}^{2}$，PV 就不為零。

但論文指出它的貢獻**很小**，而且理由可以從【證明 (c)】直接讀出來：

$$\hat{q}_{mnr} \propto \frac{m^{2} - \epsilon\hat{\nu}_{mnr}^{2}}{\hat{\nu}_{mnr}}$$

對慣性重力波而言，$m$ 增大時 $\left|m^{2} - \epsilon\hat{\nu}_{mnr}^{2}\right|$ **變小**、$\left|\hat{\nu}_{mnr}\right|$ **變大** —— **分子小、分母大，兩頭夾殺**。所以 PV 場實際上「幾乎全部由羅斯貝波貢獻」，這也是論文連 PV 的波模分解圖都省了的原因。

### 端點①到此完成

三個公式合起來，就是完整的解：

1. [移動熱源的模態投影](Projection_of_a_Moving_Heat_Source.md)【證明 (c)(d)】給出 $\hat{Q}_{mnr}$；
2. [受迫解](Forced_Response_of_Equatorial_Modes.md)【證明 (c)】一行除法給出 $\hat{\eta}_{mnr}$；
3. 本篇【證明 (a)(b)(e)】把它們轉回 $u, v, \phi, q, w$。

論文的數值實作就是照這三步做的：對 $m$ 求和（緯向波數）、對 $n$ 求和（經向模態，截斷在 $N = 200$）、對 $r$ 求和（波型）。$n$ 的截斷之所以安全，理由在 [移動熱源的模態投影](Projection_of_a_Moving_Heat_Source.md) 的 $\chi^{n/2} \approx 0.894^{n/2}$ 指數衰減。
