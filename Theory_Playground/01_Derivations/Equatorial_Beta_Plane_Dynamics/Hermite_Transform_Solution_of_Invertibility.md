# Hermite Transform Solution of the Invertibility Principle (可逆性原理的 Hermite 轉換解)

+++

## 證明目標:

**端點③的後半。** 用 Hermite 轉換把 [可逆性原理](Equatorial_PV_Invertibility_Principle.md) 的橢圓型方程式
壓成**一行除法**，再轉回物理空間得到全部平衡場。

* (a) 純量 Hermite 轉換對：

$$\hat{\psi}_{mn} = \int_{-\infty}^{\infty}\hat{\psi}_m(\hat{y})\,\mathcal{H}_n(\hat{y})\,d\hat{y}, \qquad \hat{\psi}_m(\hat{y}) = \sum_{n = 0}^{\infty}\hat{\psi}_{mn}\,\mathcal{H}_n(\hat{y})$$

* (b) **★ 可逆性原理在譜空間塌縮成一行除法：**

$$\hat{\psi}_{mn} = -\frac{a^{2}\hat{q}_{mn}}{m^{2} + \epsilon^{1/2}\left(2n + 1\right)}$$

* (c) 流函數的物理空間形式：

$$\psi\left(\xi, y, z\right) = Z(z)\sum_{m = -\infty}^{\infty}\sum_{n = 0}^{\infty}\hat{\psi}_{mn}\,\mathcal{H}_n(\hat{y})\,e^{im\xi/a}$$

* (d) 旋轉風與質量場的還原：

$$\begin{pmatrix}u_\psi \cr v_\psi \cr \phi\end{pmatrix}\left(\xi, y, z\right) = Z(z)\sum_{m = -\infty}^{\infty}\sum_{n = 0}^{\infty}\frac{\hat{\psi}_{mn}}{a}\begin{pmatrix}U_{mn} \cr V_{mn} \cr \Phi_{mn}\end{pmatrix}\left(\xi, \hat{y}\right)$$

  其中

$$\begin{pmatrix}U_{mn} \cr V_{mn} \cr \Phi_{mn}\end{pmatrix} =
\begin{pmatrix}
\epsilon^{1/4}\left[\left(\dfrac{n+1}{2}\right)^{1/2}\mathcal{H}_{n+1} - \left(\dfrac{n}{2}\right)^{1/2}\mathcal{H}_{n-1}\right] \cr
im\,\mathcal{H}_n \cr
\bar{c}\,\epsilon^{1/4}\left[\left(\dfrac{n+1}{2}\right)^{1/2}\mathcal{H}_{n+1} + \left(\dfrac{n}{2}\right)^{1/2}\mathcal{H}_{n-1}\right]
\end{pmatrix}e^{im\xi/a}$$

* (e) (d) 的結構**恰為** [赤道波本徵函數](Equatorial_Wave_Eigenfunctions.md) 在**羅斯貝波極限**下的形式：

$$\lim_{\epsilon^{1/2}\hat{\nu}_{mnr} \to 0}\mathbf{K}_{mnr} \propto \begin{pmatrix}U_{mn} \cr V_{mn} \cr \Phi_{mn}\end{pmatrix}$$

其中

