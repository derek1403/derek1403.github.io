# Balanced Rossby Dispersion Relation (平衡模式的羅斯貝波頻散關係)

+++

## 證明目標:

**端點④。** 把 [可逆性原理](Equatorial_PV_Invertibility_Principle.md) 從「診斷工具」升級成
**一套封閉的平衡理論**：配上一條近似 PV 方程式，就能自己算出頻散關係，再拿去與原始方程的精確解比較。

* (a) 封閉的平衡系統（無黏、絕熱情形）—— 預報方程式：

$$\frac{\partial q}{\partial t} + \beta\frac{\partial \psi}{\partial x} = 0$$

* (b) 封閉的平衡系統 —— 診斷方程式（即可逆性原理）：

$$\nabla^{2}\psi + \frac{\beta^{2}y^{2}}{R\Gamma}\left(\frac{\partial}{\partial z} - 1\right)\frac{\partial \psi}{\partial z} = q$$

* (c) **平衡模式的羅斯貝波頻散關係：**

$$\frac{\nu_{mn}}{2\Omega} = -\frac{m}{m^{2} + \epsilon^{1/2}\left(2n + 1\right)}$$

* (d) (c) **恰為**原始方程頻散關係 $(4.10)$ 在**低頻極限**（丟掉 $\epsilon\hat{\nu}^{2}$）下的近似：

$$\epsilon\hat{\nu}^{2} \ll m^{2} \quad \Longrightarrow \quad \epsilon\hat{\nu}^{2} - m^{2} - \frac{m}{\hat{\nu}} = \epsilon^{1/2}\left(2n + 1\right) \ \longrightarrow \ \hat{\nu} = -\frac{m}{m^{2} + \epsilon^{1/2}\left(2n + 1\right)}$$

* (e) 該近似**唯一失效的區域**是低緯向波數的 $n = 0$ 模態（sectoral harmonics）：

$$\left.\frac{\epsilon\hat{\nu}_{mn}^{2}}{m^{2}}\right|_{n = 0,\ m = 1} \approx 0.92 \qquad \text{vs.} \qquad \left.\frac{\epsilon\hat{\nu}_{mn}^{2}}{m^{2}}\right|_{n = 3,\ m = 1} \approx 0.02$$

* 註：(a)–(c) 就是 [Schubert & Masarik (2006)](../../06_References/Tropical_wave_dynamics/Schubert2006-Potential_vorticity_aspects_of_the_MJO/Potential_vorticity_aspects_of_the_MJO.ipynb) 的 $(7.1)$–$(7.3)$。
* 註：**(a) 是這套平衡理論唯一新增的近似**：它把 [PV 方程式](Equatorial_PV_Equation_and_Beta_y_Source.md) 中的 Rossby 項 $\beta v$ 換成 $\beta\,\partial\psi/\partial x$，也就是**只保留旋轉風的貢獻、丟掉輻散風**。論文實測的結果是：**這條近似才是平衡模式模擬 MJO 尾流時失準的元凶，不是 (b)**。

+++

## 假設與已知 (Assumptions & Preliminaries)

