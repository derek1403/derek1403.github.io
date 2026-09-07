# Equatorial PV Equation and the Beta-y Source (赤道 PV 方程式與 βy 源項)

+++

## 證明目標:

把 [渦度方程式與位勢–輻散方程式](Equatorial_Vorticity_and_Divergence_Equations.md) 之間的水平輻散消掉，
就會浮現一個**只含單一變數**的守恆型方程式。那個變數就是位渦距平 $q$。

* (a) 消去水平輻散後，$\mathcal{D}_t$ 括號裡自然浮現的組合即為**位渦距平**：

$$q = \frac{\partial v}{\partial x} - \frac{\partial u}{\partial y} + \frac{\beta y}{R\Gamma}\left(\frac{\partial}{\partial z} - 1\right)\frac{\partial \phi}{\partial z}$$

* (b) 它滿足帶阻尼與源項的 PV 方程式：

$$\frac{\partial q}{\partial t} + \beta v = -\alpha q + \frac{\beta y}{c_p\Gamma}\left(\frac{\partial}{\partial z} - 1\right)Q$$

* (c) **★ 源項在赤道上恆為零** —— 不論加熱多強：

$$\left.S\right|_{y = 0} = 0$$

* (d) **★ 對南北對稱的加熱，源項是 $y$ 的奇函數** —— 因此赤道南北兩側生成的 PV 距平**大小相等、正負相反**：

$$S(x, -y, z) = -S(x, y, z)$$

* (e) **★ 對高斯型的經向加熱剖面，源項的極值不在加熱中心，而在中心南北兩側 $b_0/2^{1/2}$ 處**：

$$y_{\text{ext}} = \pm\frac{b_0}{2^{1/2}}$$

其中

* $q$ : 位渦距平 (Potential vorticity anomaly) $[\text{s}^{-1}]$
* $S$ : PV 源項 (PV source term) $[\text{s}^{-2}]$
* $u$ : 擾動緯向風速 (Perturbation zonal velocity) $[\text{m}\cdot\text{s}^{-1}]$
* $v$ : 擾動經向風速 (Perturbation meridional velocity) $[\text{m}\cdot\text{s}^{-1}]$
* $\phi$ : 擾動位勢 (Perturbation geopotential) $[\text{m}^{2}\cdot\text{s}^{-2}]$
* $Q$ : 非絕熱加熱率 (Diabatic heating rate) $[\text{J}\cdot\text{kg}^{-1}\cdot\text{s}^{-1}]$
* $y_{\text{ext}}$ : 源項極值的經向位置 (Meridional location of the source extrema) $[\text{m}]$
* $x,\ y$ : 緯向、經向座標 (Zonal and meridional coordinates) $[\text{m}]$
* $z$ : 對數氣壓垂直座標 (Log-pressure vertical coordinate) $[\text{無單位}]$
* $t$ : 時間 (Time) $[\text{s}]$
* $\alpha$ : 常數阻尼率 (Constant damping rate) $[\text{s}^{-1}]$
* $\beta$ : 赤道 $\beta$ 參數 (Equatorial beta parameter) $[\text{m}^{-1}\cdot\text{s}^{-1}]$
* $\Gamma$ : 靜力穩定度 (Static stability) $[\text{K}]$，$\Gamma = 23.79 \ \text{K}$
* $R$ : 乾空氣氣體常數 (Gas constant for dry air) $[\text{J}\cdot\text{kg}^{-1}\cdot\text{K}^{-1}]$
* $c_p$ : 定壓比熱 (Specific heat at constant pressure) $[\text{J}\cdot\text{kg}^{-1}\cdot\text{K}^{-1}]$
* $b_0$ : 加熱區的經向 $e$-folding 寬度 (Meridional $e$-folding width) $[\text{m}]$，$b_0 = 450 \ \text{km}$
* $\mathcal{D}_t$ : 阻尼時間算子 (Damped-tendency operator) $[\text{s}^{-1}]$，$\mathcal{D}_t = \dfrac{\partial}{\partial t} + \alpha$
* $\mathcal{D}_z$ : 垂直算子 (Vertical operator) $[\text{無單位}]$，$\mathcal{D}_z = \dfrac{\partial}{\partial z} - 1$
* 註：(a)(b) 就是 [Schubert & Masarik (2006)](../../06_References/Tropical_wave_dynamics/Schubert2006-Potential_vorticity_aspects_of_the_MJO/Potential_vorticity_aspects_of_the_MJO.ipynb) 的 $(2.7)$ 與 $(2.6)$。
* 註：本篇證的是「$q$ **滿足什麼方程式**」。至於「$q$ **憑什麼叫位渦**」，是另一件事，已在 [線性化位渦](Linearized_Potential_Vorticity_in_Log_Pressure.md) 從 Ertel 位渦的原始定義證出來，本篇以【已知 6】【已知 7】直接引用。兩篇合起來，$q$ 與 $S$ 才算完全沒有留白。
* 註：**(c)(d)(e) 是全文的物理引擎。** 它們合起來說：一個東移的赤道熱源，會在身後拖出**兩條反號的 PV 帶** —— 作者把這個形態比喻為大型飛機後方的一對**翼尖渦 (wing-tip vortices)**。後續 [PV 尾流](PV_Wake_of_a_Moving_Heat_Source.md)、[可逆性原理](Equatorial_PV_Invertibility_Principle.md) 兩個端點都建立在這三條之上。

+++

## 假設與已知 (Assumptions & Preliminaries)

