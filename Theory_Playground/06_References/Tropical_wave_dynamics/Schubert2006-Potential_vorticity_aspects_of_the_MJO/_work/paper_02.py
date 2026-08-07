#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""a_paper.jsonl 第二批：2. Governing equations / 3. Separation of the vertical and horizontal structure。"""
from _common import append

CELLS = []

# ---------------------------------------------------------------- 2. Governing equations
CELLS.append(r"""### 2. Governing equations

Consider small amplitude motions about a resting basic state in a stratified, compressible, quasi-static atmosphere on the equatorial $\beta$-plane. Using $z = \ln(p_0/p)$ (where $p_0 = 1010\text{ mb}$ is a constant "surface" pressure) as the vertical coordinate, we can write the linearized governing equations as

$$
\frac{\partial u}{\partial t} - \beta y v + \frac{\partial \phi}{\partial x} = -\alpha u,
\qquad
\frac{\partial v}{\partial t} + \beta y u + \frac{\partial \phi}{\partial y} = -\alpha v,
\qquad
\frac{\partial \phi}{\partial z} = RT,
$$

$$
\frac{\partial u}{\partial x} + \frac{\partial v}{\partial y} + \frac{\partial w}{\partial z} - w = 0,
\qquad
\frac{\partial T}{\partial t} + \Gamma w = -\alpha T + \frac{Q}{c_p},
\tag{2.1}
$$

where $u$ is the eastward component of velocity, $v$ the northward component, $w = Dz/Dt$ the "vertical log-pressure velocity", $\phi$ the perturbation geopotential, $T$ the perturbation temperature, $\beta = 2\Omega/a$ the equatorial value of the northward gradient of the Coriolis parameter, $\Omega$ the Earth's rotation rate, $a$ the Earth's radius, $\alpha$ the constant coefficient for Rayleigh friction and Newtonian cooling, $\Gamma = d\bar{T}/dz + \kappa\bar{T}$ ($\kappa = R/c_p$) the basic state static stability computed from the basic state temperature profile $\bar{T}(z)$, and $Q(x, y, z, t)$ the diabatic source term. For simplicity we assume that $\Gamma$ is a constant, and choose the tropical tropospheric mean value $\Gamma = 23.79\text{ K}$. We seek solutions of $(2.1)$ on a domain that is infinite in $y$, periodic over $-\pi a \le x \le \pi a$, and confined between $z = 0$ and $z = z_T = \ln(1010/200) \approx 1.619$, with the boundary conditions $w = 0$ at $z = 0, z_T$.

The total energy principle for the system $(2.1)$ is

$$
\frac{d\mathcal{E}}{dt} = -2\alpha\mathcal{E} + \mathcal{G},
\tag{2.2}
$$

where the total energy $\mathcal{E}$ and the generation term $\mathcal{G}$ are defined by

$$
\mathcal{E} = \iiint \frac{1}{2}\left[u^2 + v^2 + \frac{1}{R\Gamma}\left(\frac{\partial\phi}{\partial z}\right)^2\right] e^{-z}\, dx\, dy\, dz,
$$

$$
\mathcal{G} = \iiint \frac{1}{c_p\Gamma}\frac{\partial\phi}{\partial z} Q\, e^{-z}\, dx\, dy\, dz.
\tag{2.3}
$$

In the following analysis we shall assume that the flow is steady in a reference frame moving with the heat source $Q$. Under this assumption the total energy principle $(2.2)$ becomes $2\alpha\mathcal{E} = \mathcal{G}$, i.e., there is a balance between the total energy dissipation $2\alpha\mathcal{E}$ and the diabatic generation $\mathcal{G}$. In the examples we explore here, the energy generation is due to a non-zero $Q$ in a localized, eastward moving region near the equator, while the dissipation occurs in the much broader area into which the energy has propagated via equatorial wave motions.

To derive the potential vorticity principle associated with $(2.1)$ we first cross-differentiate the horizontal momentum equations to obtain the vorticity equation

$$
\left(\frac{\partial}{\partial t} + \alpha\right)\left(\frac{\partial v}{\partial x} - \frac{\partial u}{\partial y}\right) + \beta y \left(\frac{\partial u}{\partial x} + \frac{\partial v}{\partial y}\right) + \beta v = 0,
\tag{2.4}
$$

and then combine the hydrostatic, continuity, and thermodynamic equations in such a way as to eliminate $T$ and $w$, which results in

$$
\left(\frac{\partial}{\partial t} + \alpha\right)\left(\frac{\partial}{\partial z} - 1\right)\frac{\partial\phi}{\partial z} - R\Gamma\left(\frac{\partial u}{\partial x} + \frac{\partial v}{\partial y}\right) = \kappa\left(\frac{\partial}{\partial z} - 1\right)Q.
\tag{2.5}
$$

Then, eliminating the horizontal divergence between $(2.4)$ and $(2.5)$, we obtain

$$
\frac{\partial q}{\partial t} + \beta v = -\alpha q + \frac{\beta y}{c_p\Gamma}\left(\frac{\partial}{\partial z} - 1\right)Q,
\tag{2.6}
$$

where

$$
q = \frac{\partial v}{\partial x} - \frac{\partial u}{\partial y} + \frac{\beta y}{R\Gamma}\left(\frac{\partial}{\partial z} - 1\right)\frac{\partial\phi}{\partial z}
\tag{2.7}
$$

is the potential vorticity anomaly. We shall concentrate on interpreting the flow patterns associated with a moving heat source in terms of a PV wake. For this interpretation the $y$-factor in the last term of $(2.6)$ plays a crucial role. It causes the source term $Q$ to be ineffective at generating a PV anomaly at the equator but maximizes the PV response near the poleward edges of the heat source. In this manner a moving equatorial heat source can produce two ribbons of lower tropospheric PV anomaly, a positive one off the equator in the northern hemisphere and a negative one off the equator in the southern hemisphere, with oppositely signed PV anomalies in the upper troposphere.

---

本節在**赤道 $\beta$ 平面**上，考慮一個**層結、可壓縮、準靜力（quasi-static）大氣**中，繞著**靜止基本態**的**小振幅擾動**。垂直座標取的是**對數氣壓座標** $z = \ln(p_0/p)$，其中 $p_0 = 1010\text{ mb}$ 是固定的「地面」氣壓。式 $(2.1)$ 即為線性化後的控制方程組：兩條水平動量方程、靜力方程、連續方程、熱力學方程。

各符號的意義是：$u$ 為東向風速、$v$ 為北向風速、$w = Dz/Dt$ 是「對數氣壓垂直速度」、$\phi$ 為擾動位勢、$T$ 為擾動溫度、$\beta = 2\Omega/a$ 是科氏參數北向梯度在赤道的值、$\Omega$ 為地球自轉角速度、$a$ 為地球半徑、$\alpha$ 是**瑞利摩擦（Rayleigh friction）與牛頓冷卻（Newtonian cooling）共用的常數阻尼係數**、$\Gamma = d\bar{T}/dz + \kappa\bar{T}$（$\kappa = R/c_p$）是由基本態溫度剖面 $\bar{T}(z)$ 算出的**靜力穩定度**、$Q(x,y,z,t)$ 則是**非絕熱源項**。

作者為了簡化，**把 $\Gamma$ 視為常數**，取熱帶對流層平均值 $\Gamma = 23.79\text{ K}$。求解區域在 $y$ 方向是無限的、在 $x$ 方向以 $-\pi a \le x \le \pi a$ 週期化（即繞地球一圈），垂直方向侷限在 $z = 0$ 到 $z = z_T = \ln(1010/200) \approx 1.619$ 之間（約當 $200\text{ hPa}$），上下邊界條件為 $w = 0$。

**能量約束**：式 $(2.2)$–$(2.3)$ 給出總能量原理。這裡有一個關鍵的觀念操作——**一旦假設「解在隨熱源移動的座標系中是定常的」，$(2.2)$ 就退化成 $2\alpha\mathcal{E} = \mathcal{G}$**，也就是**總能量耗散恰好與非絕熱生成達成平衡**。在本文的設定中，**能量的「生成」集中在赤道附近一塊侷限、東移的非零 $Q$ 區域，而「耗散」則分散在能量藉赤道波動傳播過去、廣大得多的區域**。

**PV 原理的推導**：先把兩條水平動量方程交叉微分，得到渦度方程 $(2.4)$；再把靜力、連續、熱力學三式組合起來消掉 $T$ 與 $w$，得到 $(2.5)$；最後在 $(2.4)$ 與 $(2.5)$ 之間消去水平輻散，就得到 **PV 距平 $q$ 的守恆型方程 $(2.6)$**，其中 $q$ 的定義是 $(2.7)$。

**本文最核心的一句話就藏在 $(2.6)$ 的最後一項**：源項前面帶著一個 $\beta y$ 的因子（相對於 $y$ 是奇函數）。這代表：

* **在赤道上（$y = 0$）加熱完全無法生成 PV 距平**——不管 $Q$ 多大都一樣；
* **PV 響應反而在熱源的南北兩側邊緣達到最大**。

於是一個東移的赤道熱源，會在對流層低層拉出**兩條 PV 距平帶**：北半球離赤道處為**正 PV**、南半球對應處為**負 PV**；而在對流層高層，由於垂直結構函數 $Z(z)$ 變號，**PV 距平的正負號整個相反**。""")

