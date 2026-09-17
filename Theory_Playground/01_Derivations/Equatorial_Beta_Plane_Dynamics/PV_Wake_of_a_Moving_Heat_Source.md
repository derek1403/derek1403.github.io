# PV Wake of a Moving Heat Source (移動熱源的 PV 尾流與三個控制參數)

+++

## 證明目標:

**端點②。** 刻意把 [PV 方程式](Equatorial_PV_Equation_and_Beta_y_Source.md) 中的 Rossby 項 $\beta v$ **拿掉**，
只留「強迫 ＋ 耗散」。這樣做的方程式可以**解析求解**，控制 PV 尾流的參數就被逼出來。

* (a) 拿掉 $\beta v$ 並在隨波座標下定常化後的方程式：

$$c\frac{\partial q}{\partial \xi} = \alpha q - \frac{\beta y}{c_p\Gamma}\left(\frac{\partial}{\partial z} - 1\right)Q$$

* (b) 其解析解 —— 三個因子的乘積：

$$q\left(\xi, y, z\right) = -\frac{\tau_{\mathrm{p}}}{\tau_{\mathrm{c}}}\left(\frac{\pi^{2}}{\pi^{2} + \alpha^{2}\tau_{\mathrm{p}}^{2}}\right)F(\xi)\,\beta y\exp\left[-\left(\frac{y - y_0}{b_0}\right)^{2}\right]Z(z)$$

* (c) 緯向結構函數在對流**後方**（$-\infty < \xi \le -a_0$）是指數尾巴：

$$F(\xi) = \frac{\sinh\left[\left(\alpha/c\right)a_0\right]}{\left(\alpha/c\right)a_0}\exp\left[\frac{\alpha}{c}\xi\right]$$

* (d) 在對流**內部**（$-a_0 \le \xi \le a_0$）：

$$F(\xi) = \frac{1 - \exp\left[-\left(\alpha/c\right)\left(a_0 - \xi\right)\right]}{2\left(\alpha/c\right)a_0} + \frac{\alpha a_0}{2\pi^{2}c}\left[1 + \cos\frac{\pi\xi}{a_0}\right] - \frac{1}{2\pi}\sin\frac{\pi\xi}{a_0}$$

* (e) 在對流**前方**（$a_0 \le \xi < \infty$）恆為零：

$$F(\xi) = 0$$

* (f) 三個控制參數的數值：

$$\frac{c}{\alpha} \approx 1728 \ \text{km}, \qquad \frac{\tau_{\mathrm{p}}}{\tau_{\mathrm{c}}} \approx 5.9, \qquad \frac{y_0}{b_0} = 0 \ \text{或} \ 1$$

其中

* $q$ : 位渦距平 (PV anomaly) $[\text{s}^{-1}]$
* $F(\xi)$ : 位渦的緯向結構函數 (Zonal structure function of the PV) $[\text{無單位}]$
* $Q$ : 非絕熱加熱率 (Diabatic heating rate) $[\text{J}\cdot\text{kg}^{-1}\cdot\text{s}^{-1}]$
* $v$ : 擾動經向風速 (Perturbation meridional velocity) $[\text{m}\cdot\text{s}^{-1}]$
* $Z(z)$ : 垂直結構函數 (Vertical structure function) $[\text{無單位}]$
* $\xi$ : 隨波緯向座標 (Translating zonal coordinate) $[\text{m}]$
* $x,\ y$ : 緯向、經向座標 (Zonal and meridional coordinates) $[\text{m}]$
* $z$ : 對數氣壓垂直座標 (Log-pressure vertical coordinate) $[\text{無單位}]$
* $\alpha$ : 常數阻尼率 (Constant damping rate) $[\text{s}^{-1}]$，$\alpha = \left(4 \ \text{days}\right)^{-1}$
* $\beta$ : 赤道 $\beta$ 參數 (Equatorial beta parameter) $[\text{m}^{-1}\cdot\text{s}^{-1}]$
* $\Gamma$ : 靜力穩定度 (Static stability) $[\text{K}]$
* $c_p$ : 定壓比熱 (Specific heat at constant pressure) $[\text{J}\cdot\text{kg}^{-1}\cdot\text{K}^{-1}]$
* $c$ : 對流包絡的東移速度 (Eastward propagation speed) $[\text{m}\cdot\text{s}^{-1}]$，$c = 5 \ \text{m}\cdot\text{s}^{-1}$
* $a_0$ : 對流區的緯向半寬 (Zonal half-width) $[\text{m}]$，$a_0 = 1250 \ \text{km}$
* $b_0$ : 對流區的經向 $e$-folding 寬度 (Meridional $e$-folding width) $[\text{m}]$，$b_0 = 450 \ \text{km}$
* $y_0$ : 對流中心的經向偏移 (Meridional offset) $[\text{m}]$
* $\tau_{\mathrm{p}}$ : 通過時間 (Passage time) $[\text{s}]$
* $\tau_{\mathrm{c}}$ : 對流翻轉時間 (Convective overturning time) $[\text{s}]$
* 註：(a)–(e) 就是 [Schubert & Masarik (2006)](../../06_References/Tropical_wave_dynamics/Schubert2006-Potential_vorticity_aspects_of_the_MJO/Potential_vorticity_aspects_of_the_MJO.ipynb) 的 $(5.1)$–$(5.4)$。
* 註：**這是一個刻意做壞的解。** 把它與完整解（[場還原](Physical_Field_Recovery_and_Zero_Kelvin_PV.md)）相比，論文發現忽略 $\beta v$ 的 $q$ 場**只有正確強度的 $68\%$**，而且往極側、往西側都伸展不夠遠。**拆掉一項再看差多少**，正是這一節的方法論價值。

+++

## 假設與已知 (Assumptions & Preliminaries)

