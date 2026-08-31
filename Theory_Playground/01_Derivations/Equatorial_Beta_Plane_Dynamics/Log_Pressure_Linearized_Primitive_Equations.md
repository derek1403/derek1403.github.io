# Log-Pressure Linearized Primitive Equations (對數氣壓座標下的線性化原始方程組)

+++

## 證明目標:

在赤道 $\beta$ 平面上，把層結、可壓縮、準靜力大氣的原始方程組，寫成以
$z = \ln\left(p_0/P\right)$ 為垂直座標的**線性化**形式。五條方程式收束為一組：

* (a) 緯向動量方程式：

$$\frac{\partial u}{\partial t} - \beta y\,v + \frac{\partial \phi}{\partial x} = -\alpha u$$

* (b) 經向動量方程式：

$$\frac{\partial v}{\partial t} + \beta y\,u + \frac{\partial \phi}{\partial y} = -\alpha v$$

* (c) 靜力方程式：

$$\frac{\partial \phi}{\partial z} = RT$$

* (d) 連續方程式（注意多出來的 $-w$ 項）：

$$\frac{\partial u}{\partial x} + \frac{\partial v}{\partial y} + \frac{\partial w}{\partial z} - w = 0$$

* (e) 熱力學方程式：

$$\frac{\partial T}{\partial t} + \Gamma w = -\alpha T + \frac{Q}{c_p}$$

* $u$ : 擾動緯向風速 (Perturbation zonal velocity) $[\text{m}\cdot\text{s}^{-1}]$
* $v$ : 擾動經向風速 (Perturbation meridional velocity) $[\text{m}\cdot\text{s}^{-1}]$
* $w$ : 擾動對數氣壓垂直速度 (Perturbation log-pressure vertical velocity) $[\text{s}^{-1}]$
* $\phi$ : 擾動位勢 (Perturbation geopotential) $[\text{m}^{2}\cdot\text{s}^{-2}]$
* $T$ : 擾動溫度 (Perturbation temperature) $[\text{K}]$
* $Q$ : 單位質量的外加對流加熱率 (Convective heating rate per unit mass) $[\text{J}\cdot\text{kg}^{-1}\cdot\text{s}^{-1}]$
* $x$ : 緯向座標 (Zonal coordinate) $[\text{m}]$
* $y$ : 經向座標，以赤道為原點 (Meridional coordinate) $[\text{m}]$
* $z$ : 對數氣壓垂直座標 (Log-pressure vertical coordinate) $[\text{無單位}]$
* $t$ : 時間 (Time) $[\text{s}]$
* $\alpha$ : 常數阻尼率 (Constant damping rate) $[\text{s}^{-1}]$，$\alpha = \left(4 \ \text{days}\right)^{-1} \approx 2.89\times10^{-6} \ \text{s}^{-1}$
* $\beta$ : 赤道 $\beta$ 參數 (Equatorial beta parameter) $[\text{m}^{-1}\cdot\text{s}^{-1}]$，$\beta \approx 2.29\times10^{-11} \ \text{m}^{-1}\cdot\text{s}^{-1}$
* $\Gamma$ : 靜力穩定度 (Static stability) $[\text{K}]$，$\Gamma \approx 23.79 \ \text{K}$
* $R$ : 乾空氣氣體常數 (Gas constant for dry air) $[\text{J}\cdot\text{kg}^{-1}\cdot\text{K}^{-1}]$，$R \approx 287 \ \text{J}\cdot\text{kg}^{-1}\cdot\text{K}^{-1}$
* $c_p$ : 定壓比熱 (Specific heat at constant pressure) $[\text{J}\cdot\text{kg}^{-1}\cdot\text{K}^{-1}]$，$c_p \approx 1004 \ \text{J}\cdot\text{kg}^{-1}\cdot\text{K}^{-1}$
* $p_0$ : 參考氣壓 (Reference pressure) $[\text{Pa}]$，$p_0 = 1010 \ \text{mb}$
* $P$ : 氣壓 (Pressure) $[\text{Pa}]$
* 註（符號提醒）：本段的符號有四處容易誤讀 ——
  * $u,\ v,\ w$ 寫成光禿的形式**就是擾動量**：由【假設 2】(a)(b-1)，$\bar{u} = \bar{v} = \bar{w} = 0$，故 $u \equiv u'$、$v \equiv v'$、$w \equiv w'$。這是恆等式，不是撇號省略。
  * $T$ 在本段指**擾動**溫度 $T'$；但【已知 1/3/4】【推導 4/5/7】中的 $T$ 是**全場**溫度。這是一次明確的符號重新定義，交接點在【證明 (c)(e)】末，見【假設 2】末的〈記號慣例〉註。
  * $\phi$（擾動位勢）、$\Phi$（全場位勢）、$\varphi$（緯度）是**三個不同的量**，僅字形相近；本段出現的是 $\phi$。
  * $Q$ 是**外加的強迫**而非因變數，故不冠「擾動」二字（見【假設 2】末的使用規則）。
* 註：這五條就是 [Schubert & Masarik (2006)](../../06_References/Tropical_wave_dynamics/Schubert2006-Potential_vorticity_aspects_of_the_MJO/Potential_vorticity_aspects_of_the_MJO.ipynb) 的 $(2.1)$，是整條 MJO 推導鏈的起點。
* 註：球座標原始方程式、連續方程式、狀態方程式、靜力平衡**都已在別處證過**，本檔一律引用（見【已知】卡片）。真正新做的只有三件事：**對數氣壓座標變換**、**繞靜止基本態線性化**、**赤道 $\beta$ 平面近似**。
* 註：$z$ 是**無因次**的對數氣壓座標，因此 $w = Dz/Dt$ 的單位是 $\left[\text{s}^{-1}\right]$ 而非 $\left[\text{m}\cdot\text{s}^{-1}\right]$。

+++

## 假設與已知 (Assumptions & Preliminaries)

