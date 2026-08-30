# Projection of a Moving Heat Source (東移熱源的緯向傅立葉係數與模態投影)

+++

## 證明目標:

給定一塊東移深對流的加熱形狀，算出它在 [受迫解](Forced_Response_of_Equatorial_Modes.md) 公式中
唯一還沒填上的那一項 $\hat{Q}_{mnr}$。

* (a) 加熱的總量與擺放位置 $y_0$ **無關** —— 這讓 $y_0$ 的對照實驗乾淨：

$$\iint \hat{Q}\left(\xi, y\right)\,d\xi\,dy = \pi^{1/2}Q_0\,a_0\,b_0$$

* (b) 加熱的緯向傅立葉係數：

$$\hat{Q}_m(y) = \frac{\pi Q_0}{2\left[\pi^{2} - \left(ma_0/a\right)^{2}\right]}\frac{\sin\left(ma_0/a\right)}{m}\exp\left[-\left(\frac{y - y_0}{b_0}\right)^{2}\right]$$

* (c) 加熱在第 $(m, n, r)$ 個赤道波模態上的投影（$n \ge 0$）：

$$\begin{aligned}
\hat{Q}_{mnr} = &\ \frac{A_{mnr}\,\epsilon^{1/2}\,\pi Q_0\,a_0\,b_0}{2\bar{c}\,a^{2}\left[\pi^{2} - \left(ma_0/a\right)^{2}\right]}\frac{\sin\left(ma_0/a\right)}{\left(ma_0/a\right)}\left(\frac{2\pi}{2 + \hat{b}_0^{2}}\right)^{1/2}\exp\left(\frac{\hat{b}_0^{2}\hat{y}_0^{2}}{4 - \hat{b}_0^{4}}\right) \cr
&\times \left[\left(\epsilon^{1/2}\hat{\nu}_{mnr} + m\right)\left(\frac{2 - \hat{b}_0^{2}}{2 + \hat{b}_0^{2}}\right)^{(n+1)/2}\left(\frac{n+1}{2}\right)^{1/2}\mathcal{H}_{n+1}\!\left(\frac{2\hat{y}_0}{\left(4 - \hat{b}_0^{4}\right)^{1/2}}\right)\right. \cr
&\qquad \left. - \left(\epsilon^{1/2}\hat{\nu}_{mnr} - m\right)\left(\frac{2 - \hat{b}_0^{2}}{2 + \hat{b}_0^{2}}\right)^{(n-1)/2}\left(\frac{n}{2}\right)^{1/2}\mathcal{H}_{n-1}\!\left(\frac{2\hat{y}_0}{\left(4 - \hat{b}_0^{4}\right)^{1/2}}\right)\right]
\end{aligned}$$

* (d) Kelvin 波（$n = -1$、$r = 2$）的投影：

$$\hat{Q}_{m,-1,2} = \frac{A_{m,-1,2}\,\epsilon^{1/4}\,\pi Q_0\,a_0\,b_0}{2\bar{c}\,a^{2}\left[\pi^{2} - \left(ma_0/a\right)^{2}\right]}\frac{\sin\left(ma_0/a\right)}{\left(ma_0/a\right)}\left(\frac{2\pi}{2 + \hat{b}_0^{2}}\right)^{1/2}\exp\left(-\frac{\hat{y}_0^{2}}{2 + \hat{b}_0^{2}}\right)$$

* (e) 對流正對赤道時，**偶數 $n$ 的模態完全不被激發**（其中 $n = 0$ 即混合羅斯貝–重力波）：

$$\left.\hat{Q}_{mnr}\right|_{\hat{y}_0 = 0} = 0 \qquad \left(n \ \text{為偶數}\right)$$

* 註：(a)–(d) 就是 [Schubert & Masarik (2006)](../../06_References/Tropical_wave_dynamics/Schubert2006-Potential_vorticity_aspects_of_the_MJO/Potential_vorticity_aspects_of_the_MJO.ipynb) 的 $(4.1)$ 之下的敘述、$(4.5)$、$(4.22)$、$(4.23)$。
* 註：本篇的兩個積分**都不重算**：緯向的升餘弦積分在【推導 2】自證（只是三角恆等式），經向的高斯 $\times$ Hermite 積分直接引用本庫 [Gaussian–Hermite Integral](../Calculus/Gaussian_Hermite_Integral.md)（論文的 $(B.1)$）。

+++

## 假設與已知 (Assumptions & Preliminaries)