# ---------------------------------------------------------------- 3. Separation
CELLS.append(r"""### 3. Separation of the vertical and horizontal structure

Our first step in the solution of $(2.1)$ is to separate off the vertical structure, under the assumption that the diabatic forcing excites only the first vertical internal mode. Thus, it is convenient to introduce a vertical structure function $Z(z)$ that satisfies the second order equation

$$
\left(\frac{d}{dz} - 1\right)\frac{dZ}{dz} = -\left(\frac{\pi^2}{z_T^2} + \frac{1}{4}\right)Z.
\tag{3.1}
$$

The solution satisfying the boundary conditions $Z'(0) = Z'(z_T) = 0$ can be written in the normalized form

$$
Z(z) = \left(\frac{\pi^2}{z_T^2} + \frac{1}{4}\right)^{-(1/2)} e^{(z - z_m)/2}\left[\frac{z_T}{2\pi}\sin\!\left(\frac{\pi z}{z_T}\right) - \cos\!\left(\frac{\pi z}{z_T}\right)\right],
\tag{3.2}
$$

while its derivative takes the form

$$
Z'(z) = \left(1 + \frac{z_T^2}{4\pi^2}\right)^{1/2} e^{(z - z_m)/2}\sin\!\left(\frac{\pi z}{z_T}\right),
\tag{3.3}
$$

where $z_m$, the level at which $Z'(z)$ reaches its maximum value, is given by $\pi z_m/z_T = \pi + \tan^{-1}(-2\pi/z_T)$, which, for $z_T \approx 1.619$, turns out to be $z_m \approx 0.5803 z_T$. For later convenience, the normalization chosen in $(3.2)$ and $(3.3)$ yields $Z'(z_m) = 1$. The functions $Z(z)$ and $Z'(z)$ are shown in Fig. 1. Also shown in Fig. 1 is the 120-day mean (November 1992–February 1993) vertical profile of the heating rate for the western Pacific warm pool [*Johnson and Ciesielski*, $2000$]. The observed mean profile of $Q/c_p$ has a peak value of approximately $4\text{ K day}^{-1}$, and its shape is closely approximated by $Z'(z)$, which is the justification for considering only the first vertical internal mode in the following analysis. Over the 120-day observational period there were two MJO passages [*Lin and Johnson*, $1996$b; *Yanai et al.*, $2000$]. During these two periods of enhanced convection the shape of the vertical profile of $Q/c_p$ was very similar to the shape of the time mean profile shown in Fig. 1, but the peak values were considerably larger, $10\text{ K day}^{-1}$ for the first MJO and $16\text{ K day}^{-1}$ for the second. Thus, for the vertical profile of heating at the time of peak convective activity during the passage of an MJO, our model uses the $Z'(z)$ profile shown in Fig. 1, but scaled so the peak value is $12\text{ K day}^{-1}$ (see Table 1) rather than $4\text{ K day}^{-1}$.

![](./pic/Schubert2006_fig1.png)

**Fig. 1.** The curves labeled $Z(z)$ and $Z'(z)$ (interpreted using the lower scale) are the vertical structure functions defined by $(3.2)$ and $(3.3)$. The curve labeled $Q/c_p$ (interpreted using the upper scale) is the 120-day mean vertical profile of heating rate for the western Pacific warm pool, as determined by [*Johnson and Ciesielski*, $2000$].

Assuming that $u, v, \phi, T, w, Q$ have the separable forms

$$
\begin{pmatrix} u(x,y,z,t) \cr v(x,y,z,t) \cr \phi(x,y,z,t) \end{pmatrix}
= \begin{pmatrix} \hat{u}(x,y,t) \cr \hat{v}(x,y,t) \cr \hat{\phi}(x,y,t) \end{pmatrix} Z(z),
\qquad
\begin{pmatrix} T(x,y,z,t) \cr w(x,y,z,t) \cr Q(x,y,z,t) \end{pmatrix}
= \begin{pmatrix} \hat{T}(x,y,t) \cr \hat{w}(x,y,t) \cr \hat{Q}(x,y,t) \end{pmatrix} Z'(z),
\tag{3.4}
$$

we can convert $(2.1)$ into the following system for the horizontal structure functions $\hat{u}, \hat{v}, \hat{\phi}, \hat{T}, \hat{w}$:

$$
\frac{\partial\hat{u}}{\partial t} - \beta y\hat{v} + \frac{\partial\hat{\phi}}{\partial x} = -\alpha\hat{u},
\qquad
\frac{\partial\hat{v}}{\partial t} + \beta y\hat{u} + \frac{\partial\hat{\phi}}{\partial y} = -\alpha\hat{v},
\qquad
\hat{\phi} = R\hat{T},
$$

$$
\frac{\partial\hat{u}}{\partial x} + \frac{\partial\hat{v}}{\partial y} - \left(\frac{\pi^2}{z_T^2} + \frac{1}{4}\right)\hat{w} = 0,
\qquad
\frac{\partial\hat{T}}{\partial t} + \Gamma\hat{w} = -\alpha\hat{T} + \frac{\hat{Q}}{c_p}.
\tag{3.5}
$$

In the next section we present an analytical solution of $(3.5)$. The solution can be considered as the primitive equation generalization of the simplest MJO model involving the first baroclinic mode response to a moving planetary scale heat source under the long wave approximation [*Chao*, $1987$].

**Table 1.** Constants

| 符號 | 值 | 符號 | 值 | 符號 | 值 |
|---|---|---|---|---|---|
| $c_p$ | $1004\ \text{J kg}^{-1}\text{K}^{-1}$ | $\beta$ | $2\Omega/a$ | $\bar{c}$ | $41.25\ \text{m s}^{-1}$ |
| $R$ | $287\ \text{J kg}^{-1}\text{K}^{-1}$ | $p_0$ | $1010\ \text{mb}$ | $\epsilon$ | $507.3$ |
| $\Omega$ | $7.292\times10^{-5}\ \text{s}^{-1}$ | $z_T$ | $1.619$ | $a_0$ | $1250\ \text{km}$ |
| $a$ | $6370\ \text{km}$ | $\Gamma$ | $23.79\ \text{K}$ | $b_0$ | $450\ \text{km}$ |
| $y_0$ | $0$ 或 $450\ \text{km}$ | $Q_0/c_p$ | $12\ \text{K day}^{-1}$ | $c$ | $5\ \text{m s}^{-1}$ |
| $\alpha$ | $(4\ \text{days})^{-1}$ | | | | |

---

求解 $(2.1)$ 的第一步是**把垂直結構分離出來**，其背後的假設是：**非絕熱強迫只激發第一垂直內模態（first vertical internal mode）**。作者為此引入滿足二階方程 $(3.1)$ 的**垂直結構函數** $Z(z)$，在上下邊界條件 $Z'(0) = Z'(z_T) = 0$ 之下解得歸一化形式 $(3.2)$，其導數則為 $(3.3)$。

其中 $z_m$ 是 $Z'(z)$ 取極大值的高度，由 $\pi z_m/z_T = \pi + \tan^{-1}(-2\pi/z_T)$ 決定；當 $z_T \approx 1.619$ 時 $z_m \approx 0.5803\, z_T$。$(3.2)$、$(3.3)$ 的歸一化方式刻意選成讓 $Z'(z_m) = 1$，方便後續運算。

**為什麼「只留第一模態」是合理的？** 這是本節的關鍵論證，證據就在圖 1：作者把 Johnson and Ciesielski (2000) 針對西太平洋暖池所算出的 **120 天平均（1992 年 11 月–1993 年 2 月）加熱率垂直剖面 $Q/c_p$** 疊上去，發現**觀測剖面的形狀與 $Z'(z)$ 幾乎重合**——這就是「後續分析只考慮第一垂直內模態」的正當性來源。

**數值的挑選**：觀測平均剖面的峰值約 $4\text{ K day}^{-1}$；但在這 120 天內有**兩次 MJO 通過**，兩次增強對流期間 $Q/c_p$ 的**形狀**與時間平均剖面非常相似，**峰值卻大得多**——第一次 MJO 約 $10\text{ K day}^{-1}$、第二次約 $16\text{ K day}^{-1}$。因此，為了代表「MJO 通過時對流最旺盛的時刻」，**模式採用圖 1 的 $Z'(z)$ 形狀，但把峰值調成 $12\text{ K day}^{-1}$**（見 Table 1），而非 $4\text{ K day}^{-1}$。

**分離變數的技術細節**（式 $(3.4)$）：值得注意的是**兩組變數用的垂直結構函數不同**——$u$、$v$、$\phi$ 用 $Z(z)$，而 $T$、$w$、$Q$ 用 $Z'(z)$。這是由靜力方程 $\partial\phi/\partial z = RT$ 與連續方程共同決定的自然配對。代回 $(2.1)$ 後，就把三維問題壓成只含 $\hat{u}, \hat{v}, \hat{\phi}, \hat{T}, \hat{w}$ 的**二維水平結構方程組 $(3.5)$**——形式上就是一組**淺水方程（shallow water system）**。

最後作者點明本文的定位：$(3.5)$ 的解析解，可視為 **Chao (1987) 那個「長波近似下、第一斜壓模態對移動行星尺度熱源之響應」的最簡 MJO 模式的原始方程推廣版**。""")

if __name__ == "__main__":
    n = append("a_paper.jsonl", CELLS)
    print("paper_02 -> a_paper.jsonl  cells=%d" % n)