* **【已知 1】 [符號約定：兩個場與兩個算子 (Notation: two fields and two operators)](https://derek1403.github.io/Theory_Playground/_build/html/01_Derivations/Equatorial_Beta_Plane_Dynamics/Equatorial_Vorticity_and_Divergence_Equations.html#assumptions-preliminaries)：** 本篇全程使用的四個縮寫，全部在 [渦度與位勢–輻散方程式](Equatorial_Vorticity_and_Divergence_Equations.md) 已經取好名字，此處集中列出、後續卡片不再重複。（已於本庫 Equatorial Vorticity and Divergence Equations【定義 1】【定義 2】【定義 3】定義，此處直接引用。）

  * (a) 擾動相對渦度：

    $$\zeta = \frac{\partial v}{\partial x} - \frac{\partial u}{\partial y}$$

  * (b) 擾動水平輻散：

    $$\delta = \frac{\partial u}{\partial x} + \frac{\partial v}{\partial y}$$

  * (c) 阻尼時間算子：

    $$\mathcal{D}_t = \frac{\partial}{\partial t} + \alpha$$

  * (d) 垂直算子：

    $$\mathcal{D}_z = \frac{\partial}{\partial z} - 1$$

  * $\zeta$ : 擾動相對渦度 (Perturbation relative vorticity) $[\text{s}^{-1}]$
  * $\delta$ : 擾動水平輻散 (Perturbation horizontal divergence) $[\text{s}^{-1}]$
  * $\mathcal{D}_t$ : 阻尼時間算子 (Damped-tendency operator) $[\text{s}^{-1}]$
  * $\mathcal{D}_z$ : 垂直算子 (Vertical operator) $[\text{無單位}]$
  * $u$ : 擾動緯向風速 (Perturbation zonal velocity) $[\text{m}\cdot\text{s}^{-1}]$
  * $v$ : 擾動經向風速 (Perturbation meridional velocity) $[\text{m}\cdot\text{s}^{-1}]$
  * $x,\ y$ : 緯向、經向座標 (Zonal and meridional coordinates) $[\text{m}]$
  * $z$ : 對數氣壓垂直座標 (Log-pressure vertical coordinate) $[\text{無單位}]$
  * $t$ : 時間 (Time) $[\text{s}]$
  * $\alpha$ : 常數阻尼率 (Constant damping rate) $[\text{s}^{-1}]$，$\alpha = \left(4 \ \text{days}\right)^{-1} \approx 2.89\times10^{-6} \ \text{s}^{-1}$
  * 註：(c)(d) 這兩個算子彼此可交換，且任何不隨 $z$ 變化的係數都能穿過 $\mathcal{D}_z$ —— 已於同一篇【推導 1】(a)(b) 證明，本篇需要時直接使用。
  * 註：$\mathcal{D}_z$ 那個 $-1$ 不是為了湊式子。由 [線性化位渦](Linearized_Potential_Vorticity_in_Log_Pressure.md)【推導 3】，$\mathcal{D}_z\left[X\right] = \dfrac{1}{\rho_{*}}\dfrac{\partial}{\partial z}\left[\rho_{*}X\right]$，也就是對數氣壓座標的**質量加權垂直微分**（偽密度 $\rho_{*} = P/g \propto e^{-z}$）。

* **【已知 2】 [赤道渦度方程式 (Equatorial vorticity equation)](https://derek1403.github.io/Theory_Playground/_build/html/01_Derivations/Equatorial_Beta_Plane_Dynamics/Equatorial_Vorticity_and_Divergence_Equations.html#a-proof-vorticity-equation)：** 相對渦度在阻尼下的收支：除了輻散造成的渦度伸展 $\beta y\,\delta$，還多出一項 $\beta v$ ─ 氣塊往北走就換到不同的行星渦度值。這個 $\beta v$ 正是後面「赤道上生不出位渦」的源頭。（已於本庫 Equatorial Vorticity and Divergence Equations【證明 (a)】完整證明，此處直接引用。）

  $$\mathcal{D}_t\left[\zeta\right] + \beta y\,\delta + \beta v = 0$$

  * $\zeta$ : 擾動相對渦度 (Perturbation relative vorticity) $[\text{s}^{-1}]$
  * $\delta$ : 擾動水平輻散 (Perturbation horizontal divergence) $[\text{s}^{-1}]$
  * $\mathcal{D}_t$ : 阻尼時間算子 (Damped-tendency operator) $[\text{s}^{-1}]$
  * $v$ : 擾動經向風速 (Perturbation meridional velocity) $[\text{m}\cdot\text{s}^{-1}]$
  * $y$ : 經向座標，以赤道為原點 (Meridional coordinate) $[\text{m}]$
  * $\beta$ : 赤道 $\beta$ 參數 (Equatorial beta parameter) $[\text{m}^{-1}\cdot\text{s}^{-1}]$

* **【已知 3】 [赤道位勢–輻散方程式 (Equatorial geopotential–divergence equation)](https://derek1403.github.io/Theory_Playground/_build/html/01_Derivations/Equatorial_Beta_Plane_Dynamics/Equatorial_Vorticity_and_Divergence_Equations.html#b-proof-geopotentialdivergence-equation)：** 位勢垂直結構在阻尼下的收支：左端是位勢的垂直梯度經 $\mathcal{D}_z$ 加工後隨時間變化，扣掉輻散造成的層結調整；右端由非絕熱加熱驅動。它與【已知 2】合起來即可消去輻散 $\delta$，導出位渦方程式。（已於同一篇【證明 (b)】完整證明，此處直接引用。）

  $$\mathcal{D}_t\left[\mathcal{D}_z\left[\frac{\partial \phi}{\partial z}\right]\right] - R\Gamma\delta = \kappa\,\mathcal{D}_z\left[Q\right]$$

  * $\mathcal{D}_t$ : 阻尼時間算子 (Damped-tendency operator) $[\text{s}^{-1}]$
  * $\mathcal{D}_z$ : 垂直算子 (Vertical operator) $[\text{無單位}]$
  * $\delta$ : 擾動水平輻散 (Perturbation horizontal divergence) $[\text{s}^{-1}]$
  * $\phi$ : 擾動位勢 (Perturbation geopotential) $[\text{m}^{2}\cdot\text{s}^{-2}]$
  * $Q$ : 非絕熱加熱率 (Diabatic heating rate) $[\text{J}\cdot\text{kg}^{-1}\cdot\text{s}^{-1}]$
  * $z$ : 對數氣壓垂直座標 (Log-pressure vertical coordinate) $[\text{無單位}]$
  * $R$ : 乾空氣氣體常數 (Gas constant for dry air) $[\text{J}\cdot\text{kg}^{-1}\cdot\text{K}^{-1}]$
  * $\Gamma$ : 靜力穩定度 (Static stability) $[\text{K}]$，$\Gamma = 23.79 \ \text{K}$
  * $\kappa$ : Poisson 常數 (Poisson constant) $[\text{無單位}]$

* **【已知 4】 [Poisson 常數 (Poisson constant)](https://derek1403.github.io/Theory_Playground/_build/html/01_Derivations/Equatorial_Beta_Plane_Dynamics/Log_Pressure_Linearized_Primitive_Equations.html#assumptions-preliminaries)：** 乾空氣氣體常數與定壓比熱之比。本篇只在【推導 4】用它把源項係數裡的 $R$ 約掉。（已於本庫 Log-Pressure Linearized Primitive Equations【定義 4】定義，此處直接引用。）

  $$\kappa = \frac{R}{c_p}$$

  * $\kappa$ : Poisson 常數 (Poisson constant) $[\text{無單位}]$，$\kappa \approx 0.286$
  * $R$ : 乾空氣氣體常數 (Gas constant for dry air) $[\text{J}\cdot\text{kg}^{-1}\cdot\text{K}^{-1}]$，$R \approx 287 \ \text{J}\cdot\text{kg}^{-1}\cdot\text{K}^{-1}$
  * $c_p$ : 定壓比熱 (Specific heat at constant pressure) $[\text{J}\cdot\text{kg}^{-1}\cdot\text{K}^{-1}]$，$c_p \approx 1004 \ \text{J}\cdot\text{kg}^{-1}\cdot\text{K}^{-1}$

* **【已知 5】 [赤道 $\beta$ 平面的科氏參數 (Coriolis parameter on the equatorial $\beta$-plane)](https://derek1403.github.io/Theory_Playground/_build/html/01_Derivations/Equatorial_Beta_Plane_Dynamics/Log_Pressure_Linearized_Primitive_Equations.html#assumptions-preliminaries)：** 科氏參數線性化成 $\beta y$，其中 $\beta$ 由地球半徑與自轉率決定、是不折不扣的常數；而 $y$ 是 Eulerian 框架下的獨立自變數。（已於本庫 Log-Pressure Linearized Primitive Equations【假設 1】【定義 5】【假設 2】(c-1) 設定，此處直接引用。）

  * (a) 科氏參數：

    $$f = \beta y$$

  * (b) $\beta$ 是常數：

    $$\beta = \frac{2\Omega}{a} = \text{const}$$

  * (c) $x,\ y,\ z,\ t$ 是**互相獨立**的自變數（這正是把全質導數寫成 $\dfrac{\partial}{\partial t} + u\dfrac{\partial}{\partial x} + v\dfrac{\partial}{\partial y} + w\dfrac{\partial}{\partial z}$ 的前提）：

    $$\frac{\partial y}{\partial t} = 0$$

  * $f$ : 科氏參數 (Coriolis parameter) $[\text{s}^{-1}]$
  * $\beta$ : 赤道 $\beta$ 參數 (Equatorial beta parameter) $[\text{m}^{-1}\cdot\text{s}^{-1}]$，$\beta \approx 2.29\times10^{-11} \ \text{m}^{-1}\cdot\text{s}^{-1}$
  * $y$ : 經向座標，以赤道為原點 (Meridional coordinate) $[\text{m}]$
  * $x$ : 緯向座標 (Zonal coordinate) $[\text{m}]$
  * $z$ : 對數氣壓垂直座標 (Log-pressure vertical coordinate) $[\text{無單位}]$
  * $t$ : 時間 (Time) $[\text{s}]$
  * $\Omega$ : 地球自轉角速度 (Earth's angular velocity) $[\text{s}^{-1}]$，$\Omega \approx 7.292\times10^{-5} \ \text{s}^{-1}$
  * $a$ : 地球半徑 (Earth's radius) $[\text{m}]$，$a = 6.37\times10^{6} \ \text{m}$
  * 註：(b)(c) 合起來就是「$\beta y$ 與時間無關」。這**不是假設**，而是座標系與 $\beta$ 平面近似本身帶來的結果，因此列在【已知】而非【假設】；用它推出「$\beta y$ 可穿過 $\mathcal{D}_t$」的那一步見【推導 1】。

* **【已知 6】 [位渦距平的顯式形式 (Explicit form of the PV anomaly)](https://derek1403.github.io/Theory_Playground/_build/html/01_Derivations/Equatorial_Beta_Plane_Dynamics/Linearized_Potential_Vorticity_in_Log_Pressure.html#b-proof-potential-vorticity-anomaly)：** 把 Ertel 位渦繞靜止基本態線性化，取「跟著氣塊走的相對距平」再乘上局地科氏參數 $\beta y$ 換回渦度單位，得到的就是下面這個組合。這是【定義 1】那個名字的**物理依據**。（已於本庫 [線性化位渦](Linearized_Potential_Vorticity_in_Log_Pressure.md)【證明 (b)】完整證明，此處直接引用。）

  $$\beta y\,\frac{\delta PV}{\overline{PV}} = \zeta + \frac{\beta y}{R\Gamma}\,\mathcal{D}_z\left[\frac{\partial \phi}{\partial z}\right]$$

  * $PV$ : Ertel 位渦 (Ertel potential vorticity) $[\text{m}^{2}\cdot\text{s}^{-1}\cdot\text{K}\cdot\text{kg}^{-1}]$
  * $\overline{PV}$ : 基本態的 Ertel 位渦 (Basic-state Ertel potential vorticity) $[\text{m}^{2}\cdot\text{s}^{-1}\cdot\text{K}\cdot\text{kg}^{-1}]$
  * $\delta PV$ : 跟著氣塊走的位渦距平 (Material potential vorticity anomaly) $[\text{m}^{2}\cdot\text{s}^{-1}\cdot\text{K}\cdot\text{kg}^{-1}]$
  * $\zeta$ : 擾動相對渦度 (Perturbation relative vorticity) $[\text{s}^{-1}]$
  * $\mathcal{D}_z$ : 垂直算子 (Vertical operator) $[\text{無單位}]$
  * $\beta$ : 赤道 $\beta$ 參數 (Equatorial beta parameter) $[\text{m}^{-1}\cdot\text{s}^{-1}]$
  * $y$ : 經向座標，以赤道為原點 (Meridional coordinate) $[\text{m}]$
  * $R$ : 乾空氣氣體常數 (Gas constant for dry air) $[\text{J}\cdot\text{kg}^{-1}\cdot\text{K}^{-1}]$
  * $\Gamma$ : 靜力穩定度 (Static stability) $[\text{K}]$，$\Gamma = 23.79 \ \text{K}$
  * $\phi$ : 擾動位勢 (Perturbation geopotential) $[\text{m}^{2}\cdot\text{s}^{-2}]$
  * $z$ : 對數氣壓垂直座標 (Log-pressure vertical coordinate) $[\text{無單位}]$
  * 註：一定要取**材料**距平（跟著氣塊走），不能取固定高度上的 Eulerian 擾動 —— 後者算出來的括號是 $\left(\dfrac{\partial}{\partial z} + \kappa\right)$ 而非 $\mathcal{D}_z$，對不上。理由見該篇〈物理解釋〉第一節。

* **【已知 7】 [位渦源項的顯式形式 (Explicit form of the PV source)](https://derek1403.github.io/Theory_Playground/_build/html/01_Derivations/Equatorial_Beta_Plane_Dynamics/Linearized_Potential_Vorticity_in_Log_Pressure.html#c-proof-potential-vorticity-source)：** 加熱不直接生成渦度，只能透過改變兩張等熵面之間的質量來生成位渦；把這個生成率算出來，就是下面這個組合。這是【定義 2】那個名字的**物理依據**。（已於本庫 [線性化位渦](Linearized_Potential_Vorticity_in_Log_Pressure.md)【證明 (c)】完整證明，此處直接引用。）

  $$\left(\frac{\partial}{\partial t}\left[\beta y\,\frac{\delta PV}{\overline{PV}}\right]\right)_{\text{加熱}} = \frac{\beta y}{c_p\Gamma}\,\mathcal{D}_z\left[Q\right]$$

  * $PV$ : Ertel 位渦 (Ertel potential vorticity) $[\text{m}^{2}\cdot\text{s}^{-1}\cdot\text{K}\cdot\text{kg}^{-1}]$
  * $\overline{PV}$ : 基本態的 Ertel 位渦 (Basic-state Ertel potential vorticity) $[\text{m}^{2}\cdot\text{s}^{-1}\cdot\text{K}\cdot\text{kg}^{-1}]$
  * $\delta PV$ : 跟著氣塊走的位渦距平 (Material potential vorticity anomaly) $[\text{m}^{2}\cdot\text{s}^{-1}\cdot\text{K}\cdot\text{kg}^{-1}]$
  * $\mathcal{D}_z$ : 垂直算子 (Vertical operator) $[\text{無單位}]$
  * $\beta$ : 赤道 $\beta$ 參數 (Equatorial beta parameter) $[\text{m}^{-1}\cdot\text{s}^{-1}]$
  * $y$ : 經向座標，以赤道為原點 (Meridional coordinate) $[\text{m}]$
  * $c_p$ : 定壓比熱 (Specific heat at constant pressure) $[\text{J}\cdot\text{kg}^{-1}\cdot\text{K}^{-1}]$
  * $\Gamma$ : 靜力穩定度 (Static stability) $[\text{K}]$，$\Gamma = 23.79 \ \text{K}$
  * $Q$ : 非絕熱加熱率 (Diabatic heating rate) $[\text{J}\cdot\text{kg}^{-1}\cdot\text{s}^{-1}]$
  * $t$ : 時間 (Time) $[\text{s}]$

* **【假設 1】 高斯型經向加熱剖面 (Gaussian meridional heating profile)：** 指定加熱的經向形狀為中心在赤道、$e$-folding 寬度為 $b_0$ 的高斯

  $$Q(x, y, z) = \tilde{Q}(x, z)\exp\left[-\left(\frac{y}{b_0}\right)^{2}\right]$$

  * $Q$ : 非絕熱加熱率 (Diabatic heating rate) $[\text{J}\cdot\text{kg}^{-1}\cdot\text{s}^{-1}]$
  * $\tilde{Q}(x, z)$ : 加熱的緯向與垂直結構 (Zonal and vertical structure of the heating) $[\text{J}\cdot\text{kg}^{-1}\cdot\text{s}^{-1}]$
  * $b_0$ : 加熱區的經向 $e$-folding 寬度 (Meridional $e$-folding width) $[\text{m}]$，$b_0 = 450 \ \text{km}$
  * $x,\ y$ : 緯向、經向座標 (Zonal and meridional coordinates) $[\text{m}]$
  * $z$ : 對數氣壓垂直座標 (Log-pressure vertical coordinate) $[\text{無單位}]$
  * 註：**這是本篇唯一的假設。** 【證明 (a)(b)(c)】完全用不到它；【證明 (d)】只需要它推出的「南北對稱」（見【推導 2】）；只有【證明 (e)】真正動用到高斯的具體形狀。
  * 註：這正是論文 $(4.1)$ 在 $y_0 = 0$ 時的經向形狀，見 [移動熱源的模態投影](Projection_of_a_Moving_Heat_Source.md)。

* **【定義 1】 位渦距平 (Potential vorticity anomaly)：** 給【已知 6】那個組合一個名字

  $$q \overset{\text{def}}{=} \zeta + \frac{\beta y}{R\Gamma}\,\mathcal{D}_z\left[\frac{\partial \phi}{\partial z}\right]$$

  * $q$ : 位渦距平 (Potential vorticity anomaly) $[\text{s}^{-1}]$
  * $\zeta$ : 擾動相對渦度 (Perturbation relative vorticity) $[\text{s}^{-1}]$
  * $\mathcal{D}_z$ : 垂直算子 (Vertical operator) $[\text{無單位}]$
  * $\beta$ : 赤道 $\beta$ 參數 (Equatorial beta parameter) $[\text{m}^{-1}\cdot\text{s}^{-1}]$
  * $y$ : 經向座標，以赤道為原點 (Meridional coordinate) $[\text{m}]$
  * $R$ : 乾空氣氣體常數 (Gas constant for dry air) $[\text{J}\cdot\text{kg}^{-1}\cdot\text{K}^{-1}]$
  * $\Gamma$ : 靜力穩定度 (Static stability) $[\text{K}]$，$\Gamma = 23.79 \ \text{K}$
  * $\phi$ : 擾動位勢 (Perturbation geopotential) $[\text{m}^{2}\cdot\text{s}^{-2}]$
  * $z$ : 對數氣壓垂直座標 (Log-pressure vertical coordinate) $[\text{無單位}]$
  * 註：這個組合**有兩個彼此獨立的來源**，兩邊指向同一個東西 ——
    * **它是位渦。** 由【已知 6】，它就是 Ertel 位渦線性化後的材料相對距平乘上 $\beta y$。「位渦距平」這個名字是這樣來的，不是硬安上去的。
    * **它會自己冒出來。** 由【證明 (a)】，它也是本篇消去 $\delta$ 之後、$\mathcal{D}_t$ 括號裡自動浮現的組合；就算完全不知道位渦是什麼，純代數操作也會走到這裡。
  * 註：兩條路殊途同歸，正是 $q$ 之所以能滿足一條乾淨守恆型方程式的原因 —— 代數上的「可收攏性」與物理上的「隨氣塊守恆」本來就是同一件事。

* **【定義 2】 PV 源項 (PV source term)：** 給【已知 7】那個生成率一個名字

  $$S \overset{\text{def}}{=} \frac{\beta y}{c_p\Gamma}\,\mathcal{D}_z\left[Q\right]$$

  * $S$ : PV 源項 (PV source term) $[\text{s}^{-2}]$
  * $\mathcal{D}_z$ : 垂直算子 (Vertical operator) $[\text{無單位}]$
  * $\beta$ : 赤道 $\beta$ 參數 (Equatorial beta parameter) $[\text{m}^{-1}\cdot\text{s}^{-1}]$
  * $y$ : 經向座標，以赤道為原點 (Meridional coordinate) $[\text{m}]$
  * $c_p$ : 定壓比熱 (Specific heat at constant pressure) $[\text{J}\cdot\text{kg}^{-1}\cdot\text{K}^{-1}]$
  * $\Gamma$ : 靜力穩定度 (Static stability) $[\text{K}]$，$\Gamma = 23.79 \ \text{K}$
  * $Q$ : 非絕熱加熱率 (Diabatic heating rate) $[\text{J}\cdot\text{kg}^{-1}\cdot\text{s}^{-1}]$
  * 註：與【定義 1】同構 —— 由【已知 7】它是加熱對位渦的**生成率**，由【證明 (b)】它也是消去 $\delta$ 之後自動留在右端的那一團。「源項」二字因此是名副其實的，不是修辭。

* **【推導 1】 $\beta y$ 可以穿過阻尼時間算子 (The factor $\beta y$ commutes with the damped-tendency operator)：** $\beta$ 是常數、$y$ 是獨立於 $t$ 的座標，故乘積律那一項為零

  $$\begin{gather*}
  \mathcal{D}_t\left[\beta y\,X\right] &\overset{\text{已知 1(c)}}{=}& \frac{\partial}{\partial t}\left[\beta y\,X\right] + \alpha\,\beta y\,X \\
  &\overset{\text{已知 5(b)}}{=}& \beta\frac{\partial}{\partial t}\left[y\,X\right] + \alpha\,\beta y\,X \\
  &=& \beta\frac{\partial y}{\partial t}X + \beta y\frac{\partial X}{\partial t} + \alpha\,\beta y\,X \\
  &\overset{\text{已知 5(c)}}{=}& \beta \cdot 0 \cdot X + \beta y\frac{\partial X}{\partial t} + \alpha\,\beta y\,X \\
  &=& \beta y\left[\frac{\partial X}{\partial t} + \alpha X\right] \\
  &\overset{\text{已知 1(c)}}{=}& \beta y\,\mathcal{D}_t\left[X\right]
  \end{gather*}$$

  * $X$ : 任意可微的場 (Arbitrary differentiable field) $[\text{依應用而定}]$
  * $\mathcal{D}_t$ : 阻尼時間算子 (Damped-tendency operator) $[\text{s}^{-1}]$
  * $\beta$ : 赤道 $\beta$ 參數 (Equatorial beta parameter) $[\text{m}^{-1}\cdot\text{s}^{-1}]$
  * $y$ : 經向座標，以赤道為原點 (Meridional coordinate) $[\text{m}]$
  * $t$ : 時間 (Time) $[\text{s}]$
  * $\alpha$ : 常數阻尼率 (Constant damping rate) $[\text{s}^{-1}]$
  * 註：**$\beta y$ 能穿過 $\mathcal{D}_t$，卻不能穿過 $\dfrac{\partial}{\partial y}$。** [渦度方程式](Equatorial_Vorticity_and_Divergence_Equations.md)【推導 2】(b) 裡那個單獨的 $-\beta v$，正是後者辦不到所留下的殘骸。本篇能把 $\zeta$ 與層結項收成單一個 $q$，靠的就是前者辦得到。

* **【推導 2】 高斯剖面必為南北對稱 (A Gaussian profile is necessarily north–south symmetric)：** 高斯的指數裡 $y$ 只以平方出現，換號不變

  $$\begin{gather*}
  Q(x, -y, z) &\overset{\text{假設 1}}{=}& \tilde{Q}(x, z)\exp\left[-\left(\frac{-y}{b_0}\right)^{2}\right] \\
  &=& \tilde{Q}(x, z)\exp\left[-\frac{y^{2}}{b_0^{2}}\right] \\
  &=& \tilde{Q}(x, z)\exp\left[-\left(\frac{y}{b_0}\right)^{2}\right] \\
  &\overset{\text{假設 1}}{=}& Q(x, y, z)
  \end{gather*}$$

  * $Q$ : 非絕熱加熱率 (Diabatic heating rate) $[\text{J}\cdot\text{kg}^{-1}\cdot\text{s}^{-1}]$
  * $\tilde{Q}(x, z)$ : 加熱的緯向與垂直結構 (Zonal and vertical structure of the heating) $[\text{J}\cdot\text{kg}^{-1}\cdot\text{s}^{-1}]$
  * $b_0$ : 加熱區的經向 $e$-folding 寬度 (Meridional $e$-folding width) $[\text{m}]$，$b_0 = 450 \ \text{km}$
  * $x,\ y$ : 緯向、經向座標 (Zonal and meridional coordinates) $[\text{m}]$
  * $z$ : 對數氣壓垂直座標 (Log-pressure vertical coordinate) $[\text{無單位}]$
  * 註：【證明 (d)】用到的其實**只有這個結論**，也就是「$Q$ 對 $y$ 是偶函數」。因此 (d) 對**任何**南北對稱的加熱分布都成立，並不限於高斯；高斯只是本鏈實際採用的具體形狀，順便讓【證明 (e)】也做得下去。

* **【推導 3】 從位勢–輻散方程式解出水平輻散 (Solving the geopotential–divergence equation for the divergence)：** 【已知 3】對 $\delta$ 而言是純代數式，直接移項

  $$\begin{gather*}
  \kappa\,\mathcal{D}_z\Big[Q\Big] &\overset{\text{已知 3}}{=}& \mathcal{D}_t\left[\mathcal{D}_z\left[\frac{\partial \phi}{\partial z}\right]\right] - R\Gamma\delta \\
  R\Gamma\delta &=& \mathcal{D}_t\left[\mathcal{D}_z\left[\frac{\partial \phi}{\partial z}\right]\right] - \kappa\,\mathcal{D}_z\Big[Q\Big] \\
  \delta &=& \frac{1}{R\Gamma}\,\mathcal{D}_t\left[\mathcal{D}_z\left[\frac{\partial \phi}{\partial z}\right]\right] - \frac{\kappa}{R\Gamma}\,\mathcal{D}_z\Big[Q\Big]
  \end{gather*}$$

  * $\kappa$ : Poisson 常數 (Poisson constant) $[\text{無單位}]$
  * $\mathcal{D}_t$ : 阻尼時間算子 (Damped-tendency operator) $[\text{s}^{-1}]$
  * $\mathcal{D}_z$ : 垂直算子 (Vertical operator) $[\text{無單位}]$
  * $\delta$ : 擾動水平輻散 (Perturbation horizontal divergence) $[\text{s}^{-1}]$
  * $Q$ : 非絕熱加熱率 (Diabatic heating rate) $[\text{J}\cdot\text{kg}^{-1}\cdot\text{s}^{-1}]$
  * $\phi$ : 擾動位勢 (Perturbation geopotential) $[\text{m}^{2}\cdot\text{s}^{-2}]$
  * $z$ : 對數氣壓垂直座標 (Log-pressure vertical coordinate) $[\text{無單位}]$
  * $R$ : 乾空氣氣體常數 (Gas constant for dry air) $[\text{J}\cdot\text{kg}^{-1}\cdot\text{K}^{-1}]$
  * $\Gamma$ : 靜力穩定度 (Static stability) $[\text{K}]$，$\Gamma = 23.79 \ \text{K}$

* **【推導 4】 源項的係數化簡 (Simplifying the source coefficient)：** $\kappa$ 的定義讓 $R$ 消掉

  $$\begin{gather*}
  \frac{\kappa}{R\Gamma} &\overset{\text{已知 4}}{=}& \frac{R/c_p}{R\Gamma} \\
  &=& \frac{1}{c_p\Gamma}
  \end{gather*}$$

  * $\kappa$ : Poisson 常數 (Poisson constant) $[\text{無單位}]$
  * $R$ : 乾空氣氣體常數 (Gas constant for dry air) $[\text{J}\cdot\text{kg}^{-1}\cdot\text{K}^{-1}]$
  * $\Gamma$ : 靜力穩定度 (Static stability) $[\text{K}]$，$\Gamma = 23.79 \ \text{K}$
  * $c_p$ : 定壓比熱 (Specific heat at constant pressure) $[\text{J}\cdot\text{kg}^{-1}\cdot\text{K}^{-1}]$

* **【推導 5】 高斯剖面下源項的經向結構 (Meridional structure of the source for a Gaussian profile)：** 把【假設 1】代進【定義 2】，$\mathcal{D}_z$ 只作用在 $z$ 上，故整個經向依賴收成 $y\,e^{-\left(y/b_0\right)^{2}}$

  $$\begin{gather*}
  S &\overset{\text{定義 2}}{=}& \frac{\beta y}{c_p\Gamma}\,\mathcal{D}_z\left[Q\right] \\
  &\overset{\text{假設 1}}{=}& \frac{\beta y}{c_p\Gamma}\,\mathcal{D}_z\left[\tilde{Q}(x, z)\exp\left[-\left(\frac{y}{b_0}\right)^{2}\right]\right] \\
  &=& \frac{\beta}{c_p\Gamma}\,\mathcal{D}_z\left[\tilde{Q}(x, z)\right]\,y\exp\left[-\left(\frac{y}{b_0}\right)^{2}\right]
  \end{gather*}$$

  * $S$ : PV 源項 (PV source term) $[\text{s}^{-2}]$
  * $\mathcal{D}_z$ : 垂直算子 (Vertical operator) $[\text{無單位}]$
  * $\beta$ : 赤道 $\beta$ 參數 (Equatorial beta parameter) $[\text{m}^{-1}\cdot\text{s}^{-1}]$
  * $c_p$ : 定壓比熱 (Specific heat at constant pressure) $[\text{J}\cdot\text{kg}^{-1}\cdot\text{K}^{-1}]$
  * $\Gamma$ : 靜力穩定度 (Static stability) $[\text{K}]$，$\Gamma = 23.79 \ \text{K}$
  * $Q$ : 非絕熱加熱率 (Diabatic heating rate) $[\text{J}\cdot\text{kg}^{-1}\cdot\text{s}^{-1}]$
  * $\tilde{Q}(x, z)$ : 加熱的緯向與垂直結構 (Zonal and vertical structure of the heating) $[\text{J}\cdot\text{kg}^{-1}\cdot\text{s}^{-1}]$
  * $x,\ y$ : 緯向、經向座標 (Zonal and meridional coordinates) $[\text{m}]$
  * $z$ : 對數氣壓垂直座標 (Log-pressure vertical coordinate) $[\text{無單位}]$
  * $b_0$ : 加熱區的經向 $e$-folding 寬度 (Meridional $e$-folding width) $[\text{m}]$，$b_0 = 450 \ \text{km}$

+++

## 證明:

### (a) proof 位渦距平的浮現 (Emergence of the potential vorticity anomaly)

把【推導 3】的 $\delta$ 代進【已知 2】。關鍵在下一步：$\beta y$ 可以穿過 $\mathcal{D}_t$（【推導 1】），因此可以**縮進 $\mathcal{D}_t$ 裡面**，於是 $\zeta$ 與層結項合併成單一個變數。

$$\begin{gather*}
0 &\overset{\text{已知 2}}{=}& \mathcal{D}_t\left[\zeta\right] + \beta y\,\delta + \beta v \\
0 &\overset{\text{推導 3}}{=}& \mathcal{D}_t\left[\zeta\right] + \frac{\beta y}{R\Gamma}\,\mathcal{D}_t\left[\mathcal{D}_z\left[\frac{\partial \phi}{\partial z}\right]\right] - \frac{\kappa\,\beta y}{R\Gamma}\,\mathcal{D}_z\left[Q\right] + \beta v \\
0 &\overset{\text{推導 1}}{=}& \mathcal{D}_t\left[\zeta\right] + \mathcal{D}_t\left[\frac{\beta y}{R\Gamma}\,\mathcal{D}_z\left[\frac{\partial \phi}{\partial z}\right]\right] - \frac{\kappa\,\beta y}{R\Gamma}\,\mathcal{D}_z\left[Q\right] + \beta v \\
0 &=& \mathcal{D}_t\left[\zeta + \frac{\beta y}{R\Gamma}\,\mathcal{D}_z\left[\frac{\partial \phi}{\partial z}\right]\right] - \frac{\kappa\,\beta y}{R\Gamma}\,\mathcal{D}_z\left[Q\right] + \beta v \\
0 &\overset{\text{定義 1}}{=}& \mathcal{D}_t\left[q\right] - \frac{\kappa\,\beta y}{R\Gamma}\,\mathcal{D}_z\left[Q\right] + \beta v
\end{gather*}$$

### (b) proof PV 方程式 (Potential vorticity equation)

把【證明 (a)】的源項係數用【推導 4】化簡，再把 $\mathcal{D}_t$ 展開。

$$\begin{gather*}
0 &\overset{\text{證明 (a)}}{=}& \mathcal{D}_t\left[q\right] - \frac{\kappa\,\beta y}{R\Gamma}\,\mathcal{D}_z\left[Q\right] + \beta v \\
0 &\overset{\text{推導 4}}{=}& \mathcal{D}_t\left[q\right] - \frac{\beta y}{c_p\Gamma}\,\mathcal{D}_z\left[Q\right] + \beta v \\
0 &\overset{\text{定義 2}}{=}& \mathcal{D}_t\left[q\right] - S + \beta v \\
0 &\overset{\text{已知 1(c)}}{=}& \frac{\partial q}{\partial t} + \alpha q - S + \beta v \\
\frac{\partial q}{\partial t} + \beta v &=& -\alpha q + S
\end{gather*}$$

### (c) proof 赤道上的源項為零 (Vanishing of the source at the equator)

$\beta y$ 在赤道上為零，把整個 $\mathcal{D}_z\left[Q\right]$ 乘成零，**與加熱強度完全無關**。

$$\begin{gather*}
\left.S\right|_{y = 0} &\overset{\text{定義 2}}{=}& \left.\frac{\beta y}{c_p\Gamma}\,\mathcal{D}_z\left[Q\right]\right|_{y = 0} \\
&=& \frac{\beta \cdot 0}{c_p\Gamma}\,\left.\mathcal{D}_z\left[Q\right]\right|_{y = 0} \\
&=& 0
\end{gather*}$$

### (d) proof 源項為 $y$ 的奇函數 (Oddness of the source in $y$)

$\beta y$ 是奇函數、加熱是偶函數（【推導 2】），兩者相乘必為奇函數。

$$\begin{gather*}
S(x, -y, z) &\overset{\text{定義 2}}{=}& \frac{\beta\left(-y\right)}{c_p\Gamma}\,\mathcal{D}_z\left[Q(x, -y, z)\right] \\
&\overset{\text{推導 2}}{=}& -\frac{\beta y}{c_p\Gamma}\,\mathcal{D}_z\left[Q(x, y, z)\right] \\
&\overset{\text{定義 2}}{=}& -S(x, y, z)
\end{gather*}$$

### (e) proof 源項極值的位置 (Location of the source extrema)

把【推導 5】的經向結構對 $y$ 微分並令其為零。$\dfrac{\beta}{c_p\Gamma}\mathcal{D}_z\left[\tilde{Q}\right]$ 與 $y$ 無關，可整個約掉。

$$\begin{gather*}
0 &\overset{\text{推導 5}}{=}& \frac{\partial}{\partial y}\left[\frac{\beta}{c_p\Gamma}\,\mathcal{D}_z\left[\tilde{Q}\right]\,y\exp\left[-\left(\frac{y}{b_0}\right)^{2}\right]\right] \\
0 &=& \frac{\partial}{\partial y}\left[y\exp\left[-\left(\frac{y}{b_0}\right)^{2}\right]\right] \\
0 &=& \exp\left[-\left(\frac{y}{b_0}\right)^{2}\right] + y\left(-\frac{2y}{b_0^{2}}\right)\exp\left[-\left(\frac{y}{b_0}\right)^{2}\right] \\
0 &=& \left[1 - \frac{2y^{2}}{b_0^{2}}\right]\exp\left[-\left(\frac{y}{b_0}\right)^{2}\right] \\
1 &=& \frac{2y^{2}}{b_0^{2}} \\
y_{\text{ext}} &=& \pm\frac{b_0}{2^{1/2}} \\
y_{\text{ext}} &\overset{\text{假設 1}}{\approx}& \pm\frac{450 \ \text{km}}{1.414} \\
y_{\text{ext}} &\approx& \pm 318 \ \text{km}
\end{gather*}$$

+++

## 物理解釋

### $q$ 不只是「代數上剛好收得起來的那一團」

【證明 (a)】給人的印象很容易是：$q$ 是為了讓式子收乾淨而硬湊出來的組合，「位渦距平」只是個好聽的名字。**不是這樣。**

由【已知 6】，把 Ertel 位渦 $PV = \dfrac{1}{\rho}\boldsymbol{\eta}_a\cdot\nabla\theta$ 繞靜止基本態線性化，取跟著氣塊走的相對距平再乘上 $\beta y$，得到的**恰好逐項是** $q$：

$$q = \beta y\,\frac{\delta PV}{\overline{PV}} = \underbrace{\zeta}_{\text{渦度變了}} - \underbrace{\beta y\,\mathcal{D}_z\left[\eta\right]}_{\text{等熵層的質量變了}}$$

其中 $\eta = -\dfrac{1}{R\Gamma}\dfrac{\partial\phi}{\partial z}$ 是等熵面的垂直位移。也就是說 $q$ 就是課本上那句「位渦＝絕對渦度 ÷ 層厚」的線性化版本，一項都不多、一項都不少。

由 [線性化位渦](Linearized_Potential_Vorticity_in_Log_Pressure.md)〈物理解釋〉還可以更進一步：絕熱無阻尼時 $q = -\beta Y$，其中 $Y$ 是氣塊離開原本緯度的距離。$q$ 說穿了就是**「這塊空氣離家多遠」的度量**。這個讀法順手解釋了 [Kelvin 波的 $q$ 為零](Physical_Field_Recovery_and_Zero_Kelvin_PV.md)：Kelvin 波的 $v \equiv 0$，沒有任何氣塊離開過它的緯度。

### 這一篇為什麼是全文的物理引擎

【證明 (b)】把 PV 的變化拆成三項：

$$\underbrace{\frac{\partial q}{\partial t}}_{\text{局地變化}} = \underbrace{-\beta v}_{\text{Rossby 項}} \underbrace{- \alpha q}_{\text{阻尼}} + \underbrace{S}_{\text{生成}}$$

其中生成項 $S = \dfrac{\beta y}{c_p\Gamma}\mathcal{D}_z\left[Q\right]$ 前面那個 **$\beta y$ 因子**，是本文與所有「$f$ 平面加熱響應」文獻最關鍵的差別。

在中緯度 $f$ 平面上，源項的係數是常數 $f_0$，加熱在哪裡最強，PV 就在哪裡生成最多。**赤道 $\beta$ 平面完全不是這樣**：

* **【證明 (c)】** —— 赤道正上方（$y = 0$）**生不出任何 PV**。這不是「比較弱」，是**嚴格為零**，而且與加熱多強無關。
* **【證明 (d)】** —— 北半球生出的 PV 與南半球**大小相等、正負相反**。
* **【證明 (e)】** —— 生成的極大值不在加熱最強的地方（$y = 0$），而在**南北兩側 $b_0/2^{1/2} \approx 318 \ \text{km}$**（約 $2.9^{\circ}$ 緯度）處。

三者合起來就是那個著名的圖像：**一個東移的赤道深對流區，會在身後拖出兩條反號的 PV 帶**，北側為正、南側為負。作者的比喻是**大型飛機後方的一對翼尖渦 (wing-tip vortices)** —— 機翼在空氣中留下的，也是這樣一對大小相等、旋向相反的渦旋。

值得對照的是本庫 [垂直結構方程式](../Atmospheric_Dynamics/Vertical_Structure_Equation.md)【證明 (a)】—— 那裡說「動力感受到的不是加熱 $Q$，而是 $-\partial Q/\partial z$」，講的是**垂直**方向的同類機制。本篇的 $\beta y$ 因子扮演的是**經向**方向的相同角色：真正決定響應的，永遠不是加熱本身，而是加熱被某個算子加工之後的東西。

### 為什麼 $\mathcal{D}_z$ 讓上下對流層反號

源項還帶著 $\mathcal{D}_z\left[Q\right]$。在 [垂直結構分離](Separation_into_Horizontal_Structure_System.md) 中會看到，第一垂直內模態的結構函數 $Z(z)$ **在對流層中層變號**。

於是完整的圖像是**四塊**，不是兩條：

| | 北半球（$y > 0$） | 南半球（$y < 0$） |
|---|---|---|
| **低層** | 正 PV（氣旋式） | 負 PV（氣旋式） |
| **高層** | 負 PV | 正 PV |

低層的那一對，就是論文所稱的「雙 ITCZ」的動力來源 —— 低層氣旋式渦度 → 邊界層輻合 → Ekman pumping → 雲量與降雨。

用【已知 7】的等熵面圖像看，上下反號的物理很直白：在加熱極大值**下方**，加熱隨高度遞增，把等熵層**壓薄** → PV 增加；在極大值**上方**恰好相反，層**變厚** → PV 減少。$\mathcal{D}_z$ 管垂直、$\beta y$ 管南北，兩個機制各管一個方向，乘起來就是這張四格表。

### 對後續三個端點的意義

* **[PV 尾流](PV_Wake_of_a_Moving_Heat_Source.md)（端點②）** —— 把【證明 (b)】的 Rossby 項 $\beta v$ 拿掉，剩下「強迫 ＋ 阻尼」就能解析求解，直接讀出控制尾流的三個參數。$q \propto -\beta y\,e^{-\left(y-y_0\right)^{2}/b_0^{2}}$ 這個形狀正是【推導 5】的產物。
* **[可逆性原理](Equatorial_PV_Invertibility_Principle.md)（端點③）** —— 【定義 1】的 $q$ 就是被反演的對象；反演能不能成功，完全看流場的資訊有沒有被裝進這個組合裡。
* **[Kelvin 波 PV 為零](Physical_Field_Recovery_and_Zero_Kelvin_PV.md)** —— 答案是「有些沒有」。Kelvin 波的 $q$ **恰好為零**，所以端點③救不回對流東側的流場。那不是近似不夠好，而是**資訊在 $q$ 這個變數裡根本不存在**。