* **【已知 1】 [緯向傅立葉轉換 (Zonal Fourier transform)](https://derek1403.github.io/Theory_Playground/_build/html/01_Derivations/Equatorial_Beta_Plane_Dynamics/Fourier_Transform_to_Shallow_Water_System.html#b-proof-zonal-fourier-transform-pair)：** 把緯向依賴換成波數 $m$ 的積分公式：在一個緯圈（週期 $2\pi a$）上對 $e^{-im\xi/a}$ 取內積並平均 ─ 這是取出各波數分量的標準操作。（已於本庫 [Fourier Transform to the Shallow Water System](Fourier_Transform_to_Shallow_Water_System.md)【證明 (b)】完整證明，此處直接引用。）

  $$\hat{Q}_m(y) = \frac{1}{2\pi a}\int_{-\pi a}^{\pi a}\hat{Q}\left(\xi, y\right)e^{-im\xi/a}\,d\xi$$

  * $\xi$ : 隨波緯向座標 (Translating zonal coordinate) $[\text{m}]$
  * $m$ : 緯向波數 (Zonal wavenumber) $[\text{無單位}]$，整數
  * $a$ : 地球半徑 (Earth's radius) $[\text{m}]$，$a = 6370 \ \text{km}$
  * $\hat{Q}$ : 加熱率的水平結構函數 (Horizontal structure function of the heating rate) $[\text{J}\cdot\text{kg}^{-1}\cdot\text{s}^{-1}]$
  * $y_0$ : 對流中心的緯向偏移 (Meridional offset of the convection center) $[\text{m}]$，$y_0 = 0$ 或 $450 \ \text{km}$

* **【已知 2】 [赤道波本徵函數與強迫向量 (Equatorial wave eigenfunctions and the forcing vector)](https://derek1403.github.io/Theory_Playground/_build/html/01_Derivations/Equatorial_Beta_Plane_Dynamics/Equatorial_Wave_Eigenfunctions.html#a-proof-explicit-form-of-the-eigenfunctions)：** 投影要用到的兩邊：本徵函數的第三分量（$n \ge 0$ 時是 $\mathcal{H}_{n+1}$ 與 $\mathcal{H}_{n-1}$ 的組合，Kelvin 波則退化成單純的高斯），以及強迫向量 ─ 加熱只進入第三分量，其餘兩個分量為零。（已於本庫 [Equatorial Wave Eigenfunctions](Equatorial_Wave_Eigenfunctions.md) 完整證明，此處直接引用。）

  * (a) 本徵函數的第三分量（$n \ge 0$，為實函數）：

    $$\Phi_{mnr}(\hat{y}) = \bar{c}\,A_{mnr}\,\epsilon^{1/4}\left[\left(\epsilon^{1/2}\hat{\nu}_{mnr} + m\right)\left(\frac{n+1}{2}\right)^{1/2}\mathcal{H}_{n+1}(\hat{y}) - \left(\epsilon^{1/2}\hat{\nu}_{mnr} - m\right)\left(\frac{n}{2}\right)^{1/2}\mathcal{H}_{n-1}(\hat{y})\right]$$

  * (b) Kelvin 波的第三分量：

    $$\Phi_{m,-1,2}(\hat{y}) = \bar{c}\,A_{m,-1,2}\,e^{-\hat{y}^{2}/2} = \bar{c}\,A_{m,-1,2}\,\pi^{1/4}\mathcal{H}_0(\hat{y})$$

  * (c) 強迫向量只有第三分量非零：

    $$\hat{\mathbf{Q}}_m(y) = \begin{pmatrix}0 \cr 0 \cr \hat{Q}_m(y)\end{pmatrix}$$

  * $\mathcal{H}_n$ : 歸一化 Hermite 函數 (Normalized Hermite function) $[\text{無單位}]$
  * $A_{mnr}$ : 本徵函數的歸一化常數 (Normalization constant) $[\text{無單位}]$
  * $\hat{\nu}_{mnr}$ : 無因次本徵頻率 (Dimensionless eigenfrequency) $[\text{無單位}]$
  * $\epsilon$ : Lamb 參數 (Lamb's parameter) $[\text{無單位}]$，$\epsilon \approx 507.3$
  * $\bar{c}$ : 等效重力波速 (Equivalent gravity wave speed) $[\text{m}\cdot\text{s}^{-1}]$
  * $\hat{y}$ : 無因次經向座標 (Dimensionless meridional coordinate) $[\text{無單位}]$，$\hat{y} = \epsilon^{1/4}y/a$
  * $\Phi$ : 本徵函數的位勢分量 (Geopotential component) $[\text{m}\cdot\text{s}^{-1}]$
  * $\hat{\mathbf{Q}}_m$ : 強迫向量 (Forcing vector) $[\text{依分量而定}]$
  * $y_0$ : 對流中心的緯向偏移 (Meridional offset of the convection center) $[\text{m}]$，$y_0 = 0$ 或 $450 \ \text{km}$
  * $\hat{Q}$ : 加熱率的水平結構函數 (Horizontal structure function of the heating rate) $[\text{J}\cdot\text{kg}^{-1}\cdot\text{s}^{-1}]$

* **【已知 3】 [能量內積 (Energy inner product)](https://derek1403.github.io/Theory_Playground/_build/html/01_Derivations/Equatorial_Beta_Plane_Dynamics/Energy_Inner_Product_and_Skew_Hermitian_Operator.html#assumptions-preliminaries)：** 三分量向量函數的內積，第三分量帶 $1/\bar{c}^{2}$ 的權重 ─ 因為強迫只有第三分量非零，投影積分實際上只剩這一項在作用。（已於本庫 [Energy Inner Product and the Skew-Hermitian Operator](Energy_Inner_Product_and_Skew_Hermitian_Operator.md)【定義 3】給出，此處直接引用。）

  $$\left(\mathbf{f},\ \mathbf{g}\right) = \int_{-\infty}^{\infty}\left(f_1g_1^{*} + f_2g_2^{*} + \frac{1}{\bar{c}^{2}}f_3g_3^{*}\right)d\hat{y}$$

  * $\mathbf{f},\ \mathbf{g}$ : 複數三分量向量函數 (Complex three-component vector functions) $[\text{依分量而定}]$
  * $f_j,\ g_j$ : 內積中的兩個三分量向量函數 (Two three-component vector functions) $[\text{依分量而定}]$
  * $\bar{c}$ : 等效重力波速 (Equivalent gravity wave speed) $[\text{m}\cdot\text{s}^{-1}]$
  * $\hat{y}$ : 無因次經向座標 (Dimensionless meridional coordinate) $[\text{無單位}]$，$\hat{y} = \epsilon^{1/4}y/a$

* **【已知 4】 [高斯 × Hermite 重疊積分 (Gaussian–Hermite overlap integral)](https://derek1403.github.io/Theory_Playground/_build/html/01_Derivations/Calculus/Gaussian_Hermite_Integral.html#a-proof-hermite-gaussian-hermite-overlap-integral)：** 高斯函數與任意階 Hermite 函數的重疊積分有封閉解，其結果由 $\chi$ 與 $\eta$ 兩個組合參數決定，適用範圍為 $0 \le \hat{b}_0 < 2^{1/2}$ ─ 這條公式讓熱源在模態上的投影不必逐項做數值積分。（已於本庫 [Gaussian–Hermite Integral](../Calculus/Gaussian_Hermite_Integral.md)【證明 (a)】完整證明，即論文的 $(B.1)$；此處直接引用。）

  $$\int_{-\infty}^{\infty}\exp\left[-\frac{\left(\hat{y} - \hat{y}_0\right)^{2}}{\hat{b}_0^{2}}\right]\mathcal{H}_k(\hat{y})\,d\hat{y} = \left(\frac{2\pi\hat{b}_0^{2}}{2 + \hat{b}_0^{2}}\right)^{1/2}\chi^{k/2}\exp\left[\frac{\hat{b}_0^{2}\hat{y}_0^{2}}{4 - \hat{b}_0^{4}}\right]\mathcal{H}_k(\eta)$$

  適用範圍 $0 \le \hat{b}_0 < 2^{1/2}$，其中 $\chi = \dfrac{2 - \hat{b}_0^{2}}{2 + \hat{b}_0^{2}}$、$\eta = \dfrac{2\hat{y}_0}{\left(4 - \hat{b}_0^{4}\right)^{1/2}}$。

  * $k$ : Hermite 函數的階數 (Order of the Hermite function) $[\text{無單位}]$
  * $\hat{b}_0,\ \hat{y}_0$ : 無因次的加熱寬度與偏移 (Dimensionless width and offset) $[\text{無單位}]$
  * $\mathcal{H}_n$ : 歸一化 Hermite 函數 (Normalized Hermite function) $[\text{無單位}]$
  * $\chi$ : 階數壓縮比 (Order-compression ratio) $[\text{無單位}]$
  * $\eta$ : 生成函數的自變數位置（本檔會代入不同的值）(Argument of the generating function) $[\text{無單位}]$

* **【已知 5】 [積化和差公式 (Product-to-sum formula)](https://dlmf.nist.gov/4.21#E1)：** 兩個餘弦的乘積可以化成和頻與差頻兩個餘弦之和 ─ 本篇用它把「升餘弦帽子 × 傅立葉核」的乘積拆成可以直接積分的項。（標準三角恆等式，此處直接引用。）

  $$\cos A\,\cos B = \frac{1}{2}\left[\cos\left(A + B\right) + \cos\left(A - B\right)\right]$$

  * $A_{mnr}$ : 本徵函數的歸一化常數 (Normalization constant) $[\text{無單位}]$
  * $A,\ B$ : 待定常數 (Undetermined constants) $[\text{依應用而定}]$

* **【已知 6】 [高斯積分 (Gaussian integral)](https://dlmf.nist.gov/7.4#E1)：** 高斯函數在全實軸上的積分值為 $\pi^{1/2}$。（標準結果，此處直接引用。）

  $$\int_{-\infty}^{\infty}e^{-s^{2}}\,ds = \pi^{1/2}$$

  * $s$ : 積分變數 (Integration variable) $[\text{依應用而定}]$

* **【假設 1】 加熱的形狀 (Shape of the heating)：** 緯向是半寬 $a_0$ 的升餘弦「帽子」、經向是中心在 $y_0$、$e$-folding 寬度為 $b_0$ 的高斯

  $$\hat{Q}\left(\xi, y\right) = \frac{1}{2}Q_0\exp\left[-\left(\frac{y - y_0}{b_0}\right)^{2}\right]
  \begin{cases}
  1 + \cos\dfrac{\pi\xi}{a_0}, & \left|\xi\right| \le a_0 \\
  0, & \left|\xi\right| \ge a_0
  \end{cases}$$

  * $Q_0$ : 加熱率的峰值 (Peak heating rate) $[\text{J}\cdot\text{kg}^{-1}\cdot\text{s}^{-1}]$，$Q_0/c_p = 12 \ \text{K}\cdot\text{day}^{-1}$
  * $a_0$ : 對流區的緯向半寬 (Zonal half-width) $[\text{m}]$，$a_0 = 1250 \ \text{km}$
  * $b_0$ : 對流區的經向 $e$-folding 寬度 (Meridional $e$-folding width) $[\text{m}]$，$b_0 = 450 \ \text{km}$
  * $y_0$ : 對流中心的緯向偏移 (Meridional offset of the convection center) $[\text{m}]$，$y_0 = 0$ 或 $450 \ \text{km}$
  * $\hat{Q}$ : 加熱率的水平結構函數 (Horizontal structure function of the heating rate) $[\text{J}\cdot\text{kg}^{-1}\cdot\text{s}^{-1}]$
  * $\xi$ : 隨波緯向座標 (Translating zonal coordinate) $[\text{m}]$
  * 註：緯向形狀在 $\left|\xi\right| = a_0$ 處**連續且一階可微**（$1 + \cos\pi = 0$、$\sin\pi = 0$），因此傅立葉係數隨 $m$ 衰減得夠快。

* **【假設 2】 對流區小於全球 (The convective region is smaller than the globe)：** 積分範圍可從 $\left[-\pi a,\ \pi a\right]$ 縮到 $\left[-a_0,\ a_0\right]$

  $$a_0 < \pi a$$

  * $a$ : 地球半徑 (Earth's radius) $[\text{m}]$，$a = 6370 \ \text{km}$
  * $a_0$ : 對流區的緯向半寬 (Zonal half-width) $[\text{m}]$，$a_0 = 1250 \ \text{km}$

* **【假設 3】 無因次寬度在【已知 4】的適用範圍內 (Dimensionless width within the valid range)：** 把本篇採用的加熱寬度 $b_0 = 450 \ \text{km}$ 換算成無因次量後約為 $0.335$，小於【已知 4】投影公式要求的上界 $2^{1/2}$，因此該公式可以直接套用而不必另做延拓。

  $$\begin{gather*}
  \hat{b}_0 &\overset{\text{已知 2}}{=}& \epsilon^{1/4}\frac{b_0}{a} \\
  &\approx& 4.746 \times \frac{450}{6370} \\
  &\approx& 0.335 \\
  &<& 2^{1/2}
  \end{gather*}$$

  * $\hat{b}_0,\ \hat{y}_0$ : 無因次的加熱寬度與偏移 (Dimensionless width and offset) $[\text{無單位}]$
  * $\epsilon$ : Lamb 參數 (Lamb's parameter) $[\text{無單位}]$，$\epsilon \approx 507.3$
  * $b_0$ : 對流區的經向 $e$-folding 寬度 (Meridional $e$-folding width) $[\text{m}]$，$b_0 = 450 \ \text{km}$
  * $a$ : 地球半徑 (Earth's radius) $[\text{m}]$，$a = 6370 \ \text{km}$

* **【定義 1】 無因次的加熱寬度與偏移 (Dimensionless width and offset of the heating)：** 沿用【已知 2】的 $\hat{y}$ 尺度

  * (a) 無因次寬度：

    $$\hat{b}_0 \overset{\text{def}}{=} \epsilon^{1/4}\frac{b_0}{a}$$

  * (b) 無因次偏移：

    $$\hat{y}_0 \overset{\text{def}}{=} \epsilon^{1/4}\frac{y_0}{a}$$

  * $\hat{b}_0,\ \hat{y}_0$ : 無因次的加熱寬度與偏移 (Dimensionless width and offset) $[\text{無單位}]$
  * $\epsilon$ : Lamb 參數 (Lamb's parameter) $[\text{無單位}]$，$\epsilon \approx 507.3$
  * $b_0$ : 對流區的經向 $e$-folding 寬度 (Meridional $e$-folding width) $[\text{m}]$，$b_0 = 450 \ \text{km}$
  * $a$ : 地球半徑 (Earth's radius) $[\text{m}]$，$a = 6370 \ \text{km}$
  * $\hat{y}$ : 無因次經向座標 (Dimensionless meridional coordinate) $[\text{無單位}]$，$\hat{y} = \epsilon^{1/4}y/a$
  * $y_0$ : 對流中心的緯向偏移 (Meridional offset of the convection center) $[\text{m}]$，$y_0 = 0$ 或 $450 \ \text{km}$
  * 註：由【已知 2】$\hat{y} = \epsilon^{1/4}y/a$，可知 $\dfrac{y - y_0}{b_0} = \dfrac{\hat{y} - \hat{y}_0}{\hat{b}_0}$ —— **高斯的形狀在無因次座標下完全不變**，這是【證明 (c)】能直接套用【已知 4】的原因。

* **【定義 2】 緯向波數的無因次組合 (Dimensionless combination of the zonal wavenumber)：** 對流半寬對應的無因次波數

  $$\mu \overset{\text{def}}{=} \frac{m a_0}{a}$$

  * $\mu$ : 對流半寬對應的無因次波數 (Dimensionless wavenumber scaled by the half-width) $[\text{無單位}]$
  * $m$ : 緯向波數 (Zonal wavenumber) $[\text{無單位}]$，整數
  * $a$ : 地球半徑 (Earth's radius) $[\text{m}]$，$a = 6370 \ \text{km}$
  * $a_0$ : 對流區的緯向半寬 (Zonal half-width) $[\text{m}]$，$a_0 = 1250 \ \text{km}$

* **【推導 1】 加熱總量 (Total heating)：** 緯向與經向的積分各自獨立

  * (a) 緯向積分（$\cos$ 在整週期上積分為零）：

    $$\begin{gather*}
    \int_{-a_0}^{a_0}\frac{1}{2}\left[1 + \cos\frac{\pi\xi}{a_0}\right]d\xi &=& \frac{1}{2}\left[2a_0 + \left.\frac{a_0}{\pi}\sin\frac{\pi\xi}{a_0}\right|_{-a_0}^{a_0}\right] \\
    &=& \frac{1}{2}\left[2a_0 + 0\right] \\
    &=& a_0
    \end{gather*}$$

  * (b) 經向積分（換元 $s = \left(y - y_0\right)/b_0$）：

    $$\begin{gather*}
    \int_{-\infty}^{\infty}\exp\left[-\left(\frac{y - y_0}{b_0}\right)^{2}\right]dy &=& b_0\int_{-\infty}^{\infty}e^{-s^{2}}\,ds \\
    &\overset{\text{已知 6}}{=}& \pi^{1/2}b_0
    \end{gather*}$$

  * $a$ : 地球半徑 (Earth's radius) $[\text{m}]$，$a = 6370 \ \text{km}$
  * $\xi$ : 隨波緯向座標 (Translating zonal coordinate) $[\text{m}]$
  * $y_0$ : 對流中心的緯向偏移 (Meridional offset of the convection center) $[\text{m}]$，$y_0 = 0$ 或 $450 \ \text{km}$
  * $b_0$ : 對流區的經向 $e$-folding 寬度 (Meridional $e$-folding width) $[\text{m}]$，$b_0 = 450 \ \text{km}$
  * $s$ : 積分變數 (Integration variable) $[\text{依應用而定}]$
  * $a_0$ : 對流區的緯向半寬 (Zonal half-width) $[\text{m}]$，$a_0 = 1250 \ \text{km}$

* **【推導 2】 升餘弦帽子的傅立葉積分 (Fourier integral of the raised-cosine hat)：** 兩段各自算，最後合併時分母恰好湊成 $\pi^{2} - \mu^{2}$

  * (a) 常數項那一段：

    $$\begin{gather*}
    \int_{-a_0}^{a_0}e^{-i\mu\xi/a_0}\,d\xi &=& \left.\frac{a_0}{-i\mu}e^{-i\mu\xi/a_0}\right|_{-a_0}^{a_0} \\
    &=& \frac{a_0}{-i\mu}\left[e^{-i\mu} - e^{i\mu}\right] \\
    &=& \frac{2a_0\sin\mu}{\mu}
    \end{gather*}$$

  * (b) 餘弦項那一段（被積函數的虛部為奇函數，積分為零，故只留餘弦）：

    $$\begin{gather*}
    \int_{-a_0}^{a_0}\cos\left(\frac{\pi\xi}{a_0}\right)e^{-i\mu\xi/a_0}\,d\xi &=& \int_{-a_0}^{a_0}\cos\left(\frac{\pi\xi}{a_0}\right)\cos\left(\frac{\mu\xi}{a_0}\right)d\xi \\
    &\overset{\text{已知 5}}{=}& \frac{1}{2}\int_{-a_0}^{a_0}\left[\cos\frac{\left(\pi + \mu\right)\xi}{a_0} + \cos\frac{\left(\pi - \mu\right)\xi}{a_0}\right]d\xi \\
    &=& \frac{a_0\sin\left(\pi + \mu\right)}{\pi + \mu} + \frac{a_0\sin\left(\pi - \mu\right)}{\pi - \mu} \\
    &=& -\frac{a_0\sin\mu}{\pi + \mu} + \frac{a_0\sin\mu}{\pi - \mu} \\
    &=& \frac{2a_0\,\mu\sin\mu}{\pi^{2} - \mu^{2}}
    \end{gather*}$$

  * (c) 兩段相加，$\mu^{2}$ 對消：

    $$\begin{gather*}
    \int_{-a_0}^{a_0}\left[1 + \cos\frac{\pi\xi}{a_0}\right]e^{-i\mu\xi/a_0}\,d\xi &\overset{\text{推導 2(a)(b)}}{=}& 2a_0\sin\mu\left[\frac{1}{\mu} + \frac{\mu}{\pi^{2} - \mu^{2}}\right] \\
    &=& 2a_0\sin\mu\cdot\frac{\pi^{2} - \mu^{2} + \mu^{2}}{\mu\left(\pi^{2} - \mu^{2}\right)} \\
    &=& \frac{2\pi^{2}a_0\sin\mu}{\mu\left(\pi^{2} - \mu^{2}\right)}
    \end{gather*}$$

  * $a$ : 地球半徑 (Earth's radius) $[\text{m}]$，$a = 6370 \ \text{km}$
  * $\mu$ : 對流半寬對應的無因次波數 (Dimensionless wavenumber scaled by the half-width) $[\text{無單位}]$
  * $\xi$ : 隨波緯向座標 (Translating zonal coordinate) $[\text{m}]$
  * $a_0$ : 對流區的緯向半寬 (Zonal half-width) $[\text{m}]$，$a_0 = 1250 \ \text{km}$
  * $i$ : 虛數單位 (Imaginary unit) $[\text{無單位}]$，$i^{2} = -1$

* **【推導 3】 經向積分的兩次套用 (Two applications of the meridional integral)：** 把【已知 4】分別取 $k = n+1$ 與 $k = n-1$

  $$\begin{gather*}
  \int_{-\infty}^{\infty}\exp\left[-\frac{\left(\hat{y} - \hat{y}_0\right)^{2}}{\hat{b}_0^{2}}\right]\left[\mathcal{P}_{mnr}\mathcal{H}_{n+1} - \mathcal{M}_{mnr}\mathcal{H}_{n-1}\right]d\hat{y}
  &\overset{\text{已知 4,假設 3}}{=}& \left(\frac{2\pi\hat{b}_0^{2}}{2 + \hat{b}_0^{2}}\right)^{1/2}\exp\left[\frac{\hat{b}_0^{2}\hat{y}_0^{2}}{4 - \hat{b}_0^{4}}\right] \\
  && \times\left[\mathcal{P}_{mnr}\,\chi^{(n+1)/2}\mathcal{H}_{n+1}(\eta) - \mathcal{M}_{mnr}\,\chi^{(n-1)/2}\mathcal{H}_{n-1}(\eta)\right]
  \end{gather*}$$

  * $\mathcal{P}_{mnr},\ \mathcal{M}_{mnr}$ : 上下行振幅 (Upper and lower branch amplitudes) $[\text{無單位}]$，$\mathcal{P}_{mnr} = \left(\epsilon^{1/2}\hat{\nu}_{mnr} + m\right)\left(\frac{n+1}{2}\right)^{1/2}$、$\mathcal{M}_{mnr} = \left(\epsilon^{1/2}\hat{\nu}_{mnr} - m\right)\left(\frac{n}{2}\right)^{1/2}$
  * $\hat{y}$ : 無因次經向座標 (Dimensionless meridional coordinate) $[\text{無單位}]$，$\hat{y} = \epsilon^{1/4}y/a$
  * $\hat{b}_0,\ \hat{y}_0$ : 無因次的加熱寬度與偏移 (Dimensionless width and offset) $[\text{無單位}]$
  * $\mathcal{H}_n$ : 歸一化 Hermite 函數 (Normalized Hermite function) $[\text{無單位}]$
  * $\chi$ : 階數壓縮比 (Order-compression ratio) $[\text{無單位}]$
  * $\eta$ : 生成函數的自變數位置（本檔會代入不同的值）(Argument of the generating function) $[\text{無單位}]$
  * 註：這兩個振幅的定義沿用 [赤道波本徵函數](Equatorial_Wave_Eigenfunctions.md)【定義 1】。

* **【推導 4】 前因子的整理 (Tidying up the prefactor)：** 把 $\dfrac{\sin\mu}{m}$ 與 $\hat{b}_0$ 換成論文的寫法

  $$\begin{gather*}
  \frac{\sin\mu}{m}\,\hat{b}_0 &\overset{\text{定義 2}}{=}& \frac{\sin\mu}{\mu}\cdot\frac{a_0}{a}\cdot\hat{b}_0 \\
  &\overset{\text{定義 1(a)}}{=}& \frac{\sin\mu}{\mu}\cdot\frac{a_0}{a}\cdot\frac{\epsilon^{1/4}b_0}{a} \\
  &=& \epsilon^{1/4}\frac{a_0\,b_0}{a^{2}}\cdot\frac{\sin\mu}{\mu}
  \end{gather*}$$

  * $\mu$ : 對流半寬對應的無因次波數 (Dimensionless wavenumber scaled by the half-width) $[\text{無單位}]$
  * $m$ : 緯向波數 (Zonal wavenumber) $[\text{無單位}]$，整數
  * $\hat{b}_0,\ \hat{y}_0$ : 無因次的加熱寬度與偏移 (Dimensionless width and offset) $[\text{無單位}]$
  * $a$ : 地球半徑 (Earth's radius) $[\text{m}]$，$a = 6370 \ \text{km}$
  * $\epsilon$ : Lamb 參數 (Lamb's parameter) $[\text{無單位}]$，$\epsilon \approx 507.3$
  * $b_0$ : 對流區的經向 $e$-folding 寬度 (Meridional $e$-folding width) $[\text{m}]$，$b_0 = 450 \ \text{km}$
  * $a_0$ : 對流區的緯向半寬 (Zonal half-width) $[\text{m}]$，$a_0 = 1250 \ \text{km}$

* **【推導 5】 Hermite 函數在原點的奇偶性 (Parity of the Hermite functions at the origin)：** $\mathcal{H}_k$ 的宇稱與 $k$ 相同，故奇階在原點為零

  $$\begin{gather*}
  \mathcal{H}_k(-\hat{y}) &=& \left(-1\right)^{k}\mathcal{H}_k(\hat{y}) \\
  \mathcal{H}_k(0) &=& \left(-1\right)^{k}\mathcal{H}_k(0) \\
  \mathcal{H}_k(0) &=& 0 \qquad \left(k \ \text{為奇數}\right)
  \end{gather*}$$

  * $\mathcal{H}_k$ : 歸一化 Hermite 函數 (Normalized Hermite function) $[\text{無單位}]$
  * $k$ : Hermite 函數的階數 (Order of the Hermite function) $[\text{無單位}]$
  * $\hat{y}$ : 無因次經向座標 (Dimensionless meridional coordinate) $[\text{無單位}]$，$\hat{y} = \epsilon^{1/4}y/a$
  * 註：第一列的宇稱性質由 [Hermite Functions and Recurrence](../Differential_Equations/Hermite_Functions_and_Recurrence.md)【證明 (a)】的遞迴關係對 $k$ 歸納即得（$\mathcal{H}_0$ 偶、$\mathcal{H}_1$ 奇，而 $\hat{y}\mathcal{H}_k$ 的宇稱與 $\mathcal{H}_k$ 相反）。

+++

## 證明:

### (a) proof 加熱總量與 $y_0$ 無關 (The total heating is independent of $y_0$)

兩個方向的積分各自算完再相乘；經向積分換元後 $y_0$ 完全消失。

$$\begin{gather*}
\iint \hat{Q}\left(\xi, y\right)d\xi\,dy &\overset{\text{假設 1}}{=}& Q_0\left[\int_{-a_0}^{a_0}\frac{1}{2}\left(1 + \cos\frac{\pi\xi}{a_0}\right)d\xi\right]\left[\int_{-\infty}^{\infty}\exp\left[-\left(\frac{y - y_0}{b_0}\right)^{2}\right]dy\right] \\
&\overset{\text{推導 1(a)(b)}}{=}& Q_0\cdot a_0\cdot\pi^{1/2}b_0 \\
&=& \pi^{1/2}Q_0\,a_0\,b_0
\end{gather*}$$

### (b) proof 緯向傅立葉係數 (Zonal Fourier coefficient)

積分範圍由【假設 2】縮到對流區內，緯向部分由【推導 2】算掉，經向部分整個提出來。

$$\begin{gather*}
\hat{Q}_m(y) &\overset{\text{已知 1,假設 1}}{=}& \frac{1}{2\pi a}\cdot\frac{Q_0}{2}\exp\left[-\left(\frac{y - y_0}{b_0}\right)^{2}\right]\int_{-\pi a}^{\pi a}\left[1 + \cos\frac{\pi\xi}{a_0}\right]_{\left|\xi\right| \le a_0}e^{-im\xi/a}\,d\xi \\
&\overset{\text{假設 2,定義 2}}{=}& \frac{Q_0}{4\pi a}\exp\left[-\left(\frac{y - y_0}{b_0}\right)^{2}\right]\int_{-a_0}^{a_0}\left[1 + \cos\frac{\pi\xi}{a_0}\right]e^{-i\mu\xi/a_0}\,d\xi \\
&\overset{\text{推導 2(c)}}{=}& \frac{Q_0}{4\pi a}\cdot\frac{2\pi^{2}a_0\sin\mu}{\mu\left(\pi^{2} - \mu^{2}\right)}\exp\left[-\left(\frac{y - y_0}{b_0}\right)^{2}\right] \\
&\overset{\text{定義 2}}{=}& \frac{\pi Q_0}{2\left(\pi^{2} - \mu^{2}\right)}\cdot\frac{a_0}{a\mu}\sin\mu\,\exp\left[-\left(\frac{y - y_0}{b_0}\right)^{2}\right] \\
&\overset{\text{定義 2}}{=}& \frac{\pi Q_0}{2\left[\pi^{2} - \left(ma_0/a\right)^{2}\right]}\frac{\sin\left(ma_0/a\right)}{m}\exp\left[-\left(\frac{y - y_0}{b_0}\right)^{2}\right]
\end{gather*}$$

### (c) proof 模態投影（$n \ge 0$）(Modal projection for $n \ge 0$)

強迫向量只有第三分量，故內積只剩一項；把【證明 (b)】與【已知 2】(a) 代進去，經向積分由【推導 3】算掉，前因子由【推導 4】整理。

$$\begin{gather*}
\hat{Q}_{mnr} &\overset{\text{已知 3,已知 2(c)}}{=}& \frac{1}{\bar{c}^{2}}\int_{-\infty}^{\infty}\hat{Q}_m\,\Phi_{mnr}^{*}\,d\hat{y} \\
&\overset{\text{證明 (b),已知 2(a),定義 1}}{=}& \frac{A_{mnr}\,\epsilon^{1/4}}{\bar{c}}\cdot\frac{\pi Q_0}{2\left(\pi^{2} - \mu^{2}\right)}\frac{\sin\mu}{m}\int_{-\infty}^{\infty}\exp\left[-\frac{\left(\hat{y} - \hat{y}_0\right)^{2}}{\hat{b}_0^{2}}\right]\left[\mathcal{P}_{mnr}\mathcal{H}_{n+1} - \mathcal{M}_{mnr}\mathcal{H}_{n-1}\right]d\hat{y} \\
&\overset{\text{推導 3}}{=}& \frac{A_{mnr}\,\epsilon^{1/4}\,\pi Q_0}{2\bar{c}\left(\pi^{2} - \mu^{2}\right)}\frac{\sin\mu}{m}\,\hat{b}_0\left(\frac{2\pi}{2 + \hat{b}_0^{2}}\right)^{1/2}\exp\left[\frac{\hat{b}_0^{2}\hat{y}_0^{2}}{4 - \hat{b}_0^{4}}\right]\left[\mathcal{P}_{mnr}\chi^{(n+1)/2}\mathcal{H}_{n+1}(\eta) - \mathcal{M}_{mnr}\chi^{(n-1)/2}\mathcal{H}_{n-1}(\eta)\right] \\
&\overset{\text{推導 4}}{=}& \frac{A_{mnr}\,\epsilon^{1/2}\,\pi Q_0\,a_0\,b_0}{2\bar{c}\,a^{2}\left(\pi^{2} - \mu^{2}\right)}\frac{\sin\mu}{\mu}\left(\frac{2\pi}{2 + \hat{b}_0^{2}}\right)^{1/2}\exp\left[\frac{\hat{b}_0^{2}\hat{y}_0^{2}}{4 - \hat{b}_0^{4}}\right]\left[\mathcal{P}_{mnr}\chi^{(n+1)/2}\mathcal{H}_{n+1}(\eta) - \mathcal{M}_{mnr}\chi^{(n-1)/2}\mathcal{H}_{n-1}(\eta)\right]
\end{gather*}$$

### (d) proof Kelvin 波的模態投影 (Modal projection for the Kelvin wave)

同【證明 (c)】的路線，但本徵函數只剩單一個 $\mathcal{H}_0$，$\pi^{1/4}$ 與 $\mathcal{H}_0(\eta)$ 裡的 $\pi^{-1/4}$ 恰好對消。

$$\begin{gather*}
\hat{Q}_{m,-1,2} &\overset{\text{已知 3,已知 2(b)(c)}}{=}& \frac{A_{m,-1,2}\,\pi^{1/4}}{\bar{c}}\cdot\frac{\pi Q_0}{2\left(\pi^{2} - \mu^{2}\right)}\frac{\sin\mu}{m}\int_{-\infty}^{\infty}\exp\left[-\frac{\left(\hat{y} - \hat{y}_0\right)^{2}}{\hat{b}_0^{2}}\right]\mathcal{H}_0(\hat{y})\,d\hat{y} \\
&\overset{\text{已知 4}}{=}& \frac{A_{m,-1,2}\,\pi^{1/4}\,\pi Q_0}{2\bar{c}\left(\pi^{2} - \mu^{2}\right)}\frac{\sin\mu}{m}\,\hat{b}_0\left(\frac{2\pi}{2 + \hat{b}_0^{2}}\right)^{1/2}\exp\left[\frac{\hat{b}_0^{2}\hat{y}_0^{2}}{4 - \hat{b}_0^{4}}\right]\mathcal{H}_0(\eta) \\
&\overset{\text{已知 2}}{=}& \frac{A_{m,-1,2}\,\pi Q_0}{2\bar{c}\left(\pi^{2} - \mu^{2}\right)}\frac{\sin\mu}{m}\,\hat{b}_0\left(\frac{2\pi}{2 + \hat{b}_0^{2}}\right)^{1/2}\exp\left[\frac{\hat{b}_0^{2}\hat{y}_0^{2}}{4 - \hat{b}_0^{4}} - \frac{\eta^{2}}{2}\right] \\
&\overset{\text{已知 4}}{=}& \frac{A_{m,-1,2}\,\pi Q_0}{2\bar{c}\left(\pi^{2} - \mu^{2}\right)}\frac{\sin\mu}{m}\,\hat{b}_0\left(\frac{2\pi}{2 + \hat{b}_0^{2}}\right)^{1/2}\exp\left[-\frac{\hat{y}_0^{2}}{2 + \hat{b}_0^{2}}\right] \\
&\overset{\text{推導 4}}{=}& \frac{A_{m,-1,2}\,\epsilon^{1/4}\,\pi Q_0\,a_0\,b_0}{2\bar{c}\,a^{2}\left(\pi^{2} - \mu^{2}\right)}\frac{\sin\mu}{\mu}\left(\frac{2\pi}{2 + \hat{b}_0^{2}}\right)^{1/2}\exp\left[-\frac{\hat{y}_0^{2}}{2 + \hat{b}_0^{2}}\right]
\end{gather*}$$

### (e) proof 對流正對赤道時偶模態不被激發 (Even modes are not excited when the convection is centred on the equator)

$\hat{y}_0 = 0$ 時【已知 4】的自變數 $\eta$ 歸零，兩個 $\mathcal{H}$ 都在原點取值。$n$ 為偶數時 $n \pm 1$ 皆為**奇數**，兩項同時歸零。

$$\begin{gather*}
\left.\eta\right|_{\hat{y}_0 = 0} &\overset{\text{已知 4}}{=}& \frac{2 \times 0}{\left(4 - \hat{b}_0^{4}\right)^{1/2}} \\
\left.\eta\right|_{\hat{y}_0 = 0} &=& 0 \\
\left.\hat{Q}_{mnr}\right|_{\hat{y}_0 = 0} &\overset{\text{證明 (c)}}{\propto}& \mathcal{P}_{mnr}\chi^{(n+1)/2}\mathcal{H}_{n+1}(0) - \mathcal{M}_{mnr}\chi^{(n-1)/2}\mathcal{H}_{n-1}(0) \\
\left.\hat{Q}_{mnr}\right|_{\hat{y}_0 = 0} &\overset{\text{推導 5}}{=}& \mathcal{P}_{mnr}\chi^{(n+1)/2}\cdot 0 - \mathcal{M}_{mnr}\chi^{(n-1)/2}\cdot 0 \\
\left.\hat{Q}_{mnr}\right|_{\hat{y}_0 = 0} &=& 0
\end{gather*}$$

+++

## 物理解釋

### 三個因子各自控制什麼被激發

【證明 (c)】的結果可以拆成三個獨立的「篩子」：

$$\hat{Q}_{mnr} \propto \underbrace{\frac{1}{\pi^{2} - \mu^{2}}\frac{\sin\mu}{\mu}}_{\text{緯向篩子：}a_0\text{ 決定}}\times\underbrace{\chi^{(n\pm1)/2}}_{\text{經向篩子：}b_0\text{ 決定}}\times\underbrace{\mathcal{H}_{n\pm1}(\eta)}_{\text{對稱性篩子：}y_0\text{ 決定}}$$

* **緯向篩子** —— $\dfrac{\sin\mu}{\mu}$ 是「有限寬度帽子」在波數空間的指紋。$\mu = \dfrac{ma_0}{a}$，代入 $a_0 = 1250 \ \text{km}$、$a = 6370 \ \text{km}$ 得 $\mu \approx 0.196\,m$。第一個零點在 $\mu = \pi$，即 $m \approx 16$ —— **緯向波數 $16$ 以上的模態幾乎不被激發**。$a_0$ 愈寬，被激發的波數愈少愈長。
* **經向篩子** —— $\chi = \dfrac{2 - \hat{b}_0^{2}}{2 + \hat{b}_0^{2}}$，代入【假設 3】的 $\hat{b}_0 \approx 0.335$ 得 $\chi \approx 0.894$。所以係數隨 $n$ 按 $0.894^{n/2}$ 衰減，$n = 200$ 時已降到 $\sim 10^{-5}$ —— **這就是論文說「$N = 200$ 截斷已足夠準確」的數學根據**。
* **對稱性篩子** —— 見下一節。

### $y_0$ 為什麼是本文最乾淨的對照變數

【證明 (a)】說：**總加熱量 $\pi^{1/2}Q_0a_0b_0$ 完全不隨 $y_0$ 改變**。

於是比較 $y_0 = 0$ 與 $y_0 = 450 \ \text{km}$ 兩組實驗時，兩者「加了多少熱」一模一樣，差別**純粹來自「熱加在哪裡」**。這是一個設計得很好的對照實驗。

而【證明 (e)】給出差別的機制：$y_0 = 0$ 時 $\eta = 0$，**所有偶數 $n$ 的模態係數嚴格為零**。

用宇稱把它讀一遍會更清楚。加熱在 $y_0 = 0$ 時是 $y$ 的**偶函數**，而由【已知 2】(a)，本徵函數的位勢分量 $\Phi_{mnr} \propto \mathcal{H}_{n\pm1}$：

| $n$ | $\Phi_{mnr}$ 的宇稱 | 與偶函數加熱的重疊 | 結果 |
|---|---|---|---|
| 偶（含 $n = 0$ 混合羅斯貝–重力波） | **奇** | 偶 $\times$ 奇 $\Rightarrow$ 積分為零 | **不被激發** |
| 奇（含 $n = -1$ Kelvin 波、$n = 1$ 起的羅斯貝波） | **偶** | 偶 $\times$ 偶 | 被激發 |

這正是論文所述「$y_0 = 0$ 時混合羅斯貝–重力波（$r = 0$、$n = 0$）的貢獻恰好消失」的數學原因，也解釋了為什麼 Kelvin 波（$n = -1$）不受影響 —— 它落在「奇」那一列。

$y_0 = 450 \ \text{km}$ 時開關被打開，但打開得不多：$\hat{y}_0 = \epsilon^{1/4}\times\dfrac{450}{6370} \approx 0.335$ 仍然很小，故論文說混合羅斯貝–重力波的貢獻「很小」而非「顯著」。

**一句話：把對流從赤道移開，等於打開了「反對稱響應」這個開關。** 尾流的南北不對稱、北半球 PV 距平強了近一倍，全部從這裡來。

### 這一篇填上了端點①的最後一塊

到此為止，[受迫解](Forced_Response_of_Equatorial_Modes.md)【證明 (c)】的右端已經完全顯式：

$$\hat{\eta}_{mnr} = \frac{\kappa\hat{Q}_{mnr}}{\alpha + i\left(\nu_{mnr} - cm/a\right)}$$

分子由本篇【證明 (c)(d)】給出、分母由 [頻散關係](Matsuno_Dispersion_Relation.md) 給出。**所有譜係數都算得出來了。**

剩下的只有「把譜係數轉回物理空間」，那是 [場還原與 Kelvin 波零 PV](Physical_Field_Recovery_and_Zero_Kelvin_PV.md) 的事。
