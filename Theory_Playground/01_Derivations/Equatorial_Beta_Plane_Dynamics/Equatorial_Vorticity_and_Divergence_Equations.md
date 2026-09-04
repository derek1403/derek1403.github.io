# Equatorial Vorticity and Divergence Equations (赤道 β 平面的渦度方程式與位勢–輻散方程式)

+++

## 證明目標:

把 [線性化原始方程組](Log_Pressure_Linearized_Primitive_Equations.md) 的五條方程式重新組合成兩條 ——
一條只談**渦度**，一條只談**位勢**，兩條共用同一個「水平輻散」當橋樑。

* (a) 渦度方程式，由兩條水平動量方程式交叉微分得到：

$$\left(\frac{\partial}{\partial t} + \alpha\right)\left(\frac{\partial v}{\partial x} - \frac{\partial u}{\partial y}\right) + \beta y\left(\frac{\partial u}{\partial x} + \frac{\partial v}{\partial y}\right) + \beta v = 0$$

* (b) 位勢–輻散方程式，由靜力、連續、熱力學三式消去 $T$ 與 $w$ 得到：

$$\left(\frac{\partial}{\partial t} + \alpha\right)\left(\frac{\partial}{\partial z} - 1\right)\frac{\partial \phi}{\partial z} - R\Gamma\left(\frac{\partial u}{\partial x} + \frac{\partial v}{\partial y}\right) = \kappa\left(\frac{\partial}{\partial z} - 1\right)Q$$

* 註：這兩條就是 [Schubert & Masarik (2006)](../../06_References/Tropical_wave_dynamics/Schubert2006-Potential_vorticity_aspects_of_the_MJO/Potential_vorticity_aspects_of_the_MJO.ipynb) 的 $(2.4)$ 與 $(2.5)$。它們的**唯一目的**是為了在下一篇 [赤道 PV 方程式](Equatorial_PV_Equation_and_Beta_y_Source.md) 中把水平輻散消掉。
* 註：兩條式子裡出現的水平輻散 $\dfrac{\partial u}{\partial x} + \dfrac{\partial v}{\partial y}$ 是**同一個量**，只是係數不同 —— (a) 是 $\beta y$、(b) 是 $-R\Gamma$。要消去它，得把 (b) 乘上 $\dfrac{\beta y}{R\Gamma}$ 再與 (a) 相加；**乘進去的這個 $\beta y$ 不是常數**，它就是下一篇 PV 方程式源項裡那個 $y$ 因子的來源，也是「赤道上生不出 PV」的根本原因。

+++

## 假設與已知 (Assumptions & Preliminaries)