* **【已知 1】 [赤道 PV 方程式 (Equatorial PV equation)](https://derek1403.github.io/Theory_Playground/_build/html/01_Derivations/Equatorial_Beta_Plane_Dynamics/Equatorial_PV_Equation_and_Beta_y_Source.html#a-proof-pv-potential-vorticity-equation)：** 位渦距平的收支：時間變化加上 $\beta v$ 的行星渦度平流，由阻尼消耗，並由加熱以 $\beta y$ 為權重的形式產生 ─ 右端的權重在赤道為零，這正是尾流只長在赤道兩側的原因。（已於本庫 [Equatorial PV Equation and the Beta-y Source](Equatorial_PV_Equation_and_Beta_y_Source.md)【證明 (a)】完整證明，此處直接引用。）

  $$\frac{\partial q}{\partial t} + \beta v = -\alpha q + \frac{\beta y}{c_p\Gamma}\left(\frac{\partial}{\partial z} - 1\right)Q$$

  * $q$ : 位渦距平 (PV anomaly) $[\text{s}^{-1}]$
  * $v$ : 擾動經向風速 (Perturbation meridional velocity) $[\text{m}\cdot\text{s}^{-1}]$
  * $Q$ : 非絕熱加熱率 (Diabatic heating rate) $[\text{J}\cdot\text{kg}^{-1}\cdot\text{s}^{-1}]$
  * $\alpha$ : 常數阻尼率 (Constant damping rate) $[\text{s}^{-1}]$，$\alpha = \left(4 \ \text{days}\right)^{-1}$
  * $\beta$ : 赤道 $\beta$ 參數 (Equatorial beta parameter) $[\text{m}^{-1}\cdot\text{s}^{-1}]$
  * $\Gamma$ : 靜力穩定度 (Static stability) $[\text{K}]$
  * $c_p$ : 定壓比熱 (Specific heat at constant pressure) $[\text{J}\cdot\text{kg}^{-1}\cdot\text{K}^{-1}]$
  * $t$ : 時間 (Time) $[\text{s}]$
  * $y_0$ : 對流中心的經向偏移 (Meridional offset) $[\text{m}]$
  * $z$ : 對數氣壓垂直座標 (Log-pressure vertical coordinate) $[\text{無單位}]$

* **【已知 2】 [垂直分離與加熱形狀 (Vertical separation and the shape of the heating)](https://derek1403.github.io/Theory_Playground/_build/html/01_Derivations/Equatorial_Beta_Plane_Dynamics/Projection_of_a_Moving_Heat_Source.html#assumptions-preliminaries)：** 本篇熱源的完整規格：垂直方向掛在 $Z'(z)$ 上，水平方向則是「經向高斯 × 緯向升餘弦帽子」，而 $Z$ 所滿足的垂直本徵方程同時定出等效重力波速 $\bar{c}$。（已於本庫 [Separation into the Horizontal Structure System](Separation_into_Horizontal_Structure_System.md) 與 [Projection of a Moving Heat Source](Projection_of_a_Moving_Heat_Source.md) 完整給出，此處直接引用。）

  * (a) 加熱的垂直分離：

    $$Q\left(\xi, y, z\right) = \hat{Q}\left(\xi, y\right)Z'(z)$$

  * (b) 加熱的形狀：

    $$\hat{Q}\left(\xi, y\right) = \frac{1}{2}Q_0\exp\left[-\left(\frac{y - y_0}{b_0}\right)^{2}\right]g(\xi), \qquad g(\xi) = \begin{cases}1 + \cos\dfrac{\pi\xi}{a_0}, & \left|\xi\right| \le a_0 \\ 0, & \left|\xi\right| \ge a_0\end{cases}$$

  * (c) 垂直結構方程式：

    $$\left(\frac{d}{dz} - 1\right)\frac{dZ}{dz} = -\lambda Z, \qquad \lambda = \frac{\pi^{2}}{z_T^{2}} + \frac{1}{4} = \frac{R\Gamma}{\bar{c}^{2}}$$

  * $Q_0$ : 加熱率的峰值 (Peak heating rate) $[\text{J}\cdot\text{kg}^{-1}\cdot\text{s}^{-1}]$，$Q_0/c_p = 12 \ \text{K}\cdot\text{day}^{-1}$
  * $a_0$ : 對流區的緯向半寬 (Zonal half-width) $[\text{m}]$，$a_0 = 1250 \ \text{km}$
  * $b_0$ : 對流區的經向 $e$-folding 寬度 (Meridional $e$-folding width) $[\text{m}]$，$b_0 = 450 \ \text{km}$
  * $y_0$ : 對流中心的經向偏移 (Meridional offset) $[\text{m}]$
  * $\bar{c}$ : 等效重力波速 (Equivalent gravity wave speed) $[\text{m}\cdot\text{s}^{-1}]$，$\bar{c} \approx 41.25 \ \text{m}\cdot\text{s}^{-1}$
  * $R$ : 乾空氣氣體常數 (Gas constant for dry air) $[\text{J}\cdot\text{kg}^{-1}\cdot\text{K}^{-1}]$
  * $\xi$ : 隨波緯向座標 (Translating zonal coordinate) $[\text{m}]$
  * $z$ : 對數氣壓垂直座標 (Log-pressure vertical coordinate) $[\text{無單位}]$
  * $\hat{Q}$ : 加熱率的水平結構函數 (Horizontal structure function of the heating rate) $[\text{J}\cdot\text{kg}^{-1}\cdot\text{s}^{-1}]$
  * $Z(z)$ : 垂直結構函數 (Vertical structure function) $[\text{無單位}]$
  * $Z'$ : 垂直結構函數 $Z$ 對 $z$ 的一階微分 (First derivative of the vertical structure function with respect to $z$) $[\text{無單位}]$，$Z' = \dfrac{dZ}{dz}$
  * $g(\xi)$ : 加熱的緯向形狀函數 (Zonal shape function of the heating) $[\text{無單位}]$
  * $\lambda$ : 第一內模態的分離常數 (Separation constant) $[\text{無單位}]$
  * $\Gamma$ : 靜力穩定度 (Static stability) $[\text{K}]$
  * $z_T$ : 對流層頂的對數氣壓高度 (Log-pressure height of the tropopause) $[\text{無單位}]$

* **【已知 3】 [隨波座標的導數替換 (Derivative replacement in the translating frame)](https://derek1403.github.io/Theory_Playground/_build/html/01_Derivations/Equatorial_Beta_Plane_Dynamics/Fourier_Transform_to_Shallow_Water_System.html#a-proof-derivative-replacement-in-the-translating-frame)：** 換到隨熱源移動的座標 $\xi = x - ct$ 後，場對時間定常，於是 $\partial/\partial t$ 整個變成 $-c\,\partial/\partial \xi$ ─ 這一步把偏微分方程降成對 $\xi$ 的常微分方程。（已於本庫 [Fourier Transform to the Shallow Water System](Fourier_Transform_to_Shallow_Water_System.md)【證明 (a)】完整證明，此處直接引用。）

  $$\frac{\partial}{\partial t} \to -c\frac{\partial}{\partial \xi}, \qquad \xi = x - ct$$

  * $c$ : 對流包絡的東移速度 (Eastward propagation speed) $[\text{m}\cdot\text{s}^{-1}]$，$c = 5 \ \text{m}\cdot\text{s}^{-1}$
  * $t$ : 時間 (Time) $[\text{s}]$
  * $\xi$ : 隨波緯向座標 (Translating zonal coordinate) $[\text{m}]$
  * $x,\ y$ : 緯向、經向座標 (Zonal and meridional coordinates) $[\text{m}]$

* **【已知 4】 [一階線性 ODE 的積分因子解 (Integrating-factor solution of a first-order linear ODE)](https://dlmf.nist.gov/1.13)：** 一階線性常微分方程的標準解法：左端乘上積分因子 $e^{-\sigma\xi}$ 之後恰好收成一個全微分，於是兩側直接積分即可 ─ 本篇的尾流解就是這樣一路積出來的。（標準結果，此處直接引用。）

  $$\frac{d\Psi}{d\xi} - \sigma\Psi = h(\xi) \quad \Longleftrightarrow \quad \frac{d}{d\xi}\left[e^{-\sigma\xi}\Psi\right] = h(\xi)\,e^{-\sigma\xi}$$

  * $\Psi(\xi)$ : 待解函數 (Unknown function) $[\text{依應用而定}]$
  * $\sigma$ : 常數係數 (Constant coefficient) $[\text{m}^{-1}]$
  * $h(\xi)$ : 強迫項 (Forcing term) $[\text{依應用而定}]$
  * $\xi$ : 隨波緯向座標 (Translating zonal coordinate) $[\text{m}]$

* **【已知 5】 指數與三角乘積的不定積分 (Antiderivative of an exponential times a cosine)：** 衰減指數乘上餘弦的不定積分：結果仍是同一個衰減指數，乘上 $\cos$ 與 $\sin$ 的線性組合；分母的 $\sigma^{2} + p^{2}$ 來自兩次分部積分後被積函數自我回歸所產生的係數。（標準結果，可對右端微分直接驗證。）

  $$\int e^{-\sigma s}\cos\left(ps\right)ds = \frac{e^{-\sigma s}}{\sigma^{2} + p^{2}}\left[-\sigma\cos\left(ps\right) + p\sin\left(ps\right)\right]$$

  * $p$ : 三角函數的波數 (Wavenumber) $[\text{m}^{-1}]$
  * $\sigma$ : 常數係數 (Constant coefficient) $[\text{m}^{-1}]$
  * $s$ : 積分變數 (Integration variable) $[\text{依應用而定}]$

* **【假設 1】 忽略 Rossby 項 (Neglect of the Rossby term)：** 本篇**刻意**把【已知 1】的 $\beta v$ 拿掉，只保留強迫與耗散

  $$\beta v \approx 0$$

  * $\beta$ : 赤道 $\beta$ 參數 (Equatorial beta parameter) $[\text{m}^{-1}\cdot\text{s}^{-1}]$
  * $v$ : 擾動經向風速 (Perturbation meridional velocity) $[\text{m}\cdot\text{s}^{-1}]$
  * 註：這是一個**已知會失準的假設**，目的是診斷而非求真解。與完整解相比，忽略 $\beta v$ 的 $q$ 場只有正確強度的 $68\%$；差額來自「低層經向風把基本態 PV 往赤道方向平流」這個被丟掉的效應。

* **【假設 2】 對流前方無尾流 (No wake ahead of the convection)：** 訊息只往後留，故遠在對流前方位渦距平為零

  $$\lim_{\xi \to +\infty}q\left(\xi, y, z\right) = 0$$

  * $q$ : 位渦距平 (PV anomaly) $[\text{s}^{-1}]$
  * $\xi$ : 隨波緯向座標 (Translating zonal coordinate) $[\text{m}]$
  * $y_0$ : 對流中心的經向偏移 (Meridional offset) $[\text{m}]$
  * $z$ : 對數氣壓垂直座標 (Log-pressure vertical coordinate) $[\text{無單位}]$

* **【定義 1】 隨波緯向衰減率 (Zonal decay rate in the translating frame)：** 把時間上的阻尼率換算成隨波座標裡的空間衰減率：熱源以速度 $c$ 東移，每往東走一段距離就衰減該段所費時間乘上 $\alpha$，故 $\sigma$ 的倒數就是尾流在緯向的 $e$-folding 長度。

  $$\sigma \overset{\text{def}}{=} \frac{\alpha}{c}$$

  * $\sigma$ : 隨波緯向衰減率 (Zonal decay rate) $[\text{m}^{-1}]$
  * $\alpha$ : 常數阻尼率 (Constant damping rate) $[\text{s}^{-1}]$，$\alpha = \left(4 \ \text{days}\right)^{-1}$
  * $c$ : 對流包絡的東移速度 (Eastward propagation speed) $[\text{m}\cdot\text{s}^{-1}]$，$c = 5 \ \text{m}\cdot\text{s}^{-1}$

* **【定義 2】 對流的緯向波數 (Zonal wavenumber of the convective hat)：** 把對流帽子的緯向半寬換算成波數：帽子在 $\pm a_0$ 之間恰好是餘弦的半個週期，故對應的波數為 $\pi/a_0$。

  $$p \overset{\text{def}}{=} \frac{\pi}{a_0}$$

  * $p$ : 對流帽子的緯向波數 (Zonal wavenumber of the hat) $[\text{m}^{-1}]$
  * $a_0$ : 對流區的緯向半寬 (Zonal half-width) $[\text{m}]$，$a_0 = 1250 \ \text{km}$

* **【定義 3】 通過時間與對流翻轉時間 (Passage time and convective overturning time)：** 尾流的強度取決於兩個時間尺度的競爭：$\tau_{\mathrm{p}}$ 是熱源掃過一個定點所需的時間，$\tau_{\mathrm{c}}$ 則是加熱把該處大氣翻轉一次所需的時間。

  * (a) 對流區通過所需的時間：

    $$\tau_{\mathrm{p}} \overset{\text{def}}{=} \frac{a_0}{c}$$

  * (b) 對流翻轉時間：

    $$\tau_{\mathrm{c}} \overset{\text{def}}{=} \frac{\bar{c}^{2}}{\kappa Q_0}$$

  * $\tau_{\mathrm{p}}$ : 通過時間 (Passage time) $[\text{s}]$
  * $\tau_{\mathrm{c}}$ : 對流翻轉時間 (Convective overturning time) $[\text{s}]$
  * $\kappa$ : Poisson 常數 (Poisson constant) $[\text{無單位}]$，$\kappa = R/c_p$
  * $a_0$ : 對流區的緯向半寬 (Zonal half-width) $[\text{m}]$，$a_0 = 1250 \ \text{km}$
  * $c_p$ : 定壓比熱 (Specific heat at constant pressure) $[\text{J}\cdot\text{kg}^{-1}\cdot\text{K}^{-1}]$
  * $\bar{c}$ : 等效重力波速 (Equivalent gravity wave speed) $[\text{m}\cdot\text{s}^{-1}]$，$\bar{c} \approx 41.25 \ \text{m}\cdot\text{s}^{-1}$
  * $Q$ : 非絕熱加熱率 (Diabatic heating rate) $[\text{J}\cdot\text{kg}^{-1}\cdot\text{s}^{-1}]$
  * $Q_0$ : 加熱率的峰值 (Peak heating rate) $[\text{J}\cdot\text{kg}^{-1}\cdot\text{s}^{-1}]$，$Q_0/c_p = 12 \ \text{K}\cdot\text{day}^{-1}$

* **【定義 4】 位渦的緯向結構函數 (Zonal structure function of the PV)：** 把【證明 (b)】中所有與 $\xi$ 有關的部分抽出來

  $$q\left(\xi, y, z\right) \overset{\text{def}}{=} \tilde{q}(\xi)\,\beta y\exp\left[-\left(\frac{y - y_0}{b_0}\right)^{2}\right]Z(z)$$

  * $\tilde{q}(\xi)$ : 位渦的緯向結構函數 (Zonal structure function) $[\text{無單位}]$
  * $q$ : 位渦距平 (PV anomaly) $[\text{s}^{-1}]$
  * $\xi$ : 隨波緯向座標 (Translating zonal coordinate) $[\text{m}]$
  * $y_0$ : 對流中心的經向偏移 (Meridional offset) $[\text{m}]$
  * $z$ : 對數氣壓垂直座標 (Log-pressure vertical coordinate) $[\text{無單位}]$
  * $\beta$ : 赤道 $\beta$ 參數 (Equatorial beta parameter) $[\text{m}^{-1}\cdot\text{s}^{-1}]$
  * $b_0$ : 對流區的經向 $e$-folding 寬度 (Meridional $e$-folding width) $[\text{m}]$，$b_0 = 450 \ \text{km}$
  * $Z(z)$ : 垂直結構函數 (Vertical structure function) $[\text{無單位}]$

* **【推導 1】 源項的垂直化簡 (Vertical simplification of the source term)：** $\mathcal{D}_z$ 只作用在 $Z'$ 上，由垂直結構方程式換回 $Z$

  $$\begin{gather*}
  \frac{\beta y}{c_p\Gamma}\left(\frac{\partial}{\partial z} - 1\right)Q &\overset{\text{已知 2(a)}}{=}& \frac{\beta y}{c_p\Gamma}\hat{Q}\left(\frac{d}{dz} - 1\right)\frac{dZ}{dz} \\
  &\overset{\text{已知 2(c)}}{=}& -\frac{\lambda\,\beta y}{c_p\Gamma}\hat{Q}\,Z(z) \\
  &\overset{\text{已知 2(b)(c)}}{=}& -\frac{R\Gamma}{\bar{c}^{2}}\cdot\frac{\beta y}{c_p\Gamma}\cdot\frac{Q_0}{2}\exp\left[-\left(\frac{y - y_0}{b_0}\right)^{2}\right]g(\xi)\,Z(z) \\
  &\overset{\text{定義 3(b)}}{=}& -\frac{1}{2\tau_{\mathrm{c}}}g(\xi)\,\beta y\exp\left[-\left(\frac{y - y_0}{b_0}\right)^{2}\right]Z(z)
  \end{gather*}$$

  * $\beta$ : 赤道 $\beta$ 參數 (Equatorial beta parameter) $[\text{m}^{-1}\cdot\text{s}^{-1}]$
  * $y_0$ : 對流中心的經向偏移 (Meridional offset) $[\text{m}]$
  * $c_p$ : 定壓比熱 (Specific heat at constant pressure) $[\text{J}\cdot\text{kg}^{-1}\cdot\text{K}^{-1}]$
  * $\Gamma$ : 靜力穩定度 (Static stability) $[\text{K}]$
  * $z$ : 對數氣壓垂直座標 (Log-pressure vertical coordinate) $[\text{無單位}]$
  * $Q$ : 非絕熱加熱率 (Diabatic heating rate) $[\text{J}\cdot\text{kg}^{-1}\cdot\text{s}^{-1}]$
  * $\hat{Q}$ : 加熱率的水平結構函數 (Horizontal structure function of the heating rate) $[\text{J}\cdot\text{kg}^{-1}\cdot\text{s}^{-1}]$
  * $Z(z)$ : 垂直結構函數 (Vertical structure function) $[\text{無單位}]$
  * $Z'$ : 垂直結構函數 $Z$ 對 $z$ 的一階微分 (First derivative of the vertical structure function with respect to $z$) $[\text{無單位}]$，$Z' = \dfrac{dZ}{dz}$
  * $\lambda$ : 第一內模態的分離常數 (Separation constant) $[\text{無單位}]$
  * $R$ : 乾空氣氣體常數 (Gas constant for dry air) $[\text{J}\cdot\text{kg}^{-1}\cdot\text{K}^{-1}]$
  * $\bar{c}$ : 等效重力波速 (Equivalent gravity wave speed) $[\text{m}\cdot\text{s}^{-1}]$，$\bar{c} \approx 41.25 \ \text{m}\cdot\text{s}^{-1}$
  * $b_0$ : 對流區的經向 $e$-folding 寬度 (Meridional $e$-folding width) $[\text{m}]$，$b_0 = 450 \ \text{km}$
  * $g(\xi)$ : 加熱的緯向形狀函數 (Zonal shape function of the heating) $[\text{無單位}]$
  * $\xi$ : 隨波緯向座標 (Translating zonal coordinate) $[\text{m}]$
  * $\tau_{\mathrm{p}}$ : 通過時間 (Passage time) $[\text{s}]$
  * $Q_0$ : 加熱率的峰值 (Peak heating rate) $[\text{J}\cdot\text{kg}^{-1}\cdot\text{s}^{-1}]$，$Q_0/c_p = 12 \ \text{K}\cdot\text{day}^{-1}$
  * 註：最後一步用到 $\dfrac{R\,Q_0}{c_p\,\bar{c}^{2}} = \dfrac{\kappa Q_0}{\bar{c}^{2}} = \dfrac{1}{\tau_{\mathrm{c}}}$。**$\tau_{\mathrm{c}}$ 就是這樣自然冒出來的**，不是外加的定義。

* **【推導 2】 緯向結構函數的常微分方程式 (ODE for the zonal structure function)：** 把【定義 4】與【推導 1】代進【證明 (a)】，經向與垂直的因子完全約掉

  $$\begin{gather*}
  c\,\frac{d\tilde{q}}{d\xi} - \alpha\tilde{q} &\overset{\text{證明 (a),定義 4,推導 1}}{=}& \frac{1}{2\tau_{\mathrm{c}}}g(\xi) \\
  \frac{d\tilde{q}}{d\xi} - \sigma\tilde{q} &\overset{\text{定義 1}}{=}& \frac{g(\xi)}{2c\,\tau_{\mathrm{c}}}
  \end{gather*}$$

  * $c_p$ : 定壓比熱 (Specific heat at constant pressure) $[\text{J}\cdot\text{kg}^{-1}\cdot\text{K}^{-1}]$
  * $\tilde{q}(\xi)$ : 位渦的緯向結構函數 (Zonal structure function) $[\text{無單位}]$
  * $\xi$ : 隨波緯向座標 (Translating zonal coordinate) $[\text{m}]$
  * $\alpha$ : 常數阻尼率 (Constant damping rate) $[\text{s}^{-1}]$，$\alpha = \left(4 \ \text{days}\right)^{-1}$
  * $\tau_{\mathrm{p}}$ : 通過時間 (Passage time) $[\text{s}]$
  * $g(\xi)$ : 加熱的緯向形狀函數 (Zonal shape function of the heating) $[\text{無單位}]$
  * $\sigma$ : 隨波緯向衰減率 (Zonal decay rate) $[\text{m}^{-1}]$

* **【推導 3】 積分因子解 (Integrating-factor solution)：** 由【假設 2】的邊界條件從 $\xi$ 積到 $+\infty$

  $$\begin{gather*}
  \left[e^{-\sigma s}\tilde{q}(s)\right]_{\xi}^{\infty} &\overset{\text{推導 2,已知 4}}{=}& \frac{1}{2c\,\tau_{\mathrm{c}}}\int_{\xi}^{\infty}g(s)\,e^{-\sigma s}\,ds \\
  -e^{-\sigma\xi}\tilde{q}(\xi) &\overset{\text{假設 2}}{=}& \frac{1}{2c\,\tau_{\mathrm{c}}}\int_{\xi}^{\infty}g(s)\,e^{-\sigma s}\,ds \\
  \tilde{q}(\xi) &=& -\frac{e^{\sigma\xi}}{2c\,\tau_{\mathrm{c}}}\int_{\xi}^{\infty}g(s)\,e^{-\sigma s}\,ds
  \end{gather*}$$

  * $\sigma$ : 隨波緯向衰減率 (Zonal decay rate) $[\text{m}^{-1}]$
  * $s$ : 積分變數 (Integration variable) $[\text{依應用而定}]$
  * $\tilde{q}(\xi)$ : 位渦的緯向結構函數 (Zonal structure function) $[\text{無單位}]$
  * $c_p$ : 定壓比熱 (Specific heat at constant pressure) $[\text{J}\cdot\text{kg}^{-1}\cdot\text{K}^{-1}]$
  * $\tau_{\mathrm{p}}$ : 通過時間 (Passage time) $[\text{s}]$
  * $g(\xi)$ : 加熱的緯向形狀函數 (Zonal shape function of the heating) $[\text{無單位}]$
  * $\xi$ : 隨波緯向座標 (Translating zonal coordinate) $[\text{m}]$

* **【推導 4】 主積分 (The master integral)：** 由【已知 2】(b)，$g$ 只在 $\left[-a_0, a_0\right]$ 上非零，故積分上限固定為 $a_0$

  $$\begin{gather*}
  J(\xi) &\overset{\text{let}}{=}& \int_{\xi}^{a_0}\left[1 + \cos\left(ps\right)\right]e^{-\sigma s}\,ds \\
  &\overset{\text{已知 5,定義 2}}{=}& \left[-\frac{e^{-\sigma s}}{\sigma} + \frac{e^{-\sigma s}}{\sigma^{2} + p^{2}}\left(-\sigma\cos\left(ps\right) + p\sin\left(ps\right)\right)\right]_{\xi}^{a_0} \\
  &\overset{\text{定義 2}}{=}& -\frac{p^{2}e^{-\sigma a_0}}{\sigma\left(\sigma^{2} + p^{2}\right)} + \frac{e^{-\sigma\xi}}{\sigma} - \frac{e^{-\sigma\xi}}{\sigma^{2} + p^{2}}\left[-\sigma\cos\left(p\xi\right) + p\sin\left(p\xi\right)\right]
  \end{gather*}$$

  * $J(\xi)$ : 主積分 (The master integral) $[\text{m}]$
  * $\xi$ : 隨波緯向座標 (Translating zonal coordinate) $[\text{m}]$
  * $a_0$ : 對流區的緯向半寬 (Zonal half-width) $[\text{m}]$，$a_0 = 1250 \ \text{km}$
  * $p$ : 對流帽子的緯向波數 (Zonal wavenumber of the hat) $[\text{m}^{-1}]$
  * $s$ : 積分變數 (Integration variable) $[\text{依應用而定}]$
  * $\sigma$ : 隨波緯向衰減率 (Zonal decay rate) $[\text{m}^{-1}]$
  * 註：第二列到第三列代入 $s = a_0$ 時用到 $\cos\left(pa_0\right) = \cos\pi = -1$、$\sin\left(pa_0\right) = \sin\pi = 0$，兩項合併成 $-\dfrac{p^{2}e^{-\sigma a_0}}{\sigma\left(\sigma^{2} + p^{2}\right)}$。

* **【推導 5】 兩個常數的無因次改寫 (Dimensionless rewriting of the two constants)：** 把 $\sigma$、$p$ 換成 $\tau_{\mathrm{p}}$ 與 $\pi$

  * (a) 衰減率乘半寬即無因次阻尼：

    $$\begin{gather*}
    \sigma a_0 &\overset{\text{定義 1}}{=}& \frac{\alpha a_0}{c} \\
    &\overset{\text{定義 3(a)}}{=}& \alpha\tau_{\mathrm{p}}
    \end{gather*}$$

  * (b) 【證明 (b)】的括號因子：

    $$\begin{gather*}
    \frac{p^{2}}{\sigma^{2} + p^{2}} &\overset{\text{定義 1,定義 2}}{=}& \frac{\pi^{2}/a_0^{2}}{\alpha^{2}/c^{2} + \pi^{2}/a_0^{2}} \\
    &\overset{\text{推導 5(a)}}{=}& \frac{\pi^{2}}{\alpha^{2}\tau_{\mathrm{p}}^{2} + \pi^{2}}
    \end{gather*}$$

  * $\sigma$ : 隨波緯向衰減率 (Zonal decay rate) $[\text{m}^{-1}]$
  * $a_0$ : 對流區的緯向半寬 (Zonal half-width) $[\text{m}]$，$a_0 = 1250 \ \text{km}$
  * $\alpha$ : 常數阻尼率 (Constant damping rate) $[\text{s}^{-1}]$，$\alpha = \left(4 \ \text{days}\right)^{-1}$
  * $c_p$ : 定壓比熱 (Specific heat at constant pressure) $[\text{J}\cdot\text{kg}^{-1}\cdot\text{K}^{-1}]$
  * $\tau_{\mathrm{p}}$ : 通過時間 (Passage time) $[\text{s}]$
  * $p$ : 對流帽子的緯向波數 (Zonal wavenumber of the hat) $[\text{m}^{-1}]$

* **【定義 5】 括號因子的簡寫 (Shorthand for the bracket factor)：** 把最終解裡反覆出現的括號收成一個無因次因子，量度阻尼在熱源通過期間的效果：通過得快（$\alpha\tau_{\mathrm{p}} \ll 1$）時 $K \to 1$、阻尼來不及作用；通過得慢時 $K \to 0$、尾流被抹掉。

  $$K \overset{\text{def}}{=} \frac{\pi^{2}}{\pi^{2} + \alpha^{2}\tau_{\mathrm{p}}^{2}}$$

  * $K$ : 括號因子 (Bracket factor) $[\text{無單位}]$
  * $\alpha$ : 常數阻尼率 (Constant damping rate) $[\text{s}^{-1}]$，$\alpha = \left(4 \ \text{days}\right)^{-1}$
  * $\tau_{\mathrm{p}}$ : 通過時間 (Passage time) $[\text{s}]$

+++

## 證明:

### (a) proof 拿掉 Rossby 項後的方程式 (The equation after dropping the Rossby term)

$$\begin{gather*}
\frac{\partial q}{\partial t} + \beta v &\overset{\text{已知 1}}{=}& -\alpha q + \frac{\beta y}{c_p\Gamma}\left(\frac{\partial}{\partial z} - 1\right)Q \\
\frac{\partial q}{\partial t} &\overset{\text{假設 1}}{=}& -\alpha q + \frac{\beta y}{c_p\Gamma}\left(\frac{\partial}{\partial z} - 1\right)Q \\
-c\frac{\partial q}{\partial \xi} &\overset{\text{已知 3}}{=}& -\alpha q + \frac{\beta y}{c_p\Gamma}\left(\frac{\partial}{\partial z} - 1\right)Q \\
c\frac{\partial q}{\partial \xi} &=& \alpha q - \frac{\beta y}{c_p\Gamma}\left(\frac{\partial}{\partial z} - 1\right)Q
\end{gather*}$$

### (b) proof 對流內部的解 (Solution inside the convective region)

把【推導 4】代進【推導 3】，再用【推導 5】與【定義 5】換成 $\tau_{\mathrm{p}}$、$K$ 的寫法。

$$\begin{gather*}
\tilde{q}(\xi) &\overset{\text{推導 3,推導 4}}{=}& -\frac{e^{\sigma\xi}}{2c\,\tau_{\mathrm{c}}}J(\xi) \\
&\overset{\text{推導 4}}{=}& -\frac{1}{2c\,\tau_{\mathrm{c}}}\left[-\frac{p^{2}e^{-\sigma\left(a_0 - \xi\right)}}{\sigma\left(\sigma^{2} + p^{2}\right)} + \frac{1}{\sigma} + \frac{\sigma\cos\left(p\xi\right) - p\sin\left(p\xi\right)}{\sigma^{2} + p^{2}}\right] \\
&\overset{\text{定義 5,推導 5(b)}}{=}& -\frac{1}{2c\,\tau_{\mathrm{c}}\,\sigma}\left[1 - K e^{-\sigma\left(a_0 - \xi\right)}\right] - \frac{1}{2c\,\tau_{\mathrm{c}}}\cdot\frac{\sigma\cos\left(p\xi\right) - p\sin\left(p\xi\right)}{\sigma^{2} + p^{2}} \\
&\overset{\text{定義 5}}{=}& -\frac{\tau_{\mathrm{p}}}{\tau_{\mathrm{c}}}K\left\{\frac{1}{2c\,\tau_{\mathrm{p}}\,\sigma K}\left[1 - K e^{-\sigma\left(a_0 - \xi\right)}\right] + \frac{\sigma\cos\left(p\xi\right) - p\sin\left(p\xi\right)}{2c\,\tau_{\mathrm{p}}K\left(\sigma^{2} + p^{2}\right)}\right\} \\
&\overset{\text{定義 3(a),推導 5(b)}}{=}& -\frac{\tau_{\mathrm{p}}}{\tau_{\mathrm{c}}}K\left\{\frac{1 - e^{-\sigma\left(a_0 - \xi\right)}}{2\sigma a_0} + \frac{\sigma}{2a_0p^{2}} + \frac{\sigma\cos\left(p\xi\right) - p\sin\left(p\xi\right)}{2a_0p^{2}}\right\} \\
&\overset{\text{定義 1,定義 2}}{=}& -\frac{\tau_{\mathrm{p}}}{\tau_{\mathrm{c}}}K\left\{\frac{1 - \exp\left[-\left(\alpha/c\right)\left(a_0 - \xi\right)\right]}{2\left(\alpha/c\right)a_0} + \frac{\alpha a_0}{2\pi^{2}c}\left[1 + \cos\frac{\pi\xi}{a_0}\right] - \frac{1}{2\pi}\sin\frac{\pi\xi}{a_0}\right\}
\end{gather*}$$

對照【定義 4】與【定義 5】，大括號內即為【證明目標 (d)】的 $F(\xi)$。

### (c) proof 對流後方的解 (Solution behind the convective region)

$\xi \le -a_0$ 時積分範圍固定為整個對流區，$\xi$ 只出現在前面的指數上。

$$\begin{gather*}
J(-a_0) &\overset{\text{推導 4}}{=}& -\frac{p^{2}e^{-\sigma a_0}}{\sigma\left(\sigma^{2} + p^{2}\right)} + \frac{e^{\sigma a_0}}{\sigma} - \frac{\sigma\,e^{\sigma a_0}}{\sigma^{2} + p^{2}} \\
J(-a_0) &=& -\frac{p^{2}e^{-\sigma a_0}}{\sigma\left(\sigma^{2} + p^{2}\right)} + \frac{p^{2}e^{\sigma a_0}}{\sigma\left(\sigma^{2} + p^{2}\right)} \\
J(-a_0) &=& \frac{p^{2}}{\sigma\left(\sigma^{2} + p^{2}\right)}\left[e^{\sigma a_0} - e^{-\sigma a_0}\right] \\
J(-a_0) &\overset{\text{定義 5,推導 5(b)}}{=}& \frac{2K\sinh\left(\sigma a_0\right)}{\sigma} \\
\tilde{q}(\xi) &\overset{\text{推導 3}}{=}& -\frac{e^{\sigma\xi}}{2c\,\tau_{\mathrm{c}}}\cdot\frac{2K\sinh\left(\sigma a_0\right)}{\sigma} \\
\tilde{q}(\xi) &\overset{\text{定義 3(a),定義 1}}{=}& -\frac{\tau_{\mathrm{p}}}{\tau_{\mathrm{c}}}K\cdot\frac{\sinh\left(\sigma a_0\right)}{\sigma a_0}e^{\sigma\xi} \\
\tilde{q}(\xi) &\overset{\text{定義 1}}{=}& -\frac{\tau_{\mathrm{p}}}{\tau_{\mathrm{c}}}K\cdot\frac{\sinh\left[\left(\alpha/c\right)a_0\right]}{\left(\alpha/c\right)a_0}\exp\left[\frac{\alpha}{c}\xi\right]
\end{gather*}$$

### (d) proof 對流前方無尾流 (No wake ahead of the convection)

$$\begin{gather*}
\tilde{q}(\xi) &\overset{\text{推導 3}}{=}& -\frac{e^{\sigma\xi}}{2c\,\tau_{\mathrm{c}}}\int_{\xi}^{\infty}g(s)\,e^{-\sigma s}\,ds \\
&\overset{\text{已知 2(b)}}{=}& -\frac{e^{\sigma\xi}}{2c\,\tau_{\mathrm{c}}}\int_{\xi}^{\infty}0\,ds \qquad \left(\xi \ge a_0\right) \\
&=& 0
\end{gather*}$$

### (e) solve 三個控制參數的數值 (Numerical values of the three control parameters)

* **尾流衰減長度：**

$$\begin{gather*}
\frac{c}{\alpha} &\overset{\text{已知 1,已知 3}}{=}& 5 \ \text{m}\cdot\text{s}^{-1}\times 4 \times 86400 \ \text{s} \\
&\approx& 1.728\times10^{6} \ \text{m} \\
&\approx& 1728 \ \text{km}
\end{gather*}$$

* **通過時間：**

$$\begin{gather*}
\tau_{\mathrm{p}} &\overset{\text{定義 3(a),已知 2}}{=}& \frac{1.25\times10^{6} \ \text{m}}{5 \ \text{m}\cdot\text{s}^{-1}} \\
&=& 2.5\times10^{5} \ \text{s} \\
&\approx& 69.4 \ \text{h}
\end{gather*}$$

* **對流翻轉時間：**

$$\begin{gather*}
\kappa Q_0 &\overset{\text{定義 3(b),已知 2}}{=}& 287 \ \text{J}\cdot\text{kg}^{-1}\cdot\text{K}^{-1} \times \frac{12}{86400} \ \text{K}\cdot\text{s}^{-1} \\
\kappa Q_0 &\approx& 3.99\times10^{-2} \ \text{m}^{2}\cdot\text{s}^{-3} \\
\tau_{\mathrm{c}} &\overset{\text{定義 3(b)}}{=}& \frac{1701 \ \text{m}^{2}\cdot\text{s}^{-2}}{3.99\times10^{-2} \ \text{m}^{2}\cdot\text{s}^{-3}} \\
\tau_{\mathrm{c}} &\approx& 4.27\times10^{4} \ \text{s} \\
\tau_{\mathrm{c}} &\approx& 11.9 \ \text{h}
\end{gather*}$$

* **時間尺度比：**

$$\begin{gather*}
\frac{\tau_{\mathrm{p}}}{\tau_{\mathrm{c}}} &\approx& \frac{2.5\times10^{5}}{4.27\times10^{4}} \\
&\approx& 5.9
\end{gather*}$$

+++

## 物理解釋

### 兩條反號 PV 帶的數學來源

【證明 (b)】的解可以拆成三個獨立的因子：

$$q = \underbrace{-\frac{\tau_{\mathrm{p}}}{\tau_{\mathrm{c}}}K}_{\text{強度}}\times\underbrace{F(\xi)}_{\text{緯向形狀}}\times\underbrace{\beta y\exp\left[-\left(\frac{y - y_0}{b_0}\right)^{2}\right]}_{\text{經向形狀}}\times\underbrace{Z(z)}_{\text{垂直形狀}}$$

**經向形狀 $\beta y\,e^{-\left(\left(y - y_0\right)/b_0\right)^{2}}$ 就是 [赤道 PV 方程式](Equatorial_PV_Equation_and_Beta_y_Source.md)【推導 5】那個「奇函數 $\times$ 偶函數」的結果。** 在 $y = 0$ 為零、南北兩側取極值且反號 —— 兩條反號 PV 帶的形狀完全由此決定，本篇只是把緯向與強度補齊。

### 三個控制參數各管什麼

| 參數 | 數值 | 控制什麼 | 出處 |
|---|---|---|---|
| $c/\alpha$ | $1728 \ \text{km}$ | 尾流往西的 $1/e$ 衰減長度 | 【證明 (c)】的 $e^{\left(\alpha/c\right)\xi}$ |
| $\tau_{\mathrm{p}}/\tau_{\mathrm{c}}$ | $\approx 5.9$ | PV 距平的**強度** | 【證明 (b)】的前因子 |
| $y_0/b_0$ | $0$ 或 $1$ | 尾流的**南北不對稱程度** | 經向因子的偏移 |

$\tau_{\mathrm{p}}/\tau_{\mathrm{c}}$ 的物理意義最值得記：它是**「對流通過的期間，總共翻轉了幾次」**。

* $\tau_{\mathrm{p}} = a_0/c$ 大 $\Leftrightarrow$ 對流**緯向寬、移動慢**；
* $\tau_{\mathrm{c}} = \bar{c}^{2}/\left(\kappa Q_0\right)$ 小 $\Leftrightarrow$ **加熱強、雨大**。

於是「又下大雨、又寬、又跑得慢」的對流 $\Rightarrow$ 比值大 $\Rightarrow$ **PV 距平大、赤道西風爆發強**。反之則小。

### 這一節的方法論價值：刻意拆掉一項

【假設 1】把 $\beta v$ 拿掉，是一個**已知會失準**的操作。它買到兩件事：

1. **方程式從偏微分降成常微分**（【推導 2】），可以解析求解，三個參數因此**顯式**地被逼出來；
2. **可以量化那一項有多重要** —— 把本篇的解與完整解相比，$q$ 只有正確強度的 $68\%$，而且往極側、往西側都伸展不夠遠。

差額的物理來源很明確：[場還原](Physical_Field_Recovery_and_Zero_Kelvin_PV.md) 的完整解中，低層經向風 $v$ 往極側與西側延伸相當遠，會**把基本態 PV 往赤道方向平流**。這個效應被【假設 1】整個丟掉了，所以本篇的 PV 距平**又弱又窄**。

論文在 §7 又踩了同一個坑一次：把 $\beta v$ 近似成 $\beta\,\partial\psi/\partial x$（即只保留旋轉風的貢獻）去建平衡模式，結果同樣不準 —— 問題**不在**可逆性原理的近似，**而在漏掉了輻散風對基本態 PV 的平流**。見 [平衡頻散關係](Balanced_Rossby_Dispersion_Relation.md)。

### 線性假設什麼時候會失效

把【證明 (b)】代入 $850 \ \text{hPa}$、$\xi = -a_0$、$\alpha\tau_{\mathrm{p}} \approx 0.72$，解退化成

$$q \approx -0.15\left(\frac{\tau_{\mathrm{p}}}{\tau_{\mathrm{c}}}\right)\beta y\exp\left[-\frac{\left(y - y_0\right)^{2}}{b_0^{2}}\right]$$

當 $\tau_{\mathrm{p}}/\tau_{\mathrm{c}}$ 繼續增大，$q$（乃至相對渦度）終將**超過 $\beta y$ 本身**。一旦如此，[赤道 PV 方程式](Equatorial_PV_Equation_and_Beta_y_Source.md)【證明 (a)】源項中的 $\beta y$ 就該換成**全位渦**、[渦度方程式](Equatorial_Vorticity_and_Divergence_Equations.md)【證明 (a)】輻散項中的 $\beta y$ 就該換成**絕對渦度** —— 那就是非線性了。

論文判斷：$\tau_{\mathrm{p}}/\tau_{\mathrm{c}} \approx 5.9$ 這個個案加進非線性項不會造成定性改變；但若比值大到能激出 $\sim 15 \ \text{m}\cdot\text{s}^{-1}$ 的強西風爆發，非線性就不可忽略。