* $\psi$ : 旋轉流的流函數 (Streamfunction) $[\text{m}^{2}\cdot\text{s}^{-1}]$
* $\phi$ : 擾動位勢 (Perturbation geopotential) $[\text{m}^{2}\cdot\text{s}^{-2}]$
* $u_\psi,\ v_\psi$ : 旋轉風的兩個分量 (Rotational wind components) $[\text{m}\cdot\text{s}^{-1}]$
* $\hat{\psi}_m$ : 流函數的緯向傅立葉係數 (Fourier coefficient of the streamfunction) $[\text{m}^{2}\cdot\text{s}^{-1}]$
* $\hat{\psi}_{mn},\ \hat{q}_{mn}$ : Hermite 轉換係數 (Hermite transform coefficients) $[\text{依變數而定}]$
* $U_{mn},\ V_{mn},\ \Phi_{mn}$ : 本徵函數的速度與位勢分量 (Velocity and geopotential components of the eigenfunction) $[\text{依分量而定}]$
* $\mathbf{K}_{mnr}$ : 本徵函數 (Eigenfunction) $[\text{依分量而定}]$
* $\mathcal{H}_n$ : 歸一化 Hermite 函數 (Normalized Hermite function) $[\text{無單位}]$
* $Z(z)$ : 垂直結構函數 (Vertical structure function) $[\text{無單位}]$
* $\hat{\nu}_{mnr}$ : 無因次本徵頻率 (Dimensionless eigenfrequency) $[\text{無單位}]$
* $\xi$ : 隨波緯向座標 (Translating zonal coordinate) $[\text{m}]$
* $y$ : 經向座標，以赤道為原點 (Meridional coordinate) $[\text{m}]$
* $\hat{y}$ : 無因次經向座標 (Dimensionless meridional coordinate) $[\text{無單位}]$
* $z$ : 對數氣壓垂直座標 (Log-pressure vertical coordinate) $[\text{無單位}]$
* $m$ : 緯向波數 (Zonal wavenumber) $[\text{無單位}]$，整數
* $n$ : 經向模態指標 (Meridional mode index) $[\text{無單位}]$
* $i$ : 虛數單位 (Imaginary unit) $[\text{無單位}]$，$i^{2} = -1$
* $a$ : 地球半徑 (Earth's radius) $[\text{m}]$
* $\epsilon$ : Lamb 參數 (Lamb's parameter) $[\text{無單位}]$，$\epsilon \approx 507.3$
* $\bar{c}$ : 等效重力波速 (Equivalent gravity wave speed) $[\text{m}\cdot\text{s}^{-1}]$
* 註：(a)–(d) 就是 [Schubert & Masarik (2006)](../../06_References/Tropical_wave_dynamics/Schubert2006-Potential_vorticity_aspects_of_the_MJO/Potential_vorticity_aspects_of_the_MJO.ipynb) 的 $(6.4)$–$(6.9)$。
* 註：本篇比 [受迫解](Forced_Response_of_Equatorial_Modes.md) **簡單得多** —— 那裡要用三分量的向量內積 $(4.8)$ 與向量轉換對，這裡因為方程式是**純量**的，只要用最單純的 Hermite 正交性即可。
* 註：(e) 是一個很有力的一致性檢查：可逆性原理**抓的就是羅斯貝波那一支**，這在數學上驗證了「PV 動力 $\approx$ 羅斯貝波動力」這個直覺。

+++

## 假設與已知 (Assumptions & Preliminaries)

* **【已知 1】 [譜空間的可逆性原理 (Invertibility principle in spectral space)](https://derek1403.github.io/Theory_Playground/_build/html/01_Derivations/Equatorial_Beta_Plane_Dynamics/Equatorial_PV_Invertibility_Principle.html#d-proof-invertibility-principle-in-spectral-space)：** 可逆性原理在緯向傅立葉空間中的樣子：左端是作用在流函數上的諧振子型算符 $\left(\frac{d^{2}}{d\hat{y}^{2}} - \hat{y}^{2}\right)$ 再減去 $m^{2}$，右端是已知的位渦 ─ 給定 $q$ 就能解出 $\psi$，這正是「可逆」的意思。（已於本庫 [Equatorial PV Invertibility Principle](Equatorial_PV_Invertibility_Principle.md)【證明 (d)】完整證明，此處直接引用。）

  $$\epsilon^{1/2}\left(\frac{d^{2}}{d\hat{y}^{2}} - \hat{y}^{2}\right)\hat{\psi}_m - m^{2}\hat{\psi}_m = a^{2}\hat{q}_m$$

  * $\hat{\psi}_m$ : 流函數的緯向傅立葉係數 (Fourier coefficient of the streamfunction) $[\text{m}^{2}\cdot\text{s}^{-1}]$
  * $\hat{q}_m$ : 位渦的緯向傅立葉係數 (Fourier coefficient of the PV) $[\text{s}^{-1}]$
  * $\epsilon$ : Lamb 參數 (Lamb's parameter) $[\text{無單位}]$，$\epsilon \approx 507.3$
  * $\hat{y}$ : 無因次經向座標 (Dimensionless meridional coordinate) $[\text{無單位}]$
  * $m$ : 緯向波數 (Zonal wavenumber) $[\text{無單位}]$，整數
  * $a$ : 地球半徑 (Earth's radius) $[\text{m}]$

* **【已知 2】 [Hermite 函數的正交歸一性與諧振子本徵值 (Orthonormality and the oscillator eigenvalue)](https://derek1403.github.io/Theory_Playground/_build/html/01_Derivations/Differential_Equations/Hermite_Orthonormality_and_Oscillator_Eigenvalue.html#d-proof-orthonormality)：** Hermite 函數的三件事：互相正交歸一、是諧振子算符本徵值為 $-\left(2n + 1\right)$ 的本徵函數，以及 Lagrange 恆等式（高斯衰減讓邊界項消失）─ 有了它們，可逆性方程在 Hermite 基底下就對角化成逐項的代數式。（已於本庫 [Hermite Orthonormality and Oscillator Eigenvalue](../Differential_Equations/Hermite_Orthonormality_and_Oscillator_Eigenvalue.md) 完整證明，此處直接引用。）

  * (a) 正交歸一：

    $$\int_{-\infty}^{\infty}\mathcal{H}_n\mathcal{H}_{n'}\,d\hat{y} = \begin{cases}1, & n' = n \\ 0, & n' \neq n\end{cases}$$

  * (b) 諧振子本徵值：

    $$\left(\frac{d^{2}}{d\hat{y}^{2}} - \hat{y}^{2}\right)\mathcal{H}_n = -\left(2n + 1\right)\mathcal{H}_n$$

  * (c) Lagrange 恆等式與邊界項的消失（高斯衰減）：

    $$\int_{-\infty}^{\infty}\left[f\frac{d^{2}g}{d\hat{y}^{2}} - g\frac{d^{2}f}{d\hat{y}^{2}}\right]d\hat{y} = 0$$

  * $\mathcal{H}_n$ : 歸一化 Hermite 函數 (Normalized Hermite function) $[\text{無單位}]$
  * $f,\ g$ : 帶高斯衰減的任意二階可微函數 (Twice-differentiable functions with Gaussian decay) $[\text{無單位}]$
  * $\hat{y}$ : 無因次經向座標 (Dimensionless meridional coordinate) $[\text{無單位}]$

* **【已知 3】 [Hermite 函數的遞迴與微分關係 (Recurrence and derivative relations)](https://derek1403.github.io/Theory_Playground/_build/html/01_Derivations/Differential_Equations/Hermite_Functions_and_Recurrence.html#a-proof-recurrence-relation)：** 乘以 $\hat{y}$ 與對 $\hat{y}$ 微分這兩個操作，都只會把 $\mathcal{H}_n$ 送到相鄰的 $\mathcal{H}_{n \pm 1}$ ─ 這使得含 $\beta y$ 與 $d/dy$ 的項在 Hermite 基底下只耦合相鄰階，不會全域糾纏。（已於本庫 [Hermite Functions and Recurrence](../Differential_Equations/Hermite_Functions_and_Recurrence.md) 完整證明，此處直接引用。）

  * (a) 遞迴關係：

    $$\hat{y}\,\mathcal{H}_n = \left(\frac{n+1}{2}\right)^{1/2}\mathcal{H}_{n+1} + \left(\frac{n}{2}\right)^{1/2}\mathcal{H}_{n-1}$$

  * (b) 微分關係：

    $$\frac{d\mathcal{H}_n}{d\hat{y}} = -\left(\frac{n+1}{2}\right)^{1/2}\mathcal{H}_{n+1} + \left(\frac{n}{2}\right)^{1/2}\mathcal{H}_{n-1}$$

  * $\hat{y}$ : 無因次經向座標 (Dimensionless meridional coordinate) $[\text{無單位}]$
  * $\mathcal{H}_n$ : 歸一化 Hermite 函數 (Normalized Hermite function) $[\text{無單位}]$
  * $n$ : 經向模態指標 (Meridional mode index) $[\text{無單位}]$

* **【已知 4】 [平衡關係、旋轉風與座標換算 (Balance relation, rotational wind, and coordinate conversions)](https://derek1403.github.io/Theory_Playground/_build/html/01_Derivations/Equatorial_Beta_Plane_Dynamics/Equatorial_PV_Invertibility_Principle.html#b-proof-local-balance-relation)：** 本篇要用到的三組換算：局地平衡關係把位勢綁到流函數（$\phi = \beta y\,\psi$）、旋轉風由流函數的兩個偏導給出，以及經向座標的無因次化。（已於本庫 [Equatorial PV Invertibility Principle](Equatorial_PV_Invertibility_Principle.md) 完整證明或給出，此處直接引用。）

  * (a) 局地平衡關係：

    $$\phi = \beta y\,\psi$$

  * (b) 旋轉風：

    $$\left(u_\psi,\ v_\psi\right) = \left(-\frac{\partial \psi}{\partial y},\ \frac{\partial \psi}{\partial \xi}\right)$$

  * (c) 無因次經向座標與 Lamb 參數：

    $$\hat{y} = \epsilon^{1/4}\frac{y}{a}, \qquad \epsilon = \frac{4\Omega^{2}a^{2}}{\bar{c}^{2}}, \qquad \beta = \frac{2\Omega}{a}$$

  * $\bar{c}$ : 等效重力波速 (Equivalent gravity wave speed) $[\text{m}\cdot\text{s}^{-1}]$
  * $\Omega$ : 地球自轉角速度 (Earth's angular velocity) $[\text{s}^{-1}]$
  * $Z(z)$ : 垂直結構函數 (Vertical structure function) $[\text{無單位}]$
  * $\phi$ : 擾動位勢 (Perturbation geopotential) $[\text{m}^{2}\cdot\text{s}^{-2}]$
  * $\beta$ : 赤道 $\beta$ 參數 (Equatorial beta parameter) $[\text{m}^{-1}\cdot\text{s}^{-1}]$
  * $y$ : 經向座標，以赤道為原點 (Meridional coordinate) $[\text{m}]$
  * $\psi$ : 旋轉流的流函數 (Streamfunction) $[\text{m}^{2}\cdot\text{s}^{-1}]$
  * $u,\ v$ : 擾動緯向、經向風速 (Perturbation velocities) $[\text{m}\cdot\text{s}^{-1}]$
  * $v$ : 擾動經向風速 (Perturbation meridional velocity) $[\text{m}\cdot\text{s}^{-1}]$
  * $\xi$ : 隨波緯向座標 (Translating zonal coordinate) $[\text{m}]$
  * $\hat{y}$ : 無因次經向座標 (Dimensionless meridional coordinate) $[\text{無單位}]$
  * $\epsilon$ : Lamb 參數 (Lamb's parameter) $[\text{無單位}]$，$\epsilon \approx 507.3$
  * $a$ : 地球半徑 (Earth's radius) $[\text{m}]$

* **【已知 5】 [赤道波本徵函數 (Equatorial wave eigenfunctions)](https://derek1403.github.io/Theory_Playground/_build/html/01_Derivations/Equatorial_Beta_Plane_Dynamics/Equatorial_Wave_Eigenfunctions.html#a-proof-explicit-form-of-the-eigenfunctions)：** 本徵函數的三個分量：第一與第三分量是 $\mathcal{H}_{n+1}$ 與 $\mathcal{H}_{n-1}$ 的組合（差在正負號），第二分量則是單一個 $\mathcal{H}_n$ ─ 本篇只拿它來和 Hermite 轉換解出的結果對照。（已於本庫 [Equatorial Wave Eigenfunctions](Equatorial_Wave_Eigenfunctions.md)【證明 (a)】完整證明，僅供【證明 (e)】對照用。）

  $$\mathbf{K}_{mnr} = A_{mnr}\begin{pmatrix}
  \epsilon^{1/4}\left[\mathcal{P}_{mnr}\mathcal{H}_{n+1} + \mathcal{M}_{mnr}\mathcal{H}_{n-1}\right] \cr
  -i\left(\epsilon\hat{\nu}_{mnr}^{2} - m^{2}\right)\mathcal{H}_n \cr
  \bar{c}\,\epsilon^{1/4}\left[\mathcal{P}_{mnr}\mathcal{H}_{n+1} - \mathcal{M}_{mnr}\mathcal{H}_{n-1}\right]\end{pmatrix}$$

  * $\mathcal{P}_{mnr} = \left(\epsilon^{1/2}\hat{\nu}_{mnr} + m\right)\left(\frac{n+1}{2}\right)^{1/2}$、$\mathcal{M}_{mnr} = \left(\epsilon^{1/2}\hat{\nu}_{mnr} - m\right)\left(\frac{n}{2}\right)^{1/2}$ : 上下行振幅 (Amplitudes) $[\text{無單位}]$
  * $\hat{\nu}_{mnr}$ : 無因次本徵頻率 (Dimensionless eigenfrequency) $[\text{無單位}]$
  * $\mathbf{K}_{mnr}$ : 本徵函數 (Eigenfunction) $[\text{依分量而定}]$
  * $A$ : 未定的整體常數 (Undetermined overall constant) $[\text{無單位}]$
  * $\epsilon$ : Lamb 參數 (Lamb's parameter) $[\text{無單位}]$，$\epsilon \approx 507.3$
  * $\mathcal{P}_{mnr},\ \mathcal{M}_{mnr}$ : 上行、下行振幅 (Upper and lower branch amplitudes) $[\text{無單位}]$，皆為實數
  * $\mathcal{H}_n$ : 歸一化 Hermite 函數 (Normalized Hermite function) $[\text{無單位}]$
  * $\bar{c}$ : 等效重力波速 (Equivalent gravity wave speed) $[\text{m}\cdot\text{s}^{-1}]$
  * $A_{mnr}$ : 歸一化常數 (Normalization constant) $[\text{無單位}]$
  * $i$ : 虛數單位 (Imaginary unit) $[\text{無單位}]$，$i^{2} = -1$

* **【假設 1】 展開的完備性與逐項運算 (Completeness and term-by-term operations)：** $\hat{\psi}_m$ 與 $\hat{q}_m$ 都可用 $\left\{\mathcal{H}_n\right\}$ 展開，且積分／微分可與求和交換

  $$\hat{\psi}_m(\hat{y}) = \sum_{n = 0}^{\infty}\hat{\psi}_{mn}\mathcal{H}_n(\hat{y}), \qquad \hat{q}_m(\hat{y}) = \sum_{n = 0}^{\infty}\hat{q}_{mn}\mathcal{H}_n(\hat{y})$$

  * $\hat{\psi}_{mn},\ \hat{q}_{mn}$ : Hermite 轉換係數 (Hermite transform coefficients) $[\text{依變數而定}]$
  * $\hat{y}$ : 無因次經向座標 (Dimensionless meridional coordinate) $[\text{無單位}]$
  * $\mathcal{H}_n$ : 歸一化 Hermite 函數 (Normalized Hermite function) $[\text{無單位}]$
  * $\hat{\psi}_m$ : 流函數的緯向傅立葉係數 (Fourier coefficient of the streamfunction) $[\text{m}^{2}\cdot\text{s}^{-1}]$
  * $\hat{q}_m$ : 位渦的緯向傅立葉係數 (Fourier coefficient of the PV) $[\text{s}^{-1}]$

* **【假設 2】 分母恆不為零 (The denominator never vanishes)：** 保證【證明 (b)】的除法處處良好定義

  $$m^{2} + \epsilon^{1/2}\left(2n + 1\right) > 0$$

  * $m$ : 緯向波數 (Zonal wavenumber) $[\text{無單位}]$，整數
  * $\epsilon$ : Lamb 參數 (Lamb's parameter) $[\text{無單位}]$，$\epsilon \approx 507.3$
  * $n$ : 經向模態指標 (Meridional mode index) $[\text{無單位}]$
  * 註：由於 $\epsilon^{1/2} \approx 22.5 > 0$ 且 $2n + 1 \ge 1$，即使 $m = 0$ 分母仍至少為 $22.5$。**這與 [受迫解](Forced_Response_of_Equatorial_Modes.md) 需要靠阻尼 $\alpha$ 才不發散是完全不同的情形** —— 橢圓型問題天生沒有共振。

* **【假設 3】 羅斯貝波極限 (Rossby wave limit)：** 【證明 (e)】的對照只在低頻極限下成立

  $$\left|\epsilon^{1/2}\hat{\nu}_{mnr}\right| \ll \left|m\right|$$

  * $\epsilon$ : Lamb 參數 (Lamb's parameter) $[\text{無單位}]$，$\epsilon \approx 507.3$
  * $\hat{\nu}_{mnr}$ : 無因次本徵頻率 (Dimensionless eigenfrequency) $[\text{無單位}]$
  * $m$ : 緯向波數 (Zonal wavenumber) $[\text{無單位}]$，整數
  * $n$ : 經向模態指標 (Meridional mode index) $[\text{無單位}]$
  * $r$ : 波型指標 (Wave-type index) $[\text{無單位}]$

* **【推導 1】 純量算符的自伴性 (Self-adjointness of the scalar operator)：** 兩次分部積分（邊界項由高斯衰減殺掉），算符可從 $\hat{\psi}_m$ 轉移到 $\mathcal{H}_n$ 上

  $$\begin{gather*}
  \int_{-\infty}^{\infty}\mathcal{H}_n\left(\frac{d^{2}}{d\hat{y}^{2}} - \hat{y}^{2}\right)\hat{\psi}_m\,d\hat{y}
  &=& \int_{-\infty}^{\infty}\left[\mathcal{H}_n\frac{d^{2}\hat{\psi}_m}{d\hat{y}^{2}} - \hat{y}^{2}\mathcal{H}_n\hat{\psi}_m\right]d\hat{y} \\
  &\overset{\text{已知 2(c)}}{=}& \int_{-\infty}^{\infty}\left[\hat{\psi}_m\frac{d^{2}\mathcal{H}_n}{d\hat{y}^{2}} - \hat{y}^{2}\hat{\psi}_m\mathcal{H}_n\right]d\hat{y} \\
  &=& \int_{-\infty}^{\infty}\hat{\psi}_m\left(\frac{d^{2}}{d\hat{y}^{2}} - \hat{y}^{2}\right)\mathcal{H}_n\,d\hat{y} \\
  &\overset{\text{已知 2(b)}}{=}& -\left(2n + 1\right)\int_{-\infty}^{\infty}\hat{\psi}_m\mathcal{H}_n\,d\hat{y}
  \end{gather*}$$

  * $\mathcal{H}_n$ : 歸一化 Hermite 函數 (Normalized Hermite function) $[\text{無單位}]$
  * $n$ : 經向模態指標 (Meridional mode index) $[\text{無單位}]$
  * $\hat{y}$ : 無因次經向座標 (Dimensionless meridional coordinate) $[\text{無單位}]$
  * $\hat{\psi}_m$ : 流函數的緯向傅立葉係數 (Fourier coefficient of the streamfunction) $[\text{m}^{2}\cdot\text{s}^{-1}]$
  * $m$ : 緯向波數 (Zonal wavenumber) $[\text{無單位}]$，整數

* **【推導 2】 座標換算的兩個常數 (Two conversion constants)：** 把有因次的 $y$ 換成無因次 $\hat{y}$ 時，經向微分與 $\beta y$ 這兩處各自吐出一個常數係數；先在這裡算清楚，主證明才能一路用無因次量走完。值得注意的是兩者的係數同為 $\dfrac{\bar{c}\epsilon^{1/4}}{a}$。

  * (a) 經向微分：

    $$\frac{d}{dy} \overset{\text{已知 4(c)}}{=} \frac{\epsilon^{1/4}}{a}\frac{d}{d\hat{y}}$$

  * (b) $\beta y$ 的無因次形式，其係數與 $\dfrac{\bar{c}\epsilon^{1/4}}{a}$ 相同：

    $$\begin{gather*}
    \beta y &\overset{\text{已知 4(c)}}{=}& \frac{2\Omega}{a}\cdot\frac{a\,\hat{y}}{\epsilon^{1/4}} \\
    &=& \frac{2\Omega}{\epsilon^{1/4}}\hat{y} \\
    &\overset{\text{已知 4(c)}}{=}& \frac{\bar{c}\,\epsilon^{1/4}}{a}\hat{y}
    \end{gather*}$$

  * $y$ : 經向座標，以赤道為原點 (Meridional coordinate) $[\text{m}]$
  * $\epsilon$ : Lamb 參數 (Lamb's parameter) $[\text{無單位}]$，$\epsilon \approx 507.3$
  * $a$ : 地球半徑 (Earth's radius) $[\text{m}]$
  * $\hat{y}$ : 無因次經向座標 (Dimensionless meridional coordinate) $[\text{無單位}]$
  * $\beta$ : 赤道 $\beta$ 參數 (Equatorial beta parameter) $[\text{m}^{-1}\cdot\text{s}^{-1}]$
  * $\Omega$ : 地球自轉角速度 (Earth's angular velocity) $[\text{s}^{-1}]$
  * $\bar{c}$ : 等效重力波速 (Equivalent gravity wave speed) $[\text{m}\cdot\text{s}^{-1}]$
  * 註：(b) 最後一步用到 $\bar{c} = \dfrac{2\Omega a}{\epsilon^{1/2}}$，即【已知 4】(c) 中 $\epsilon$ 定義的改寫。

* **【推導 3】 羅斯貝極限下的兩個振幅 (The two amplitudes in the Rossby limit)：** 在羅斯貝波的低頻極限（$\epsilon\hat{\nu}_{mnr}^{2} \ll m^{2}$）下，上下行振幅與第二分量的係數都退化成只含 $m$ 與 $n$ 的簡單形式 ─ 這三個近似值就是後面把 Hermite 級數解收成封閉式的全部素材。

  * (a) 上行振幅：

    $$\begin{gather*}
    \mathcal{P}_{mnr} &\overset{\text{已知 5,假設 3}}{\approx}& m\left(\frac{n+1}{2}\right)^{1/2}
    \end{gather*}$$

  * (b) 下行振幅：

    $$\begin{gather*}
    \mathcal{M}_{mnr} &\overset{\text{已知 5,假設 3}}{\approx}& -m\left(\frac{n}{2}\right)^{1/2}
    \end{gather*}$$

  * (c) 第二分量的係數：

    $$\begin{gather*}
    -i\left(\epsilon\hat{\nu}_{mnr}^{2} - m^{2}\right) &\overset{\text{已知 5,假設 3}}{\approx}& i\,m^{2}
    \end{gather*}$$

  * $\mathcal{P}_{mnr},\ \mathcal{M}_{mnr}$ : 上行、下行振幅 (Upper and lower branch amplitudes) $[\text{無單位}]$，皆為實數
  * $m$ : 緯向波數 (Zonal wavenumber) $[\text{無單位}]$，整數
  * $n$ : 經向模態指標 (Meridional mode index) $[\text{無單位}]$
  * $r$ : 波型指標 (Wave-type index) $[\text{無單位}]$
  * $\epsilon$ : Lamb 參數 (Lamb's parameter) $[\text{無單位}]$，$\epsilon \approx 507.3$
  * $\hat{\nu}_{mnr}$ : 無因次本徵頻率 (Dimensionless eigenfrequency) $[\text{無單位}]$
  * $i$ : 虛數單位 (Imaginary unit) $[\text{無單位}]$，$i^{2} = -1$

+++

## 證明:

### (a) proof Hermite 轉換對 (Hermite transform pair)

反轉換式即【假設 1】；正轉換式由兩側乘 $\mathcal{H}_{n'}$ 再積分得到。

$$\begin{gather*}
\int_{-\infty}^{\infty}\hat{\psi}_m\,\mathcal{H}_{n'}\,d\hat{y} &\overset{\text{假設 1}}{=}& \int_{-\infty}^{\infty}\left[\sum_{n = 0}^{\infty}\hat{\psi}_{mn}\mathcal{H}_n\right]\mathcal{H}_{n'}\,d\hat{y} \\
&\overset{\text{假設 1}}{=}& \sum_{n = 0}^{\infty}\hat{\psi}_{mn}\int_{-\infty}^{\infty}\mathcal{H}_n\mathcal{H}_{n'}\,d\hat{y} \\
&\overset{\text{已知 2(a)}}{=}& \hat{\psi}_{mn'}
\end{gather*}$$

### (b) proof 譜空間的一行除法 (One-line division in spectral space)

把【已知 1】兩側乘 $\mathcal{H}_n$ 再對 $\hat{y}$ 積分。左端第一項由【推導 1】把算符轉移到 $\mathcal{H}_n$ 上，換成本徵值 $-(2n+1)$。

$$\begin{gather*}
a^{2}\hat{q}_{mn} &\overset{\text{證明 (a)}}{=}& \int_{-\infty}^{\infty}a^{2}\hat{q}_m\,\mathcal{H}_n\,d\hat{y} \\
a^{2}\hat{q}_{mn} &\overset{\text{已知 1}}{=}& \epsilon^{1/2}\int_{-\infty}^{\infty}\mathcal{H}_n\left(\frac{d^{2}}{d\hat{y}^{2}} - \hat{y}^{2}\right)\hat{\psi}_m\,d\hat{y} - m^{2}\int_{-\infty}^{\infty}\hat{\psi}_m\mathcal{H}_n\,d\hat{y} \\
a^{2}\hat{q}_{mn} &\overset{\text{推導 1}}{=}& -\epsilon^{1/2}\left(2n + 1\right)\int_{-\infty}^{\infty}\hat{\psi}_m\mathcal{H}_n\,d\hat{y} - m^{2}\int_{-\infty}^{\infty}\hat{\psi}_m\mathcal{H}_n\,d\hat{y} \\
a^{2}\hat{q}_{mn} &\overset{\text{證明 (a)}}{=}& -\left[m^{2} + \epsilon^{1/2}\left(2n + 1\right)\right]\hat{\psi}_{mn} \\
\hat{\psi}_{mn} &\overset{\text{假設 2}}{=}& -\frac{a^{2}\hat{q}_{mn}}{m^{2} + \epsilon^{1/2}\left(2n + 1\right)}
\end{gather*}$$

### (c) proof 流函數的物理空間形式 (Physical-space form of the streamfunction)

把【假設 1】的 Hermite 反轉換、緯向傅立葉反轉換與垂直結構逐層套上。

$$\begin{gather*}
\psi\left(\xi, y, z\right) &\overset{\text{已知 4}}{=}& Z(z)\,\hat{\psi}\left(\xi, \hat{y}\right) \\
&\overset{\text{已知 1}}{=}& Z(z)\sum_{m = -\infty}^{\infty}\hat{\psi}_m(\hat{y})\,e^{im\xi/a} \\
&\overset{\text{假設 1}}{=}& Z(z)\sum_{m = -\infty}^{\infty}\sum_{n = 0}^{\infty}\hat{\psi}_{mn}\,\mathcal{H}_n(\hat{y})\,e^{im\xi/a}
\end{gather*}$$

### (d) proof 旋轉風與質量場的還原 (Recovery of the rotational wind and mass fields)

三個場分別對 $y$ 微分、對 $\xi$ 微分、乘 $\beta y$；三種操作在 $\left\{\mathcal{H}_n\right\}$ 上都只用到【已知 3】。

* **緯向風：**

$$\begin{gather*}
u_\psi &\overset{\text{已知 4(b)}}{=}& -\frac{\partial \psi}{\partial y} \\
&\overset{\text{證明 (c),推導 2(a)}}{=}& -Z(z)\sum_{m}\sum_{n}\hat{\psi}_{mn}\frac{\epsilon^{1/4}}{a}\frac{d\mathcal{H}_n}{d\hat{y}}e^{im\xi/a} \\
&\overset{\text{已知 3(b)}}{=}& Z(z)\sum_{m}\sum_{n}\frac{\hat{\psi}_{mn}}{a}\,\epsilon^{1/4}\left[\left(\frac{n+1}{2}\right)^{1/2}\mathcal{H}_{n+1} - \left(\frac{n}{2}\right)^{1/2}\mathcal{H}_{n-1}\right]e^{im\xi/a}
\end{gather*}$$

* **經向風：**

$$\begin{gather*}
v_\psi &\overset{\text{已知 4(b)}}{=}& \frac{\partial \psi}{\partial \xi} \\
&\overset{\text{證明 (c)}}{=}& Z(z)\sum_{m}\sum_{n}\hat{\psi}_{mn}\,\mathcal{H}_n\frac{im}{a}e^{im\xi/a} \\
&=& Z(z)\sum_{m}\sum_{n}\frac{\hat{\psi}_{mn}}{a}\left[im\,\mathcal{H}_n\right]e^{im\xi/a}
\end{gather*}$$

* **質量場：**

$$\begin{gather*}
\phi &\overset{\text{已知 4(a)}}{=}& \beta y\,\psi \\
&\overset{\text{證明 (c),推導 2(b)}}{=}& Z(z)\sum_{m}\sum_{n}\hat{\psi}_{mn}\frac{\bar{c}\,\epsilon^{1/4}}{a}\,\hat{y}\,\mathcal{H}_n\,e^{im\xi/a} \\
&\overset{\text{已知 3(a)}}{=}& Z(z)\sum_{m}\sum_{n}\frac{\hat{\psi}_{mn}}{a}\,\bar{c}\,\epsilon^{1/4}\left[\left(\frac{n+1}{2}\right)^{1/2}\mathcal{H}_{n+1} + \left(\frac{n}{2}\right)^{1/2}\mathcal{H}_{n-1}\right]e^{im\xi/a}
\end{gather*}$$

### (e) verify 與赤道波本徵函數的一致性 (Consistency with the equatorial wave eigenfunctions)

把【推導 3】的三個極限代進【已知 5】，三個分量都退化成【證明 (d)】的形式（差一個共同的常數 $A_{mnr}m$，由【假設 1】的規範自由度吸收）。

$$\begin{gather*}
\lim_{\epsilon^{1/2}\hat{\nu}_{mnr} \to 0}\mathbf{K}_{mnr}
&\overset{\text{已知 5,推導 3(a)(b)(c)}}{=}& A_{mnr}\,m\begin{pmatrix}
\epsilon^{1/4}\left[\left(\frac{n+1}{2}\right)^{1/2}\mathcal{H}_{n+1} - \left(\frac{n}{2}\right)^{1/2}\mathcal{H}_{n-1}\right] \cr
i\,m\,\mathcal{H}_n \cr
\bar{c}\,\epsilon^{1/4}\left[\left(\frac{n+1}{2}\right)^{1/2}\mathcal{H}_{n+1} + \left(\frac{n}{2}\right)^{1/2}\mathcal{H}_{n-1}\right]\end{pmatrix} \\
&\overset{\text{證明 (d)}}{\propto}& \begin{pmatrix}U_{mn} \cr V_{mn} \cr \Phi_{mn}\end{pmatrix}e^{-im\xi/a}
\end{gather*}$$

+++

## 物理解釋

### 反演就是「除以一個正數」

【證明 (b)】把整條橢圓型偏微分方程壓成

$$\hat{\psi}_{mn} = -\frac{a^{2}}{\underbrace{m^{2} + \epsilon^{1/2}\left(2n + 1\right)}_{\text{恆為正}}}\,\hat{q}_{mn}$$

每個譜分量只要**除以一個正數**就完成反演。這比 [受迫解](Forced_Response_of_Equatorial_Modes.md) 還簡單 —— 那裡的分母是複數（含阻尼與失諧），這裡是實正數。

差別的根源是**方程式的型別**：可逆性原理是**橢圓型**（無時間導數、無共振），受迫問題是**雙曲型加阻尼**（有共振峰）。

### 反演天生會「平滑化」

分母 $m^{2} + \epsilon^{1/2}\left(2n + 1\right)$ 隨 $m$、$n$ **單調遞增**。於是：

$$\text{波數愈高} \quad\Longrightarrow\quad \left|\hat{\psi}_{mn}/\hat{q}_{mn}\right| \text{ 愈小} \quad\Longrightarrow\quad \text{同樣強度的 PV 距平誘導出的流場愈弱}$$

這就是 PV 反演的**平滑化性質**：$q$ 場中的小尺度細節，在還原出來的 $\psi$ 場中會被大幅壓抑。物理上很合理 —— 一小塊 PV 異常只能影響它附近，影響範圍大約是變形半徑。

代入數值：$\epsilon^{1/2} \approx 22.5$，所以對 $n = 0$、$m = 1$ 的行星尺度模態，分母 $\approx 23.5$；對 $n = 10$ 的模態，分母 $\approx 473$ —— **相差 20 倍**。

### 「PV 動力 $=$ 羅斯貝波動力」的數學驗證

【證明 (e)】說：可逆性原理還原出來的 $\left(U_{mn}, V_{mn}, \Phi_{mn}\right)$ **恰好就是**完整赤道波本徵函數 $\mathbf{K}_{mnr}$ 在羅斯貝波極限（$\epsilon^{1/2}\hat{\nu} \to 0$）下的形式。

這在數學上驗證了一個很重要的說法：**可逆性原理只看得見羅斯貝波那一支**。

實作上論文正是這樣用的：【證明 (b)】右端的 $\hat{q}_{mn}$ 直接取 [場還原](Physical_Field_Recovery_and_Zero_Kelvin_PV.md) 中**羅斯貝波的貢獻** $\hat{q}_{mn0}$。這個近似之所以合理，是因為總 PV 場本來就幾乎全部由羅斯貝波貢獻（見該篇的結構解釋）。

### 端點③的成績單與那道破綻

把反演解與原始方程解相比，論文的結論是**兩者相當接近** —— 平衡模式的質量場與旋轉風場，是原始方程解中羅斯貝波貢獻的良好近似。**對流尾流（西側）的流場，確實可以只靠 PV 還原出來。**

**唯一的破綻在對流東側。** 原因有二，且兩者都指向同一個地方：

1. **[Kelvin 波的 PV 恰好為零](Physical_Field_Recovery_and_Zero_Kelvin_PV.md)【證明 (d)】** —— 東側的流場主要由 Kelvin 波構成，而它在 $q$ 裡完全不留痕跡。**資訊根本不存在，反演再準也救不回來。**
2. **[平衡關係 $\phi = \beta y\psi$ 在赤道最不準](Equatorial_PV_Invertibility_Principle.md)【假設 2】** —— 被丟掉的 $\beta\,\partial\psi/\partial y$ 項在 $y \to 0$ 時相對最大。

論文誠實地把這道破綻寫出來：「最明顯的差異是，原始方程模式中赤道上的緯向氣壓梯度力，在可逆性原理的解裡完全沒有被重現。」

**這是本文最有價值的一句話** —— 它劃出了 PV 思維的**邊界**：PV 反演在羅斯貝波主導的區域非常好用，但在重力波（含 Kelvin 波）主導的區域，它原則上就失效。