* **【已知 1】 [原始方程式 (Primitive Equations)](https://derek1403.github.io/PC-NTU/Advanced-Atmospheric-Dynamics/_build/html/lecture/week2/week2.html#primitive-equations)：** 球座標下、經傳統／淺層近似與靜力平衡簡化後的方程組。（已於 Advanced Atmospheric Dynamics 課程 week2 完整證明，此處直接引用；更早的球座標基底變換見本庫 [球座標變換的動量方程](../Coordinate_System/spherical_coordinate_transformation_momentum_equation.md)。）

  * (a) 緯向動量方程式：

    $$\frac{Du}{Dt} - fv - \frac{uv\tan\varphi}{a} = -\frac{1}{\rho a\cos\varphi}\frac{\partial P}{\partial \lambda} + F_\lambda$$

  * (b) 經向動量方程式：

    $$\frac{Dv}{Dt} + fu + \frac{u^{2}\tan\varphi}{a} = -\frac{1}{\rho a}\frac{\partial P}{\partial \varphi} + F_\varphi$$

  * (c) 靜力平衡：

    $$\frac{\partial P}{\partial z_{\text{g}}} = -\rho g$$

  * $u$ : 全場緯向風速 (Total zonal velocity) $[\text{m}\cdot\text{s}^{-1}]$
  * $v$ : 全場經向風速 (Total meridional velocity) $[\text{m}\cdot\text{s}^{-1}]$
  * $P$ : 氣壓 (Pressure) $[\text{Pa}]$
  * $\rho$ : 密度 (Density) $[\text{kg}\cdot\text{m}^{-3}]$
  * $z_{\text{g}}$ : 幾何高度 (Geometric height) $[\text{m}]$
  * $g$ : 重力加速度 (Gravitational acceleration) $[\text{m}\cdot\text{s}^{-2}]$，$g \approx 9.81 \ \text{m}\cdot\text{s}^{-2}$
  * $f$ : 科氏參數 (Coriolis parameter) $[\text{s}^{-1}]$，$f = 2\Omega\sin\varphi$
  * $\Omega$ : 地球自轉角速度 (Earth's angular velocity) $[\text{s}^{-1}]$，$\Omega \approx 7.292\times10^{-5} \ \text{s}^{-1}$
  * $a$ : 地球半徑 (Earth's radius) $[\text{m}]$，$a \approx 6.37\times10^{6} \ \text{m}$
  * $\lambda$ : 經度 (Longitude) $[\text{rad}]$
  * $\varphi$ : 緯度 (Latitude) $[\text{rad}]$
  * $F_\lambda,\ F_\varphi$ : 緯向、經向的摩擦力 (Frictional forces) $[\text{m}\cdot\text{s}^{-2}]$
  * $t$ : 時間 (Time) $[\text{s}]$

* **【已知 2】 [質量守恆（隨體積元形式）(Mass conservation, material-element form)](https://derek1403.github.io/PC-NTU/Advanced-Atmospheric-Dynamics/_build/html/lecture/week1/week1.html#continuity-equation)：** 隨流體移動的質量元其質量不變，此即連續方程式的 Lagrangian 敘述。（已於 week1 由雷諾傳輸定理完整證明，此處直接引用。）

  $$\frac{D\left(\delta M\right)}{Dt} = 0$$

  * $\delta M$ : 隨流體移動的質量元 (Material mass element) $[\text{kg}]$
  * $t$ : 時間 (Time) $[\text{s}]$
  * $\frac{D}{Dt}$ : 全質導數 (Material derivative) $[\text{s}^{-1}]$

* **【已知 3】 [狀態方程式 (Equation of State)](https://derek1403.github.io/PC-NTU/Advanced-Atmospheric-Dynamics/_build/html/lecture/week1/week1.html#equation-of-state)：** 乾空氣的理想氣體定律：氣壓由密度與溫度的乘積決定，比例係數是乾空氣氣體常數 $R$。它讓熱力學量與動力學量得以互換，是後面把第一定律的作功項換成 $w$ 的關鍵。（已於 week1 完整證明，此處直接引用。）

  $$P = \rho R T$$

  * $T$ : 全場溫度 (Total temperature) $[\text{K}]$
  * $R$ : 乾空氣氣體常數 (Gas constant for dry air) $[\text{J}\cdot\text{kg}^{-1}\cdot\text{K}^{-1}]$，$R \approx 287 \ \text{J}\cdot\text{kg}^{-1}\cdot\text{K}^{-1}$
  * $P$ : 氣壓 (Pressure) $[\text{Pa}]$
  * $\rho$ : 密度 (Density) $[\text{kg}\cdot\text{m}^{-3}]$

* **【已知 4】 [熱力學第一定律（大氣形式）(First law of thermodynamics)](https://glossary.ametsoc.org/wiki/First_law_of_thermodynamics)：** 對單位質量的空氣塊，內能變化＋對外作功＝**總**非絕熱加熱。（標準結果，此處直接引用。）

  $$c_p\frac{DT}{Dt} - \frac{1}{\rho}\frac{DP}{Dt} = Q_{\text{total}}$$

  * $c_p$ : 定壓比熱 (Specific heat at constant pressure) $[\text{J}\cdot\text{kg}^{-1}\cdot\text{K}^{-1}]$，$c_p \approx 1004 \ \text{J}\cdot\text{kg}^{-1}\cdot\text{K}^{-1}$
  * $Q_{\text{total}}$ : 單位質量的總非絕熱加熱率 (Total diabatic heating rate per unit mass) $[\text{J}\cdot\text{kg}^{-1}\cdot\text{s}^{-1}]$
  * $T$ : 全場溫度 (Total temperature) $[\text{K}]$
  * $t$ : 時間 (Time) $[\text{s}]$
  * $\rho$ : 密度 (Density) $[\text{kg}\cdot\text{m}^{-3}]$
  * $P$ : 氣壓 (Pressure) $[\text{Pa}]$

* **【定義 1】 對數氣壓垂直座標 (Log-pressure vertical coordinate)：** 用氣壓的對數當垂直座標，$p_0$ 為固定的「地面」氣壓

  $$z \overset{\text{def}}{=} \ln\left(\frac{p_0}{P}\right)$$

  * $z$ : 對數氣壓垂直座標 (Log-pressure vertical coordinate) $[\text{無單位}]$
  * $p_0$ : 參考氣壓 (Reference pressure) $[\text{Pa}]$，$p_0 = 1010 \ \text{mb}$
  * $P$ : 氣壓 (Pressure) $[\text{Pa}]$
  * 註：等 $z$ 面與等 $P$ 面**是同一組面**，因此水平微分算子 $\partial/\partial x$、$\partial/\partial y$ 在兩個座標系中完全相同。

* **【定義 2】 對數氣壓垂直速度 (Log-pressure vertical velocity)：** 在【定義 1】的座標下，「垂直速度」是 $z$ 的全質導數

  $$w \overset{\text{def}}{=} \frac{Dz}{Dt}$$

  * $w$ : 全場對數氣壓垂直速度 (Total log-pressure vertical velocity) $[\text{s}^{-1}]$
  * $z$ : 對數氣壓垂直座標 (Log-pressure vertical coordinate) $[\text{無單位}]$
  * $t$ : 時間 (Time) $[\text{s}]$
  * 註：$z$ 無因次，故 $w$ 的單位是 $\left[\text{s}^{-1}\right]$，不是速度。

* **【定義 3】 氣壓垂直速度與位勢 (Pressure velocity and geopotential)：** 壓力座標系中的兩個標準量

  * (a) 氣壓垂直速度：

    $$\omega \overset{\text{def}}{=} \frac{DP}{Dt}$$

  * (b) 位勢：

    $$\Phi \overset{\text{def}}{=} g\,z_{\text{g}}$$

  * $\omega$ : 氣壓垂直速度 (Pressure velocity) $[\text{Pa}\cdot\text{s}^{-1}]$
  * $\Phi$ : 全場位勢 (Total geopotential) $[\text{m}^{2}\cdot\text{s}^{-2}]$
  * $P$ : 氣壓 (Pressure) $[\text{Pa}]$
  * $t$ : 時間 (Time) $[\text{s}]$
  * $g$ : 重力加速度 (Gravitational acceleration) $[\text{m}\cdot\text{s}^{-2}]$，$g \approx 9.81 \ \text{m}\cdot\text{s}^{-2}$
  * $z_{\text{g}}$ : 幾何高度 (Geometric height) $[\text{m}]$

* **【定義 4】 Poisson 常數 (Poisson constant)：** 氣體常數與定壓比熱之比

  $$\kappa \overset{\text{def}}{=} \frac{R}{c_p}$$

  * $\kappa$ : Poisson 常數 (Poisson constant) $[\text{無單位}]$，$\kappa \approx 0.286$
  * $R$ : 乾空氣氣體常數 (Gas constant for dry air) $[\text{J}\cdot\text{kg}^{-1}\cdot\text{K}^{-1}]$，$R \approx 287 \ \text{J}\cdot\text{kg}^{-1}\cdot\text{K}^{-1}$
  * $c_p$ : 定壓比熱 (Specific heat at constant pressure) $[\text{J}\cdot\text{kg}^{-1}\cdot\text{K}^{-1}]$，$c_p \approx 1004 \ \text{J}\cdot\text{kg}^{-1}\cdot\text{K}^{-1}$

* **【定義 5】 赤道 $\beta$ 參數 (Equatorial beta parameter)：** 科氏參數在赤道的北向梯度

  $$\beta \overset{\text{def}}{=} \frac{2\Omega}{a}$$

  * $\beta$ : 赤道 $\beta$ 參數 (Equatorial beta parameter) $[\text{m}^{-1}\cdot\text{s}^{-1}]$，$\beta \approx 2.29\times10^{-11} \ \text{m}^{-1}\cdot\text{s}^{-1}$
  * $\Omega$ : 地球自轉角速度 (Earth's angular velocity) $[\text{s}^{-1}]$，$\Omega \approx 7.292\times10^{-5} \ \text{s}^{-1}$
  * $a$ : 地球半徑 (Earth's radius) $[\text{m}]$，$a \approx 6.37\times10^{6} \ \text{m}$

* **【定義 6】 靜力穩定度 (Static stability)：** 由基本態溫度剖面算出的層結度量

  $$\Gamma \overset{\text{def}}{=} \frac{d\bar{T}}{dz} + \kappa\bar{T}$$

  * $\Gamma$ : 靜力穩定度 (Static stability) $[\text{K}]$
  * $\bar{T}(z)$ : 基本態溫度剖面 (Basic-state temperature profile) $[\text{K}]$
  * $z$ : 對數氣壓垂直座標 (Log-pressure vertical coordinate) $[\text{無單位}]$
  * $\kappa$ : Poisson 常數 (Poisson constant) $[\text{無單位}]$，$\kappa \approx 0.286$

* **【假設 1】 赤道 $\beta$ 平面 (Equatorial $\beta$-plane)：** 把球面在赤道附近攤平成直角座標，並把科氏參數線性化

  * (a) 局地直角座標，$y$ 為離赤道的距離：

    $$x \overset{\text{def}}{=} a\lambda, \qquad y \overset{\text{def}}{=} a\varphi$$

  * (b) 赤道附近 $\left|\varphi\right| \ll 1$，故 $\sin\varphi \approx \varphi$，科氏參數線性化為：

    $$\begin{gather*}
    f &\overset{\text{已知 1}}{=}& 2\Omega\sin\varphi \\
    &\approx& 2\Omega\varphi \\
    &\overset{\text{假設 1(a)}}{=}& \frac{2\Omega}{a}y \\
    &\overset{\text{定義 5}}{=}& \beta y
    \end{gather*}$$

  * (c) 承 (a)，並由 $\left|\varphi\right| \ll 1$ 得 $\cos\varphi \approx 1$，水平微分的度規因子退化為直角座標：

    $$\begin{gather*}
    a\cos\varphi\,\partial\lambda &\approx& a\,\partial\lambda \\
    &\overset{\text{假設 1(a)}}{=}& \partial x \\
    \end{gather*}$$

  * (d) 水平微分的度規因子退化為直角座標：
  
    $$\begin{gather*}
    y &\overset{\text{假設 1(a)}}{=}& a\varphi \\
    \partial y &=& a \partial \varphi \\
    \end{gather*}$$


  * $x$ : 緯向座標 (Zonal coordinate) $[\text{m}]$
  * $y$ : 經向座標，以赤道為原點 (Meridional coordinate) $[\text{m}]$
  * $a$ : 地球半徑 (Earth's radius) $[\text{m}]$，$a \approx 6.37\times10^{6} \ \text{m}$
  * $\lambda$ : 經度 (Longitude) $[\text{rad}]$
  * $\varphi$ : 緯度 (Latitude) $[\text{rad}]$
  * $f$ : 科氏參數 (Coriolis parameter) $[\text{s}^{-1}]$，$f = 2\Omega\sin\varphi$
  * $\Omega$ : 地球自轉角速度 (Earth's angular velocity) $[\text{s}^{-1}]$，$\Omega \approx 7.292\times10^{-5} \ \text{s}^{-1}$
  * $\beta$ : 赤道 $\beta$ 參數 (Equatorial beta parameter) $[\text{m}^{-1}\cdot\text{s}^{-1}]$，$\beta \approx 2.29\times10^{-11} \ \text{m}^{-1}\cdot\text{s}^{-1}$
  * 註：【已知 1】(a)(b) 中的度規（曲率）項 $\dfrac{uv\tan\varphi}{a}$、$\dfrac{u^{2}\tan\varphi}{a}$ **不是**靠 $\tan\varphi$ 小而捨棄的 —— 它們是擾動量的**二次項**，由【假設 2】(c-2) 消掉。

* **【假設 2】 繞靜止基本態的小振幅線性化 (Linearization about a resting basic state)：** 基本態靜止、只隨高度變化，擾動量小到二次項可捨

  * (a) 基本態靜止：

    $$\bar{u} = \bar{v} = \bar{w} = 0$$

  * (b) 全場一律拆成「只隨高度變化的基本態」與「擾動」：

    $$u = \bar{u} + u', \qquad v = \bar{v} + v', \qquad w = \bar{w} + w'$$

    $$T = \bar{T}(z) + T', \qquad \Phi = \bar{\Phi}(z) + \phi$$

  * (b-1) 由 (a)，三個速度分量的基本態為零，故**速度本身就是擾動量** —— 這是恆等式，不是記號省略：

    $$u \overset{\text{假設 2(a)}}{=} u', \qquad v \overset{\text{假設 2(a)}}{=} v', \qquad w \overset{\text{假設 2(a)}}{=} w'$$

  * (c) 小振幅：任意兩個擾動量的乘積一律捨棄：

    $$\left(\text{擾動}\right)\times\left(\text{擾動}\right) \approx 0$$

    

  * (c-1) 由 (a)(b)(c)，作用在任一擾動量 $X'$ 上的全質導數退化成純時間導數：

    $$\begin{gather*}
    \frac{DX'}{Dt} &=& \frac{\partial X'}{\partial t} + u\frac{\partial X'}{\partial x} + v\frac{\partial X'}{\partial y} + w\frac{\partial X'}{\partial z} \\
    &\overset{\text{假設 2(b)}}{=}& \frac{\partial X'}{\partial t} + \left(\bar{u} + u'\right)\frac{\partial X'}{\partial x} + \left(\bar{v} + v'\right)\frac{\partial X'}{\partial y} + \left(\bar{w} + w'\right)\frac{\partial X'}{\partial z} \\
    &\overset{\text{假設 2(a)}}{=}& \frac{\partial X'}{\partial t} + u'\frac{\partial X'}{\partial x} + v'\frac{\partial X'}{\partial y} + w'\frac{\partial X'}{\partial z} \\
    &\overset{\text{假設 2(c)}}{\approx}& \frac{\partial X'}{\partial t}
    \end{gather*}$$

    

  * (c-2) 【已知 1】(a) 的度規項是兩個**全場**風速的乘積，展開後只剩擾動的二次項：

    $$\begin{gather*}
    \frac{uv\tan\varphi}{a} &\overset{\text{假設 2(b)}}{=}& \frac{\left(\bar{u} + u'\right)\left(\bar{v} + v'\right)\tan\varphi}{a} \\
    &\overset{\text{假設 2(a)}}{=}& \frac{u'v'\tan\varphi}{a} \\
    &\overset{\text{假設 2(c)}}{\approx}& 0
    \end{gather*}$$

  * (c-3) 同理，【已知 1】(b) 的度規項亦可捨棄：

    $$\begin{gather*}
    \frac{u^{2}\tan\varphi}{a} &\overset{\text{假設 2(b)}}{=}& \frac{\left(\bar{u} + u'\right)^{2}\tan\varphi}{a} \\
    &\overset{\text{假設 2(a)}}{=}& \frac{\left(u'\right)^{2}\tan\varphi}{a} \\
    &\overset{\text{假設 2(c)}}{\approx}& 0
    \end{gather*}$$

  * (d) 但若被作用的量本身含**基本態**，其垂直平流項是「擾動 $\times$ 基本態」的**一次項**，**不可**捨棄：

    $$\begin{gather*}
    \frac{D\bar{T}(z)}{Dt} &=& \frac{\partial \bar{T}(z)}{\partial t} + u\frac{\partial \bar{T}(z)}{\partial x} + v\frac{\partial \bar{T}(z)}{\partial y} + w\frac{\partial \bar{T}(z)}{\partial z} \\
    &=& 0 + u \cdot 0  + v \cdot 0 + w\frac{d\bar{T}}{dz} \\
    &=& w\frac{d\bar{T}}{dz} \\
    &\overset{\text{假設 2(b-1)}}{=}& w'\frac{d\bar{T}}{dz}
    \end{gather*}$$



  * $u',\ v'$ : 擾動緯向、經向風速 (Perturbation zonal and meridional velocities) $[\text{m}\cdot\text{s}^{-1}]$
  * $w'$ : 擾動對數氣壓垂直速度 (Perturbation log-pressure vertical velocity) $[\text{s}^{-1}]$
  * $T'$ : 擾動溫度 (Perturbation temperature) $[\text{K}]$
  * $\phi$ : 擾動位勢 (Perturbation geopotential) $[\text{m}^{2}\cdot\text{s}^{-2}]$
  * $X'$ : 任一擾動量的代稱 (Any perturbation quantity) $[\text{依應用而定}]$
  * $\bar{T}(z)$ : 基本態溫度剖面 (Basic-state temperature profile) $[\text{K}]$
  * $\bar{\Phi}(z)$ : 基本態位勢 (Basic-state geopotential) $[\text{m}^{2}\cdot\text{s}^{-2}]$
  * $\bar{u}$ : 基本態緯向風速 (Basic state zonal velocity) $[\text{m}\cdot\text{s}^{-1}]$
  * $\bar{v}$ : 基本態經向風速 (Basic state meridional velocity) $[\text{m}\cdot\text{s}^{-1}]$
  * $\bar{w}$ : 基本態對數氣壓垂直速度 (Basic state log-pressure vertical velocity) $[\text{s}^{-1}]$
  * $z$ : 對數氣壓垂直座標 (Log-pressure vertical coordinate) $[\text{無單位}]$
  * $\Phi$ : 全場位勢 (Total geopotential) $[\text{m}^{2}\cdot\text{s}^{-2}]$
  * $T$ : 全場溫度 (Total temperature) $[\text{K}]$
  * $t$ : 時間 (Time) $[\text{s}]$
  * $u$ : 全場緯向風速 (Total zonal velocity) $[\text{m}\cdot\text{s}^{-1}]$
  * $x$ : 緯向座標 (Zonal coordinate) $[\text{m}]$
  * $v$ : 全場經向風速 (Total meridional velocity) $[\text{m}\cdot\text{s}^{-1}]$
  * $y$ : 經向座標，以赤道為原點 (Meridional coordinate) $[\text{m}]$
  * $w$ : 全場對數氣壓垂直速度 (Total log-pressure vertical velocity) $[\text{s}^{-1}]$
  * $\varphi$ : 緯度 (Latitude) $[\text{rad}]$
  * $a$ : 地球半徑 (Earth's radius) $[\text{m}]$，$a \approx 6.37\times10^{6} \ \text{m}$
  * $\frac{D}{Dt}$ : 全質導數 (Material derivative) $[\text{s}^{-1}]$
  * **註（記號慣例）：** 風速與溫度的撇號處理**不是同一回事**，必須分開講：
    * **$u,\ v,\ w$**：由 (a)(b-1)，$u \equiv u'$、$v \equiv v'$、$w \equiv w'$ —— 這是**恆等式**。寫 $u$ 或寫 $u'$ 指的是同一個量，因此【證明】中一律寫光禿的 $u, v, w$，並無資訊損失。
    * **$T$**：$\bar{T}(z) \neq 0$，故 $T$ 與 $T'$ 是**兩個不同的量**。本檔【已知 1/3/4】【推導 4/5/7】中的 $T$ 一律是**全場溫度**；要到【證明 (c)(e)】線性化完成、$\bar{T}$ 已被【定義 6】的 $\Gamma$ 吸收之後，符號 $T$ 才**改指**擾動溫度。這是一次明確的**符號重新定義**，不是撇號省略；交接點見【證明 (c)(e)】末的註。
    * **為何不乾脆一路寫 $T'$？** 因為本推導鏈的撇號 $'$ 專門表示 $d/dz$（垂直結構函數 $Z'$，見 [垂直結構方程式](Vertical_Structure_Equation_in_Log_Pressure.md)）。若讓 $T'$ 兼表「擾動」，[垂直結構分離](Separation_into_Horizontal_Structure_System.md) $(3.4)$ 會寫成 $T' = \hat{T}'Z'(z)$ —— 同一行出現兩種意義的撇號。[Schubert & Masarik (2006)](../../06_References/Tropical_wave_dynamics/Schubert2006-Potential_vorticity_aspects_of_the_MJO/Potential_vorticity_aspects_of_the_MJO.ipynb) $(2.1)$ 印刷體亦用光禿的 $T$。
    * **「擾動」前綴的使用規則**（本推導鏈通用）：只加在線性化系統的**因變數**（$u, v, w, \phi, T, \zeta, \delta, q$ 及其 $\hat{\ }$／轉換版本）上；$Q$ 是**外加的強迫**、不是因變數，故一律不冠「擾動」。

* **【假設 3】 準靜力 (Quasi-static)：** 垂直加速度遠小於重力，垂直動量方程式退化為【已知 1】(c) 的靜力平衡；系統的垂直方程式因此由診斷關係取代預報關係

  $$\frac{Dw_{\text{g}}}{Dt} \ll g$$

  * $w_{\text{g}}$ : 幾何垂直速度 (Geometric vertical velocity) $[\text{m}\cdot\text{s}^{-1}]$
  * $t$ : 時間 (Time) $[\text{s}]$
  * $g$ : 重力加速度 (Gravitational acceleration) $[\text{m}\cdot\text{s}^{-2}]$，$g \approx 9.81 \ \text{m}\cdot\text{s}^{-2}$

* **【假設 4】 Rayleigh 摩擦與 Newtonian 冷卻 (Rayleigh friction and Newtonian cooling)：** 動量與溫度的耗散都取成「與擾動量成正比」，且**共用同一個常數阻尼率** $\alpha$

  * (a) 動量耗散：

    $$\left(F_\lambda,\ F_\varphi\right) = \left(-\alpha u,\ -\alpha v\right)$$

  * (b) 溫度耗散：

    $$\left(\frac{\partial T'}{\partial t}\right)_{\text{cooling}} = -\alpha T'$$

  * (b-1) Newtonian 冷卻本身就是一種非絕熱加熱，故【已知 4】的 $Q_{\text{total}}$ 可拆成「外加的對流強迫」與「向基本態的輻射鬆弛」兩塊；此式與 (b) 等價，只是改用加熱率而非傾向表述：

    $$Q_{\text{total}} = Q - c_p\,\alpha T'$$

  * $\alpha$ : 常數阻尼率 (Constant damping rate) $[\text{s}^{-1}]$，$\alpha = \left(4 \ \text{days}\right)^{-1} \approx 2.89\times10^{-6} \ \text{s}^{-1}$
  * $F_\lambda,\ F_\varphi$ : 緯向、經向的摩擦力 (Frictional forces) $[\text{m}\cdot\text{s}^{-2}]$
  * $\lambda$ : 經度 (Longitude) $[\text{rad}]$
  * $\varphi$ : 緯度 (Latitude) $[\text{rad}]$
  * $u$ : 擾動緯向風速 (Perturbation zonal velocity) $[\text{m}\cdot\text{s}^{-1}]$
  * $v$ : 擾動經向風速 (Perturbation meridional velocity) $[\text{m}\cdot\text{s}^{-1}]$
  * $T'$ : 擾動溫度 (Perturbation temperature) $[\text{K}]$
  * $Q_{\text{total}}$ : 單位質量的總非絕熱加熱率 (Total diabatic heating rate per unit mass) $[\text{J}\cdot\text{kg}^{-1}\cdot\text{s}^{-1}]$
  * $Q$ : 單位質量的外加對流加熱率 (Convective heating rate per unit mass) $[\text{J}\cdot\text{kg}^{-1}\cdot\text{s}^{-1}]$
  * $c_p$ : 定壓比熱 (Specific heat at constant pressure) $[\text{J}\cdot\text{kg}^{-1}\cdot\text{K}^{-1}]$，$c_p \approx 1004 \ \text{J}\cdot\text{kg}^{-1}\cdot\text{K}^{-1}$
  * $t$ : 時間 (Time) $[\text{s}]$
  * 註：(a) 寫光禿的 $u, v$、(b) 卻寫 $T'$，**並非不一致** —— 由【假設 2】(b-1) 有 $u \equiv u'$，但 $\bar{T} \neq 0$ 故 $T \neq T'$；溫度必須帶撇號，否則會把基本態剖面 $\bar{T}$ 也一起阻尼掉。
  * 註：兩者取同一個 $\alpha$ 純粹是為了讓後面 [受迫解](Forced_Response_of_Equatorial_Modes.md) 的分母能收成單一個 $\alpha + i(\cdots)$；放寬成不同阻尼率也做得下去，只是式子變醜。

* **【假設 5】 靜力穩定度為常數 (Constant static stability)：** 基本態的靜力穩定度取熱帶對流層平均值

  $$\Gamma = \text{const} $$

  * $\Gamma$ : 靜力穩定度 (Static stability) $[\text{K}]$ ， $\Gamma \approx 23.79  \text{K}$
  * 註：**本篇的五條【證明】並不需要這一條** —— $\Gamma$ 在【證明 (e)】只是被【定義 6】收攏起來的一個符號。列在此處是因為它是模式設定的一部分，且從 [渦度與位勢–輻散方程式](Equatorial_Vorticity_and_Divergence_Equations.md) 起就必須用到（$\Gamma$ 要能穿過垂直算子 $\partial/\partial z - 1$，才做得成消去）。

* **【假設 6】 基本態靜力平衡 (Basic-state hydrostatic balance)：** 基本態自身即為系統的一個解（靜止、無強迫、只隨高度變化），故【推導 4】的靜力關係對它單獨成立

  $$\frac{d\bar{\Phi}}{dz} = R\bar{T}$$

  * $\bar{\Phi}(z)$ : 基本態位勢 (Basic-state geopotential) $[\text{m}^{2}\cdot\text{s}^{-2}]$
  * $\bar{T}(z)$ : 基本態溫度剖面 (Basic-state temperature profile) $[\text{K}]$
  * $R$ : 乾空氣氣體常數 (Gas constant for dry air) $[\text{J}\cdot\text{kg}^{-1}\cdot\text{K}^{-1}]$，$R \approx 287 \ \text{J}\cdot\text{kg}^{-1}\cdot\text{K}^{-1}$
  * $z$ : 對數氣壓垂直座標 (Log-pressure vertical coordinate) $[\text{無單位}]$
  * 註：這一條**推導不出來** —— 【推導 4】只給一條 $\dfrac{d\bar{\Phi}}{dz} + \dfrac{\partial \phi}{\partial z} = R\bar{T} + RT'$，一條方程式拆不出兩條。要拆開，必須另外要求基本態自身是平衡態。本庫在 [擾動場的流體靜力平衡](../Fluid_Dynamics_in_Cylindrical_Coordinates/Hydrostatic_Balance_for_Perturbations.md) 的【假設 2】亦作同樣處理。


* **【推導 1】 座標變換算子 (Coordinate transformation operators)：** 【定義 1】兩側取指數再微分，得到 $z$ 與 $P$ 之間的三條換算

  * (a) 氣壓的顯式形式：

    $$\begin{gather*}
    z &\overset{\text{定義 1}}{=}& \ln\left(\frac{p_0}{P}\right) \\
    e^{z} &=& \frac{p_0}{P} \\
    P &=& p_0\,e^{-z}
    \end{gather*}$$

  * (b) 氣壓對 $z$ 的導數：

    $$\begin{gather*}
    \frac{dP}{dz} &\overset{\text{推導 1(a)}}{=}& \frac{d}{dz}\left[p_0\,e^{-z}\right] \\
    &=& -p_0\,e^{-z} \\
    &\overset{\text{推導 1(a)}}{=}& -P
    \end{gather*}$$

  * (c) 垂直微分算子的互換：

    $$\begin{gather*}
    \frac{\partial}{\partial z} &=& \frac{dP}{dz}\frac{\partial}{\partial P} \\
    &\overset{\text{推導 1(b)}}{=}& -P\frac{\partial}{\partial P}
    \end{gather*}$$

  * $z$ : 對數氣壓垂直座標 (Log-pressure vertical coordinate) $[\text{無單位}]$
  * $p_0$ : 參考氣壓 (Reference pressure) $[\text{Pa}]$，$p_0 = 1010 \ \text{mb}$
  * $P$ : 氣壓 (Pressure) $[\text{Pa}]$

* **【推導 2】 兩種垂直速度的關係 (Relation between the two vertical velocities)：** $w$ 與 $\omega$ 只差一個 $-P$

  $$\begin{gather*}
  w &\overset{\text{定義 2}}{=}& \frac{Dz}{Dt} \\
  w &=& \frac{\partial z}{\partial t} + u\frac{\partial z}{\partial x} + v\frac{\partial z}{\partial y} + \frac{DP}{Dt}\frac{\partial z}{\partial P} \\
  w &\overset{\text{定義 1}}{=}& 0 + u \cdot 0 + v \cdot 0 + \frac{DP}{Dt}\frac{dz}{dP} \\
  w &\overset{\text{推導 1(b)}}{=}& -\frac{1}{P}\frac{DP}{Dt} \\
  w &\overset{\text{定義 3(a)}}{=}& -\frac{\omega}{P} \\
  \omega &=& -P\,w \\
  \omega &\overset{\text{推導 1(a)}}{=}& -p_0\,e^{-z}\,w
  \end{gather*}$$

  * $w$ : 全場對數氣壓垂直速度 (Total log-pressure vertical velocity) $[\text{s}^{-1}]$
  * $z$ : 對數氣壓垂直座標 (Log-pressure vertical coordinate) $[\text{無單位}]$
  * $t$ : 時間 (Time) $[\text{s}]$
  * $P$ : 氣壓 (Pressure) $[\text{Pa}]$
  * $\omega$ : 氣壓垂直速度 (Pressure velocity) $[\text{Pa}\cdot\text{s}^{-1}]$

* **【推導 3】 壓力座標的水平壓力梯度力 (Horizontal pressure gradient force in pressure coordinates)：** 沿等壓面移動時 $P$ 不變，這條約束把 $-\frac{1}{\rho}\nabla P$ 換成 $-\nabla\Phi$

  * (a) 沿等壓面的全微分為零，解出等壓面的傾斜度：

    $$\begin{gather*}
    dP &=& \left.\frac{\partial P}{\partial x}\right|_{z_{\text{g}}}dx + \left.\frac{\partial P}{\partial y}\right|_{z_{\text{g}}}dy + \frac{\partial P}{\partial z_{\text{g}}}dz_{\text{g}} \\
    0 &\overset{\text{沿等壓面}}{=}& \left.\frac{\partial P}{\partial x}\right|_{z_{\text{g}}}dx + \left.\frac{\partial P}{\partial y}\right|_{z_{\text{g}}}dy + \frac{\partial P}{\partial z_{\text{g}}}dz_{\text{g}} \\
    0 &\overset{\text{固定 } y}{=}& \left.\frac{\partial P}{\partial x}\right|_{z_{\text{g}}}dx + \left.\frac{\partial P}{\partial y}\right|_{z_{\text{g}}} \cdot 0 + \frac{\partial P}{\partial z_{\text{g}}}dz_{\text{g}} \\
    0 &=& \left.\frac{\partial P}{\partial x}\right|_{z_{\text{g}}}dx + \frac{\partial P}{\partial z_{\text{g}}}dz_{\text{g}} \\
    - \frac{\partial P}{\partial z_{\text{g}}}dz_{\text{g}} &=& \left.\frac{\partial P}{\partial x}\right|_{z_{\text{g}}}dx  \\
    \left.\frac{\partial z_{\text{g}}}{\partial x}\right|_{P} &=& -\frac{\left.\partial P/\partial x\right|_{z_{\text{g}}}}{\partial P/\partial z_{\text{g}}} \\
    \left.\frac{\partial z_{\text{g}}}{\partial x}\right|_{P} &\overset{\text{已知 1(c)}}{=}& \frac{1}{\rho g}\left.\frac{\partial P}{\partial x}\right|_{z_{\text{g}}}
    \end{gather*}$$

  * (b) 代入【定義 3】(b)，兩種寫法互換：

    $$\begin{gather*}
    \left.\frac{\partial \Phi}{\partial x}\right|_{P} &\overset{\text{定義 3(b)}}{=}& g\left.\frac{\partial z_{\text{g}}}{\partial x}\right|_{P} \\
    &\overset{\text{推導 3(a)}}{=}& \frac{1}{\rho}\left.\frac{\partial P}{\partial x}\right|_{z_{\text{g}}} \\
    \end{gather*}$$

  * $P$ : 氣壓 (Pressure) $[\text{Pa}]$
  * $x$ : 緯向座標 (Zonal coordinate) $[\text{m}]$
  * $y$ : 經向座標，以赤道為原點 (Meridional coordinate) $[\text{m}]$
  * $z_{\text{g}}$ : 幾何高度 (Geometric height) $[\text{m}]$
  * $\rho$ : 密度 (Density) $[\text{kg}\cdot\text{m}^{-3}]$
  * $g$ : 重力加速度 (Gravitational acceleration) $[\text{m}\cdot\text{s}^{-2}]$，$g \approx 9.81 \ \text{m}\cdot\text{s}^{-2}$
  * $\Phi$ : 全場位勢 (Total geopotential) $[\text{m}^{2}\cdot\text{s}^{-2}]$
  * 註：$y$ 方向的推導與 (a)(b) 逐字相同，只需把 $x$ 換成 $y$。由【定義 1】的註，等 $P$ 面即等 $z$ 面，故 $\left.\nabla\Phi\right|_{P} = \left.\nabla\Phi\right|_{z}$。

* **【推導 4】 對數氣壓座標的靜力關係 (Hydrostatic relation in log-pressure coordinates)：** 從幾何高度的靜力平衡，兩次換座標

  $$\begin{gather*}
  \frac{\partial \Phi}{\partial P} &\overset{\text{定義 3(b)}}{=}& g\frac{\partial z_{\text{g}}}{\partial P} \\
  \frac{\partial \Phi}{\partial P} &\overset{\text{已知 1(c),假設 3}}{=}& g\cdot\frac{1}{-\rho g} \\
  \frac{\partial \Phi}{\partial P} &=& -\frac{1}{\rho} \\
  \frac{\partial \Phi}{\partial P} &\overset{\text{已知 3}}{=}& -\frac{RT}{P} \\
  -P\frac{\partial \Phi}{\partial P} &\overset{\text{已知 3}}{=}& RT \\
  \frac{\partial \Phi}{\partial z} &\overset{\text{推導 1(c)}}{=}& RT \\
  \end{gather*}$$

  * $\Phi$ : 全場位勢 (Total geopotential) $[\text{m}^{2}\cdot\text{s}^{-2}]$
  * $P$ : 氣壓 (Pressure) $[\text{Pa}]$
  * $g$ : 重力加速度 (Gravitational acceleration) $[\text{m}\cdot\text{s}^{-2}]$，$g \approx 9.81 \ \text{m}\cdot\text{s}^{-2}$
  * $z_{\text{g}}$ : 幾何高度 (Geometric height) $[\text{m}]$
  * $\rho$ : 密度 (Density) $[\text{kg}\cdot\text{m}^{-3}]$
  * $R$ : 乾空氣氣體常數 (Gas constant for dry air) $[\text{J}\cdot\text{kg}^{-1}\cdot\text{K}^{-1}]$，$R \approx 287 \ \text{J}\cdot\text{kg}^{-1}\cdot\text{K}^{-1}$
  * $T$ : 全場溫度 (Total temperature) $[\text{K}]$

* **【推導 5】 壓力座標的連續方程式 (Continuity equation in pressure coordinates)：** 靜力平衡讓質量元的厚度可以用**氣壓厚度**度量，質量守恆於是變成純粹的三維輻散條件

  * (a) 用【已知 1】(c) 把質量元換成氣壓厚度：

    $$\begin{gather*}
    \delta M &=& \rho\,\delta x\,\delta y\,\delta z_{\text{g}} \\
    &\overset{\text{已知 1(c)}}{=}& -\frac{1}{g}\,\delta x\,\delta y\,\delta P
    \end{gather*}$$

  * (b) 代入【已知 2】並取對數微分，常數 $-1/g$ 消掉：

    $$\begin{gather*}
    0 &\overset{\text{已知 2}}{=}& \frac{1}{\delta M}\frac{D\left(\delta M\right)}{Dt} \\
    &=& \frac{D}{Dt} \Big[\ln (\delta M) \Big]\\
    &\overset{\text{推導 5(a)}}{=}& \frac{D}{Dt} \Big[\ln (-\frac{1}{g}\,\delta x\,\delta y\,\delta P) \Big]\\
    &=& \frac{D}{Dt} \Big[ \ln (\frac{1}{g}) +\ln (\delta x) +\ln (\delta y) +\ln (-\delta P) \Big]\\
    &=& \frac{D}{Dt} \Big[ \ln (\frac{1}{g})\Big] + \frac{D \ln (\delta x)}{Dt}  +\frac{D\ln (\delta y)}{Dt} +\frac{D \ln (-\delta P)}{Dt} \\
    &=& 0 + \frac{D \ln (\delta x)}{Dt}  +\frac{D\ln (\delta y)}{Dt} +\frac{D \ln (-\delta P)}{Dt} \\
    &=& \frac{1}{\delta x}\frac{D\left(\delta x\right)}{Dt} + \frac{1}{\delta y}\frac{D\left(\delta y\right)}{Dt} + \frac{1}{-\delta P}\frac{D\left(-\delta P\right)}{Dt} \\
    &=& \frac{1}{\delta x}\frac{D\left(\delta x\right)}{Dt} + \frac{1}{\delta y}\frac{D\left(\delta y\right)}{Dt} + \frac{1}{\delta P}\frac{D\left(\delta P\right)}{Dt}
    \end{gather*}$$

  * (c) 取 $\delta x,\delta y,\delta P \to 0$ 的極限，三項各自變成偏導數：

    $$\begin{gather*}
    0 &\overset{\text{推導 5(b)}}{=}& \frac{1}{\delta x}\frac{D\left(\delta x\right)}{Dt} + \frac{1}{\delta y}\frac{D\left(\delta y\right)}{Dt} + \frac{1}{\delta P}\frac{D\left(\delta P\right)}{Dt} \\
    &=& \frac{1}{\delta x} \delta u + \frac{1}{\delta y}\delta v + \frac{1}{\delta P}\frac{D\left(\delta P\right)}{Dt} \\
    &\overset{\text{定義 3(a)}}{=}& \frac{1}{\delta x} \delta u + \frac{1}{\delta y}\delta v + \frac{1}{\delta P}\delta \omega \\
    &=&\lim_{\delta \to 0} \left[ \frac{\delta u}{\delta x} + \frac{\delta v}{\delta y} + \frac{\delta \omega}{\delta P} \right]\\
    &\overset{\text{定義 3(a)}}{=}& \left.\frac{\partial u}{\partial x}\right|_{P} + \left.\frac{\partial v}{\partial y}\right|_{P} + \frac{\partial \omega}{\partial P}
    \end{gather*}$$

  * $\delta M$ : 隨流體移動的質量元 (Material mass element) $[\text{kg}]$
  * $\rho$ : 密度 (Density) $[\text{kg}\cdot\text{m}^{-3}]$
  * $x$ : 緯向座標 (Zonal coordinate) $[\text{m}]$
  * $y$ : 經向座標，以赤道為原點 (Meridional coordinate) $[\text{m}]$
  * $z_{\text{g}}$ : 幾何高度 (Geometric height) $[\text{m}]$
  * $g$ : 重力加速度 (Gravitational acceleration) $[\text{m}\cdot\text{s}^{-2}]$，$g \approx 9.81 \ \text{m}\cdot\text{s}^{-2}$
  * $P$ : 氣壓 (Pressure) $[\text{Pa}]$
  * $t$ : 時間 (Time) $[\text{s}]$
  * $u$ : 全場緯向風速 (Total zonal velocity) $[\text{m}\cdot\text{s}^{-1}]$
  * $v$ : 全場經向風速 (Total meridional velocity) $[\text{m}\cdot\text{s}^{-1}]$
  * $\omega$ : 氣壓垂直速度 (Pressure velocity) $[\text{Pa}\cdot\text{s}^{-1}]$
  * $\frac{D}{Dt}$ : 全質導數 (Material derivative) $[\text{s}^{-1}]$

* **【推導 6】 對數氣壓座標的連續方程式 (Continuity equation in log-pressure coordinates)：** 把【推導 5】的 $\partial\omega/\partial P$ 換成 $z$ 的形式，$-w$ 這一項就是這樣冒出來的

  $$\begin{gather*}
  \frac{\partial \omega}{\partial P} &\overset{\text{推導 1(c)}}{=}& -\frac{1}{P}\frac{\partial \omega}{\partial z} \\
  &\overset{\text{推導 2}}{=}& -\frac{1}{P}\frac{\partial}{\partial z}\left[-P\,w\right] \\
  &=& \frac{1}{P}\left[\frac{dP}{dz}w + P\frac{\partial w}{\partial z}\right] \\
  &\overset{\text{推導 1(b)}}{=}& \frac{1}{P}\left[-P\,w + P\frac{\partial w}{\partial z}\right] \\
  &=& \frac{\partial w}{\partial z} - w
  \end{gather*}$$

  * $\omega$ : 氣壓垂直速度 (Pressure velocity) $[\text{Pa}\cdot\text{s}^{-1}]$
  * $P$ : 氣壓 (Pressure) $[\text{Pa}]$
  * $z$ : 對數氣壓垂直座標 (Log-pressure vertical coordinate) $[\text{無單位}]$
  * $w$ : 全場對數氣壓垂直速度 (Total log-pressure vertical velocity) $[\text{s}^{-1}]$

* **【推導 7】 對數氣壓座標的熱力學方程式 (Thermodynamic equation in log-pressure coordinates)：** 把第一定律的作功項換成 $w$

  $$\begin{gather*}
  Q_{\text{total}} &\overset{\text{已知 4}}{=}& c_p\frac{DT}{Dt} - \frac{1}{\rho}\frac{DP}{Dt} \\
  Q_{\text{total}} &\overset{\text{已知 3}}{=}& c_p\frac{DT}{Dt} - \frac{RT}{P}\frac{DP}{Dt} \\
  Q_{\text{total}} &\overset{\text{定義 3(a)}}{=}& c_p\frac{DT}{Dt} - \frac{RT}{P}\omega \\
  Q_{\text{total}} &\overset{\text{推導 2}}{=}& c_p\frac{DT}{Dt} - \frac{RT}{P}\left(-P\,w\right) \\
  Q_{\text{total}} &=& c_p\frac{DT}{Dt} + R\,T\,w \\
  \frac{Q_{\text{total}}}{c_p} &=& \frac{DT}{Dt} + \frac{R}{c_p}T\,w \\
  \frac{Q_{\text{total}}}{c_p} &\overset{\text{定義 4}}{=}& \frac{DT}{Dt} + \kappa\,T\,w
  \end{gather*}$$

  * $Q_{\text{total}}$ : 單位質量的總非絕熱加熱率 (Total diabatic heating rate per unit mass) $[\text{J}\cdot\text{kg}^{-1}\cdot\text{s}^{-1}]$
  * $c_p$ : 定壓比熱 (Specific heat at constant pressure) $[\text{J}\cdot\text{kg}^{-1}\cdot\text{K}^{-1}]$，$c_p \approx 1004 \ \text{J}\cdot\text{kg}^{-1}\cdot\text{K}^{-1}$
  * $T$ : 全場溫度 (Total temperature) $[\text{K}]$
  * $t$ : 時間 (Time) $[\text{s}]$
  * $\rho$ : 密度 (Density) $[\text{kg}\cdot\text{m}^{-3}]$
  * $P$ : 氣壓 (Pressure) $[\text{Pa}]$
  * $R$ : 乾空氣氣體常數 (Gas constant for dry air) $[\text{J}\cdot\text{kg}^{-1}\cdot\text{K}^{-1}]$，$R \approx 287 \ \text{J}\cdot\text{kg}^{-1}\cdot\text{K}^{-1}$
  * $\omega$ : 氣壓垂直速度 (Pressure velocity) $[\text{Pa}\cdot\text{s}^{-1}]$
  * $w$ : 全場對數氣壓垂直速度 (Total log-pressure vertical velocity) $[\text{s}^{-1}]$
  * $\kappa$ : Poisson 常數 (Poisson constant) $[\text{無單位}]$，$\kappa \approx 0.286$

+++

## 證明:

### (a) proof 緯向動量方程式 (Zonal momentum equation)

從【已知 1】(a) 起手，依序丟掉度規項、換掉壓力梯度力與科氏參數、線性化全質導數，最後接上阻尼。

$$\begin{gather*}
-\frac{1}{\rho a\cos\varphi}\frac{\partial P}{\partial \lambda} + F_\lambda &\overset{\text{已知 1(a)}}{=}& \frac{Du}{Dt} - fv - \frac{uv\tan\varphi}{a} \\
-\frac{1}{\rho a\cos\varphi}\frac{\partial P}{\partial \lambda} + F_\lambda &\overset{\text{假設 2(c-2)}}{\approx}& \frac{Du}{Dt} - fv \\
-\frac{1}{\rho a\cos\varphi}\frac{\partial P}{\partial \lambda} + F_\lambda &\overset{\text{假設 1(b)}}{=}& \frac{Du}{Dt} - \beta y\,v \\
-\frac{1}{\rho a\cos\varphi}\frac{\partial P}{\partial \lambda} + F_\lambda &\overset{\text{假設 2(c-1)}}{\approx}& \frac{\partial u}{\partial t} - \beta y\,v \\
-\frac{1}{\rho}\frac{\partial P}{\partial x} + F_\lambda &\overset{\text{假設 1(c)}}{=}& \frac{\partial u}{\partial t} - \beta y\,v \\
-\frac{\partial \Phi}{\partial x} + F_\lambda &\overset{\text{推導 3(b)}}{=}& \frac{\partial u}{\partial t} - \beta y\,v \\
-\frac{\partial \phi}{\partial x} + F_\lambda &\overset{\text{假設 2(b)}}{=}& \frac{\partial u}{\partial t} - \beta y\,v \\
-\frac{\partial \phi}{\partial x} - \alpha u &\overset{\text{假設 4(a)}}{=}& \frac{\partial u}{\partial t} - \beta y\,v \\
\frac{\partial u}{\partial t} - \beta y\,v + \frac{\partial \phi}{\partial x} &=& -\alpha u
\end{gather*}$$

### (b) proof 經向動量方程式 (Meridional momentum equation)

與【證明 (a)】逐步平行，只是科氏項與度規項的符號相反。

$$\begin{gather*}
-\frac{1}{\rho a}\frac{\partial P}{\partial \varphi} + F_\varphi &\overset{\text{已知 1(b)}}{=}& \frac{Dv}{Dt} + fu + \frac{u^{2}\tan\varphi}{a} \\
-\frac{1}{\rho a}\frac{\partial P}{\partial \varphi} + F_\varphi &\overset{\text{假設 2(c-3)}}{\approx}& \frac{Dv}{Dt} + fu \\
-\frac{1}{\rho a}\frac{\partial P}{\partial \varphi} + F_\varphi &\overset{\text{假設 1(b)}}{=}& \frac{Dv}{Dt} + \beta y\,u \\
-\frac{1}{\rho a}\frac{\partial P}{\partial \varphi} + F_\varphi &\overset{\text{假設 2(c-1)}}{\approx}& \frac{\partial v}{\partial t} + \beta y\,u \\
-\frac{1}{\rho}\frac{\partial P}{\partial y} + F_\varphi &\overset{\text{假設 1(d)}}{=}& \frac{\partial v}{\partial t} + \beta y\,u \\
-\frac{\partial \Phi}{\partial y} + F_\varphi &\overset{\text{推導 3(b)}}{=}& \frac{\partial v}{\partial t} + \beta y\,u \\
-\frac{\partial \phi}{\partial y} + F_\varphi &\overset{\text{假設 2(b)}}{=}& \frac{\partial v}{\partial t} + \beta y\,u \\
-\frac{\partial \phi}{\partial y} - \alpha v &\overset{\text{假設 4(a)}}{=}& \frac{\partial v}{\partial t} + \beta y\,u \\
\frac{\partial v}{\partial t} + \beta y\,u + \frac{\partial \phi}{\partial y} &=& -\alpha v
\end{gather*}$$

### (c) proof 靜力方程式 (Hydrostatic equation)

把【推導 4】拆成基本態與擾動兩部分，基本態自成一條，剩下的就是目標式。

$$\begin{gather*}
\frac{\partial \Phi}{\partial z} &\overset{\text{推導 4}}{=}& RT \\
\frac{\partial}{\partial z}\left[\bar{\Phi} + \phi\right] &\overset{\text{假設 2(b)}}{=}& R\left[\bar{T} + T'\right] \\
\frac{d\bar{\Phi}}{dz} + \frac{\partial \phi}{\partial z} &=& R\bar{T} + RT' \\
\frac{\partial \phi}{\partial z} &\overset{\text{假設 6}}{=}& RT'
\end{gather*}$$

* 註：由【假設 6】，第三列左右兩側的基本態各自成立 $d\bar{\Phi}/dz = R\bar{T}$，同時消去後只剩擾動的靜力關係。
* 註：**符號交接點** —— 由此以下，符號 $T$ 改指擾動溫度 $T'$（見【假設 2】末的〈記號慣例〉註），故本式即【證明目標】(c) 的 $\dfrac{\partial \phi}{\partial z} = RT$。

### (d) proof 連續方程式 (Continuity equation)

把【推導 6】代進【推導 5】，$-w$ 項自然出現；線性化不影響本式（它本來就是線性的）。

$$\begin{gather*}
0 &\overset{\text{推導 5(c)}}{=}& \frac{\partial u}{\partial x} + \frac{\partial v}{\partial y} + \frac{\partial \omega}{\partial P} \\
&\overset{\text{推導 6}}{=}& \frac{\partial u}{\partial x} + \frac{\partial v}{\partial y} + \frac{\partial w}{\partial z} - w
\end{gather*}$$

### (e) proof 熱力學方程式 (Thermodynamic equation)

把【推導 7】線性化：全質導數只留時間項與**基本態**的垂直平流，兩個 $\bar{T}$ 相關項合併成【定義 6】的 $\Gamma$。

$$\begin{gather*}
\frac{Q_{\text{total}}}{c_p} &\overset{\text{推導 7}}{=}& \frac{DT}{Dt} + \kappa\,T\,w \\
\frac{Q_{\text{total}}}{c_p} &\overset{\text{假設 2(b)}}{=}& \frac{D}{Dt} \Big[\bar{T} + T'\Big] + \kappa\left(\bar{T} + T'\right)w \\
\frac{Q_{\text{total}}}{c_p} &=& \frac{D \bar{T}}{Dt}  +\frac{D T'}{Dt}  + \kappa \bar{T} w + \kappa  T' w\\
\frac{Q_{\text{total}}}{c_p} &\overset{\text{假設 2(d)}}{=}&  w\frac{d\bar{T}}{dz}  +\frac{D T'}{Dt}  + \kappa \bar{T} w + \kappa  T' w\\
\frac{Q_{\text{total}}}{c_p} &\overset{\text{假設 2(c-1)}}{=}&  w\frac{d\bar{T}}{dz}  +\frac{\partial T'}{\partial t}  + \kappa \bar{T} w + \kappa  T' w\\
\frac{Q_{\text{total}}}{c_p} &\overset{\text{假設 2(c)}}{\approx}&  w\frac{d\bar{T}}{dz}  +\frac{\partial T'}{\partial t}  + \kappa \bar{T} w + \kappa  \cdot 0\\
\frac{Q_{\text{total}}}{c_p} &=& \frac{\partial T'}{\partial t} + w\frac{d\bar{T}}{dz} + \kappa\bar{T}w \\
\frac{Q_{\text{total}}}{c_p} &=& \frac{\partial T'}{\partial t} + \left[\frac{d\bar{T}}{dz} + \kappa\bar{T}\right]w \\
\frac{Q_{\text{total}}}{c_p} &\overset{\text{定義 6}}{=}& \frac{\partial T'}{\partial t} + \Gamma w \\
\frac{Q}{c_p} - \alpha T' &\overset{\text{假設 4(b-1)}}{=}& \frac{\partial T'}{\partial t} + \Gamma w \\
\frac{\partial T'}{\partial t} + \Gamma w &=& -\alpha T' + \frac{Q}{c_p}
\end{gather*}$$

* 註：**符號交接點** —— 全場溫度的基本態部分已整個被【定義 6】的 $\Gamma$ 吸收，式中只剩擾動量；由此以下符號 $T$ 改指 $T'$（見【假設 2】末的〈記號慣例〉註），故本式即【證明目標】(e) 的 $\dfrac{\partial T}{\partial t} + \Gamma w = -\alpha T + \dfrac{Q}{c_p}$。

+++

## 結構解釋

### $-w$ 這一項從哪裡來

【證明 (d)】的連續方程式多了一個 $-w$，這是對數氣壓座標**唯一**不直觀的地方。它的來源在【推導 6】的第三列：$\dfrac{\partial}{\partial z}\left[-Pw\right]$ 展開時，$P$ 本身隨 $z$ 變（【推導 1】(b) 的 $dP/dz = -P$），於是產生了一個額外的 $-w$。

物理上，這是**密度隨高度指數遞減**留下的痕跡。等價的寫法是

$$\frac{\partial u}{\partial x} + \frac{\partial v}{\partial y} + e^{z}\frac{\partial}{\partial z}\left[e^{-z}w\right] = 0$$

也就是「以 $e^{-z} \propto P$ 為權重的垂直質量通量」的散度為零。這個 $e^{-z}$ 權重之後會一路出現在能量積分 $(2.3)$ 裡。

### 為什麼 $u,v,\phi$ 與 $T,w,Q$ 註定要用不同的垂直結構函數

【證明 (c)】說 $\dfrac{\partial\phi}{\partial z} = RT$：**$T$ 是 $\phi$ 的垂直導數**。【證明 (d)】說 $w$ 出現在 $\dfrac{\partial w}{\partial z}$ 裡跟 $u,v$ 的水平輻散平衡。

這兩件事合起來就決定了：若 $u,v,\phi \propto Z(z)$，則必然 $T,w,Q \propto Z'(z)$ —— 這裡的 $Z'$ 是**垂直結構函數 $Z$ 對 $z$ 的一階微分** $\dfrac{dZ}{dz}$（本庫的撇號一律只表示對 $z$ 微分，見【假設 2】末的〈記號慣例〉註）。這正是 [垂直結構分離](Separation_into_Horizontal_Structure_System.md) 中 $(3.4)$ 那個「兩組變數用兩個不同函數」的來源 —— 它不是湊出來的，是靜力方程式逼出來的。

### 三個近似各自買到了什麼

| 近似 | 出處 | 買到什麼 | 代價 |
|---|---|---|---|
| 對數氣壓座標 | 【定義 1】 | 密度從方程式裡**完全消失**（【推導 4】【推導 5】），系統變成常係數 | 多一個 $-w$ 項；$w$ 不再是速度 |
| 線性化 | 【假設 2】 | 可用正規模態展開；解可疊加 | 無法描述強西風爆發等非線性效應 |
| 赤道 $\beta$ 平面 | 【假設 1】 | $f = \beta y$ 為 $y$ 的**奇函數**，這是全文物理引擎的源頭 | 只在 $\left|\varphi\right| \ll 1$ 有效；球面推廣見論文 §7 |

$f = \beta y$ 這個「線性且過原點」的形式，是後面 [赤道 PV 方程式](Equatorial_PV_Equation_and_Beta_y_Source.md) 裡「赤道上生不出 PV」這個核心結論的唯一來源。