* **【已知 1】 [對數氣壓座標下的線性化原始方程組 (Log-pressure linearized primitive equations)](https://derek1403.github.io/Theory_Playground/_build/html/01_Derivations/Equatorial_Beta_Plane_Dynamics/Log_Pressure_Linearized_Primitive_Equations.html#assumptions-preliminaries)：** 對數氣壓座標下、繞靜止基本態線性化後的五條方程式。本篇要做的是對 (a)(b) 交叉微分得到渦度方程式，再把 (c)(d)(e) 組合起來消去 $T$ 與 $w$，得到位勢–輻散方程式。（已於本庫 Log-Pressure Linearized Primitive Equations 完整證明，此處直接引用。）

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

  * $u$ : 擾動緯向風速 (Perturbation zonal velocity) $[\text{m}\cdot\text{s}^{-1}]$
  * $v$ : 擾動經向風速 (Perturbation meridional velocity) $[\text{m}\cdot\text{s}^{-1}]$
  * $w$ : 擾動對數氣壓垂直速度 (Perturbation log-pressure vertical velocity) $[\text{s}^{-1}]$
  * $\phi$ : 擾動位勢 (Perturbation geopotential) $[\text{m}^{2}\cdot\text{s}^{-2}]$
  * $T$ : 擾動溫度 (Perturbation temperature) $[\text{K}]$
  * $Q$ : 單位質量的外加對流加熱率 (Convective heating rate per unit mass) $[\text{J}\cdot\text{kg}^{-1}\cdot\text{s}^{-1}]$
  * $x,\ y$ : 緯向、經向座標 (Zonal and meridional coordinates) $[\text{m}]$
  * $z$ : 對數氣壓垂直座標 (Log-pressure vertical coordinate) $[\text{無單位}]$
  * $t$ : 時間 (Time) $[\text{s}]$
  * $\beta$ : 赤道 $\beta$ 參數 (Equatorial beta parameter) $[\text{m}^{-1}\cdot\text{s}^{-1}]$，$\beta \approx 2.29\times10^{-11} \ \text{m}^{-1}\cdot\text{s}^{-1}$
  * $\alpha$ : 常數阻尼率 (Constant damping rate) $[\text{s}^{-1}]$，$\alpha = \left(4 \ \text{days}\right)^{-1} \approx 2.89\times10^{-6} \ \text{s}^{-1}$
  * $\Gamma$ : 靜力穩定度 (Static stability) $[\text{K}]$，$\Gamma = 23.79 \ \text{K}$
  * $R$ : 乾空氣氣體常數 (Gas constant for dry air) $[\text{J}\cdot\text{kg}^{-1}\cdot\text{K}^{-1}]$，$R \approx 287 \ \text{J}\cdot\text{kg}^{-1}\cdot\text{K}^{-1}$
  * $c_p$ : 定壓比熱 (Specific heat at constant pressure) $[\text{J}\cdot\text{kg}^{-1}\cdot\text{K}^{-1}]$，$c_p \approx 1004 \ \text{J}\cdot\text{kg}^{-1}\cdot\text{K}^{-1}$

* **【已知 2】 [Clairaut 定理（混合偏導數可交換）(Clairaut's theorem)](https://dlmf.nist.gov/1.5#E4)：** 二階連續可微的函數，其混合偏導數與求導次序無關。（標準結果，此處直接引用。）

  $$\frac{\partial}{\partial x}\left[\frac{\partial \phi}{\partial y}\right] = \frac{\partial}{\partial y}\left[\frac{\partial \phi}{\partial x}\right]$$

  * $x,\ y$ : 緯向、經向座標 (Zonal and meridional coordinates) $[\text{m}]$
  * $\phi$ : 擾動位勢 (Perturbation geopotential) $[\text{m}^{2}\cdot\text{s}^{-2}]$

* **【已知 3】 [Poisson 常數 (Poisson constant)](https://derek1403.github.io/Theory_Playground/_build/html/01_Derivations/Equatorial_Beta_Plane_Dynamics/Log_Pressure_Linearized_Primitive_Equations.html#assumptions-preliminaries)：** 乾空氣氣體常數與定壓比熱之比，是「加熱率」與「位勢垂直梯度的變化」之間的固定換算因子。（已於本庫 Log-Pressure Linearized Primitive Equations【定義 4】定義，此處直接引用。）

  $$\kappa = \frac{R}{c_p}$$

  * $\kappa$ : Poisson 常數 (Poisson constant) $[\text{無單位}]$，$\kappa \approx 0.286$
  * $R$ : 乾空氣氣體常數 (Gas constant for dry air) $[\text{J}\cdot\text{kg}^{-1}\cdot\text{K}^{-1}]$，$R \approx 287 \ \text{J}\cdot\text{kg}^{-1}\cdot\text{K}^{-1}$
  * $c_p$ : 定壓比熱 (Specific heat at constant pressure) $[\text{J}\cdot\text{kg}^{-1}\cdot\text{K}^{-1}]$，$c_p \approx 1004 \ \text{J}\cdot\text{kg}^{-1}\cdot\text{K}^{-1}$

* **【假設 1】 場的光滑性 (Smoothness of the fields)：** $u,\ v,\ \phi,\ T,\ w,\ Q$ 對所有自變數皆二階連續可微，因此【已知 2】適用，且各階微分算子可任意交換次序

  $$u,\ v,\ \phi,\ T,\ w,\ Q \in C^{2}$$

  * $u$ : 擾動緯向風速 (Perturbation zonal velocity) $[\text{m}\cdot\text{s}^{-1}]$
  * $v$ : 擾動經向風速 (Perturbation meridional velocity) $[\text{m}\cdot\text{s}^{-1}]$
  * $\phi$ : 擾動位勢 (Perturbation geopotential) $[\text{m}^{2}\cdot\text{s}^{-2}]$
  * $T$ : 擾動溫度 (Perturbation temperature) $[\text{K}]$
  * $w$ : 擾動對數氣壓垂直速度 (Perturbation log-pressure vertical velocity) $[\text{s}^{-1}]$
  * $Q$ : 單位質量的外加對流加熱率 (Convective heating rate per unit mass) $[\text{J}\cdot\text{kg}^{-1}\cdot\text{s}^{-1}]$
  * $C^{2}$ : 二階連續可微的函數類 (Class of twice continuously differentiable functions) $[\text{無單位}]$

* **【假設 2】 [靜力穩定度為常數 (Constant static stability)](https://derek1403.github.io/Theory_Playground/_build/html/01_Derivations/Equatorial_Beta_Plane_Dynamics/Log_Pressure_Linearized_Primitive_Equations.html#assumptions-preliminaries)：** 沿用 [線性化原始方程組](Log_Pressure_Linearized_Primitive_Equations.md)【假設 5】的模式設定，$\Gamma$ 不隨 $x, y, z, t$ 變化

  $$\begin{gather*} 
  \Gamma &=&  23.79 \ \text{K} 
  \end{gather*}$$

  * $\Gamma$ : 靜力穩定度 (Static stability) $[\text{K}]$，$\Gamma = 23.79 \ \text{K}$
  * 註：這一條是【證明 (b)】做得成的關鍵 —— 唯有 $\Gamma$ 為常數，$\Gamma w$ 中的 $\Gamma$ 才能穿過垂直算子 $\mathcal{D}_z$（見【推導 1】(b)），$w$ 才換得成 $-\delta$。

* **【定義 1】 擾動相對渦度 (Perturbation relative vorticity)：** 水平風場的垂直渦度分量

  $$\zeta \overset{\text{def}}{=} \frac{\partial v}{\partial x} - \frac{\partial u}{\partial y}$$

  * $\zeta$ : 擾動相對渦度 (Perturbation relative vorticity) $[\text{s}^{-1}]$
  * $v$ : 擾動經向風速 (Perturbation meridional velocity) $[\text{m}\cdot\text{s}^{-1}]$
  * $x,\ y$ : 緯向、經向座標 (Zonal and meridional coordinates) $[\text{m}]$
  * $u$ : 擾動緯向風速 (Perturbation zonal velocity) $[\text{m}\cdot\text{s}^{-1}]$

* **【定義 2】 水平輻散 (Horizontal divergence)：** 水平風場的散度

  $$\delta \overset{\text{def}}{=} \frac{\partial u}{\partial x} + \frac{\partial v}{\partial y}$$

  * $\delta$ : 擾動水平輻散 (Perturbation horizontal divergence) $[\text{s}^{-1}]$
  * $u$ : 擾動緯向風速 (Perturbation zonal velocity) $[\text{m}\cdot\text{s}^{-1}]$
  * $x,\ y$ : 緯向、經向座標 (Zonal and meridional coordinates) $[\text{m}]$
  * $v$ : 擾動經向風速 (Perturbation meridional velocity) $[\text{m}\cdot\text{s}^{-1}]$

* **【定義 3】 阻尼時間算子與垂直算子 (Damped-tendency and vertical operators)：** 兩個反覆出現的線性算子，先取名字以免式子過長

  * (a) 阻尼時間算子：

    $$\mathcal{D}_t \overset{\text{def}}{=} \frac{\partial}{\partial t} + \alpha$$

  * (b) 垂直算子：

    $$\mathcal{D}_z \overset{\text{def}}{=} \frac{\partial}{\partial z} - 1$$

  * $\mathcal{D}_t$ : 阻尼時間算子 (Damped-tendency operator) $[\text{s}^{-1}]$
  * $\mathcal{D}_z$ : 垂直算子 (Vertical operator) $[\text{無單位}]$
  * $t$ : 時間 (Time) $[\text{s}]$
  * $\alpha$ : 常數阻尼率 (Constant damping rate) $[\text{s}^{-1}]$，$\alpha = \left(4 \ \text{days}\right)^{-1} \approx 2.89\times10^{-6} \ \text{s}^{-1}$
  * $z$ : 對數氣壓垂直座標 (Log-pressure vertical coordinate) $[\text{無單位}]$
  * 註：$\mathcal{D}_z$ 就是 [線性化原始方程組](Log_Pressure_Linearized_Primitive_Equations.md)【證明 (d)】那個 $\dfrac{\partial w}{\partial z} - w$ 的算子形式；它的來源是密度隨高度指數遞減。

* **【推導 1】 兩個算子的可交換性 (Commutativity of the two operators)：** $\mathcal{D}_t$ 只含 $t$、$\mathcal{D}_z$ 只含 $z$，且 $\alpha,\ \Gamma,\ R,\ c_p$ 皆為常數，故兩算子可任意交換次序、也可與常數係數對調

  * (a) 兩算子彼此可交換：

    $$\begin{gather*}
    \mathcal{D}_z\Big[\mathcal{D}_t\,X\Big] &\overset{\text{定義 3(a)(b)}}{=}& \left(\frac{\partial}{\partial z} - 1\right)\left[\frac{\partial X}{\partial t} + \alpha X\right] \\
    &=& \frac{\partial}{\partial z}\left[\frac{\partial X}{\partial t} + \alpha X\right] - \left[\frac{\partial X}{\partial t} + \alpha X\right] \\
    &\overset{\text{假設 1}}{=}& \frac{\partial}{\partial t}\left[\frac{\partial X}{\partial z} - X\right] + \alpha\left[\frac{\partial X}{\partial z} - X\right] \\
    &\overset{\text{定義 3(a)(b)}}{=}& \mathcal{D}_t\Big[\mathcal{D}_z\,X\Big]
    \end{gather*}$$

  * (b) 靜力穩定度可穿過 $\mathcal{D}_z$：

    $$\begin{gather*}
    \mathcal{D}_z\Big[\Gamma\,X\Big] &\overset{\text{定義 3(b)}}{=}& \frac{\partial}{\partial z}\Big[\Gamma X\Big] - \Gamma X \\
    &\overset{\text{假設 2}}{=}& \Gamma\frac{\partial X}{\partial z} - \Gamma X \\
    &\overset{\text{定義 3(b)}}{=}& \Gamma\,\mathcal{D}_z\Big[X\Big]
    \end{gather*}$$

  * (c) 普適物理常數可穿過 $\mathcal{D}_z$：

    $$\begin{gather*}
    \mathcal{D}_z\Big[c\,X\Big] &\overset{\text{定義 3(b)}}{=}& \frac{\partial}{\partial z}\Big[c X\Big] - c X \\
    &\overset{\text{已知 3}}{=}& c\frac{\partial X}{\partial z} - c X \\
    &\overset{\text{定義 3(b)}}{=}& c\,\mathcal{D}_z\Big[X\Big]
    \end{gather*}$$

  * $X$ : 任意二階連續可微的場 (Arbitrary $C^{2}$ field) $[\text{依應用而定}]$
  * $c$ : 任意不隨 $z$ 變化的物理常數（本篇用到的是 $R$ 與 $c_p$）(Arbitrary physical constant) $[\text{依應用而定}]$
  * $\mathcal{D}_t$ : 阻尼時間算子 (Damped-tendency operator) $[\text{s}^{-1}]$
  * $z$ : 對數氣壓垂直座標 (Log-pressure vertical coordinate) $[\text{無單位}]$
  * $t$ : 時間 (Time) $[\text{s}]$
  * $\alpha$ : 常數阻尼率 (Constant damping rate) $[\text{s}^{-1}]$，$\alpha = \left(4 \ \text{days}\right)^{-1} \approx 2.89\times10^{-6} \ \text{s}^{-1}$
  * $\Gamma$ : 靜力穩定度 (Static stability) $[\text{K}]$，$\Gamma = 23.79 \ \text{K}$
  * $R$ : 乾空氣氣體常數 (Gas constant for dry air) $[\text{J}\cdot\text{kg}^{-1}\cdot\text{K}^{-1}]$，$R \approx 287 \ \text{J}\cdot\text{kg}^{-1}\cdot\text{K}^{-1}$
  * $c_p$ : 定壓比熱 (Specific heat at constant pressure) $[\text{J}\cdot\text{kg}^{-1}\cdot\text{K}^{-1}]$，$c_p \approx 1004 \ \text{J}\cdot\text{kg}^{-1}\cdot\text{K}^{-1}$
  * $\mathcal{D}_z$ : 垂直算子 (Vertical operator) $[\text{無單位}]$
  * 註：(b) 與 (c) 形式相同、依據卻不同 —— (c) 的 $R$ 與 $c_p$ 是普適物理常數，本來就不隨 $z$ 變化；(b) 的 $\Gamma$ 則是**靠【假設 2】才成為常數**的模式設定量。真實大氣的 $\Gamma$ 隨高度變化，那時 (b) 就不成立，【證明 (b)】也就做不下去。

* **【推導 2】 兩條動量方程式的交叉微分 (Cross-differentiation of the momentum equations)：** 對【已知 1】(b) 取 $\partial/\partial x$、對【已知 1】(a) 取 $\partial/\partial y$，注意 $\beta y$ 對 $x$ 是常數、對 $y$ 不是

  * (a) 經向動量方程式對 $x$ 微分（$\beta y$ 與 $x$ 無關，直接穿過）：

    $$\begin{gather*}
    -\alpha v &\overset{\text{已知 1(b)}}{=}& \frac{\partial v}{\partial t} + \beta y\,u + \frac{\partial \phi}{\partial y} \\
    \frac{\partial}{\partial x}\Big[-\alpha v\Big] &=& \frac{\partial}{\partial x}\left[\frac{\partial v}{\partial t} + \beta y\,u + \frac{\partial \phi}{\partial y}\right] \\
    -\alpha\frac{\partial v}{\partial x} &=& \frac{\partial}{\partial x}\left[\frac{\partial v}{\partial t}\right] + \beta \frac{\partial \left(y\,u\right)}{\partial x} + \frac{\partial}{\partial x}\left[\frac{\partial \phi}{\partial y}\right] \\
    -\alpha\frac{\partial v}{\partial x} &=& \frac{\partial}{\partial x}\left[\frac{\partial v}{\partial t}\right] + \beta \frac{\partial y}{\partial x}u + \beta y\frac{\partial u}{\partial x} + \frac{\partial}{\partial x}\left[\frac{\partial \phi}{\partial y}\right] \\
    -\alpha\frac{\partial v}{\partial x} &=& \frac{\partial}{\partial x}\left[\frac{\partial v}{\partial t}\right] + \beta \cdot 0 \cdot u + \beta y\frac{\partial u}{\partial x} + \frac{\partial}{\partial x}\left[\frac{\partial \phi}{\partial y}\right] \\
    -\alpha\frac{\partial v}{\partial x} &=& \frac{\partial}{\partial x}\left[\frac{\partial v}{\partial t}\right] + \beta y\frac{\partial u}{\partial x} + \frac{\partial}{\partial x}\left[\frac{\partial \phi}{\partial y}\right] \\
    -\alpha\frac{\partial v}{\partial x} &\overset{\text{假設 1}}{=}& \frac{\partial}{\partial t}\left[\frac{\partial v}{\partial x}\right] + \beta y\frac{\partial u}{\partial x} + \frac{\partial}{\partial x}\left[\frac{\partial \phi}{\partial y}\right]
    \end{gather*}$$

  * (b) 緯向動量方程式對 $y$ 微分（$\beta y$ 與 $y$ 有關，乘積律生出一個 $-\beta v$）：

    $$\begin{gather*}
    -\alpha u &\overset{\text{已知 1(a)}}{=}& \frac{\partial u}{\partial t} - \beta y\,v + \frac{\partial \phi}{\partial x} \\
    \frac{\partial}{\partial y}\Big[-\alpha u\Big] &=& \frac{\partial}{\partial y}\left[\frac{\partial u}{\partial t} - \beta y\,v + \frac{\partial \phi}{\partial x}\right] \\
    -\alpha\frac{\partial u}{\partial y} &=& \frac{\partial}{\partial y}\left[\frac{\partial u}{\partial t}\right] - \beta\frac{\partial \left(y\,v\right)}{\partial y} + \frac{\partial}{\partial y}\left[\frac{\partial \phi}{\partial x}\right] \\
    -\alpha\frac{\partial u}{\partial y} &=& \frac{\partial}{\partial y}\left[\frac{\partial u}{\partial t}\right] - \beta\frac{\partial y}{\partial y}v - \beta y \frac{\partial v}{\partial y} + \frac{\partial}{\partial y}\left[\frac{\partial \phi}{\partial x}\right] \\
    -\alpha\frac{\partial u}{\partial y} &=& \frac{\partial}{\partial y}\left[\frac{\partial u}{\partial t}\right] - \beta v - \beta y\frac{\partial v}{\partial y} + \frac{\partial}{\partial y}\left[\frac{\partial \phi}{\partial x}\right] \\
    -\alpha\frac{\partial u}{\partial y} &\overset{\text{假設 1}}{=}& \frac{\partial}{\partial t}\left[\frac{\partial u}{\partial y}\right] - \beta v - \beta y\frac{\partial v}{\partial y} + \frac{\partial}{\partial y}\left[\frac{\partial \phi}{\partial x}\right]
    \end{gather*}$$

  * $x,\ y$ : 緯向、經向座標 (Zonal and meridional coordinates) $[\text{m}]$
  * $\alpha$ : 常數阻尼率 (Constant damping rate) $[\text{s}^{-1}]$，$\alpha = \left(4 \ \text{days}\right)^{-1} \approx 2.89\times10^{-6} \ \text{s}^{-1}$
  * $v$ : 擾動經向風速 (Perturbation meridional velocity) $[\text{m}\cdot\text{s}^{-1}]$
  * $t$ : 時間 (Time) $[\text{s}]$
  * $\beta$ : 赤道 $\beta$ 參數 (Equatorial beta parameter) $[\text{m}^{-1}\cdot\text{s}^{-1}]$，$\beta \approx 2.29\times10^{-11} \ \text{m}^{-1}\cdot\text{s}^{-1}$
  * $u$ : 擾動緯向風速 (Perturbation zonal velocity) $[\text{m}\cdot\text{s}^{-1}]$
  * $\phi$ : 擾動位勢 (Perturbation geopotential) $[\text{m}^{2}\cdot\text{s}^{-2}]$
  * 註：(b) 中那個**單獨的 $-\beta v$** 就是 Rossby 項的來源 —— 它完全來自 $\dfrac{\partial}{\partial y}\left[\beta y\right] = \beta$，也就是「科氏參數隨緯度變化」這件事。

* **【推導 3】 熱力學方程式的垂直算子形式 (Vertical-operator form of the thermodynamic equation)：** 對【已知 1】(e) 施加 $\mathcal{D}_z$，並用【已知 1】(d) 把 $w$ 換成 $-\delta$

  * (a) 連續方程式改寫成 $\mathcal{D}_z$ 作用在 $w$ 上：

    $$\begin{gather*}
    0 &\overset{\text{已知 1(d)}}{=}& \frac{\partial u}{\partial x} + \frac{\partial v}{\partial y} + \frac{\partial w}{\partial z} - w \\
    0 &\overset{\text{定義 2}}{=}& \delta + \frac{\partial w}{\partial z} - w \\
    0 &=& \delta + \left(\frac{\partial }{\partial z} - 1\right)  w \\
    0 &\overset{\text{定義 3(b)}}{=}& \delta + \mathcal{D}_z\Big[w\Big] \\
    \mathcal{D}_z\Big[w\Big] &=& -\delta
    \end{gather*}$$

  * (b) 熱力學方程式改寫成 $\mathcal{D}_t$ 的形式：

    $$\begin{gather*}
    \frac{Q}{c_p} &\overset{\text{已知 1(e)}}{=}& \frac{\partial T}{\partial t} + \alpha T + \Gamma w \\
    &=&  \left(\frac{\partial}{\partial t} + \alpha\right) \Big[T\Big] + \Gamma w \\
    &\overset{\text{定義 3(a)}}{=}& \mathcal{D}_t\Big[T\Big] + \Gamma w
    \end{gather*}$$

  * $\delta$ : 擾動水平輻散 (Perturbation horizontal divergence) $[\text{s}^{-1}]$
  * $w$ : 擾動對數氣壓垂直速度 (Perturbation log-pressure vertical velocity) $[\text{s}^{-1}]$
  * $z$ : 對數氣壓垂直座標 (Log-pressure vertical coordinate) $[\text{無單位}]$
  * $\mathcal{D}_t$ : 阻尼時間算子 (Damped-tendency operator) $[\text{s}^{-1}]$
  * $Q$ : 單位質量的外加對流加熱率 (Convective heating rate per unit mass) $[\text{J}\cdot\text{kg}^{-1}\cdot\text{s}^{-1}]$
  * $c_p$ : 定壓比熱 (Specific heat at constant pressure) $[\text{J}\cdot\text{kg}^{-1}\cdot\text{K}^{-1}]$，$c_p \approx 1004 \ \text{J}\cdot\text{kg}^{-1}\cdot\text{K}^{-1}$
  * $T$ : 擾動溫度 (Perturbation temperature) $[\text{K}]$
  * $t$ : 時間 (Time) $[\text{s}]$
  * $\alpha$ : 常數阻尼率 (Constant damping rate) $[\text{s}^{-1}]$，$\alpha = \left(4 \ \text{days}\right)^{-1} \approx 2.89\times10^{-6} \ \text{s}^{-1}$
  * $\Gamma$ : 靜力穩定度 (Static stability) $[\text{K}]$，$\Gamma = 23.79 \ \text{K}$
  * $\mathcal{D}_z$ : 垂直算子 (Vertical operator) $[\text{無單位}]$

+++

## 證明:

### (a) proof 渦度方程式 (Vorticity equation)

把【推導 2】(a) 減去【推導 2】(b)，位勢的混合偏導數對消，剩下的依【定義 1】【定義 2】收攏。

$$\begin{gather*}
-\alpha\frac{\partial v}{\partial x} + \alpha\frac{\partial u}{\partial y} &\overset{\text{推導 2(a)(b)}}{=}& \frac{\partial}{\partial t}\left[\frac{\partial v}{\partial x} - \frac{\partial u}{\partial y}\right] + \beta y\frac{\partial u}{\partial x} + \beta y\frac{\partial v}{\partial y} + \beta v + \frac{\partial}{\partial x}\left[\frac{\partial \phi}{\partial y}\right] - \frac{\partial}{\partial y}\left[\frac{\partial \phi}{\partial x}\right] \\
-\alpha\left[\frac{\partial v}{\partial x} - \frac{\partial u}{\partial y}\right] &\overset{\text{已知 2}}{=}& \frac{\partial}{\partial t}\left[\frac{\partial v}{\partial x} - \frac{\partial u}{\partial y}\right] + \beta y\left[\frac{\partial u}{\partial x} + \frac{\partial v}{\partial y}\right] + \beta v \\
0 &=& \frac{\partial}{\partial t}\left[\frac{\partial v}{\partial x} - \frac{\partial u}{\partial y}\right] + \alpha\left[\frac{\partial v}{\partial x} - \frac{\partial u}{\partial y}\right] + \beta y\left[\frac{\partial u}{\partial x} + \frac{\partial v}{\partial y}\right] + \beta v \\
0 &=& \left(\frac{\partial}{\partial t} + \alpha \right) \left[\frac{\partial v}{\partial x} - \frac{\partial u}{\partial y}\right]  + \beta y\left[\frac{\partial u}{\partial x} + \frac{\partial v}{\partial y}\right] + \beta v \\
0 &\overset{\text{定義 3(a)}}{=}& \mathcal{D}_t\left[\frac{\partial v}{\partial x} - \frac{\partial u}{\partial y}\right] + \beta y\left[\frac{\partial u}{\partial x} + \frac{\partial v}{\partial y}\right] + \beta v \\
0 &\overset{\text{定義 1,定義 2}}{=}& \mathcal{D}_t\Big[\zeta\Big] + \beta y\,\delta + \beta v
\end{gather*}$$

### (b) proof 位勢–輻散方程式 (Geopotential–divergence equation)

對【推導 3】(b) 施加 $\mathcal{D}_z$：$w$ 那一項被【推導 3】(a) 換成 $-\delta$，$T$ 那一項被【已知 1】(c) 換成 $\dfrac{\partial\phi}{\partial z}$。

$$\begin{gather*}
\frac{Q}{c_p} &\overset{\text{推導 3(b)}}{=}& \mathcal{D}_t\Big[T\Big] + \Gamma w \\
\mathcal{D}_z\left[\frac{Q}{c_p}\right] &=& \mathcal{D}_z\left[\mathcal{D}_t\Big[T\Big] + \Gamma w\right] \\
\mathcal{D}_z\left[\frac{Q}{c_p}\right] &\overset{\text{推導 1(a)(b)}}{=}& \mathcal{D}_t\left[\mathcal{D}_z\Big[T\Big]\right] + \Gamma\,\mathcal{D}_z\Big[w\Big] \\
\mathcal{D}_z\left[\frac{Q}{c_p}\right] &\overset{\text{推導 3(a)}}{=}& \mathcal{D}_t\left[\mathcal{D}_z\Big[T\Big]\right] - \Gamma\delta \\
\mathcal{D}_z\left[\frac{Q}{c_p}\right] &\overset{\text{已知 1(c)}}{=}& \mathcal{D}_t\left[\mathcal{D}_z\left[\frac{1}{R}\frac{\partial \phi}{\partial z}\right]\right] - \Gamma\delta \\
\frac{1}{c_p}\mathcal{D}_z\Big[Q\Big] &\overset{\text{推導 1(c)}}{=}& \frac{1}{R}\,\mathcal{D}_t\left[\mathcal{D}_z\left[\frac{\partial \phi}{\partial z}\right]\right] - \Gamma\delta \\
\frac{R}{c_p}\,\mathcal{D}_z\Big[Q\Big] &=& \mathcal{D}_t\left[\mathcal{D}_z\left[\frac{\partial \phi}{\partial z}\right]\right] - R\Gamma\delta \\
\kappa\,\mathcal{D}_z\Big[Q\Big] &\overset{\text{已知 3}}{=}& \mathcal{D}_t\left[\mathcal{D}_z\left[\frac{\partial \phi}{\partial z}\right]\right] - R\Gamma\delta
\end{gather*}$$

+++

## 結構解釋

### 為什麼要做這兩條

原方程組有五個未知數 $u, v, \phi, T, w$。這一篇做的事很單純：**把 $T$ 與 $w$ 消掉，只留 $\zeta$、$\delta$、$\phi$ 三個量**。

* 【證明 (a)】走的是「動量方程式交叉微分」這條路，$\phi$ 因為混合偏導數對消而**自動消失** —— 這是渦度方程式永遠比動量方程式乾淨的原因。
* 【證明 (b)】走的是「靜力＋連續＋熱力學」這條路，$T$ 由靜力方程式換成 $\partial\phi/\partial z$、$w$ 由連續方程式換成 $-\delta$。

兩條式子最後都只含 $\left(\zeta,\ \delta\right)$ 或 $\left(\phi,\ \delta\right)$，而且**兩條裡的 $\delta$ 是同一個量**（只是係數一個是 $\beta y$、一個是 $-R\Gamma$）。下一步把 $\delta$ 從兩條之間消掉，$\zeta$ 與 $\phi$ 就被收攏成單一個守恆量 —— 那就是 PV 距平 $q$；式子裡另外還會留下一個 $\beta v$ 的 Rossby 項。

### $\beta v$ 這一項的分量

【推導 2】的註已經點出：$\beta v$ 完全來自 $\dfrac{\partial}{\partial y}\left[\beta y\right] = \beta$。

在 [PV 方程式](Equatorial_PV_Equation_and_Beta_y_Source.md) 中，這一項會變成 $\dfrac{\partial q}{\partial t} + \beta v = \cdots$ 裡的 Rossby 項，代表「氣塊南北位移時，背景 PV 梯度 $\beta$ 造成的局地 PV 變化」。

論文 §5 刻意把這一項拿掉做對照實驗，結果 PV 距平只剩正確強度的 $68\%$，而且往極側、往西側都伸展不夠遠 —— 見 [PV 尾流](PV_Wake_of_a_Moving_Heat_Source.md)。

### $\mathcal{D}_z = \dfrac{\partial}{\partial z} - 1$ 為什麼會出現在加熱項上

【證明 (b)】的左端是 $\kappa\,\mathcal{D}_z\left[Q\right]$，不是 $\kappa Q$。也就是說：**動力場感受到的不是加熱本身，而是「加熱經過 $\mathcal{D}_z$ 加工後」的東西**。

這與本庫 [垂直結構方程式](../Atmospheric_Dynamics/Vertical_Structure_Equation.md)【證明 (a)】的結論是同一件事的不同座標版本 —— 那裡是 Boussinesq 的 $-\partial Q/\partial z$，這裡是對數氣壓的 $\left(\partial/\partial z - 1\right)Q$。多出來的 $-1$ 純粹是密度指數遞減的貢獻。

物理後果是：**垂直方向均勻的加熱（$\partial Q/\partial z = 0$ 且 $Q \neq 0$）仍然有效**（因為 $\mathcal{D}_z Q = -Q \neq 0$），這一點與 Boussinesq 的情形不同。真正無效的是滿足 $\partial Q/\partial z = Q$、即 $Q \propto e^{z}$ 的加熱剖面。