* **【已知 1】 [赤道 PV 方程式 (Equatorial PV equation)](https://derek1403.github.io/Theory_Playground/_build/html/01_Derivations/Equatorial_Beta_Plane_Dynamics/Equatorial_PV_Equation_and_Beta_y_Source.html#b-proof-pv-potential-vorticity-equation)：** 位渦距平的收支：時間變化加上 $\beta v$ 的行星渦度平流，由阻尼消耗，並由加熱以 $\beta y$ 為權重的形式產生 ─ 右端的權重在赤道為零，這正是「赤道上生不出位渦」的來源。（已於本庫 [Equatorial PV Equation and the Beta-y Source](Equatorial_PV_Equation_and_Beta_y_Source.md)【證明 (b)】完整證明，此處直接引用。）

  $$\frac{\partial q}{\partial t} + \beta v = -\alpha q + \frac{\beta y}{c_p\Gamma}\left(\frac{\partial}{\partial z} - 1\right)Q$$

  * $q$ : 位渦距平 (PV anomaly) $[\text{s}^{-1}]$
  * $v$ : 擾動經向風速 (Perturbation meridional velocity) $[\text{m}\cdot\text{s}^{-1}]$
  * $\alpha$ : 常數阻尼率 (Constant damping rate) $[\text{s}^{-1}]$
  * $Q$ : 非絕熱加熱率 (Diabatic heating rate) $[\text{J}\cdot\text{kg}^{-1}\cdot\text{s}^{-1}]$
  * $\beta$ : 赤道 $\beta$ 參數 (Equatorial beta parameter) $[\text{m}^{-1}\cdot\text{s}^{-1}]$，$\beta = 2\Omega/a$
  * $t$ : 時間 (Time) $[\text{s}]$
  * $y$ : 經向座標，以赤道為原點 (Meridional coordinate) $[\text{m}]$
  * $c_p$ : 定壓比熱 (Specific heat at constant pressure) $[\text{J}\cdot\text{kg}^{-1}\cdot\text{K}^{-1}]$
  * $R,\ \Gamma$ : 氣體常數與靜力穩定度 (Gas constant and static stability) $[\text{J}\cdot\text{kg}^{-1}\cdot\text{K}^{-1}],\ [\text{K}]$
  * $z$ : 對數氣壓垂直座標 (Log-pressure vertical coordinate) $[\text{無單位}]$

* **【已知 2】 [可逆性原理及其譜形式 (Invertibility principle and its spectral form)](https://derek1403.github.io/Theory_Playground/_build/html/01_Derivations/Equatorial_Beta_Plane_Dynamics/Hermite_Transform_Solution_of_Invertibility.html#b-proof-one-line-division-in-spectral-space)：** 位渦與流函數之間的可逆關係：(a) 在物理空間裡是一個帶 $\beta^{2}y^{2}$ 加權垂直項的橢圓算符作用在 $\psi$ 上；(b) 在 Hermite–傅立葉譜空間裡，這個算符對角化成單純的除法 ─ 給定 $\hat{q}_{mn}$ 就直接得到 $\hat{\psi}_{mn}$。（已於本庫 [Equatorial PV Invertibility Principle](Equatorial_PV_Invertibility_Principle.md)【證明 (c)】與 [Hermite Transform Solution](Hermite_Transform_Solution_of_Invertibility.md)【證明 (b)】完整證明，此處直接引用。）

  * (a) 物理空間形式：

    $$\nabla^{2}\psi + \frac{\beta^{2}y^{2}}{R\Gamma}\left(\frac{\partial}{\partial z} - 1\right)\frac{\partial \psi}{\partial z} = q$$

  * (b) 譜空間形式：

    $$\hat{\psi}_{mn} = -\frac{a^{2}\hat{q}_{mn}}{m^{2} + \epsilon^{1/2}\left(2n + 1\right)}$$

  * $\psi$ : 旋轉流的流函數 (Streamfunction) $[\text{m}^{2}\cdot\text{s}^{-1}]$
  * $\hat{\psi}_{mn},\ \hat{q}_{mn}$ : Hermite 轉換係數 (Hermite transform coefficients) $[\text{依變數而定}]$
  * $\epsilon$ : Lamb 參數 (Lamb's parameter) $[\text{無單位}]$，$\epsilon \approx 507.3$
  * $m$ : 緯向波數 (Zonal wavenumber) $[\text{無單位}]$，整數
  * $n$ : 經向模態指標 (Meridional mode index) $[\text{無單位}]$
  * $a$ : 地球半徑 (Earth's radius) $[\text{m}]$
  * $R,\ \Gamma$ : 氣體常數與靜力穩定度 (Gas constant and static stability) $[\text{J}\cdot\text{kg}^{-1}\cdot\text{K}^{-1}],\ [\text{K}]$
  * $\beta$ : 赤道 $\beta$ 參數 (Equatorial beta parameter) $[\text{m}^{-1}\cdot\text{s}^{-1}]$，$\beta = 2\Omega/a$
  * $y$ : 經向座標，以赤道為原點 (Meridional coordinate) $[\text{m}]$
  * $z$ : 對數氣壓垂直座標 (Log-pressure vertical coordinate) $[\text{無單位}]$
  * $q$ : 位渦距平 (PV anomaly) $[\text{s}^{-1}]$

* **【已知 3】 [Matsuno 頻散關係 (Matsuno dispersion relation)](https://derek1403.github.io/Theory_Playground/_build/html/01_Derivations/Equatorial_Beta_Plane_Dynamics/Matsuno_Dispersion_Relation.html#a-proof-notation-mapping-and-scale-restoration)：** 完整淺水系統的頻散關係，三個根分別對應東行重力波、西行重力波與羅斯貝波。本篇要證的是：平衡理論只保留其中的羅斯貝支。（已於本庫 [Matsuno Dispersion Relation](Matsuno_Dispersion_Relation.md)【證明 (a)】完整證明，此處直接引用。）

  $$\epsilon\hat{\nu}_{mnr}^{2} - m^{2} - \frac{m}{\hat{\nu}_{mnr}} = \epsilon^{1/2}\left(2n + 1\right), \qquad \hat{\nu}_{mnr} = \frac{\nu_{mnr}}{2\Omega}$$

  * $\hat{\nu}_{mnr}$ : 原始方程模式的無因次本徵頻率 (Dimensionless eigenfrequency of the primitive equation model) $[\text{無單位}]$
  * $\Omega$ : 地球自轉角速度 (Earth's angular velocity) $[\text{s}^{-1}]$
  * $\epsilon$ : Lamb 參數 (Lamb's parameter) $[\text{無單位}]$，$\epsilon \approx 507.3$
  * $\nu_{mn}$ : 平衡模式的本徵頻率 (Eigenfrequency of the balanced model) $[\text{s}^{-1}]$
  * $\nu_{mnr}$ : 第 $(m, n, r)$ 個本徵頻率 (Eigenfrequency) $[\text{s}^{-1}]$，實數

* **【已知 4】 [垂直分離、緯向傅立葉與 Hermite 轉換 (Vertical separation, zonal Fourier, and Hermite transforms)](https://derek1403.github.io/Theory_Playground/_build/html/01_Derivations/Equatorial_Beta_Plane_Dynamics/Hermite_Transform_Solution_of_Invertibility.html#a-proof-hermite-hermite-transform-pair)：** 本篇一次用到的三層轉換：垂直方向分離出 $Z(z)$、緯向轉成波數 $m$、經向展開成 Hermite 級數 ─ 三者合起來把偏微分方程變成對 $\left(m,\ n\right)$ 逐項的代數式。（已於本庫多篇完整證明，此處一併引用。）

  $$\left(\psi,\ q\right) = \left(\hat{\psi},\ \hat{q}\right)Z(z), \qquad \frac{\partial}{\partial x} \to \frac{im}{a}, \qquad \hat{\psi}_m(\hat{y}) = \sum_{n = 0}^{\infty}\hat{\psi}_{mn}\mathcal{H}_n(\hat{y})$$

  * $Z(z)$ : 垂直結構函數 (Vertical structure function) $[\text{無單位}]$
  * $\mathcal{H}_n$ : 歸一化 Hermite 函數 (Normalized Hermite function) $[\text{無單位}]$
  * $\hat{y}$ : 無因次經向座標 (Dimensionless meridional coordinate) $[\text{無單位}]$
  * $\psi$ : 旋轉流的流函數 (Streamfunction) $[\text{m}^{2}\cdot\text{s}^{-1}]$
  * $q$ : 位渦距平 (PV anomaly) $[\text{s}^{-1}]$
  * $\hat{\psi}_{mn},\ \hat{q}_{mn}$ : Hermite 轉換係數 (Hermite transform coefficients) $[\text{依變數而定}]$
  * $z$ : 對數氣壓垂直座標 (Log-pressure vertical coordinate) $[\text{無單位}]$
  * $x,\ y$ : 緯向、經向座標 (Zonal and meridional coordinates) $[\text{m}]$
  * $m$ : 緯向波數 (Zonal wavenumber) $[\text{無單位}]$，整數
  * $a$ : 地球半徑 (Earth's radius) $[\text{m}]$
  * $\hat{\psi}_m$ : 流函數的緯向傅立葉係數 (Fourier coefficient of the streamfunction) $[\text{m}^{2}\cdot\text{s}^{-1}]$

* **【假設 1】 無黏絕熱 (Inviscid and adiabatic)：** 本篇討論的是平衡系統的**自由波**，故【已知 1】右端的阻尼與加熱項一併拿掉

  $$\alpha = 0, \qquad Q = 0$$

  * $\alpha$ : 常數阻尼率 (Constant damping rate) $[\text{s}^{-1}]$
  * $Q$ : 非絕熱加熱率 (Diabatic heating rate) $[\text{J}\cdot\text{kg}^{-1}\cdot\text{s}^{-1}]$

* **【假設 2】 用旋轉風近似經向風 (Approximating the meridional wind by its rotational part)：** 把經向風整個用它的旋轉部分取代，等於丟掉輻散風 $v_\chi$；這是這套平衡理論**唯一新增**的近似

  $$v \approx \frac{\partial \psi}{\partial x}$$

  * $v$ : 擾動經向風速 (Perturbation meridional velocity) $[\text{m}\cdot\text{s}^{-1}]$
  * $\psi$ : 旋轉流的流函數 (Streamfunction) $[\text{m}^{2}\cdot\text{s}^{-1}]$
  * $x,\ y$ : 緯向、經向座標 (Zonal and meridional coordinates) $[\text{m}]$
  * 註：被丟掉的是**輻散風** $v_\chi$。它看起來只是小修正，但論文實測發現：把【已知 1】右端的強迫與耗散搬回來、用本假設建平衡模式去模擬 MJO 尾流，結果**不準**；而問題**不在**可逆性原理【已知 2】，就在這一條。理由見【物理解釋】。

* **【假設 3】 平面波解 (Plane wave solutions)：** 尋找可分離的振盪解

  $$\psi \propto Z(z)\,\mathcal{H}_n(\hat{y})\exp\left[i\left(\frac{mx}{a} - \nu_{mn}t\right)\right]$$

  * $\nu_{mn}$ : 平衡模式的本徵頻率 (Eigenfrequency of the balanced model) $[\text{s}^{-1}]$
  * $\psi$ : 旋轉流的流函數 (Streamfunction) $[\text{m}^{2}\cdot\text{s}^{-1}]$
  * $Z(z)$ : 垂直結構函數 (Vertical structure function) $[\text{無單位}]$
  * $z$ : 對數氣壓垂直座標 (Log-pressure vertical coordinate) $[\text{無單位}]$
  * $\mathcal{H}_n$ : 歸一化 Hermite 函數 (Normalized Hermite function) $[\text{無單位}]$
  * $\hat{y}$ : 無因次經向座標 (Dimensionless meridional coordinate) $[\text{無單位}]$
  * $x,\ y$ : 緯向、經向座標 (Zonal and meridional coordinates) $[\text{m}]$
  * $a$ : 地球半徑 (Earth's radius) $[\text{m}]$
  * $t$ : 時間 (Time) $[\text{s}]$
  * $i$ : 虛數單位 (Imaginary unit) $[\text{無單位}]$，$i^{2} = -1$

* **【假設 4】 振幅不為零 (Nonzero amplitude)：** 【證明 (c)】兩側同除 $\hat{\psi}_{mn}$ 時需要

  $$\hat{\psi}_{mn} \neq 0$$

  * $\hat{\psi}_{mn},\ \hat{q}_{mn}$ : Hermite 轉換係數 (Hermite transform coefficients) $[\text{依變數而定}]$
  * $m$ : 緯向波數 (Zonal wavenumber) $[\text{無單位}]$，整數
  * $n$ : 經向模態指標 (Meridional mode index) $[\text{無單位}]$

* **【假設 5】 低頻近似 (Low-frequency approximation)：** 【證明 (d)】比較兩條頻散關係時所加的條件

  $$\epsilon\hat{\nu}_{mnr}^{2} \ll m^{2}$$

  * $\epsilon$ : Lamb 參數 (Lamb's parameter) $[\text{無單位}]$，$\epsilon \approx 507.3$
  * $\hat{\nu}_{mnr}$ : 原始方程模式的無因次本徵頻率 (Dimensionless eigenfrequency of the primitive equation model) $[\text{無單位}]$
  * $m$ : 緯向波數 (Zonal wavenumber) $[\text{無單位}]$，整數
  * $n$ : 經向模態指標 (Meridional mode index) $[\text{無單位}]$
  * $r$ : 波型指標 (Wave-type index) $[\text{無單位}]$

* **【推導 1】 譜空間的 PV–流函數關係 (Spectral PV–streamfunction relation)：** 把【已知 2】(b) 反過來寫

  $$\begin{gather*}
  \hat{\psi}_{mn} &\overset{\text{已知 2(b)}}{=}& -\frac{a^{2}\hat{q}_{mn}}{m^{2} + \epsilon^{1/2}\left(2n + 1\right)} \\
  \hat{q}_{mn} &=& -\frac{m^{2} + \epsilon^{1/2}\left(2n + 1\right)}{a^{2}}\hat{\psi}_{mn}
  \end{gather*}$$

  * $\hat{\psi}_{mn},\ \hat{q}_{mn}$ : Hermite 轉換係數 (Hermite transform coefficients) $[\text{依變數而定}]$
  * $m$ : 緯向波數 (Zonal wavenumber) $[\text{無單位}]$，整數
  * $n$ : 經向模態指標 (Meridional mode index) $[\text{無單位}]$
  * $a$ : 地球半徑 (Earth's radius) $[\text{m}]$
  * $\epsilon$ : Lamb 參數 (Lamb's parameter) $[\text{無單位}]$，$\epsilon \approx 507.3$

* **【推導 2】 預報方程式的譜形式 (Spectral form of the prognostic equation)：** 把【假設 3】的平面波代進【證明 (a)】

  $$\begin{gather*}
  0 &\overset{\text{證明 (a)}}{=}& \frac{\partial q}{\partial t} + \beta\frac{\partial \psi}{\partial x} \\
  0 &\overset{\text{假設 3,已知 4}}{=}& -i\nu_{mn}\hat{q}_{mn} + \beta\frac{im}{a}\hat{\psi}_{mn} \\
  \nu_{mn}\,\hat{q}_{mn} &=& \frac{\beta m}{a}\hat{\psi}_{mn}
  \end{gather*}$$

  * $q$ : 位渦距平 (PV anomaly) $[\text{s}^{-1}]$
  * $t$ : 時間 (Time) $[\text{s}]$
  * $\beta$ : 赤道 $\beta$ 參數 (Equatorial beta parameter) $[\text{m}^{-1}\cdot\text{s}^{-1}]$，$\beta = 2\Omega/a$
  * $\psi$ : 旋轉流的流函數 (Streamfunction) $[\text{m}^{2}\cdot\text{s}^{-1}]$
  * $x,\ y$ : 緯向、經向座標 (Zonal and meridional coordinates) $[\text{m}]$
  * $\nu_{mn}$ : 平衡模式的本徵頻率 (Eigenfrequency of the balanced model) $[\text{s}^{-1}]$
  * $m$ : 緯向波數 (Zonal wavenumber) $[\text{無單位}]$，整數
  * $n$ : 經向模態指標 (Meridional mode index) $[\text{無單位}]$
  * $\hat{\psi}_{mn},\ \hat{q}_{mn}$ : Hermite 轉換係數 (Hermite transform coefficients) $[\text{依變數而定}]$
  * $a$ : 地球半徑 (Earth's radius) $[\text{m}]$
  * $i$ : 虛數單位 (Imaginary unit) $[\text{無單位}]$，$i^{2} = -1$

* **【推導 3】 兩個無因次比值的數值 (Numerical values of the two dimensionless ratios)：** 用【證明 (c)】的頻率估計【假設 5】的失準程度

  * (a) $n = 0$、$m = 1$：

    $$\begin{gather*}
    \hat{\nu}_{10} &\overset{\text{證明 (c)}}{=}& -\frac{1}{1 + 22.52 \times 1} \\
    \hat{\nu}_{10} &\approx& -0.0426 \\
    \frac{\epsilon\hat{\nu}_{10}^{2}}{m^{2}} &\approx& \frac{507.3 \times 0.0426^{2}}{1} \\
    \frac{\epsilon\hat{\nu}_{10}^{2}}{m^{2}} &\approx& 0.92
    \end{gather*}$$

  * (b) $n = 3$、$m = 1$：

    $$\begin{gather*}
    \hat{\nu}_{13} &\overset{\text{證明 (c)}}{=}& -\frac{1}{1 + 22.52 \times 7} \\
    \hat{\nu}_{13} &\approx& -0.00630 \\
    \frac{\epsilon\hat{\nu}_{13}^{2}}{m^{2}} &\approx& \frac{507.3 \times 0.00630^{2}}{1} \\
    \frac{\epsilon\hat{\nu}_{13}^{2}}{m^{2}} &\approx& 0.02
    \end{gather*}$$

  * $\hat{\nu}_{mnr}$ : 原始方程模式的無因次本徵頻率 (Dimensionless eigenfrequency of the primitive equation model) $[\text{無單位}]$
  * $\epsilon$ : Lamb 參數 (Lamb's parameter) $[\text{無單位}]$，$\epsilon \approx 507.3$
  * $m$ : 緯向波數 (Zonal wavenumber) $[\text{無單位}]$，整數

+++

## 證明:

### (a) proof 平衡系統的預報方程式 (Prognostic equation of the balanced system)

從完整的 PV 方程式出發，丟掉阻尼與加熱（【假設 1】），再把 $v$ 換成旋轉風（【假設 2】）。

$$\begin{gather*}
\frac{\partial q}{\partial t} + \beta v &\overset{\text{已知 1}}{=}& -\alpha q + \frac{\beta y}{c_p\Gamma}\left(\frac{\partial}{\partial z} - 1\right)Q \\
\frac{\partial q}{\partial t} + \beta v &\overset{\text{假設 1}}{=}& 0 \\
\frac{\partial q}{\partial t} + \beta\frac{\partial \psi}{\partial x} &\overset{\text{假設 2}}{=}& 0
\end{gather*}$$

### (b) proof 平衡系統的診斷方程式 (Diagnostic equation of the balanced system)

直接引用可逆性原理。

$$\nabla^{2}\psi + \frac{\beta^{2}y^{2}}{R\Gamma}\left(\frac{\partial}{\partial z} - 1\right)\frac{\partial \psi}{\partial z} \overset{\text{已知 2(a)}}{=} q$$

### (c) proof 平衡模式的頻散關係 (Dispersion relation of the balanced model)

把【推導 1】的 $\hat{q}_{mn}$ 代進【推導 2】，$\hat{\psi}_{mn}$ 兩側約掉。

$$\begin{gather*}
\frac{\beta m}{a}\hat{\psi}_{mn} &\overset{\text{推導 2}}{=}& \nu_{mn}\,\hat{q}_{mn} \\
\frac{\beta m}{a}\hat{\psi}_{mn} &\overset{\text{推導 1}}{=}& -\nu_{mn}\frac{m^{2} + \epsilon^{1/2}\left(2n + 1\right)}{a^{2}}\hat{\psi}_{mn} \\
\frac{\beta m}{a} &\overset{\text{假設 4}}{=}& -\nu_{mn}\frac{m^{2} + \epsilon^{1/2}\left(2n + 1\right)}{a^{2}} \\
\nu_{mn} &=& -\frac{\beta m\,a}{m^{2} + \epsilon^{1/2}\left(2n + 1\right)} \\
\frac{\nu_{mn}}{2\Omega} &\overset{\text{已知 1}}{=}& -\frac{m}{m^{2} + \epsilon^{1/2}\left(2n + 1\right)}
\end{gather*}$$

### (d) proof 與原始方程頻散關係的關係 (Relation to the primitive equation dispersion relation)

在【已知 3】中丟掉 $\epsilon\hat{\nu}^{2}$（【假設 5】），剩下的兩項就解得出 $\hat{\nu}$，且結果與【證明 (c)】完全相同。

$$\begin{gather*}
\epsilon^{1/2}\left(2n + 1\right) &\overset{\text{已知 3}}{=}& \epsilon\hat{\nu}_{mnr}^{2} - m^{2} - \frac{m}{\hat{\nu}_{mnr}} \\
\epsilon^{1/2}\left(2n + 1\right) &\overset{\text{假設 5}}{\approx}& -m^{2} - \frac{m}{\hat{\nu}_{mnr}} \\
\frac{m}{\hat{\nu}_{mnr}} &=& -m^{2} - \epsilon^{1/2}\left(2n + 1\right) \\
\hat{\nu}_{mnr} &=& -\frac{m}{m^{2} + \epsilon^{1/2}\left(2n + 1\right)} \\
\hat{\nu}_{mnr} &\overset{\text{證明 (c)}}{=}& \frac{\nu_{mn}}{2\Omega}
\end{gather*}$$

### (e) solve 近似失效的區域 (Where the approximation fails)

【假設 5】要求 $\epsilon\hat{\nu}^{2}/m^{2} \ll 1$。【推導 3】把兩個代表性情形算出來，一望即知。

$$\begin{gather*}
\left.\frac{\epsilon\hat{\nu}_{mn}^{2}}{m^{2}}\right|_{n = 0,\ m = 1} &\overset{\text{推導 3(a)}}{\approx}& 0.92 \\
\left.\frac{\epsilon\hat{\nu}_{mn}^{2}}{m^{2}}\right|_{n = 3,\ m = 1} &\overset{\text{推導 3(b)}}{\approx}& 0.02
\end{gather*}$$

+++

## 物理解釋

### 平衡理論為什麼「幾乎」成功

【證明 (d)】說得很清楚：**平衡模式的頻散關係，就是原始方程頻散關係丟掉 $\epsilon\hat{\nu}^{2}$ 之後的結果。**

那一項是什麼？回頭看 [Matsuno 頻散關係](Matsuno_Dispersion_Relation.md)：$\epsilon\hat{\nu}^{2}$ 是**重力波動力**的貢獻（頻率平方項），$\dfrac{m}{\hat{\nu}}$ 才是 **PV（羅斯貝）動力**的貢獻。丟掉前者，等於宣告「這個模式只描述 PV 動力」。

對絕大多數模態而言，這個宣告是安全的 —— 【證明 (e)】的 $n = 3$ 情形，重力波項只佔 $2\%$。

### 唯一失效的角落：低波數的 $n = 0$

【證明 (e)】的 $n = 0$、$m = 1$ 情形，重力波項佔了 $92\%$ —— **與 PV 項同量級**。這時候把 $\epsilon\hat{\nu}^{2}$ 丟掉當然不合法。

論文對此的詮釋很精準：**在原始方程模式裡，這些低波數的 $n = 0$ 模態同時混著重力波動力與 PV 動力，而平衡模式只能準確抓住 PV 那一半。**

從 [Matsuno 頻散關係](Matsuno_Dispersion_Relation.md)【證明 (b)】也看得到同一件事：$n = 0$ 時三次式**退化**（可因式分解、且有一根必須捨棄），這一支本來就是混合羅斯貝–重力波 —— 名字裡就寫著「混合」。

### 一個誠實而重要的負面結果

既然 $n = 0$ 模態在 $y_0 = 0$ 或 $y_0 \ll b_0$ 時幾乎不被激發（見 [移動熱源的模態投影](Projection_of_a_Moving_Heat_Source.md)【證明 (e)】），那把強迫與耗散搬回【證明 (a)】，是不是就能準確模擬 MJO 尾流了？

**論文實際做了，答案是不行。**

而且問題**不在**可逆性原理【證明 (b)】，**而在【假設 2】** —— 把 $\beta v$ 近似成 $\beta\,\partial\psi/\partial x$，也就是**漏掉了輻散風對基本態 PV 的平流**。

這與 [PV 尾流](PV_Wake_of_a_Moving_Heat_Source.md) 的「忽略 $\beta v$ 只剩 $68\%$ 強度」是**同一件事的兩個側面**：

| 篇章 | 對 $\beta v$ 做了什麼 | 後果 |
|---|---|---|
| [PV 尾流](PV_Wake_of_a_Moving_Heat_Source.md) | **整項丟掉** | $q$ 只有 $68\%$ 強度，往極側／西側都不夠遠 |
| 本篇【假設 2】 | **只留旋轉風** | 同樣不準（輻散風的貢獻被丟掉） |

論文的圖 3、圖 5 第三面板顯示：**輻散流會延伸到加熱區的極側**，正是它讓 PV 距平更強、也伸展得更往極側。

### 三個端點的總結

| 端點 | 成績 | 邊界在哪 |
|---|---|---|
| ① [受迫解](Physical_Field_Recovery_and_Zero_Kelvin_PV.md) | **成功** —— 完整解出 $u, v, \phi, q, w$ | 線性、定常、單一垂直模態 |
| ② [PV 尾流](PV_Wake_of_a_Moving_Heat_Source.md) | **成功** —— 三個控制參數 $c/\alpha$、$\tau_{\mathrm{p}}/\tau_{\mathrm{c}}$、$y_0/b_0$ | 丟掉 $\beta v$ 只剩 $68\%$ 強度 |
| ③ [可逆性原理](Hermite_Transform_Solution_of_Invertibility.md) | **部分成功** —— 西側尾流可還原 | 東側救不回（[Kelvin 波 PV $= 0$](Physical_Field_Recovery_and_Zero_Kelvin_PV.md)） |
| ④ **本篇** | **部分成功** —— 頻散關係吻合得很好 | 低波數 $n = 0$ 失準；且**當成預報模式時整個不準** |

**四個端點合起來，論文真正的貢獻其實是後兩個的「失敗」**：它們把「PV 思維在赤道能走到哪裡」這條界線畫了出來 —— PV 反演在羅斯貝波主導處極好用，但重力波（Kelvin 波）與輻散風攜帶的資訊，PV 這個變數裝不下。
