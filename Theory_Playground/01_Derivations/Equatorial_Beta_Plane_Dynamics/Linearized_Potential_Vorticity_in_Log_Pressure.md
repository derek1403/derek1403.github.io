# Linearized Potential Vorticity in Log-Pressure Coordinates (對數氣壓座標下的線性化位渦)

+++

## 證明目標:

[赤道 PV 方程式](Equatorial_PV_Equation_and_Beta_y_Source.md) 裡那個 $q$，是消去輻散之後**代數上自動浮現**的組合。
本篇要回答的是另一個問題：**憑什麼叫它「位渦」？**
做法是從 [Ertel 位渦](../Fluid_Dynamics_Variable_Coordinate_Physics/PV_Representations_and_Mappings/Relation_Between_PV_and_PVb.md) 的原始定義出發，換到對數氣壓座標、繞靜止基本態線性化，看它會長成什麼樣子。

* (a) 線性化後，Ertel 位渦退化成「**絕對渦度 ÷ 單位位溫所含的質量**」：

$$PV = \frac{\beta y + \zeta}{\rho_{*}}\frac{\partial \theta}{\partial z}$$

* (b) **★ 把「跟著氣塊走的相對位渦距平」乘上 $\beta y$，得到的正是 $q$**：

$$\beta y\,\frac{\delta PV}{\overline{PV}} = \zeta + \frac{\beta y}{R\Gamma}\,\mathcal{D}_z\left[\frac{\partial \phi}{\partial z}\right]$$

* (c) **★ 非絕熱加熱對它的生成率，正是 $S$**：

$$\left(\frac{\partial}{\partial t}\left[\beta y\,\frac{\delta PV}{\overline{PV}}\right]\right)_{\text{加熱}} = \frac{\beta y}{c_p\Gamma}\,\mathcal{D}_z\left[Q\right]$$

其中

* $PV$ : Ertel 位渦 (Ertel potential vorticity) $[\text{m}^{2}\cdot\text{s}^{-1}\cdot\text{K}\cdot\text{kg}^{-1}]$
* $\overline{PV}$ : 基本態的 Ertel 位渦 (Basic-state Ertel potential vorticity) $[\text{m}^{2}\cdot\text{s}^{-1}\cdot\text{K}\cdot\text{kg}^{-1}]$
* $\delta PV$ : 跟著氣塊走的位渦距平 (Material potential vorticity anomaly) $[\text{m}^{2}\cdot\text{s}^{-1}\cdot\text{K}\cdot\text{kg}^{-1}]$
* $\rho_{*}$ : 對數氣壓座標的偽密度 (Log-pressure pseudo-density) $[\text{kg}\cdot\text{m}^{-2}]$
* $\theta$ : 位溫 (Potential temperature) $[\text{K}]$
* $\eta$ : 等熵面的垂直位移 (Vertical displacement of an isentropic surface) $[\text{無單位}]$
* $\zeta$ : 擾動相對渦度 (Perturbation relative vorticity) $[\text{s}^{-1}]$
* $\phi$ : 擾動位勢 (Perturbation geopotential) $[\text{m}^{2}\cdot\text{s}^{-2}]$
* $T$ : 擾動溫度 (Perturbation temperature) $[\text{K}]$
* $Q$ : 非絕熱加熱率 (Diabatic heating rate) $[\text{J}\cdot\text{kg}^{-1}\cdot\text{s}^{-1}]$
* $y$ : 經向座標，以赤道為原點 (Meridional coordinate) $[\text{m}]$
* $z$ : 對數氣壓垂直座標 (Log-pressure vertical coordinate) $[\text{無單位}]$
* $z_{\text{g}}$ : 幾何高度 (Geometric height) $[\text{m}]$
* $t$ : 時間 (Time) $[\text{s}]$
* $\beta$ : 赤道 $\beta$ 參數 (Equatorial beta parameter) $[\text{m}^{-1}\cdot\text{s}^{-1}]$
* $\Gamma$ : 靜力穩定度 (Static stability) $[\text{K}]$，$\Gamma = 23.79 \ \text{K}$
* $R$ : 乾空氣氣體常數 (Gas constant for dry air) $[\text{J}\cdot\text{kg}^{-1}\cdot\text{K}^{-1}]$
* $c_p$ : 定壓比熱 (Specific heat at constant pressure) $[\text{J}\cdot\text{kg}^{-1}\cdot\text{K}^{-1}]$
* $\mathcal{D}_z$ : 垂直算子 (Vertical operator) $[\text{無單位}]$
* 註（符號提醒）：$\boldsymbol{\eta}_a$（**粗體、帶下標** $a$）是絕對渦度**向量**；$\eta$（細體、無下標）是等熵面的垂直位移**純量**。兩者只是字形相近，毫無關係。同理 $\zeta$（相對渦度）與 $\theta$（位溫）在本篇一律不縮寫。
* 註：**(b) 是全篇的重點。** [Schubert & Masarik (2006)](../../06_References/Tropical_wave_dynamics/Schubert2006-Potential_vorticity_aspects_of_the_MJO/Potential_vorticity_aspects_of_the_MJO.ipynb) 在 $(2.7)$ 只寫了一句 "is the potential vorticity anomaly" 就走人，沒有交代這個組合與 Ertel 位渦的關係。本篇把那一步補上。
* 註：**必須走「跟著氣塊走」的距平，不能走「固定高度上的擾動」。** 若把 $PV$ 在固定 $z$ 上線性化成 Eulerian 擾動 $PV'$，算出來的括號是 $\left(\dfrac{\partial}{\partial z} + \kappa\right)$ 而**不是** $\mathcal{D}_z = \dfrac{\partial}{\partial z} - 1$，對不上 $(2.7)$。原因見〈物理解釋〉第一節。

+++

## 假設與已知 (Assumptions & Preliminaries)

