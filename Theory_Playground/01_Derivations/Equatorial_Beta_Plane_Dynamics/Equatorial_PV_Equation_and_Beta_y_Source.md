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

* 註：(a)(b) 就是 [Schubert & Masarik (2006)](../../06_References/Tropical_wave_dynamics/Schubert2006-Potential_vorticity_aspects_of_the_MJO/Potential_vorticity_aspects_of_the_MJO.ipynb) 的 $(2.7)$ 與 $(2.6)$。
* 註：**(c)(d)(e) 是全文的物理引擎。** 它們合起來說：一個東移的赤道熱源，會在身後拖出**兩條反號的 PV 帶** —— 作者把這個形態比喻為大型飛機後方的一對**翼尖渦 (wing-tip vortices)**。後續 [PV 尾流](PV_Wake_of_a_Moving_Heat_Source.md)、[可逆性原理](Equatorial_PV_Invertibility_Principle.md) 兩個端點都建立在這三條之上。

+++

## 假設與已知 (Assumptions & Preliminaries)

* **【已知 1】 [赤道渦度方程式 (Equatorial vorticity equation)](https://derek1403.github.io/Theory_Playground/_build/html/01_Derivations/Equatorial_Beta_Plane_Dynamics/Equatorial_Vorticity_and_Divergence_Equations.html#a-proof-vorticity-equation)：** 相對渦度在阻尼下的收支：除了輻散造成的渦度伸展 $\beta y\,\delta$，還多出一項 $\beta v$ ─ 氣塊往北走就換到不同的行星渦度值。這個 $\beta v$ 正是後面「赤道上生不出位渦」的源頭。（已於本庫 Equatorial Vorticity and Divergence Equations【證明 (a)】完整證明，此處直接引用。）

  $$\mathcal{D}_t\left[\zeta\right] + \beta y\,\delta + \beta v = 0$$

  * $\zeta$ : 擾動相對渦度 (Perturbation relative vorticity) $[\text{s}^{-1}]$，$\zeta = \dfrac{\partial v}{\partial x} - \dfrac{\partial u}{\partial y}$
  * $\delta$ : 擾動水平輻散 (Perturbation horizontal divergence) $[\text{s}^{-1}]$，$\delta = \dfrac{\partial u}{\partial x} + \dfrac{\partial v}{\partial y}$
  * $\mathcal{D}_t$ : 阻尼時間算子 (Damped-tendency operator) $[\text{s}^{-1}]$，$\mathcal{D}_t = \dfrac{\partial}{\partial t} + \alpha$
  * $v$ : 擾動經向風速 (Perturbation meridional velocity) $[\text{m}\cdot\text{s}^{-1}]$
  * $y$ : 經向座標，以赤道為原點 (Meridional coordinate) $[\text{m}]$
  * $\beta$ : 赤道 $\beta$ 參數 (Equatorial beta parameter) $[\text{m}^{-1}\cdot\text{s}^{-1}]$
  * $\alpha$ : 常數阻尼率 (Constant damping rate) $[\text{s}^{-1}]$

* **【已知 2】 [赤道位勢–輻散方程式 (Equatorial geopotential–divergence equation)](https://derek1403.github.io/Theory_Playground/_build/html/01_Derivations/Equatorial_Beta_Plane_Dynamics/Equatorial_Vorticity_and_Divergence_Equations.html#b-proof-geopotentialdivergence-equation)：** 位勢垂直結構在阻尼下的收支：左端是位勢的垂直梯度經 $\mathcal{D}_z$ 加工後隨時間變化，扣掉輻散造成的層結調整；右端由非絕熱加熱驅動。它與【已知 1】合起來即可消去輻散 $\delta$，導出位渦方程式。（已於同一篇【證明 (b)】完整證明，此處直接引用。）

  $$\mathcal{D}_t\left[\mathcal{D}_z\left[\frac{\partial \phi}{\partial z}\right]\right] - R\Gamma\delta = \kappa\,\mathcal{D}_z\left[Q\right]$$

  * $\mathcal{D}_z$ : 垂直算子 (Vertical operator) $[\text{無單位}]$，$\mathcal{D}_z = \dfrac{\partial}{\partial z} - 1$
  * $\phi$ : 擾動位勢 (Perturbation geopotential) $[\text{m}^{2}\cdot\text{s}^{-2}]$
  * $Q$ : 非絕熱加熱率 (Diabatic heating rate) $[\text{J}\cdot\text{kg}^{-1}\cdot\text{s}^{-1}]$
  * $z$ : 對數氣壓垂直座標 (Log-pressure vertical coordinate) $[\text{無單位}]$
  * $R$ : 乾空氣氣體常數 (Gas constant for dry air) $[\text{J}\cdot\text{kg}^{-1}\cdot\text{K}^{-1}]$
  * $\Gamma$ : 靜力穩定度 (Static stability) $[\text{K}]$，$\Gamma = 23.79 \ \text{K}$
  * $c_p$ : 定壓比熱 (Specific heat at constant pressure) $[\text{J}\cdot\text{kg}^{-1}\cdot\text{K}^{-1}]$
  * $\kappa$ : Poisson 常數 (Poisson constant) $[\text{無單位}]$，$\kappa = R/c_p$
  * $\delta$ : 擾動水平輻散 (Perturbation horizontal divergence) $[\text{s}^{-1}]$，$\delta = \dfrac{\partial u}{\partial x} + \dfrac{\partial v}{\partial y}$
  * $\mathcal{D}_t$ : 阻尼時間算子 (Damped-tendency operator) $[\text{s}^{-1}]$，$\mathcal{D}_t = \dfrac{\partial}{\partial t} + \alpha$

* **【假設 1】 $\beta y$ 與時間無關 (The factor $\beta y$ is time-independent)：** $\beta$ 為常數、$y$ 為獨立座標，故 $\beta y$ 可自由穿過 $\mathcal{D}_t$

  $$\frac{\partial}{\partial t}\left[\beta y\right] = 0$$

  * $t$ : 時間 (Time) $[\text{s}]$
  * $\beta$ : 赤道 $\beta$ 參數 (Equatorial beta parameter) $[\text{m}^{-1}\cdot\text{s}^{-1}]$
  * $y$ : 經向座標，以赤道為原點 (Meridional coordinate) $[\text{m}]$

* **【假設 2】 加熱的南北對稱性 (North–south symmetry of the heating)：** 【證明 (d)】只討論經向對稱的加熱分布

  $$Q(x, -y, z) = Q(x, y, z)$$

  * $Q$ : 非絕熱加熱率 (Diabatic heating rate) $[\text{J}\cdot\text{kg}^{-1}\cdot\text{s}^{-1}]$
  * $x,\ y$ : 緯向、經向座標 (Zonal and meridional coordinates) $[\text{m}]$
  * $y$ : 經向座標，以赤道為原點 (Meridional coordinate) $[\text{m}]$
  * $z$ : 對數氣壓垂直座標 (Log-pressure vertical coordinate) $[\text{無單位}]$

* **【假設 3】 高斯型經向加熱剖面 (Gaussian meridional heating profile)：** 【證明 (e)】另外指定加熱的經向形狀為中心在赤道、$e$-folding 寬度為 $b_0$ 的高斯

  $$Q(x, y, z) = \tilde{Q}(x, z)\exp\left[-\left(\frac{y}{b_0}\right)^{2}\right]$$

  * $b_0$ : 加熱區的經向 $e$-folding 寬度 (Meridional $e$-folding width) $[\text{m}]$，$b_0 = 450 \ \text{km}$
  * $\tilde{Q}(x, z)$ : 加熱的緯向與垂直結構 (Zonal and vertical structure of the heating) $[\text{J}\cdot\text{kg}^{-1}\cdot\text{s}^{-1}]$
  * $Q$ : 非絕熱加熱率 (Diabatic heating rate) $[\text{J}\cdot\text{kg}^{-1}\cdot\text{s}^{-1}]$
  * $y$ : 經向座標，以赤道為原點 (Meridional coordinate) $[\text{m}]$
  * 註：本卡片是【假設 2】的一個具體實現（高斯是偶函數）。這正是論文 $(4.1)$ 在 $y_0 = 0$ 時的經向形狀，見 [移動熱源的模態投影](Projection_of_a_Moving_Heat_Source.md)。

* **【定義 1】 位渦距平 (Potential vorticity anomaly)：** 相對渦度加上「$\beta y$ 加權的層結項」

  $$q \overset{\text{def}}{=} \zeta + \frac{\beta y}{R\Gamma}\,\mathcal{D}_z\left[\frac{\partial \phi}{\partial z}\right]$$

  * $q$ : 位渦距平 (Potential vorticity anomaly) $[\text{s}^{-1}]$
  * $\zeta$ : 擾動相對渦度 (Perturbation relative vorticity) $[\text{s}^{-1}]$，$\zeta = \dfrac{\partial v}{\partial x} - \dfrac{\partial u}{\partial y}$
  * $\beta$ : 赤道 $\beta$ 參數 (Equatorial beta parameter) $[\text{m}^{-1}\cdot\text{s}^{-1}]$
  * $y$ : 經向座標，以赤道為原點 (Meridional coordinate) $[\text{m}]$
  * $R$ : 乾空氣氣體常數 (Gas constant for dry air) $[\text{J}\cdot\text{kg}^{-1}\cdot\text{K}^{-1}]$
  * $\Gamma$ : 靜力穩定度 (Static stability) $[\text{K}]$，$\Gamma = 23.79 \ \text{K}$
  * $\mathcal{D}_t$ : 阻尼時間算子 (Damped-tendency operator) $[\text{s}^{-1}]$，$\mathcal{D}_t = \dfrac{\partial}{\partial t} + \alpha$
  * $\phi$ : 擾動位勢 (Perturbation geopotential) $[\text{m}^{2}\cdot\text{s}^{-2}]$
  * $z$ : 對數氣壓垂直座標 (Log-pressure vertical coordinate) $[\text{無單位}]$
  * $\mathcal{D}_z$ : 垂直算子 (Vertical operator) $[\text{無單位}]$，$\mathcal{D}_z = \dfrac{\partial}{\partial z} - 1$
  * 註：這個組合**不是憑空指定的**，而是【證明 (a)】消去 $\delta$ 之後，$\mathcal{D}_t$ 括號裡**自動浮現**的東西；本卡片只是替它取個名字。

* **【定義 2】 PV 源項 (PV source term)：** 加熱透過 $\beta y$ 加權後真正注入 PV 的部分

  $$S \overset{\text{def}}{=} \frac{\beta y}{c_p\Gamma}\,\mathcal{D}_z\left[Q\right]$$

  * $S$ : PV 源項 (PV source term) $[\text{s}^{-2}]$
  * $\beta$ : 赤道 $\beta$ 參數 (Equatorial beta parameter) $[\text{m}^{-1}\cdot\text{s}^{-1}]$
  * $y$ : 經向座標，以赤道為原點 (Meridional coordinate) $[\text{m}]$
  * $c_p$ : 定壓比熱 (Specific heat at constant pressure) $[\text{J}\cdot\text{kg}^{-1}\cdot\text{K}^{-1}]$
  * $\Gamma$ : 靜力穩定度 (Static stability) $[\text{K}]$，$\Gamma = 23.79 \ \text{K}$
  * $\mathcal{D}_t$ : 阻尼時間算子 (Damped-tendency operator) $[\text{s}^{-1}]$，$\mathcal{D}_t = \dfrac{\partial}{\partial t} + \alpha$
  * $Q$ : 非絕熱加熱率 (Diabatic heating rate) $[\text{J}\cdot\text{kg}^{-1}\cdot\text{s}^{-1}]$
  * $\mathcal{D}_z$ : 垂直算子 (Vertical operator) $[\text{無單位}]$，$\mathcal{D}_z = \dfrac{\partial}{\partial z} - 1$

* **【推導 1】 從位勢–輻散方程式解出水平輻散 (Solving the geopotential–divergence equation for the divergence)：** 【已知 2】對 $\delta$ 而言是純代數式，直接移項

  $$\begin{gather*}
  \kappa\,\mathcal{D}_z\left[Q\right] &\overset{\text{已知 2}}{=}& \mathcal{D}_t\left[\mathcal{D}_z\left[\frac{\partial \phi}{\partial z}\right]\right] - R\Gamma\delta \\
  R\Gamma\delta &=& \mathcal{D}_t\left[\mathcal{D}_z\left[\frac{\partial \phi}{\partial z}\right]\right] - \kappa\,\mathcal{D}_z\left[Q\right] \\
  \delta &=& \frac{1}{R\Gamma}\,\mathcal{D}_t\left[\mathcal{D}_z\left[\frac{\partial \phi}{\partial z}\right]\right] - \frac{\kappa}{R\Gamma}\,\mathcal{D}_z\left[Q\right]
  \end{gather*}$$

  * $\kappa$ : Poisson 常數 (Poisson constant) $[\text{無單位}]$，$\kappa = R/c_p$
  * $\mathcal{D}_t$ : 阻尼時間算子 (Damped-tendency operator) $[\text{s}^{-1}]$，$\mathcal{D}_t = \dfrac{\partial}{\partial t} + \alpha$
  * $Q$ : 非絕熱加熱率 (Diabatic heating rate) $[\text{J}\cdot\text{kg}^{-1}\cdot\text{s}^{-1}]$
  * $\phi$ : 擾動位勢 (Perturbation geopotential) $[\text{m}^{2}\cdot\text{s}^{-2}]$
  * $z$ : 對數氣壓垂直座標 (Log-pressure vertical coordinate) $[\text{無單位}]$
  * $R$ : 乾空氣氣體常數 (Gas constant for dry air) $[\text{J}\cdot\text{kg}^{-1}\cdot\text{K}^{-1}]$
  * $\Gamma$ : 靜力穩定度 (Static stability) $[\text{K}]$，$\Gamma = 23.79 \ \text{K}$
  * $\delta$ : 擾動水平輻散 (Perturbation horizontal divergence) $[\text{s}^{-1}]$，$\delta = \dfrac{\partial u}{\partial x} + \dfrac{\partial v}{\partial y}$
  * $\mathcal{D}_z$ : 垂直算子 (Vertical operator) $[\text{無單位}]$，$\mathcal{D}_z = \dfrac{\partial}{\partial z} - 1$

* **【推導 2】 源項的係數化簡 (Simplifying the source coefficient)：** $\kappa$ 的定義讓 $R$ 消掉

  $$\begin{gather*}
  \frac{\kappa}{R\Gamma} &\overset{\text{已知 2}}{=}& \frac{R/c_p}{R\Gamma} \\
  &=& \frac{1}{c_p\Gamma}
  \end{gather*}$$

  * $\kappa$ : Poisson 常數 (Poisson constant) $[\text{無單位}]$，$\kappa = R/c_p$
  * $R$ : 乾空氣氣體常數 (Gas constant for dry air) $[\text{J}\cdot\text{kg}^{-1}\cdot\text{K}^{-1}]$
  * $\Gamma$ : 靜力穩定度 (Static stability) $[\text{K}]$，$\Gamma = 23.79 \ \text{K}$
  * $c_p$ : 定壓比熱 (Specific heat at constant pressure) $[\text{J}\cdot\text{kg}^{-1}\cdot\text{K}^{-1}]$

* **【推導 3】 高斯剖面下源項的經向結構 (Meridional structure of the source for a Gaussian profile)：** 把【假設 3】代進【定義 2】，$\mathcal{D}_z$ 只作用在 $z$ 上，故整個經向依賴收成 $y\,e^{-\left(y/b_0\right)^{2}}$

  $$\begin{gather*}
  S &\overset{\text{定義 2}}{=}& \frac{\beta y}{c_p\Gamma}\,\mathcal{D}_z\left[Q\right] \\
  &\overset{\text{假設 3}}{=}& \frac{\beta y}{c_p\Gamma}\,\mathcal{D}_z\left[\tilde{Q}(x, z)\exp\left[-\left(\frac{y}{b_0}\right)^{2}\right]\right] \\
  &=& \frac{\beta}{c_p\Gamma}\,\mathcal{D}_z\left[\tilde{Q}(x, z)\right]\,y\exp\left[-\left(\frac{y}{b_0}\right)^{2}\right]
  \end{gather*}$$

  * $S$ : PV 源項 (PV source term) $[\text{s}^{-2}]$
  * $\beta$ : 赤道 $\beta$ 參數 (Equatorial beta parameter) $[\text{m}^{-1}\cdot\text{s}^{-1}]$
  * $y$ : 經向座標，以赤道為原點 (Meridional coordinate) $[\text{m}]$
  * $c_p$ : 定壓比熱 (Specific heat at constant pressure) $[\text{J}\cdot\text{kg}^{-1}\cdot\text{K}^{-1}]$
  * $\Gamma$ : 靜力穩定度 (Static stability) $[\text{K}]$，$\Gamma = 23.79 \ \text{K}$
  * $\mathcal{D}_t$ : 阻尼時間算子 (Damped-tendency operator) $[\text{s}^{-1}]$，$\mathcal{D}_t = \dfrac{\partial}{\partial t} + \alpha$
  * $Q$ : 非絕熱加熱率 (Diabatic heating rate) $[\text{J}\cdot\text{kg}^{-1}\cdot\text{s}^{-1}]$
  * $\tilde{Q}(x, z)$ : 加熱的緯向與垂直結構 (Zonal and vertical structure of the heating) $[\text{J}\cdot\text{kg}^{-1}\cdot\text{s}^{-1}]$
  * $x,\ y$ : 緯向、經向座標 (Zonal and meridional coordinates) $[\text{m}]$
  * $z$ : 對數氣壓垂直座標 (Log-pressure vertical coordinate) $[\text{無單位}]$
  * $b_0$ : 加熱區的經向 $e$-folding 寬度 (Meridional $e$-folding width) $[\text{m}]$，$b_0 = 450 \ \text{km}$
  * $\mathcal{D}_z$ : 垂直算子 (Vertical operator) $[\text{無單位}]$，$\mathcal{D}_z = \dfrac{\partial}{\partial z} - 1$

+++

## 證明:

### (a) proof 位渦距平的浮現 (Emergence of the potential vorticity anomaly)

把【推導 1】的 $\delta$ 代進【已知 1】。關鍵在下一步：$\beta y$ 與時間無關（【假設 1】），因此可以**縮進 $\mathcal{D}_t$ 裡面**，於是 $\zeta$ 與層結項合併成單一個變數。

$$\begin{gather*}
0 &\overset{\text{已知 1}}{=}& \mathcal{D}_t\left[\zeta\right] + \beta y\,\delta + \beta v \\
0 &\overset{\text{推導 1}}{=}& \mathcal{D}_t\left[\zeta\right] + \frac{\beta y}{R\Gamma}\,\mathcal{D}_t\left[\mathcal{D}_z\left[\frac{\partial \phi}{\partial z}\right]\right] - \frac{\kappa\,\beta y}{R\Gamma}\,\mathcal{D}_z\left[Q\right] + \beta v \\
0 &\overset{\text{假設 1}}{=}& \mathcal{D}_t\left[\zeta\right] + \mathcal{D}_t\left[\frac{\beta y}{R\Gamma}\,\mathcal{D}_z\left[\frac{\partial \phi}{\partial z}\right]\right] - \frac{\kappa\,\beta y}{R\Gamma}\,\mathcal{D}_z\left[Q\right] + \beta v \\
0 &=& \mathcal{D}_t\left[\zeta + \frac{\beta y}{R\Gamma}\,\mathcal{D}_z\left[\frac{\partial \phi}{\partial z}\right]\right] - \frac{\kappa\,\beta y}{R\Gamma}\,\mathcal{D}_z\left[Q\right] + \beta v \\
0 &\overset{\text{定義 1}}{=}& \mathcal{D}_t\left[q\right] - \frac{\kappa\,\beta y}{R\Gamma}\,\mathcal{D}_z\left[Q\right] + \beta v
\end{gather*}$$

### (b) proof PV 方程式 (Potential vorticity equation)

把【證明 (a)】的源項係數用【推導 2】化簡，再把 $\mathcal{D}_t$ 展開。

$$\begin{gather*}
0 &\overset{\text{證明 (a)}}{=}& \mathcal{D}_t\left[q\right] - \frac{\kappa\,\beta y}{R\Gamma}\,\mathcal{D}_z\left[Q\right] + \beta v \\
0 &\overset{\text{推導 2}}{=}& \mathcal{D}_t\left[q\right] - \frac{\beta y}{c_p\Gamma}\,\mathcal{D}_z\left[Q\right] + \beta v \\
0 &\overset{\text{定義 2}}{=}& \mathcal{D}_t\left[q\right] - S + \beta v \\
0 &\overset{\text{已知 1}}{=}& \frac{\partial q}{\partial t} + \alpha q - S + \beta v \\
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

$\beta y$ 是奇函數、加熱是偶函數（【假設 2】），兩者相乘必為奇函數。

$$\begin{gather*}
S(x, -y, z) &\overset{\text{定義 2}}{=}& \frac{\beta\left(-y\right)}{c_p\Gamma}\,\mathcal{D}_z\left[Q(x, -y, z)\right] \\
&\overset{\text{假設 2}}{=}& -\frac{\beta y}{c_p\Gamma}\,\mathcal{D}_z\left[Q(x, y, z)\right] \\
&\overset{\text{定義 2}}{=}& -S(x, y, z)
\end{gather*}$$

### (e) proof 源項極值的位置 (Location of the source extrema)

把【推導 3】的經向結構對 $y$ 微分並令其為零。$\dfrac{\beta}{c_p\Gamma}\mathcal{D}_z\left[\tilde{Q}\right]$ 與 $y$ 無關，可整個約掉。

$$\begin{gather*}
0 &\overset{\text{推導 3}}{=}& \frac{\partial}{\partial y}\left[\frac{\beta}{c_p\Gamma}\,\mathcal{D}_z\left[\tilde{Q}\right]\,y\exp\left[-\left(\frac{y}{b_0}\right)^{2}\right]\right] \\
0 &=& \frac{\partial}{\partial y}\left[y\exp\left[-\left(\frac{y}{b_0}\right)^{2}\right]\right] \\
0 &=& \exp\left[-\left(\frac{y}{b_0}\right)^{2}\right] + y\left(-\frac{2y}{b_0^{2}}\right)\exp\left[-\left(\frac{y}{b_0}\right)^{2}\right] \\
0 &=& \left[1 - \frac{2y^{2}}{b_0^{2}}\right]\exp\left[-\left(\frac{y}{b_0}\right)^{2}\right] \\
1 &=& \frac{2y^{2}}{b_0^{2}} \\
y_{\text{ext}} &=& \pm\frac{b_0}{2^{1/2}} \\
y_{\text{ext}} &\overset{\text{假設 3}}{\approx}& \pm\frac{450 \ \text{km}}{1.414} \\
y_{\text{ext}} &\approx& \pm 318 \ \text{km}
\end{gather*}$$

+++

## 物理解釋

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

### 對後續三個端點的意義

* **[PV 尾流](PV_Wake_of_a_Moving_Heat_Source.md)（端點②）** —— 把【證明 (b)】的 Rossby 項 $\beta v$ 拿掉，剩下「強迫 ＋ 阻尼」就能解析求解，直接讀出控制尾流的三個參數。$q \propto -\beta y\,e^{-\left(y-y_0\right)^{2}/b_0^{2}}$ 這個形狀正是【推導 3】的產物。
* **[可逆性原理](Equatorial_PV_Invertibility_Principle.md)（端點③）** —— 【定義 1】的 $q$ 就是被反演的對象；反演能不能成功，完全看流場的資訊有沒有被裝進這個組合裡。
* **[Kelvin 波 PV 為零](Physical_Field_Recovery_and_Zero_Kelvin_PV.md)** —— 答案是「有些沒有」。Kelvin 波的 $q$ **恰好為零**，所以端點③救不回對流東側的流場。那不是近似不夠好，而是**資訊在 $q$ 這個變數裡根本不存在**。
