# Matsuno Dispersion Relation (Matsuno 頻散關係的記法對照與特例)

+++

## 證明目標:

赤道波的頻散關係**已在 Advanced Atmospheric Dynamics 的 [project2_1](https://derek1403.github.io/PC-NTU/Advanced-Atmospheric-Dynamics/_build/html/project/project2/project2_1.html) 完整證明過**，
本篇**不重證**，只做三件事：記法對照、尺度還原、以及兩個必須特別處理的特例。

* (a) project2_1 的全無因次頻散關係，經 $\omega = \epsilon^{1/4}\hat{\nu}$、$k = \epsilon^{-1/4}m$ 還原後，就是 Schubert 的形式：

$$\epsilon\hat{\nu}^{2} - m^{2} - \frac{m}{\hat{\nu}} = \epsilon^{1/2}\left(2n + 1\right)$$

* (b) $n = 0$ 時三次式可因式分解，且其中一根必須捨棄：

$$\left(\epsilon^{1/2}\hat{\nu} + m\right)\left(\epsilon^{1/2}\hat{\nu}^{2} - m\hat{\nu} - 1\right) = 0$$

* (c) Kelvin 波（令 $V = 0$ 單獨求得）的本徵值，可形式上視為 (a) 在 $n = -1$ 的解：

$$\epsilon^{1/2}\hat{\nu} = m$$

其中

* $\hat{\nu}$ : Schubert 記法的無因次頻率 (Dimensionless frequency) $[\text{無單位}]$
* $\omega$ : 無因次頻率 (Dimensionless frequency) $[\text{無單位}]$
* $k$ : 無因次緯向波數 (Dimensionless zonal wavenumber) $[\text{無單位}]$
* $U,\ V$ : 本徵函數的速度分量 (Velocity components of the eigenfunction) $[\text{無單位}]$
* $m$ : 緯向波數 (Zonal wavenumber) $[\text{無單位}]$，整數
* $n$ : 經向模態指標 (Meridional mode index) $[\text{無單位}]$
* $\epsilon$ : Lamb 參數 (Lamb's parameter) $[\text{無單位}]$，$\epsilon \approx 507.3$
* 註：(a)–(c) 對應 [Schubert & Masarik (2006)](../../06_References/Tropical_wave_dynamics/Schubert2006-Potential_vorticity_aspects_of_the_MJO/Potential_vorticity_aspects_of_the_MJO.ipynb) 的 $(4.10)$ 及其後的討論。
* 註：**本篇是整條推導鏈中唯一的「記法橋樑」**，被 [赤道波本徵函數](Equatorial_Wave_Eigenfunctions.md)、[受迫解](Forced_Response_of_Equatorial_Modes.md)、[場還原與 Kelvin 波零 PV](Physical_Field_Recovery_and_Zero_Kelvin_PV.md)、[平衡頻散關係](Balanced_Rossby_Dispersion_Relation.md) 四篇引用。取消它的話那四篇各自都要重寫一次對照。
* 註：$(2n+1)$ 這個「量子化」的來源是 Weber 方程式的有界性要求（Hermite 函數的階數必須是非負整數），已在 project2_1 證過；其數學根源見本庫 [Hermite 函數的正交歸一性與諧振子本徵值](../Differential_Equations/Hermite_Orthonormality_and_Oscillator_Eigenvalue.md)【證明 (a)】的 $-(2n+1)$。

+++

## 假設與已知 (Assumptions & Preliminaries)

* **【已知 1】 [赤道 $\beta$ 平面無因次淺水方程的頻散關係 (Dispersion relation of the nondimensional equatorial shallow water equations)](https://derek1403.github.io/PC-NTU/Advanced-Atmospheric-Dynamics/_build/html/project/project2/project2_1.html)：** 赤道 $\beta$ 平面淺水系統的頻散關係（project2_1 記法）：頻率與緯向波數被一條三次方程綁在一起，右端的 $2n$ 來自經向 Hermite 模態的量子化。本篇要做的就是把它翻譯成 Schubert 的無因次記法。（已於 Advanced Atmospheric Dynamics 的 project2_1 完整證明，含 Weber 方程式、Hermite 量子化與本徵函數；此處直接引用。）

  $$\omega^{2} - k^{2} - \frac{k}{\omega} - 1 = 2n \qquad \left(n = 0,\ 1,\ 2,\ \ldots\right)$$

  * $\omega$ : 無因次頻率 (Dimensionless frequency) $[\text{無單位}]$
  * $k$ : 無因次緯向波數 (Dimensionless zonal wavenumber) $[\text{無單位}]$
  * $n$ : 經向模態指標 (Meridional mode index) $[\text{無單位}]$
  * 註：project2_1 的無因次化取赤道變形半徑 $L_e = \left(\bar{c}/\beta\right)^{1/2}$ 為長度尺度、$T_e = \left(\beta\bar{c}\right)^{-1/2}$ 為時間尺度。

* **【已知 2】 [線性算符 $\mathcal{L}$ 與其本徵值問題 (Linear operator and its eigenvalue problem)](https://derek1403.github.io/Theory_Playground/_build/html/01_Derivations/Equatorial_Beta_Plane_Dynamics/Fourier_Transform_to_Shallow_Water_System.html#e-proof-vector-form)：** 水平結構方程組的算符形式與它的本徵值問題：$\mathcal{L}$ 作用在本徵函數 $\mathbf{K}_{mnr}$ 上等於 $i\nu_{mnr}$ 乘回自己，本徵值為純虛數 ─ 這保證模態是不增不減的振盪，而頻散關係就是這個本徵值問題的可解條件。（已於本庫 [Fourier Transform to the Shallow Water System](Fourier_Transform_to_Shallow_Water_System.md) 完整證明，此處直接引用。）

  * (a) 算符本身：

    $$\mathcal{L} = \begin{pmatrix} 0 & -\beta y & \dfrac{im}{a} \cr \beta y & 0 & \dfrac{d}{dy} \cr \bar{c}^{2}\dfrac{im}{a} & \bar{c}^{2}\dfrac{d}{dy} & 0 \end{pmatrix}$$

  * (b) 本徵值問題（本徵值由 [能量內積與反厄米性](Energy_Inner_Product_and_Skew_Hermitian_Operator.md)【證明 (e)】保證為純虛數 $i\nu$）：

    $$\mathcal{L}\mathbf{K}_{mnr} = i\nu_{mnr}\mathbf{K}_{mnr}, \qquad \mathbf{K}_{mnr}(\hat{y}) = \begin{pmatrix}U_{mnr} \cr V_{mnr} \cr \Phi_{mnr}\end{pmatrix}$$

  * $\mathbf{K}_{mnr}$ : 第 $(m, n, r)$ 個本徵函數 (Eigenfunction) $[\text{依分量而定}]$
  * $\nu_{mnr}$ : 第 $(m, n, r)$ 個本徵頻率 (Eigenfrequency) $[\text{s}^{-1}]$，實數
  * $r$ : 三次式三個根的指標 (Root index) $[\text{無單位}]$，$r = 0, 1, 2$
  * $\bar{c}$ : 等效重力波速 (Equivalent gravity wave speed) $[\text{m}\cdot\text{s}^{-1}]$，$\bar{c} \approx 41.25 \ \text{m}\cdot\text{s}^{-1}$
  * $m$ : 緯向波數 (Zonal wavenumber) $[\text{無單位}]$，整數
  * $a$ : 地球半徑 (Earth's radius) $[\text{m}]$
  * $\beta$ : 赤道 $\beta$ 參數 (Equatorial beta parameter) $[\text{m}^{-1}\cdot\text{s}^{-1}]$，$\beta = 2\Omega/a$
  * $\mathcal{L}$ : 水平結構的線性算符 (Linear operator) $[\text{s}^{-1}]$
  * $y$ : 經向座標，以赤道為原點 (Meridional coordinate) $[\text{m}]$
  * $\hat{y}$ : 無因次經向座標 (Dimensionless meridional coordinate) $[\text{無單位}]$
  * $U,\ V$ : 本徵函數的速度分量 (Velocity components of the eigenfunction) $[\text{無單位}]$
  * $\Phi$ : 本徵函數的位勢分量 (Geopotential component) $[\text{m}\cdot\text{s}^{-1}]$
  * $i$ : 虛數單位 (Imaginary unit) $[\text{無單位}]$，$i^{2} = -1$

* **【已知 3】 [Lamb 參數與無因次經向座標 (Lamb's parameter and dimensionless meridional coordinate)](https://derek1403.github.io/Theory_Playground/_build/html/01_Derivations/Equatorial_Beta_Plane_Dynamics/Energy_Inner_Product_and_Skew_Hermitian_Operator.html#assumptions-preliminaries)：** 兩個把問題無因次化的量：$\epsilon$ 量度旋轉相對於層結的強弱，$\hat{y}$ 則以赤道變形半徑為長度單位 ─ 本篇的記法換算全靠這兩個定義。（已於本庫 [Energy Inner Product and the Skew-Hermitian Operator](Energy_Inner_Product_and_Skew_Hermitian_Operator.md)【定義 2】給出，此處直接引用。）

  $$\epsilon = \frac{4\Omega^{2}a^{2}}{\bar{c}^{2}}, \qquad \hat{y} = \left(\frac{\beta}{\bar{c}}\right)^{1/2}y = \epsilon^{1/4}\frac{y}{a}$$

  * $\epsilon$ : Lamb 參數 (Lamb's parameter) $[\text{無單位}]$，$\epsilon \approx 507.3$
  * $\hat{y}$ : 無因次經向座標 (Dimensionless meridional coordinate) $[\text{無單位}]$
  * $\Omega$ : 地球自轉角速度 (Earth's angular velocity) $[\text{s}^{-1}]$
  * $a$ : 地球半徑 (Earth's radius) $[\text{m}]$
  * $\bar{c}$ : 等效重力波速 (Equivalent gravity wave speed) $[\text{m}\cdot\text{s}^{-1}]$，$\bar{c} \approx 41.25 \ \text{m}\cdot\text{s}^{-1}$
  * $\beta$ : 赤道 $\beta$ 參數 (Equatorial beta parameter) $[\text{m}^{-1}\cdot\text{s}^{-1}]$，$\beta = 2\Omega/a$
  * $y$ : 經向座標，以赤道為原點 (Meridional coordinate) $[\text{m}]$

* **【假設 1】 赤道捕捉（有界性）(Equatorial trapping / boundedness)：** 只接受在 $\hat{y} \to \pm\infty$ 時歸零的解；發散的解不是物理解，必須捨棄

  $$\lim_{\left|\hat{y}\right| \to \infty}\mathbf{K}_{mnr}(\hat{y}) = 0$$

  * $\hat{y}$ : 無因次經向座標 (Dimensionless meridional coordinate) $[\text{無單位}]$
  * $\mathbf{K}_{mnr}$ : 第 $(m, n, r)$ 個本徵函數 (Eigenfunction) $[\text{依分量而定}]$
  * $m$ : 緯向波數 (Zonal wavenumber) $[\text{無單位}]$，整數
  * $n$ : 經向模態指標 (Meridional mode index) $[\text{無單位}]$
  * $r$ : 三次式三個根的指標 (Root index) $[\text{無單位}]$，$r = 0, 1, 2$

* **【定義 1】 Schubert 記法的無因次頻率 (Dimensionless frequency in Schubert's notation)：** 以行星自轉頻率 $2\Omega$ 為尺度

  $$\hat{\nu} \overset{\text{def}}{=} \frac{\nu}{2\Omega}$$

  * $\hat{\nu}$ : Schubert 記法的無因次頻率 (Dimensionless frequency) $[\text{無單位}]$
  * $\nu_{mnr}$ : 第 $(m, n, r)$ 個本徵頻率 (Eigenfrequency) $[\text{s}^{-1}]$，實數
  * $\Omega$ : 地球自轉角速度 (Earth's angular velocity) $[\text{s}^{-1}]$

* **【推導 1】 兩套無因次化的換算 (Conversion between the two nondimensionalizations)：** project2_1 的 $(\omega, k)$ 與 Schubert 的 $(\hat{\nu}, m)$ 只差 $\epsilon^{1/4}$ 的冪次

  * (a) 頻率：

    $$\begin{gather*}
    \omega &\overset{\text{已知 1}}{=}& \nu\left(\beta\bar{c}\right)^{-1/2} \\
    &\overset{\text{已知 2}}{=}& \nu\left(\frac{2\Omega\bar{c}}{a}\right)^{-1/2} \\
    &\overset{\text{定義 1}}{=}& 2\Omega\hat{\nu}\left(\frac{a}{2\Omega\bar{c}}\right)^{1/2} \\
    &=& \hat{\nu}\left(\frac{4\Omega^{2}a^{2}}{\bar{c}^{2}}\cdot\frac{\bar{c}}{2\Omega a}\right)^{1/2} \\
    &\overset{\text{已知 3}}{=}& \hat{\nu}\left(\epsilon\cdot\epsilon^{-1/2}\right)^{1/2} \\
    &=& \epsilon^{1/4}\hat{\nu}
    \end{gather*}$$

  * (b) 緯向波數：

    $$\begin{gather*}
    k &\overset{\text{已知 1}}{=}& \frac{m}{a}\left(\frac{\bar{c}}{\beta}\right)^{1/2} \\
    &\overset{\text{已知 2}}{=}& \frac{m}{a}\left(\frac{a\bar{c}}{2\Omega}\right)^{1/2} \\
    &=& m\left(\frac{\bar{c}}{2\Omega a}\right)^{1/2} \\
    &\overset{\text{已知 3}}{=}& m\left(\epsilon^{-1/2}\right)^{1/2} \\
    &=& \epsilon^{-1/4}m
    \end{gather*}$$

  * $\omega$ : 無因次頻率 (Dimensionless frequency) $[\text{無單位}]$
  * $\nu_{mnr}$ : 第 $(m, n, r)$ 個本徵頻率 (Eigenfrequency) $[\text{s}^{-1}]$，實數
  * $\beta$ : 赤道 $\beta$ 參數 (Equatorial beta parameter) $[\text{m}^{-1}\cdot\text{s}^{-1}]$，$\beta = 2\Omega/a$
  * $\bar{c}$ : 等效重力波速 (Equivalent gravity wave speed) $[\text{m}\cdot\text{s}^{-1}]$，$\bar{c} \approx 41.25 \ \text{m}\cdot\text{s}^{-1}$
  * $\Omega$ : 地球自轉角速度 (Earth's angular velocity) $[\text{s}^{-1}]$
  * $a$ : 地球半徑 (Earth's radius) $[\text{m}]$
  * $\hat{\nu}$ : Schubert 記法的無因次頻率 (Dimensionless frequency) $[\text{無單位}]$
  * $\epsilon$ : Lamb 參數 (Lamb's parameter) $[\text{無單位}]$，$\epsilon \approx 507.3$
  * $k$ : 無因次緯向波數 (Dimensionless zonal wavenumber) $[\text{無單位}]$
  * $m$ : 緯向波數 (Zonal wavenumber) $[\text{無單位}]$，整數
  * 註：(a) 第四列用到 $\dfrac{\bar{c}}{2\Omega a} = \epsilon^{-1/2}$，這是【已知 3】$\epsilon$ 定義的直接改寫。

* **【推導 2】 Kelvin 波的本徵問題 (Eigenvalue problem for the Kelvin wave)：** 在【已知 2】(b) 中令 $V = 0$，三條式子退化成兩條

  * (a) 第一分量（$V = 0$）：

    $$\begin{gather*}
    i\nu U &\overset{\text{已知 2(a)(b)}}{=}& -\beta y\cdot 0 + \frac{im}{a}\Phi \\
    \Phi &=& \frac{a\nu}{m}U
    \end{gather*}$$

  * (b) 第三分量（$V = 0$，故 $dV/dy = 0$）：

    $$\begin{gather*}
    i\nu\Phi &\overset{\text{已知 2(a)(b)}}{=}& \bar{c}^{2}\frac{im}{a}U + \bar{c}^{2}\frac{d}{dy}\left[0\right] \\
    \Phi &=& \frac{\bar{c}^{2}m}{a\nu}U
    \end{gather*}$$

  * (c) 第二分量（$V = 0$，故右端為零）：

    $$\begin{gather*}
    0 &\overset{\text{已知 2(a)(b)}}{=}& \beta y\,U + \frac{d\Phi}{dy} \\
    \frac{d\Phi}{dy} &=& -\beta y\,U
    \end{gather*}$$

  * $\nu_{mnr}$ : 第 $(m, n, r)$ 個本徵頻率 (Eigenfrequency) $[\text{s}^{-1}]$，實數
  * $U,\ V$ : 本徵函數的速度分量 (Velocity components of the eigenfunction) $[\text{無單位}]$
  * $\beta$ : 赤道 $\beta$ 參數 (Equatorial beta parameter) $[\text{m}^{-1}\cdot\text{s}^{-1}]$，$\beta = 2\Omega/a$
  * $y$ : 經向座標，以赤道為原點 (Meridional coordinate) $[\text{m}]$
  * $m$ : 緯向波數 (Zonal wavenumber) $[\text{無單位}]$，整數
  * $a$ : 地球半徑 (Earth's radius) $[\text{m}]$
  * $\Phi$ : 本徵函數的位勢分量 (Geopotential component) $[\text{m}\cdot\text{s}^{-1}]$
  * $\bar{c}$ : 等效重力波速 (Equivalent gravity wave speed) $[\text{m}\cdot\text{s}^{-1}]$，$\bar{c} \approx 41.25 \ \text{m}\cdot\text{s}^{-1}$
  * $i$ : 虛數單位 (Imaginary unit) $[\text{無單位}]$，$i^{2} = -1$

* **【推導 3】 Kelvin 波解的有界性篩選 (Boundedness selection for the Kelvin wave)：** 兩個根裡只有一個滿足【假設 1】

  * (a) 由【推導 2】(a)(b) 消去 $U$ 與 $\Phi$，得兩個根：

    $$\begin{gather*}
    \frac{a\nu}{m} &\overset{\text{推導 2(a)(b)}}{=}& \frac{\bar{c}^{2}m}{a\nu} \\
    \nu^{2} &=& \frac{\bar{c}^{2}m^{2}}{a^{2}} \\
    \nu &=& \pm\frac{\bar{c}m}{a}
    \end{gather*}$$

  * (b) 把 (a) 代進【推導 2】(c) 解出 $\Phi$ 的經向結構：

    $$\begin{gather*}
    \frac{d\Phi}{dy} &\overset{\text{推導 2(c)(a)}}{=}& -\beta y\frac{m}{a\nu}\Phi \\
    \frac{d\Phi}{dy} &\overset{\text{推導 3(a)}}{=}& \mp\frac{\beta y}{\bar{c}}\Phi \\
    \overset{\text{已知 3}}{\Rightarrow}\quad \Phi &\propto& \exp\left[\mp\frac{\hat{y}^{2}}{2}\right]
    \end{gather*}$$

  * (c) 取正號的根才有界：

    $$\begin{gather*}
    \nu &\overset{\text{假設 1,推導 3(b)}}{=}& +\frac{\bar{c}m}{a} \\
    \end{gather*}$$

  * $a$ : 地球半徑 (Earth's radius) $[\text{m}]$
  * $\nu_{mnr}$ : 第 $(m, n, r)$ 個本徵頻率 (Eigenfrequency) $[\text{s}^{-1}]$，實數
  * $m$ : 緯向波數 (Zonal wavenumber) $[\text{無單位}]$，整數
  * $\bar{c}$ : 等效重力波速 (Equivalent gravity wave speed) $[\text{m}\cdot\text{s}^{-1}]$，$\bar{c} \approx 41.25 \ \text{m}\cdot\text{s}^{-1}$
  * $\Phi$ : 本徵函數的位勢分量 (Geopotential component) $[\text{m}\cdot\text{s}^{-1}]$
  * $y$ : 經向座標，以赤道為原點 (Meridional coordinate) $[\text{m}]$
  * $\beta$ : 赤道 $\beta$ 參數 (Equatorial beta parameter) $[\text{m}^{-1}\cdot\text{s}^{-1}]$，$\beta = 2\Omega/a$
  * $\hat{y}$ : 無因次經向座標 (Dimensionless meridional coordinate) $[\text{無單位}]$
  * 註：(b) 最後一列是解一階可分離變數 ODE 的**巨大跳躍**，故用行首箭頭；過程為 $\dfrac{d\Phi}{\Phi} = \mp\dfrac{\beta y}{\bar{c}}dy$，兩側積分得 $\ln\Phi = \mp\dfrac{\beta y^{2}}{2\bar{c}}$，再用【已知 3】的 $\hat{y}^{2} = \dfrac{\beta}{\bar{c}}y^{2}$ 換掉。

+++

## 證明:

### (a) proof 記法對照與尺度還原 (Notation mapping and scale restoration)

把【推導 1】的兩條換算代進【已知 1】，兩側同乘 $\epsilon^{1/2}$ 即得 Schubert 的形式。

$$\begin{gather*}
2n &\overset{\text{已知 1}}{=}& \omega^{2} - k^{2} - \frac{k}{\omega} - 1 \\
2n &\overset{\text{推導 1(a)(b)}}{=}& \epsilon^{1/2}\hat{\nu}^{2} - \epsilon^{-1/2}m^{2} - \frac{\epsilon^{-1/4}m}{\epsilon^{1/4}\hat{\nu}} - 1 \\
2n &=& \epsilon^{-1/2}\left[\epsilon\hat{\nu}^{2} - m^{2} - \frac{m}{\hat{\nu}}\right] - 1 \\
2n + 1 &=& \epsilon^{-1/2}\left[\epsilon\hat{\nu}^{2} - m^{2} - \frac{m}{\hat{\nu}}\right] \\
\epsilon\hat{\nu}^{2} - m^{2} - \frac{m}{\hat{\nu}} &=& \epsilon^{1/2}\left(2n + 1\right)
\end{gather*}$$

### (b) proof $n = 0$ 的因式分解 (Factorization for $n = 0$)

把【證明 (a)】取 $n = 0$，兩側同乘 $\hat{\nu}$ 化成三次式，再驗證因式分解成立。

$$\begin{gather*}
\epsilon^{1/2} &\overset{\text{證明 (a)}}{=}& \epsilon\hat{\nu}^{2} - m^{2} - \frac{m}{\hat{\nu}} \\
\epsilon^{1/2}\hat{\nu} &=& \epsilon\hat{\nu}^{3} - m^{2}\hat{\nu} - m \\
0 &=& \epsilon\hat{\nu}^{3} - \epsilon^{1/2}\hat{\nu} - m^{2}\hat{\nu} - m \\
0 &=& \left(\epsilon^{1/2}\hat{\nu} + m\right)\left(\epsilon^{1/2}\hat{\nu}^{2} - m\hat{\nu} - 1\right)
\end{gather*}$$

### (c) proof Kelvin 波的本徵值 (Kelvin wave eigenvalue)

把【推導 3】(c) 換成 Schubert 的無因次記法。

$$\begin{gather*}
\hat{\nu} &\overset{\text{定義 1,推導 3(c)}}{=}& \frac{1}{2\Omega}\cdot\frac{\bar{c}m}{a} \\
\hat{\nu} &=& m\cdot\frac{\bar{c}}{2\Omega a} \\
\hat{\nu} &\overset{\text{已知 3}}{=}& m\,\epsilon^{-1/2} \\
\epsilon^{1/2}\hat{\nu} &=& m
\end{gather*}$$

### (d) verify Kelvin 波確實是 $n = -1$ 的形式解 (Kelvin wave as the formal $n = -1$ solution)

把【證明 (c)】代進【證明 (a)】的左端，看它是否等於 $n = -1$ 時的右端。

$$\begin{gather*}
\epsilon\hat{\nu}^{2} - m^{2} - \frac{m}{\hat{\nu}} &\overset{\text{證明 (c)}}{=}& \epsilon\cdot\frac{m^{2}}{\epsilon} - m^{2} - \frac{m\,\epsilon^{1/2}}{m} \\
&=& m^{2} - m^{2} - \epsilon^{1/2} \\
&=& -\epsilon^{1/2} \\
&=& \epsilon^{1/2}\left[2\left(-1\right) + 1\right]
\end{gather*}$$

+++

## 結構解釋

### 一張記法對照表

| 物理量 | project2_1（全無因次） | Schubert (2006) | 換算 |
|---|---|---|---|
| 頻率 | $\omega$ | $\hat{\nu} = \nu/\left(2\Omega\right)$ | $\omega = \epsilon^{1/4}\hat{\nu}$ |
| 緯向波數 | $k$ | $m$（整數） | $k = \epsilon^{-1/4}m$ |
| 經向座標 | $y$（已無因次） | $\hat{y} = \epsilon^{1/4}\left(y/a\right)$ | 同一個量 |
| 長度尺度 | $L_e = \left(\bar{c}/\beta\right)^{1/2}$ | $a\,\epsilon^{-1/4}$ | 同一個量 |
| 頻散關係 | $\omega^{2} - k^{2} - \dfrac{k}{\omega} - 1 = 2n$ | $\epsilon\hat{\nu}^{2} - m^{2} - \dfrac{m}{\hat{\nu}} = \epsilon^{1/2}\left(2n+1\right)$ | 兩側 $\times\,\epsilon^{1/2}$ |

**兩者是同一條式子。** Schubert 之所以不全無因次化，是因為他要保留整數的緯向波數 $m$（球面繞一圈的週期性要求 $m \in \mathbb{Z}$），而 project2_1 的 $k$ 是連續的。

代入 $\epsilon \approx 507.3$：$\epsilon^{1/4} \approx 4.746$、$\epsilon^{1/2} \approx 22.52$。所以 Schubert 的 $m = 1$ 對應 project2_1 的 $k \approx 0.211$ —— **行星尺度的波在赤道變形半徑的尺度上其實是「長波」**，這正是長波近似（Gill 1980）能在 MJO 問題上大致work 的原因。

### 三個根與四類波

【證明 (a)】對每組 $(m, n)$ 是 $\hat{\nu}$ 的**三次方程**，故有三個根，用 $r = 0, 1, 2$ 標記：

| $r$ | 波型 | 特徵 |
|---|---|---|
| $0$ | 西傳羅斯貝波 (Rossby) | $\left\|\hat{\nu}\right\|$ 最小；PV 動力主導 |
| $1$ | 西傳慣性重力波 (Westward IG) | $\left\|\hat{\nu}\right\|$ 大 |
| $2$ | 東傳慣性重力波 (Eastward IG) | $\left\|\hat{\nu}\right\|$ 大 |

再加上兩個特例，就湊滿赤道波的完整家族：

* **$n = 0$（混合羅斯貝–重力波）** —— 【證明 (b)】的因式分解顯示三次式退化。根 $\epsilon^{1/2}\hat{\nu} = -m$ **必須捨棄**（其本徵函數在 $\hat{y} \to \pm\infty$ 發散，違反【假設 1】），剩下 $\epsilon^{1/2}\hat{\nu}^{2} - m\hat{\nu} - 1 = 0$ 的兩根，索引為 $r = 0$（混合羅斯貝–重力波）與 $r = 2$（東傳慣性重力波）。
* **$n = -1$（Kelvin 波）** —— 【證明 (c)(d)】。它**不是**三次式的根，是令 $V = 0$ 另外解出來的；但形式上塞進 $n = -1$ 完全自洽，因此後面所有級數的 $n$ 都從 $-1$ 開始數，索引為 $r = 2$。

### 為什麼捨棄的根一定是那一個

【推導 3】(b) 把 Kelvin 型解的經向結構解成 $\Phi \propto e^{\mp\hat{y}^{2}/2}$ —— **兩個根給出的是彼此的倒數**：一個是高斯（有界），一個是反高斯（發散）。

$n = 0$ 那個被捨棄的根 $\epsilon^{1/2}\hat{\nu} = -m$ 是同一件事的鏡像：它對應「往西傳的 Kelvin 型解」，而赤道 $\beta$ 平面上只捕捉得住東傳的那一支。這個非對稱性的來源，正是 $f = \beta y$ 在赤道**變號**這件事 —— 它讓赤道成為一道波導，而波導只對特定傳播方向有效。