* **【已知 1】 [符號約定：相對渦度與垂直算子 (Notation: relative vorticity and the vertical operator)](https://derek1403.github.io/Theory_Playground/_build/html/01_Derivations/Equatorial_Beta_Plane_Dynamics/Equatorial_Vorticity_and_Divergence_Equations.html#assumptions-preliminaries)：** 本篇沿用 [渦度與位勢–輻散方程式](Equatorial_Vorticity_and_Divergence_Equations.md) 已經取好名字的兩個符號，不重新定義。（已於本庫 Equatorial Vorticity and Divergence Equations【定義 1】【定義 3(b)】定義，此處直接引用。）

  * (a) 擾動相對渦度：

    $$\zeta = \frac{\partial v}{\partial x} - \frac{\partial u}{\partial y}$$

  * (b) 垂直算子：

    $$\mathcal{D}_z = \frac{\partial}{\partial z} - 1$$

  * $\zeta$ : 擾動相對渦度 (Perturbation relative vorticity) $[\text{s}^{-1}]$
  * $\mathcal{D}_z$ : 垂直算子 (Vertical operator) $[\text{無單位}]$
  * $u$ : 擾動緯向風速 (Perturbation zonal velocity) $[\text{m}\cdot\text{s}^{-1}]$
  * $v$ : 擾動經向風速 (Perturbation meridional velocity) $[\text{m}\cdot\text{s}^{-1}]$
  * $x,\ y$ : 緯向、經向座標 (Zonal and meridional coordinates) $[\text{m}]$
  * $z$ : 對數氣壓垂直座標 (Log-pressure vertical coordinate) $[\text{無單位}]$

* **【已知 2】 [對數氣壓座標下的線性化原始方程組 (Log-pressure linearized primitive equations)](https://derek1403.github.io/Theory_Playground/_build/html/01_Derivations/Equatorial_Beta_Plane_Dynamics/Log_Pressure_Linearized_Primitive_Equations.html#assumptions-preliminaries)：** 本篇只用得到其中的靜力與熱力學兩條。（已於本庫 Log-Pressure Linearized Primitive Equations 完整證明，此處直接引用。）

  * (a) 靜力方程式：

    $$\frac{\partial \phi}{\partial z} = RT$$

  * (b) 熱力學方程式：

    $$\frac{\partial T}{\partial t} + \Gamma w = -\alpha T + \frac{Q}{c_p}$$

  * $\phi$ : 擾動位勢 (Perturbation geopotential) $[\text{m}^{2}\cdot\text{s}^{-2}]$
  * $T$ : 擾動溫度 (Perturbation temperature) $[\text{K}]$
  * $w$ : 擾動對數氣壓垂直速度 (Perturbation log-pressure vertical velocity) $[\text{s}^{-1}]$
  * $Q$ : 非絕熱加熱率 (Diabatic heating rate) $[\text{J}\cdot\text{kg}^{-1}\cdot\text{s}^{-1}]$
  * $z$ : 對數氣壓垂直座標 (Log-pressure vertical coordinate) $[\text{無單位}]$
  * $t$ : 時間 (Time) $[\text{s}]$
  * $R$ : 乾空氣氣體常數 (Gas constant for dry air) $[\text{J}\cdot\text{kg}^{-1}\cdot\text{K}^{-1}]$，$R \approx 287 \ \text{J}\cdot\text{kg}^{-1}\cdot\text{K}^{-1}$
  * $\Gamma$ : 靜力穩定度 (Static stability) $[\text{K}]$，$\Gamma = 23.79 \ \text{K}$
  * $\alpha$ : 常數阻尼率 (Constant damping rate) $[\text{s}^{-1}]$，$\alpha = \left(4 \ \text{days}\right)^{-1} \approx 2.89\times10^{-6} \ \text{s}^{-1}$
  * $c_p$ : 定壓比熱 (Specific heat at constant pressure) $[\text{J}\cdot\text{kg}^{-1}\cdot\text{K}^{-1}]$，$c_p \approx 1004 \ \text{J}\cdot\text{kg}^{-1}\cdot\text{K}^{-1}$

* **【已知 3】 [對數氣壓座標與參數設定 (Log-pressure coordinate and parameter definitions)](https://derek1403.github.io/Theory_Playground/_build/html/01_Derivations/Equatorial_Beta_Plane_Dynamics/Log_Pressure_Linearized_Primitive_Equations.html#assumptions-preliminaries)：** 座標本身的換算與三個參數的定義。（已於本庫 Log-Pressure Linearized Primitive Equations【定義 1】【推導 1】【定義 4】【定義 6】【假設 1(b)】【假設 5】定義或證明，此處直接引用。）

  * (a) 座標定義與氣壓的顯式形式：

    $$z = \ln\left(\frac{p_0}{P}\right), \qquad P = p_0\,e^{-z}$$

  * (b) 垂直微分算子的互換：

    $$\frac{\partial}{\partial z} = -P\frac{\partial}{\partial P}$$

  * (c) Poisson 常數：

    $$\kappa = \frac{R}{c_p}$$

  * (d) 靜力穩定度，且取為常數：

    $$\Gamma = \frac{d\bar{T}}{dz} + \kappa\bar{T} = \text{const}$$

  * (e) 赤道 $\beta$ 平面上的科氏參數：

    $$f = \beta y$$

  * $z$ : 對數氣壓垂直座標 (Log-pressure vertical coordinate) $[\text{無單位}]$
  * $P$ : 氣壓 (Pressure) $[\text{Pa}]$
  * $p_0$ : 參考氣壓 (Reference pressure) $[\text{Pa}]$，$p_0 = 1010 \ \text{mb}$
  * $\kappa$ : Poisson 常數 (Poisson constant) $[\text{無單位}]$，$\kappa \approx 0.286$
  * $R$ : 乾空氣氣體常數 (Gas constant for dry air) $[\text{J}\cdot\text{kg}^{-1}\cdot\text{K}^{-1}]$，$R \approx 287 \ \text{J}\cdot\text{kg}^{-1}\cdot\text{K}^{-1}$
  * $c_p$ : 定壓比熱 (Specific heat at constant pressure) $[\text{J}\cdot\text{kg}^{-1}\cdot\text{K}^{-1}]$，$c_p \approx 1004 \ \text{J}\cdot\text{kg}^{-1}\cdot\text{K}^{-1}$
  * $\Gamma$ : 靜力穩定度 (Static stability) $[\text{K}]$，$\Gamma = 23.79 \ \text{K}$
  * $\bar{T}(z)$ : 基本態溫度剖面 (Basic-state temperature profile) $[\text{K}]$
  * $f$ : 科氏參數 (Coriolis parameter) $[\text{s}^{-1}]$
  * $\beta$ : 赤道 $\beta$ 參數 (Equatorial beta parameter) $[\text{m}^{-1}\cdot\text{s}^{-1}]$，$\beta \approx 2.29\times10^{-11} \ \text{m}^{-1}\cdot\text{s}^{-1}$
  * $y$ : 經向座標，以赤道為原點 (Meridional coordinate) $[\text{m}]$

* **【已知 4】 [幾何高度的靜力平衡 (Hydrostatic balance in geometric height)](https://derek1403.github.io/Theory_Playground/_build/html/01_Derivations/Equatorial_Beta_Plane_Dynamics/Log_Pressure_Linearized_Primitive_Equations.html#assumptions-preliminaries)：** 換座標時要用的原始形式。（已於本庫 Log-Pressure Linearized Primitive Equations【已知 1(c)】引用，此處沿用。）

  $$\frac{\partial P}{\partial z_{\text{g}}} = -\rho g$$

  * $P$ : 氣壓 (Pressure) $[\text{Pa}]$
  * $z_{\text{g}}$ : 幾何高度 (Geometric height) $[\text{m}]$
  * $\rho$ : 密度 (Density) $[\text{kg}\cdot\text{m}^{-3}]$
  * $g$ : 重力加速度 (Gravitational acceleration) $[\text{m}\cdot\text{s}^{-2}]$，$g \approx 9.81 \ \text{m}\cdot\text{s}^{-2}$

* **【已知 5】 [繞靜止基本態的小振幅線性化 (Linearization about a resting basic state)](https://derek1403.github.io/Theory_Playground/_build/html/01_Derivations/Equatorial_Beta_Plane_Dynamics/Log_Pressure_Linearized_Primitive_Equations.html#assumptions-preliminaries)：** 基本態靜止、只隨高度變化，任意兩個擾動量的乘積一律捨棄。（已於本庫 Log-Pressure Linearized Primitive Equations【假設 2】設定，此處直接引用。）

  * (a) 基本態靜止，故速度本身就是擾動量：

    $$\bar{u} = \bar{v} = \bar{w}_{\text{g}} = 0$$

  * (b) 基本態只隨高度變化：

    $$\bar{\theta} = \bar{\theta}(z), \qquad \frac{\partial \bar{\theta}}{\partial x} = \frac{\partial \bar{\theta}}{\partial y} = 0$$

  * (c) 小振幅：

    $$\left(\text{擾動}\right)\times\left(\text{擾動}\right) \approx 0$$

  * $\bar{u},\ \bar{v}$ : 基本態緯向、經向風速 (Basic-state zonal and meridional velocities) $[\text{m}\cdot\text{s}^{-1}]$
  * $\bar{w}_{\text{g}}$ : 基本態幾何垂直速度 (Basic-state geometric vertical velocity) $[\text{m}\cdot\text{s}^{-1}]$
  * $\bar{\theta}(z)$ : 基本態位溫剖面 (Basic-state potential temperature profile) $[\text{K}]$
  * $x,\ y$ : 緯向、經向座標 (Zonal and meridional coordinates) $[\text{m}]$
  * $z$ : 對數氣壓垂直座標 (Log-pressure vertical coordinate) $[\text{無單位}]$

* **【已知 6】 [Ertel 位渦 (Ertel potential vorticity)](https://derek1403.github.io/Theory_Playground/_build/html/01_Derivations/Fluid_Dynamics_Variable_Coordinate_Physics/PV_Representations_and_Mappings/Relation_Between_PV_and_PVb.html#assumptions-preliminaries)：** 絕對渦度向量與位溫梯度的內積，除以密度。這是與座標無關的原始定義。（已於本庫 [位渦 $PV$ 與浮力位渦 $PV_b$ 的關係](../Fluid_Dynamics_Variable_Coordinate_Physics/PV_Representations_and_Mappings/Relation_Between_PV_and_PVb.md)【已知 1】定義，此處直接引用。）

  $$PV \overset{\text{def}}{=} \frac{1}{\rho}\boldsymbol{\eta}_a \cdot \nabla\theta$$

  * $PV$ : Ertel 位渦 (Ertel potential vorticity) $[\text{m}^{2}\cdot\text{s}^{-1}\cdot\text{K}\cdot\text{kg}^{-1}]$
  * $\rho$ : 密度 (Density) $[\text{kg}\cdot\text{m}^{-3}]$
  * $\boldsymbol{\eta}_a$ : 絕對渦度向量 (Absolute vorticity vector) $[\text{s}^{-1}]$，$\boldsymbol{\eta}_a = \nabla\times\mathbf{V} + f\hat{k}$
  * $\theta$ : 位溫 (Potential temperature) $[\text{K}]$
  * $\mathbf{V}$ : 三維風速向量 (Three-dimensional velocity vector) $[\text{m}\cdot\text{s}^{-1}]$
  * $f$ : 科氏參數 (Coriolis parameter) $[\text{s}^{-1}]$
  * 註：Ertel 位渦是**隨氣塊守恆**的（絕熱、無摩擦時 $\dfrac{D\left(PV\right)}{Dt} = 0$）。「隨氣塊」這三個字是本篇【證明 (b)】為什麼要取材料距平、而不是固定高度上擾動的全部理由。

* **【已知 7】 [位溫 (Potential temperature)](https://glossary.ametsoc.org/wiki/Potential_temperature)：** 把氣塊絕熱移到參考氣壓 $p_0$ 時的溫度。（標準結果，此處直接引用。）

  $$\theta = T_{\text{full}}\left(\frac{p_0}{P}\right)^{\kappa}$$

  * $\theta$ : 位溫 (Potential temperature) $[\text{K}]$
  * $T_{\text{full}}$ : 全場溫度 (Total temperature) $[\text{K}]$
  * $p_0$ : 參考氣壓 (Reference pressure) $[\text{Pa}]$，$p_0 = 1010 \ \text{mb}$
  * $P$ : 氣壓 (Pressure) $[\text{Pa}]$
  * $\kappa$ : Poisson 常數 (Poisson constant) $[\text{無單位}]$，$\kappa \approx 0.286$
  * 註：在【已知 3】(a) 的座標下 $\left(\dfrac{p_0}{P}\right)^{\kappa} = e^{\kappa z}$，故 $\theta = T_{\text{full}}\,e^{\kappa z}$。本篇沿用 [線性化原始方程組](Log_Pressure_Linearized_Primitive_Equations.md)【假設 2】末〈記號慣例〉的做法：需要區分時，全場溫度寫 $T_{\text{full}} = \bar{T} + T$，光禿的 $T$ 一律是擾動溫度。

* **【定義 1】 對數氣壓座標的偽密度 (Log-pressure pseudo-density)：** 單位水平面積、單位 $z$ 厚度所含的質量

  $$\rho_{*} \overset{\text{def}}{=} \frac{P}{g}$$

  * $\rho_{*}$ : 對數氣壓座標的偽密度 (Log-pressure pseudo-density) $[\text{kg}\cdot\text{m}^{-2}]$
  * $P$ : 氣壓 (Pressure) $[\text{Pa}]$
  * $g$ : 重力加速度 (Gravitational acceleration) $[\text{m}\cdot\text{s}^{-2}]$，$g \approx 9.81 \ \text{m}\cdot\text{s}^{-2}$
  * 註：名字裡的「偽」是因為它的單位是 $\left[\text{kg}\cdot\text{m}^{-2}\right]$ 而非 $\left[\text{kg}\cdot\text{m}^{-3}\right]$ —— $z$ 無因次，所以「單位厚度」不帶長度。它在對數氣壓座標中扮演的角色與 $\rho$ 在幾何高度座標中完全相同：質量元 $\delta M = \rho\,\delta x\,\delta y\,\delta z_{\text{g}} = \rho_{*}\,\delta x\,\delta y\,\delta z$。

* **【定義 2】 等熵面的垂直位移 (Vertical displacement of an isentropic surface)：** 某張等熵面在擾動狀態下，相對它在基本態中所在層位的位移，以 $z$ 為量度

  $$\eta \overset{\text{def}}{=} z_{\text{擾動}} - z_{\text{基本態}}$$

  * $\eta$ : 等熵面的垂直位移 (Vertical displacement of an isentropic surface) $[\text{無單位}]$
  * $z$ : 對數氣壓垂直座標 (Log-pressure vertical coordinate) $[\text{無單位}]$
  * 註：$\eta > 0$ 代表等熵面被抬高。它是一階小量，因此凡是 $\eta \times \left(\text{擾動}\right)$ 一律由【已知 5】(c) 捨去。
  * 註（符號提醒）：$\eta$ 與【已知 6】的絕對渦度向量 $\boldsymbol{\eta}_a$ **毫無關係**，只是字形相近。

* **【推導 1】 絕對渦度與位溫梯度的內積 (The dot product of absolute vorticity and the potential temperature gradient)：** 展開成三個分量，前兩項的兩個因子**都是擾動量**，故整項由【已知 5】(c) 捨去；只有垂直分量存活

  $$\begin{gather*}
  \boldsymbol{\eta}_a \cdot \nabla\theta &\overset{\text{已知 6}}{=}& \left(\frac{\partial w_{\text{g}}}{\partial y} - \frac{\partial v}{\partial z_{\text{g}}}\right)\frac{\partial \theta}{\partial x} + \left(\frac{\partial u}{\partial z_{\text{g}}} - \frac{\partial w_{\text{g}}}{\partial x}\right)\frac{\partial \theta}{\partial y} + \left(f + \frac{\partial v}{\partial x} - \frac{\partial u}{\partial y}\right)\frac{\partial \theta}{\partial z_{\text{g}}} \\
  &\overset{\text{已知 5(a)(b)}}{=}& \underbrace{\left(\frac{\partial w_{\text{g}}}{\partial y} - \frac{\partial v}{\partial z_{\text{g}}}\right)}_{\text{擾動}}\underbrace{\frac{\partial \theta}{\partial x}}_{\text{擾動}} + \underbrace{\left(\frac{\partial u}{\partial z_{\text{g}}} - \frac{\partial w_{\text{g}}}{\partial x}\right)}_{\text{擾動}}\underbrace{\frac{\partial \theta}{\partial y}}_{\text{擾動}} + \left(f + \frac{\partial v}{\partial x} - \frac{\partial u}{\partial y}\right)\frac{\partial \theta}{\partial z_{\text{g}}} \\
  &\overset{\text{已知 5(c)}}{\approx}& \left(f + \frac{\partial v}{\partial x} - \frac{\partial u}{\partial y}\right)\frac{\partial \theta}{\partial z_{\text{g}}} \\
  &\overset{\text{已知 1(a),已知 3(e)}}{=}& \left(\beta y + \zeta\right)\frac{\partial \theta}{\partial z_{\text{g}}}
  \end{gather*}$$

  * $\boldsymbol{\eta}_a$ : 絕對渦度向量 (Absolute vorticity vector) $[\text{s}^{-1}]$
  * $\theta$ : 位溫 (Potential temperature) $[\text{K}]$
  * $u$ : 擾動緯向風速 (Perturbation zonal velocity) $[\text{m}\cdot\text{s}^{-1}]$
  * $v$ : 擾動經向風速 (Perturbation meridional velocity) $[\text{m}\cdot\text{s}^{-1}]$
  * $w_{\text{g}}$ : 擾動幾何垂直速度 (Perturbation geometric vertical velocity) $[\text{m}\cdot\text{s}^{-1}]$
  * $x,\ y$ : 緯向、經向座標 (Zonal and meridional coordinates) $[\text{m}]$
  * $z_{\text{g}}$ : 幾何高度 (Geometric height) $[\text{m}]$
  * $f$ : 科氏參數 (Coriolis parameter) $[\text{s}^{-1}]$
  * $\beta$ : 赤道 $\beta$ 參數 (Equatorial beta parameter) $[\text{m}^{-1}\cdot\text{s}^{-1}]$
  * $\zeta$ : 擾動相對渦度 (Perturbation relative vorticity) $[\text{s}^{-1}]$
  * 註：$\dfrac{\partial \theta}{\partial x}$ 之所以整個是擾動量，是因為【已知 5】(b) 的 $\dfrac{\partial \bar{\theta}}{\partial x} = 0$ —— 基本態位溫只隨高度變化，水平方向沒有梯度可貢獻。這與 [線性化原始方程組](Log_Pressure_Linearized_Primitive_Equations.md)【假設 2】(c-2)(c-3) 消掉度規項用的是同一招。
  * 註：垂直分量**不能**同樣捨去，因為 $f = \beta y$ 與 $\dfrac{\partial \bar{\theta}}{\partial z_{\text{g}}}$ 都是**基本態**量，$\left(f+\zeta\right)\dfrac{\partial\theta}{\partial z_{\text{g}}}$ 展開後含有「基本態 $\times$ 基本態」與「基本態 $\times$ 擾動」兩種一階以內的項。

* **【推導 2】 密度加權垂直微分的座標變換 (Coordinate change of the density-weighted vertical derivative)：** $\dfrac{1}{\rho}\dfrac{\partial}{\partial z_{\text{g}}}$ 這個組合換到對數氣壓座標後，密度 $\rho$ 完全消失，換成氣壓

  $$\begin{gather*}
  \frac{\partial}{\partial z_{\text{g}}} &=& \frac{\partial P}{\partial z_{\text{g}}}\frac{\partial}{\partial P} \\
  &\overset{\text{已知 4}}{=}& -\rho g\frac{\partial}{\partial P} \\
  &\overset{\text{已知 3(b)}}{=}& -\rho g\left(-\frac{1}{P}\frac{\partial}{\partial z}\right) \\
  &=& \frac{\rho g}{P}\frac{\partial}{\partial z} \\
  \frac{1}{\rho}\frac{\partial}{\partial z_{\text{g}}} &=& \frac{g}{P}\frac{\partial}{\partial z} \\
  &\overset{\text{定義 1}}{=}& \frac{1}{\rho_{*}}\frac{\partial}{\partial z}
  \end{gather*}$$

  * $z_{\text{g}}$ : 幾何高度 (Geometric height) $[\text{m}]$
  * $P$ : 氣壓 (Pressure) $[\text{Pa}]$
  * $\rho$ : 密度 (Density) $[\text{kg}\cdot\text{m}^{-3}]$
  * $g$ : 重力加速度 (Gravitational acceleration) $[\text{m}\cdot\text{s}^{-2}]$，$g \approx 9.81 \ \text{m}\cdot\text{s}^{-2}$
  * $z$ : 對數氣壓垂直座標 (Log-pressure vertical coordinate) $[\text{無單位}]$
  * $\rho_{*}$ : 對數氣壓座標的偽密度 (Log-pressure pseudo-density) $[\text{kg}\cdot\text{m}^{-2}]$
  * 註：最後一列說明了為什麼 $\rho_{*}$ 值得單獨取名字 —— 它讓「幾何高度座標的 $\rho$」與「對數氣壓座標的 $\rho_{*}$」在公式裡站在完全相同的位置。

* **【推導 3】 垂直算子就是偽密度加權的垂直微分 (The vertical operator is the pseudo-density-weighted vertical derivative)：** 偽密度隨 $z$ 指數遞減，這個 $e^{-z}$ 微分下來就是 $\mathcal{D}_z$ 裡那個 $-1$

  * (a) 偽密度的顯式形式：

    $$\begin{gather*}
    \rho_{*} &\overset{\text{定義 1}}{=}& \frac{P}{g} \\
    &\overset{\text{已知 3(a)}}{=}& \frac{p_0}{g}\,e^{-z}
    \end{gather*}$$

  * (b) 偽密度加權的垂直微分：

    $$\begin{gather*}
    \frac{1}{\rho_{*}}\frac{\partial}{\partial z}\left[\rho_{*} X\right] &\overset{\text{推導 3(a)}}{=}& \frac{g}{p_0}e^{z}\frac{\partial}{\partial z}\left[\frac{p_0}{g}e^{-z}X\right] \\
    &=& e^{z}\frac{\partial}{\partial z}\left[e^{-z}X\right] \\
    &=& e^{z}\left[e^{-z}\frac{\partial X}{\partial z} - e^{-z}X\right] \\
    &=& \frac{\partial X}{\partial z} - X \\
    &\overset{\text{已知 1(b)}}{=}& \mathcal{D}_z\left[X\right]
    \end{gather*}$$

  * $\rho_{*}$ : 對數氣壓座標的偽密度 (Log-pressure pseudo-density) $[\text{kg}\cdot\text{m}^{-2}]$
  * $P$ : 氣壓 (Pressure) $[\text{Pa}]$
  * $p_0$ : 參考氣壓 (Reference pressure) $[\text{Pa}]$，$p_0 = 1010 \ \text{mb}$
  * $g$ : 重力加速度 (Gravitational acceleration) $[\text{m}\cdot\text{s}^{-2}]$，$g \approx 9.81 \ \text{m}\cdot\text{s}^{-2}$
  * $z$ : 對數氣壓垂直座標 (Log-pressure vertical coordinate) $[\text{無單位}]$
  * $X$ : 任意可微的場 (Arbitrary differentiable field) $[\text{依應用而定}]$
  * $\mathcal{D}_z$ : 垂直算子 (Vertical operator) $[\text{無單位}]$
  * 註：**這一條把 $\mathcal{D}_z$ 的來歷講死了。** [渦度與位勢–輻散方程式](Equatorial_Vorticity_and_Divergence_Equations.md)【定義 3】的註只說「它的來源是密度隨高度指數遞減」，這裡給出等式：$\mathcal{D}_z$ **就是**偽密度加權的垂直微分。連續方程式那個 $-w$、與 $q$ 裡那個 $-1$，是同一個 $\rho_{*} \propto e^{-z}$ 的兩張臉。

* **【推導 4】 基本態的位溫垂直梯度 (Vertical gradient of the basic-state potential temperature)：** 把【已知 7】用在基本態上，$\Gamma$ 的定義式**自己長出來**

  $$\begin{gather*}
  \bar{\theta} &\overset{\text{已知 7}}{=}& \bar{T}\,e^{\kappa z} \\
  \frac{\partial \bar{\theta}}{\partial z} &=& \frac{d\bar{T}}{dz}e^{\kappa z} + \kappa\bar{T}e^{\kappa z} \\
  &=& \left[\frac{d\bar{T}}{dz} + \kappa\bar{T}\right]e^{\kappa z} \\
  &\overset{\text{已知 3(d)}}{=}& \Gamma\,e^{\kappa z}
  \end{gather*}$$

  * $\bar{\theta}(z)$ : 基本態位溫剖面 (Basic-state potential temperature profile) $[\text{K}]$
  * $\bar{T}(z)$ : 基本態溫度剖面 (Basic-state temperature profile) $[\text{K}]$
  * $\kappa$ : Poisson 常數 (Poisson constant) $[\text{無單位}]$，$\kappa \approx 0.286$
  * $z$ : 對數氣壓垂直座標 (Log-pressure vertical coordinate) $[\text{無單位}]$
  * $\Gamma$ : 靜力穩定度 (Static stability) $[\text{K}]$，$\Gamma = 23.79 \ \text{K}$
  * 註：**這就是 [線性化原始方程組](Log_Pressure_Linearized_Primitive_Equations.md)【定義 6】把 $\Gamma$ 定成 $\dfrac{d\bar{T}}{dz} + \kappa\bar{T}$ 的理由。** 那張卡片只給了式子、沒說為什麼是這個組合；答案是：它就是基本態位溫的垂直梯度（除掉共同因子 $e^{\kappa z}$）。$\Gamma > 0$ 等價於 $\dfrac{\partial \bar{\theta}}{\partial z} > 0$，也就是層結穩定。

* **【推導 5】 等熵位移與溫度、位勢的關係 (Relating the isentropic displacement to temperature and geopotential)：** 等熵面上位溫不變，把「面移動了 $\eta$」翻譯成「原地的位溫擾動是多少」

  $$\begin{gather*}
  \bar{\theta}(z) &\overset{\text{定義 2}}{=}& \bar{\theta}\left(z + \eta\right) + \theta'\left(z + \eta\right) \\
  &\overset{\text{已知 5(c)}}{\approx}& \bar{\theta}(z) + \eta\frac{\partial \bar{\theta}}{\partial z} + \theta' \\
  0 &=& \eta\frac{\partial \bar{\theta}}{\partial z} + \theta' \\
  \theta' &=& -\eta\frac{\partial \bar{\theta}}{\partial z} \\
  T\,e^{\kappa z} &\overset{\text{已知 7,推導 4}}{=}& -\eta\,\Gamma\,e^{\kappa z} \\
  \eta &=& -\frac{T}{\Gamma} \\
  \eta &\overset{\text{已知 2(a)}}{=}& -\frac{1}{R\Gamma}\frac{\partial \phi}{\partial z}
  \end{gather*}$$

  * $\bar{\theta}(z)$ : 基本態位溫剖面 (Basic-state potential temperature profile) $[\text{K}]$
  * $\theta'$ : 擾動位溫 (Perturbation potential temperature) $[\text{K}]$
  * $\eta$ : 等熵面的垂直位移 (Vertical displacement of an isentropic surface) $[\text{無單位}]$
  * $T$ : 擾動溫度 (Perturbation temperature) $[\text{K}]$
  * $\kappa$ : Poisson 常數 (Poisson constant) $[\text{無單位}]$，$\kappa \approx 0.286$
  * $\Gamma$ : 靜力穩定度 (Static stability) $[\text{K}]$，$\Gamma = 23.79 \ \text{K}$
  * $\phi$ : 擾動位勢 (Perturbation geopotential) $[\text{m}^{2}\cdot\text{s}^{-2}]$
  * $R$ : 乾空氣氣體常數 (Gas constant for dry air) $[\text{J}\cdot\text{kg}^{-1}\cdot\text{K}^{-1}]$，$R \approx 287 \ \text{J}\cdot\text{kg}^{-1}\cdot\text{K}^{-1}$
  * $z$ : 對數氣壓垂直座標 (Log-pressure vertical coordinate) $[\text{無單位}]$
  * 註：第一列的意思是「本來在 $z$ 的那張等熵面，現在跑到 $z+\eta$；它的位溫值不變，仍是 $\bar{\theta}(z)$」。負號的物理是：等熵面被**抬高**（$\eta > 0$），代表原地的空氣是從下方（較冷、位溫較低）被抬上來的，故 $T < 0$。
  * 註：$\eta$ 與 $\dfrac{\partial\phi}{\partial z}$ 只差一個負常數 —— 這是後面 [可逆性原理](Equatorial_PV_Invertibility_Principle.md) 能把 $q$ 反演回質量場的根本原因：$q$ 的層結項裝的就是等熵面的形狀。

* **【推導 6】 等熵層質量的線性變化 (Linear change of the mass between two isentropes)：** 夾在兩張等熵面之間、單位水平面積的氣柱，其質量的相對變化恰好是 $\mathcal{D}_z\left[\eta\right]$

  * (a) 基本態：底面在 $z$、頂面在 $z + \Delta z$：

    $$\overline{\Delta m} = \rho_{*}(z)\,\Delta z$$

  * (b) 擾動態：底面移到 $z + \eta(z)$、頂面移到 $z + \Delta z + \eta(z + \Delta z)$，故厚度與偽密度各自改變：

    $$\begin{gather*}
    \Delta z_{\text{擾動}} &=& \left[z + \Delta z + \eta\left(z+\Delta z\right)\right] - \left[z + \eta(z)\right] \\
    &=& \Delta z + \left[\eta\left(z+\Delta z\right) - \eta(z)\right] \\
    &\overset{\Delta z \to 0}{=}& \Delta z\left(1 + \frac{\partial \eta}{\partial z}\right) \\
    \rho_{*}\left(z + \eta\right) &\overset{\text{推導 3(a)}}{=}& \frac{p_0}{g}e^{-\left(z+\eta\right)} \\
    &=& \rho_{*}(z)\,e^{-\eta} \\
    &\overset{\text{已知 5(c)}}{\approx}& \rho_{*}(z)\left(1 - \eta\right)
    \end{gather*}$$

  * (c) 兩者相乘，捨去 $\eta$ 的二次項：

    $$\begin{gather*}
    \Delta m &\overset{\text{推導 6(b)}}{=}& \rho_{*}(z)\left(1 - \eta\right)\Delta z\left(1 + \frac{\partial \eta}{\partial z}\right) \\
    &\overset{\text{已知 5(c)}}{\approx}& \rho_{*}(z)\,\Delta z\left(1 - \eta + \frac{\partial \eta}{\partial z}\right) \\
    &\overset{\text{推導 6(a)}}{=}& \overline{\Delta m}\left(1 + \frac{\partial \eta}{\partial z} - \eta\right) \\
    \frac{\Delta m - \overline{\Delta m}}{\overline{\Delta m}} &=& \frac{\partial \eta}{\partial z} - \eta \\
    \frac{\delta\left(\Delta m\right)}{\overline{\Delta m}} &\overset{\text{已知 1(b)}}{=}& \mathcal{D}_z\left[\eta\right]
    \end{gather*}$$

  * $\Delta m$ : 兩等熵面之間、單位水平面積的質量 (Mass per unit area between two isentropes) $[\text{kg}\cdot\text{m}^{-2}]$
  * $\overline{\Delta m}$ : 同上，基本態值 (Same, basic-state value) $[\text{kg}\cdot\text{m}^{-2}]$
  * $\rho_{*}$ : 對數氣壓座標的偽密度 (Log-pressure pseudo-density) $[\text{kg}\cdot\text{m}^{-2}]$
  * $\eta$ : 等熵面的垂直位移 (Vertical displacement of an isentropic surface) $[\text{無單位}]$
  * $z$ : 對數氣壓垂直座標 (Log-pressure vertical coordinate) $[\text{無單位}]$
  * $p_0$ : 參考氣壓 (Reference pressure) $[\text{Pa}]$，$p_0 = 1010 \ \text{mb}$
  * $g$ : 重力加速度 (Gravitational acceleration) $[\text{m}\cdot\text{s}^{-2}]$，$g \approx 9.81 \ \text{m}\cdot\text{s}^{-2}$
  * $\mathcal{D}_z$ : 垂直算子 (Vertical operator) $[\text{無單位}]$
  * 註：$\mathcal{D}_z\left[\eta\right]$ 這兩項各有各的物理 —— $\dfrac{\partial\eta}{\partial z}$ 是**厚度**變了（上下兩面拉開或壓扁），$-\eta$ 是**密度**變了（整層被抬到氣壓較低處，同樣厚度裝的質量變少）。在不可壓縮的 Boussinesq 系統裡只有第一項，第二項純粹是可壓縮性的貢獻。
  * 註：兩張等熵面都是**物質面**（絕熱時氣塊不能穿越），所以「這一層的質量」才是有意義的追蹤對象。這正是位渦守恆的物理基礎。

* **【推導 7】 加熱造成的等熵面相對位移速率 (Diabatic rate of change of the isentropic displacement)：** 把熱力學方程式改寫成 $\eta$ 的傾向方程式，三項各有各的身分

  $$\begin{gather*}
  \frac{\partial T}{\partial t} &\overset{\text{已知 2(b)}}{=}& -\Gamma w - \alpha T + \frac{Q}{c_p} \\
  \frac{\partial \eta}{\partial t} &\overset{\text{推導 5,已知 3(d)}}{=}& -\frac{1}{\Gamma}\frac{\partial T}{\partial t} \\
  &=& -\frac{1}{\Gamma}\left[-\Gamma w - \alpha T + \frac{Q}{c_p}\right] \\
  &=& \underbrace{w}_{\text{隨氣流升降}} + \underbrace{\frac{\alpha T}{\Gamma}}_{\text{Newtonian 鬆弛}} - \underbrace{\frac{Q}{c_p\Gamma}}_{\text{加熱}} \\
  \left(\frac{\partial \eta}{\partial t}\right)_{\text{加熱}} &=& -\frac{Q}{c_p\Gamma}
  \end{gather*}$$

  * $T$ : 擾動溫度 (Perturbation temperature) $[\text{K}]$
  * $\eta$ : 等熵面的垂直位移 (Vertical displacement of an isentropic surface) $[\text{無單位}]$
  * $t$ : 時間 (Time) $[\text{s}]$
  * $w$ : 擾動對數氣壓垂直速度 (Perturbation log-pressure vertical velocity) $[\text{s}^{-1}]$
  * $\Gamma$ : 靜力穩定度 (Static stability) $[\text{K}]$，$\Gamma = 23.79 \ \text{K}$
  * $\alpha$ : 常數阻尼率 (Constant damping rate) $[\text{s}^{-1}]$，$\alpha = \left(4 \ \text{days}\right)^{-1} \approx 2.89\times10^{-6} \ \text{s}^{-1}$
  * $Q$ : 非絕熱加熱率 (Diabatic heating rate) $[\text{J}\cdot\text{kg}^{-1}\cdot\text{s}^{-1}]$
  * $c_p$ : 定壓比熱 (Specific heat at constant pressure) $[\text{J}\cdot\text{kg}^{-1}\cdot\text{K}^{-1}]$，$c_p \approx 1004 \ \text{J}\cdot\text{kg}^{-1}\cdot\text{K}^{-1}$
  * 註：第一項 $w$ 是**絕熱**位移 —— 等熵面隨氣流一起上下，氣塊沒有穿越它，位渦不變。真正改變位渦的是第三項：加熱讓氣塊的位溫上升，於是氣塊**穿越**到上方的等熵面去；換個角度看，就是等熵面相對氣塊往下掉，故取負號。

+++

## 證明:

### (a) proof 位渦的對數氣壓形式 (Ertel PV in log-pressure coordinates)

把【推導 1】的內積與【推導 2】的座標變換代進【已知 6】。$\rho$ 與 $\dfrac{\partial}{\partial z_{\text{g}}}$ 一起消失，換成偽密度 $\rho_{*}$ 與 $\dfrac{\partial}{\partial z}$。

$$\begin{gather*}
PV &\overset{\text{已知 6}}{=}& \frac{1}{\rho}\boldsymbol{\eta}_a \cdot \nabla\theta \\
&\overset{\text{推導 1}}{=}& \frac{1}{\rho}\left(\beta y + \zeta\right)\frac{\partial \theta}{\partial z_{\text{g}}} \\
&=& \left(\beta y + \zeta\right)\frac{1}{\rho}\frac{\partial \theta}{\partial z_{\text{g}}} \\
&\overset{\text{推導 2}}{=}& \left(\beta y + \zeta\right)\frac{1}{\rho_{*}}\frac{\partial \theta}{\partial z} \\
&=& \frac{\beta y + \zeta}{\rho_{*}}\frac{\partial \theta}{\partial z}
\end{gather*}$$

### (b) proof 位渦距平 (Potential vorticity anomaly)

先把【證明 (a)】改寫成「絕對渦度 ÷ 單位位溫的質量」，再與基本態相除。
關鍵在於：兩張等熵面是**物質面**，跟著氣塊走時 $\Delta\theta$ 是這一柱空氣的**標籤**、不隨時間變，因此相除之後 $\Delta\theta$ 直接對消，只剩「渦度的相對變化」減「質量的相對變化」。

$$\begin{gather*}
PV &\overset{\text{證明 (a)}}{=}& \frac{\beta y + \zeta}{\rho_{*}}\frac{\partial \theta}{\partial z} \\
&\overset{\text{定義 1}}{=}& \frac{\left(\beta y + \zeta\right)\Delta\theta}{\Delta m} \\
\overline{PV} &\overset{\text{推導 6(a)}}{=}& \frac{\beta y\,\Delta\theta}{\overline{\Delta m}} \\
\frac{PV}{\overline{PV}} &=& \frac{\left(\beta y + \zeta\right)\big/\Delta m}{\beta y\big/\overline{\Delta m}} \\
&=& \frac{1 + \dfrac{\zeta}{\beta y}}{1 + \dfrac{\delta\left(\Delta m\right)}{\overline{\Delta m}}} \\
&\overset{\text{已知 5(c)}}{\approx}& \left(1 + \frac{\zeta}{\beta y}\right)\left(1 - \frac{\delta\left(\Delta m\right)}{\overline{\Delta m}}\right) \\
&\overset{\text{已知 5(c)}}{\approx}& 1 + \frac{\zeta}{\beta y} - \frac{\delta\left(\Delta m\right)}{\overline{\Delta m}} \\
\frac{\delta PV}{\overline{PV}} &=& \frac{\zeta}{\beta y} - \frac{\delta\left(\Delta m\right)}{\overline{\Delta m}} \\
&\overset{\text{推導 6(c)}}{=}& \frac{\zeta}{\beta y} - \mathcal{D}_z\left[\eta\right] \\
\beta y\,\frac{\delta PV}{\overline{PV}} &=& \zeta - \beta y\,\mathcal{D}_z\left[\eta\right] \\
&\overset{\text{推導 5}}{=}& \zeta - \beta y\,\mathcal{D}_z\left[-\frac{1}{R\Gamma}\frac{\partial \phi}{\partial z}\right] \\
&=& \zeta + \frac{\beta y}{R\Gamma}\,\mathcal{D}_z\left[\frac{\partial \phi}{\partial z}\right]
\end{gather*}$$

### (c) proof 位渦源項 (Potential vorticity source)

加熱不直接生成渦度，只能透過**改變等熵層的厚薄**來改變位渦。
因此把【證明 (b)】對時間微分時，$\zeta$ 那一項沒有加熱的份，只剩 $\eta$ 那一項。

$$\begin{gather*}
\beta y\,\frac{\delta PV}{\overline{PV}} &\overset{\text{證明 (b)}}{=}& \zeta - \beta y\,\mathcal{D}_z\left[\eta\right] \\
\left(\frac{\partial}{\partial t}\left[\beta y\,\frac{\delta PV}{\overline{PV}}\right]\right)_{\text{加熱}} &=& \underbrace{\left(\frac{\partial \zeta}{\partial t}\right)_{\text{加熱}}}_{=\ 0} - \beta y\,\mathcal{D}_z\left[\left(\frac{\partial \eta}{\partial t}\right)_{\text{加熱}}\right] \\
&\overset{\text{推導 7}}{=}& -\beta y\,\mathcal{D}_z\left[-\frac{Q}{c_p\Gamma}\right] \\
&\overset{\text{已知 3(d)}}{=}& \frac{\beta y}{c_p\Gamma}\,\mathcal{D}_z\left[Q\right]
\end{gather*}$$

+++

## 物理解釋

### 為什麼一定要走「跟著氣塊走」的距平

【證明 (b)】取的是 $\dfrac{\delta PV}{\overline{PV}}$，其中 $\delta PV$ 是**氣塊自己的位渦，減去它原本所在層位的基本態位渦**。這不是隨便選的。

如果改成「固定高度上的 Eulerian 擾動」$PV'$ —— 也就是把 $\theta = \bar\theta + \theta'$ 直接代進【證明 (a)】、比較同一個 $z$ 上的新舊值 —— 算出來會是

$$\beta y\,\frac{PV'}{\overline{PV}} = \zeta + \frac{\beta y}{\Gamma}\left(\frac{\partial}{\partial z} + \kappa\right)T$$

括號裡是 $\left(\dfrac{\partial}{\partial z} + \kappa\right)$，**不是** $\mathcal{D}_z = \dfrac{\partial}{\partial z} - 1$。兩者差了 $\beta y\left(1 + \kappa\right)\eta$。

差別的來源是：由【推導 3】(a) 與【推導 4】，基本態位渦本身隨高度指數成長，

$$\overline{PV} = \frac{g}{p_0}\,\beta y\,\Gamma\,e^{\left(1+\kappa\right)z}, \qquad \frac{\partial \overline{PV}}{\partial z} = \left(1+\kappa\right)\overline{PV}$$

所以一個氣塊只要**上下移動一點點**，即使它的位渦一點都沒變，固定高度上量到的 $PV'$ 也會出現一個假訊號 $-\eta\,\dfrac{\partial\overline{PV}}{\partial z}$。而 Ertel 位渦是**隨氣塊**守恆的（【已知 6】註），所以要寫出一條乾淨的守恆律，就必須把這個假訊號扣掉 —— 扣掉之後剩下的，正是 $\dfrac{\delta PV}{\overline{PV}}$，也正是 $q$。

換句話說：**$(2.7)$ 那個 $\mathcal{D}_z$ 之所以是 $\dfrac{\partial}{\partial z}-1$ 而不是 $\dfrac{\partial}{\partial z}+\kappa$，是「材料距平」與「Eulerian 擾動」之差在算符上的印記。**

### $q$ 就是氣塊離家多遠

把【證明 (b)】的推導在絕熱、無阻尼的情形下重跑一次，可以得到一個更露骨的結果。
取一柱空氣，原本在 $y_0$、位渦為 $\dfrac{\beta y_0\,\Delta\theta}{\overline{\Delta m}}$；它南北移動了 $Y$、渦度變成 $\zeta$、質量變成 $\Delta m$。位渦守恆給

$$\frac{\left(\beta y_0 + \beta Y + \zeta\right)\Delta\theta}{\Delta m} = \frac{\beta y_0\,\Delta\theta}{\overline{\Delta m}}$$

用【推導 6】(c) 展開並線性化（$y \approx y_0$），整理得

$$\zeta - \beta y\,\mathcal{D}_z\left[\eta\right] = -\beta Y \qquad \Longrightarrow \qquad q = -\beta Y$$

**$q$ 不多不少就是「$-\beta\ \times$ 氣塊離開原本緯度的距離」。** 對時間微分、注意 $\dfrac{\partial Y}{\partial t} = v$，立刻回到 [PV 方程式](Equatorial_PV_Equation_and_Beta_y_Source.md)【證明 (b)】的 Rossby 項 $\dfrac{\partial q}{\partial t} + \beta v = 0$。

這個讀法順手解釋了本鏈另一個結論：**[Kelvin 波的 $q$ 恰好為零](Physical_Field_Recovery_and_Zero_Kelvin_PV.md)**。Kelvin 波的定義性質就是 $v \equiv 0$ —— 沒有經向運動，就沒有任何氣塊離開它的原始緯度，$Y \equiv 0$，於是 $q \equiv 0$。那不是近似造成的巧合，而是**恆等式**：Kelvin 波根本沒有把任何資訊存進 $q$ 這個變數裡。

### 加熱為什麼生成的是上下反號的一對

【證明 (c)】說加熱透過 $\mathcal{D}_z\left[Q\right]$ 生成位渦。用【推導 6】的兩張等熵面來看就很直白：

* 在加熱極大值**下方**，加熱隨高度遞增，上面那張等熵面被推得比下面那張更快往下掉 → 這一層**變薄** → 質量變少 → 位渦增加。
* 在加熱極大值**上方**，情況完全相反 → 這一層**變厚** → 位渦減少。

於是同一個加熱在垂直方向生成一對反號的位渦。這正是 [PV 方程式](Equatorial_PV_Equation_and_Beta_y_Source.md)〈物理解釋〉裡那張「四塊」表格的上下兩列。至於南北兩側為什麼也反號，那是 $\beta y$ 這個奇函數因子的功勞，與本篇的 $\mathcal{D}_z$ 無關 —— 兩個機制各管一個方向。

### $\mathcal{D}_z$ 的兩張臉

本篇最省事的收穫大概是【推導 3】：

$$\mathcal{D}_z\left[X\right] = \frac{1}{\rho_{*}}\frac{\partial}{\partial z}\left[\rho_{*}X\right], \qquad \rho_{*} \propto e^{-z}$$

同一個 $\rho_{*} \propto e^{-z}$，在 [線性化原始方程組](Log_Pressure_Linearized_Primitive_Equations.md)【推導 6】長成連續方程式裡那個礙眼的 $-w$，在本篇長成位渦裡那個 $-1$。看懂這一點之後，$\mathcal{D}_z$ 就不再是「為了讓式子短一點而取的名字」，而是**對數氣壓座標下唯一正確的「質量加權垂直微分」**。

順帶一提，[Schubert & Masarik (2006)](../../06_References/Tropical_wave_dynamics/Schubert2006-Potential_vorticity_aspects_of_the_MJO/Potential_vorticity_aspects_of_the_MJO.ipynb) $(2.3)$ 的總能量積分帶著權重 $e^{-z}\,dx\,dy\,dz$ —— 那也是同一個 $\rho_{*}$。能量、連續方程式、位渦，三處的 $e^{-z}$ 是同一件事。
