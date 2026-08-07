#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""a_paper.jsonl 第四批：5. / 6. / 7. / Appendix A / Appendix B。"""
from _common import append

CELLS = []

# ---------------------------------------------------------------- 5.
CELLS.append(r"""### 5. Parameters controlling the PV wake

Eq. $(2.6)$ states that $q$ changes locally in time due to the Rossby term $\beta v$, the damping term $-\alpha q$, and the generation term $(c_p\Gamma)^{-1}\beta y(\partial/\partial z - 1)Q$. Insight into the importance of the $\beta v$ term and into the critical parameters governing the PV wake can be obtained by calculating the hypothetical PV distribution that would result from forcing and dissipation only, i.e., the PV distribution resulting from the neglect of the Rossby term in $(2.6)$. With the $\beta v$ term neglected, and with the replacement $\partial/\partial t \to -c(\partial/\partial\xi)$, $(2.6)$ reduces to

$$
c\frac{\partial q}{\partial\xi} = \alpha q - \frac{\beta y}{c_p\Gamma}\left(\frac{\partial}{\partial z} - 1\right)Q,
\tag{5.1}
$$

where $Q$ is defined in $(3.4)$ and $(4.1)$. The solution of $(5.1)$ is easily obtained and can be written in the form

$$
q(\xi, y, z) = -\frac{\tau_{\mathrm{p}}}{\tau_{\mathrm{c}}}\left(\frac{\pi^{2}}{\pi^{2} + \alpha^{2}\tau_{\mathrm{p}}^{2}}\right)F(\xi)\,\beta y \exp\!\left[-\left(\frac{y - y_0}{b_0}\right)^{2}\right]Z(z),
\tag{5.2}
$$

where

$$
F(\xi) = \frac{\sinh\left[(\alpha/c)a_0\right]}{(\alpha/c)a_0}\exp\left[(\alpha/c)\xi\right]
\qquad\text{if}\quad -\infty < \xi \le -a_0,
\tag{5.3}
$$

$$
F(\xi) = \frac{1 - \exp\left[-(\alpha/c)(a_0 - \xi)\right]}{2(\alpha/c)a_0} + \frac{\alpha a_0}{2\pi^{2}c}\left[1 + \cos(\pi\xi/a_0)\right] - \frac{1}{2\pi}\sin(\pi\xi/a_0)
\tag{5.4}
$$

if $-a_0 \le \xi \le a_0$, and $F(\xi) = 0$ if $a_0 \le \xi < \infty$. In $(5.2)$ the parameter $\tau_{\mathrm{p}} = a_0/c$ is a measure of the passage time of the convective region and the parameter $\tau_{\mathrm{c}} = \bar{c}^{2}/(\kappa Q_0)$ is a measure of the convective overturning time. A plot of $(5.2)$ for $y_0 = 0$, with the remaining parameters listed in Table 1, is shown in Fig. 7. This solution illustrates how a propagating convective region leaves in its wake two trailing PV strips on opposite sides of the equator.

![](./pic/Schubert2006_fig7.png)

**Fig. 7.** Hypothetical potential vorticity resulting from forcing and dissipation only, as computed from $(5.2)$ with $y_0 = 0$.

However, a comparison of Fig. 7 with the top panel of Fig. 4 shows that the neglect of $\beta v$ results in a $q$ field that has only $68\%$ of the correct strength and does not extend far enough poleward or westward. The lower tropospheric meridional flow shown in Fig. 3 extends poleward and westward a considerable distance and results in an advection of basic state PV towards the equator. This effect, included in Figs. 3 and 4 but excluded from Fig. 7, tends to make the PV anomaly stronger and broader in both its westward and north-south extent.

In spite of this weakness, the solution $(5.2)$ reveals that three important parameters controlling the PV wake are the wake decay length $c/\alpha$, the ratio of time scales $\tau_{\mathrm{p}}/\tau_{\mathrm{c}}$, and the dimensionless offset $y_0/b_0$. For the examples shown in Fig. 7 the wake decay length is $c/\alpha = 1728\text{ km}$, i.e., the PV anomaly trailing to the west of the convective region has a $1/e$ decay scale of $1728\text{ km}$. The ratio $\tau_{\mathrm{p}}/\tau_{\mathrm{c}}$, which controls the strength of the PV anomaly, is a measure of the number of convective overturnings during the passage of the convection. The factor $\tau_{\mathrm{p}}/\tau_{\mathrm{c}}$ is large, and the corresponding PV anomaly is large, for intensely raining, zonally wide, slowly moving convective regions, while it is small, and the corresponding PV anomaly is small, for weakly raining, zonally narrow, fast moving convective regions. For the case shown in Fig. 4, $a_0 = 1250\text{ km}$ and $c = 5\text{ m s}^{-1}$ so that $\tau_{\mathrm{p}} = 69.4\text{ h}$, while $\bar{c} = 41.25\text{ m s}^{-1}$ and $Q_0/c_p = 12\text{ K day}^{-1}$ so that $\tau_{\mathrm{c}} = 11.9\text{ h}$, resulting in $\tau_{\mathrm{p}}/\tau_{\mathrm{c}} = 5.8$.

Finally it is worth noting that the solution $(5.2)$ can be used to obtain a rough indication of when nonlinear effects are expected to become important. For example, at 850 hPa and $x = -a_0$, and for $\alpha\tau_{\mathrm{p}} \approx 0.72$, $(5.2)$ becomes $q \approx -0.15(\tau_{\mathrm{p}}/\tau_{\mathrm{c}})\beta y \exp[-(y - y_0)^{2}/b_0^{2}]$. As $\tau_{\mathrm{p}}/\tau_{\mathrm{c}}$ becomes larger we expect that the potential vorticity anomaly $q$ (and hence the relative vorticity $\partial v/\partial x - \partial u/\partial y$) will eventually become larger than $\beta y$, in which case the factor $\beta y$ in the last term of $(2.6)$ should be replaced by the total potential vorticity and the factor $\beta y$ in the divergence term of $(2.4)$ should be replaced by the absolute vorticity (a nonlinear effect). Although the inclusion of nonlinear terms in the case $\tau_{\mathrm{p}}/\tau_{\mathrm{c}} = 5.8$ should not lead to qualitative changes from the linear solution, larger values of $\tau_{\mathrm{p}}/\tau_{\mathrm{c}}$ that cause intense westerly wind bursts ($\sim 15\text{ m s}^{-1}$) should be expected to have significant nonlinear effects. For detailed discussions on the role of nonlinear effects the reader is referred to [*Gill and Phlips*, $1986$], [*Van Tuyl*, $1987$] and [*Gandu and Silva Dias*, $1998$], who have used models similar to ours, and to [*Majda and Klein*, $2003$], [*Majda et al.*, $2004$b] and [*Biello and Majda*, $2005$], who have used a systematic multiscale perturbation theory to develop simplified nonlinear (or quasi-linear) model equations for tropical interactions across multiple spatial and temporal scales.

---

本節的手法是一個很典型的「**拆項實驗（term-by-term diagnosis）**」：$(2.6)$ 說 PV 距平 $q$ 的局地變化由三項決定——**羅斯貝項 $\beta v$**、**阻尼項 $-\alpha q$**、**生成項 $(c_p\Gamma)^{-1}\beta y(\partial/\partial z - 1)Q$**。作者刻意**把 $\beta v$ 項拿掉**，只留「強迫 ＋ 耗散」，看看解會長成什麼樣——這樣就能同時（a）看出 $\beta v$ 到底有多重要，（b）把控制 PV 尾流的關鍵參數逼出來。

拿掉 $\beta v$ 之後，$(2.6)$ 化成一階常微分方程 $(5.1)$，可以**解析求解**得 $(5.2)$，其緯向結構函數 $F(\xi)$ 分三段給在 $(5.3)$、$(5.4)$：對流後方（$\xi \le -a_0$）是**指數衰減的尾巴**，對流內部（$|\xi| \le a_0$）是解析組合，對流前方（$\xi \ge a_0$）**恆為零**（因為訊息只往後留）。

**注意 $(5.2)$ 的結構**：$q \propto -\beta y \exp[-(y-y_0)^2/b_0^2]$，這個 $\beta y$ 乘上偶函數高斯的組合，**就是「兩條反號 PV 帶」的數學來源**——在 $y = y_0$ 處為零、南北兩側取極值且反號。圖 7 畫的就是這件事。

**$\beta v$ 有多重要？** 拿圖 7 跟圖 4 上圖一比：**忽略 $\beta v$ 的 $q$ 場只有正確強度的 $68\%$**，而且往極側、往西側都拉得不夠遠。原因在圖 3——低層經向風 $v$ 往極側與西側延伸相當遠，會**把基本態 PV 往赤道方向平流**；這個效應含在圖 3、4 裡，卻被圖 7 排除掉了，因此它**同時讓 PV 距平更強、也讓它在東西向與南北向都更寬**。

**三個控制參數**（本節最重要的產出）：

1. **尾流衰減長度 $c/\alpha$** —— 對流西側 PV 距平的 $1/e$ 衰減尺度。本文設定下 $c/\alpha = 1728\text{ km}$。
2. **時間尺度比 $\tau_{\mathrm{p}}/\tau_{\mathrm{c}}$** —— 控制 PV 距平的**強度**。其中 $\tau_{\mathrm{p}} = a_0/c$ 是**對流區通過所需的時間**，$\tau_{\mathrm{c}} = \bar{c}^{2}/(\kappa Q_0)$ 是**對流翻轉時間**。這個比值的物理意義就是：**對流通過的期間，總共翻轉了幾次**。
    * **又下大雨、緯向又寬、又移動得慢** → $\tau_{\mathrm{p}}/\tau_{\mathrm{c}}$ 大 → **PV 距平大**；
    * **雨小、窄、跑得快** → 比值小 → PV 距平小。
    * 本文個案：$a_0 = 1250\text{ km}$、$c = 5\text{ m s}^{-1}$ → $\tau_{\mathrm{p}} = 69.4\text{ h}$；$\bar{c} = 41.25\text{ m s}^{-1}$、$Q_0/c_p = 12\text{ K day}^{-1}$ → $\tau_{\mathrm{c}} = 11.9\text{ h}$，故 **$\tau_{\mathrm{p}}/\tau_{\mathrm{c}} = 5.8$**。
3. **無因次偏移量 $y_0/b_0$** —— 控制 PV 尾流的**南北不對稱程度**。

**線性假設什麼時候會失效？** 作者用 $(5.2)$ 做了一個漂亮的自我檢查：在 $850\text{ hPa}$、$x = -a_0$、$\alpha\tau_{\mathrm{p}} \approx 0.72$ 時，$(5.2)$ 簡化為

$$
q \approx -0.15\left(\frac{\tau_{\mathrm{p}}}{\tau_{\mathrm{c}}}\right)\beta y \exp\!\left[-\frac{(y-y_0)^{2}}{b_0^{2}}\right]
$$

當 $\tau_{\mathrm{p}}/\tau_{\mathrm{c}}$ 繼續增大，**$q$（乃至相對渦度 $\partial v/\partial x - \partial u/\partial y$）終將超過 $\beta y$ 本身**。一旦如此，$(2.6)$ 最後一項的 $\beta y$ 就該換成**全 PV**、$(2.4)$ 輻散項的 $\beta y$ 就該換成**絕對渦度**——那就是非線性了。作者判斷：**$\tau_{\mathrm{p}}/\tau_{\mathrm{c}} = 5.8$ 這個個案，加進非線性項不會造成定性上的改變**；但若比值大到能激出 $\sim 15\text{ m s}^{-1}$ 的強西風爆發（westerly wind burst），**非線性效應就不可忽略**。""")

# ---------------------------------------------------------------- 6.
CELLS.append(r"""### 6. An invertibility principle

We now show that the wind and mass fields in the wake of a convective envelope can be approximately recovered from the PV through a simple invertibility principle. The argument begins by returning to $(2.7)$, written in the form

$$
\nabla^{2}\psi + \frac{\beta y}{R\Gamma}\left(\frac{\partial}{\partial z} - 1\right)\frac{\partial\phi}{\partial z} = q,
\tag{6.1}
$$

where $\psi$ is the streamfunction for the rotational part of the flow and $\nabla^{2} = \partial^{2}/\partial x^{2} + \partial^{2}/\partial y^{2}$ is the horizontal Laplacian operator. Eq. $(6.1)$ can be converted into an invertibility principle by introducing an approximate balance relation between the wind and mass fields, i.e., a relation between $\psi$ and $\phi$. The balance approximation used here is derived from the linear balance relation $\nabla\cdot(\beta y\nabla\psi) = \nabla^{2}\phi$, with the additional assumption that $\beta y$ can be treated as slowly varying. With this additional assumption, the linear balance approximation can be written as $\nabla^{2}(\phi - \beta y\psi) = 0$, from which, with the condition $\phi - \beta y\psi \to 0$ as $y \to \pm\infty$, it immediately follows that $\phi = \beta y\psi$. Using this in $(6.1)$ we obtain

$$
\nabla^{2}\psi + \frac{\beta^{2}y^{2}}{R\Gamma}\left(\frac{\partial}{\partial z} - 1\right)\frac{\partial\psi}{\partial z} = q.
\tag{6.2}
$$

Concerning the boundary conditions for $(6.2)$, we here use the simple conditions $\psi \to 0$ as $y \to \pm\infty$ and $\partial\psi/\partial z = 0$ at $z = 0, z_T$, noting that the lower condition could easily be generalized to allow temperature variations at $z = 0$. Eq. $(6.2)$, together with its boundary conditions, constitute an invertibility principle. From this principle we can recover $\psi$, and then compute the rotational wind field from $(u_\psi, v_\psi) = (-\partial\psi/\partial y, \partial\psi/\partial x)$ and the mass field from $\phi = \beta y\psi$. Although the invertibility principle $(6.2)$ can be used in conjunction with an approximate PV equation to form a closed balanced theory (see Section 7), our discussion in this section is limited to the use of $(6.2)$ as a diagnostic aid for interpretation of the primitive equation model results.

To solve $(6.2)$ we follow the arguments of Sections 3 and 4 by separating off the vertical dependence, assuming the solution is steady in a reference frame moving eastward at speed $c$, and then taking the Fourier transform in the zonal direction. We find that $(6.2)$ reduces to

$$
\epsilon^{1/2}\left(\frac{d^{2}}{d\hat{y}^{2}} - \hat{y}^{2}\right)\hat{\psi}_m - m^{2}\hat{\psi}_m = a^{2}\hat{q}_m,
\tag{6.3}
$$

where, as before, $\hat{y} = \epsilon^{1/4}(y/a)$ is the dimensionless meridional coordinate.

We now solve $(6.3)$ by transforming in $\hat{y}$. The mathematical apparatus is simpler than in Section 4, where we introduced the vector inner product $(4.8)$ and the vector transform pair $(4.19)$ and $(4.20)$. To solve the scalar Eq. $(6.3)$ we can use the scalar transform pair

$$
\hat{\psi}_{mn} = \int_{-\infty}^{\infty}\hat{\psi}_m(\hat{y})\mathcal{H}_n(\hat{y})\,d\hat{y},
\tag{6.4}
$$

$$
\hat{\psi}_m(\hat{y}) = \sum_{n=0}^{\infty}\hat{\psi}_{mn}\mathcal{H}_n(\hat{y}).
\tag{6.5}
$$

A transform pair similar to $(6.4)$ and $(6.5)$ also exists for $\hat{q}_{mn}$, $\hat{q}_m(\hat{y})$. Note that $(6.4)$ can be obtained through multiplication of $(6.5)$ by $\mathcal{H}_{n'}(\hat{y})$, followed by integration over $\hat{y}$ and use of the orthogonality relation $(4.18)$. Multiplying $(6.3)$ by $\mathcal{H}_n(\hat{y})$ and integrating over $\hat{y}$ (i.e., taking the Hermite transform of $(6.3)$) we obtain

$$
\hat{\psi}_{mn} = -\frac{a^{2}\hat{q}_{mn}}{m^{2} + \epsilon^{1/2}(2n + 1)}.
\tag{6.6}
$$

In the derivation of $(6.6)$ we have used two integrations by parts (with vanishing boundary terms) and the fact that $\mathcal{H}_n(\hat{y})$ is an eigenfunction of the operator $(d^{2}/d\hat{y}^{2} - \hat{y}^{2})$, i.e., $(d^{2}/d\hat{y}^{2} - \hat{y}^{2})\mathcal{H}_n(\hat{y}) = -(2n + 1)\mathcal{H}_n(\hat{y})$. The simplicity of the spectral form of the invertibility principle $(6.6)$ is in fact due to this eigenfunction property of $\mathcal{H}_n(\hat{y})$.

Combining the inverse Hermite transform $(6.5)$, the inverse Fourier transform defined in $(4.2)$, and the assumed vertical structure, we obtain

$$
\psi(\xi, y, z) = Z(z)\sum_{m=-\infty}^{\infty}\sum_{n=0}^{\infty}\hat{\psi}_{mn}\mathcal{H}_n(\hat{y})\, e^{im\xi/a},
\tag{6.7}
$$

so that the physical space streamfunction field can be plotted by substituting $(6.6)$ in $(6.7)$ and then numerically evaluating the sums over $m$ and $n$. However, we would like to examine more than just the $\psi(\xi, y, z)$ field, in particular the $u_\psi(\xi, y, z)$, $v_\psi(\xi, y, z)$, and $\phi(\xi, y, z)$ fields, all of which can be determined from the $\psi$ field. Noting that $u_\psi = -\partial\psi/\partial y$, $v_\psi = \partial\psi/\partial\xi$, and $\phi = \beta y\psi$, and using the recurrence and derivative relations $(4.13)$ and $(4.14)$, we have

$$
\begin{pmatrix}u_\psi(\xi, y, z) \\ v_\psi(\xi, y, z) \\ \phi(\xi, y, z)\end{pmatrix}
= Z(z)\sum_{m=-\infty}^{\infty}\sum_{n=0}^{\infty}\frac{\hat{\psi}_{mn}}{a}
\begin{pmatrix}U_{mn}(\xi, \hat{y}) \\ V_{mn}(\xi, \hat{y}) \\ \Phi_{mn}(\xi, \hat{y})\end{pmatrix}
\tag{6.8}
$$

where

$$
\begin{pmatrix}U_{mn}(\xi, \hat{y}) \\ V_{mn}(\xi, \hat{y}) \\ \Phi_{mn}(\xi, \hat{y})\end{pmatrix}
=
\begin{pmatrix}
\epsilon^{1/4}\left[\left(\dfrac{n+1}{2}\right)^{1/2}\mathcal{H}_{n+1}(\hat{y}) - \left(\dfrac{n}{2}\right)^{1/2}\mathcal{H}_{n-1}(\hat{y})\right] \\[3mm]
im\,\mathcal{H}_n(\hat{y}) \\[3mm]
\bar{c}\epsilon^{1/4}\left[\left(\dfrac{n+1}{2}\right)^{1/2}\mathcal{H}_{n+1}(\hat{y}) + \left(\dfrac{n}{2}\right)^{1/2}\mathcal{H}_{n-1}(\hat{y})\right]
\end{pmatrix} e^{im\xi/a},
\tag{6.9}
$$

which are readily seen to be the Rossby wave approximations of $(4.11)$. To summarize, once $\hat{q}_{mn}$ is known, we can compute $\hat{\psi}_{mn}$ from $(6.6)$, and then $u_\psi(\xi, y, z)$, $v_\psi(\xi, y, z)$, $\phi(\xi, y, z)$ via numerical evaluation of $(6.8)$. For $\hat{q}_{mn}$ in $(6.6)$ we use the Rossby wave contribution to the total $q(\xi, y, z)$ field given in $(4.25)$, i.e., we set $\hat{q}_{mn} = \hat{q}_{mn0}$, the latter of which is defined in $(4.26)$. This is a reasonable approximation since the total $q(\xi, y, z)$ field is dominated by the Rossby wave contribution. Plots of $u_\psi(\xi, y, z)$, $v_\psi(\xi, y, z)$, $\phi(\xi, y, z)$ and the Rossby wave contribution to $q(\xi, y, z)$ for $y_0 = 0$ are shown in Fig. 8, while the same fields for $y_0 = 450\text{ km}$ are shown in Fig. 9. A comparison of the second panels in Figs. 8 and 9 with the second panels of Figs. 3 and 5 shows that the balanced model mass field and rotational wind field are fairly good approximations of the Rossby wave contributions to the primitive equation results, the most apparent difference being that the zonal pressure gradient force at the equator in the primitive equation model is not reproduced in the solutions of the invertibility principle.

![](./pic/Schubert2006_fig8.png)

**Fig. 8.** The top panel shows the Rossby wave contribution to the $q(\xi, y, z)$ field, while the second panel shows the $u_\psi(\xi, y, z)$, $v_\psi(\xi, y, z)$, $\phi(\xi, y, z)$ fields resulting from the solution of the invertibility principle $(6.2)$ when its right hand side is given by the PV field shown in the top panel. This figure is for $y_0 = 0$.

![](./pic/Schubert2006_fig9.png)

**Fig. 9.** Same as Fig. 8 but for $y_0 = 450\text{ km}$.

---

本節要證明的事情是：**對流包絡尾流中的風場與質量場，可以「只靠 PV」近似地還原回來**。

**推導的三個環節：**

1. **回到 PV 的定義。** 把 $(2.7)$ 改寫成 $(6.1)$，其中 $\psi$ 是旋轉流的流函數（$\nabla^{2}\psi$ 就是相對渦度）。**但 $(6.1)$ 裡同時有 $\psi$ 與 $\phi$ 兩個未知數，還不是一個可解的診斷方程。**
2. **補上一條平衡關係，把 $\phi$ 與 $\psi$ 綁在一起。** 出發點是**線性平衡關係** $\nabla\cdot(\beta y\nabla\psi) = \nabla^{2}\phi$。再加一個關鍵假設——**$\beta y$ 可視為緩變（slowly varying）**——就能把它寫成 $\nabla^{2}(\phi - \beta y\psi) = 0$；配上 $y \to \pm\infty$ 時 $\phi - \beta y\psi \to 0$ 的條件，立刻得到一個**局地（local）而非積分型**的關係：

    $$
    \phi = \beta y\psi
    $$

    **這一步是整個赤道可逆性原理的樞紐**——它把中緯度「$\phi = f\psi$」的地轉關係，直接搬到赤道 $\beta$ 平面上（$f \to \beta y$）。
3. **代回去，得到可逆性原理 $(6.2)$。** 這是一個只含 $\psi$ 與 $q$ 的**橢圓型偏微分方程**；配上邊界條件 $\psi \to 0$（$y \to \pm\infty$）與 $\partial\psi/\partial z = 0$（$z = 0, z_T$），就構成完整的可逆性原理。**知道 $q$ → 解出 $\psi$ → 旋轉風 $(u_\psi, v_\psi) = (-\partial\psi/\partial y, \partial\psi/\partial x)$、質量場 $\phi = \beta y\psi$ 全部到手。**

**求解方式比第 4 節簡單得多**：因為 $(6.3)$ 是**純量方程**，不需要向量內積 $(4.8)$，只要用純量的 **Hermite 轉換對 $(6.4)$–$(6.5)$**。關鍵技巧是——$\mathcal{H}_n(\hat{y})$ 本身就是算符 $(d^{2}/d\hat{y}^{2} - \hat{y}^{2})$ 的本徵函數：

$$
\left(\frac{d^{2}}{d\hat{y}^{2}} - \hat{y}^{2}\right)\mathcal{H}_n(\hat{y}) = -(2n + 1)\mathcal{H}_n(\hat{y})
$$

（就是量子諧振子那組本徵函數。）於是整個橢圓方程在譜空間塌縮成一行**除法**：

$$
\hat{\psi}_{mn} = -\frac{a^{2}\hat{q}_{mn}}{m^{2} + \epsilon^{1/2}(2n + 1)}
\tag{6.6}
$$

分母 $m^{2} + \epsilon^{1/2}(2n+1)$ 恆為正，**這就是「反演」的具體長相——每個譜分量只要除以一個正數即可**。它同時也告訴我們：**波數愈高（$m$、$n$ 愈大），同樣的 PV 距平能誘導出的流場愈弱**，也就是 PV 反演天生具有「平滑化」的性質。

$(6.7)$–$(6.9)$ 把譜係數轉回物理空間。值得注意的是，$(6.9)$ 的結構**正好就是 $(4.11)$ 在羅斯貝波極限下的近似**——這在數學上驗證了「可逆性原理抓的就是羅斯貝波那一支」。

**實作與驗證**：$(6.6)$ 右邊的 $\hat{q}_{mn}$ 直接取 $(4.25)$ 中**羅斯貝波的貢獻** $\hat{q}_{mn0}$（合理，因為總 PV 場本來就幾乎全是羅斯貝波）。圖 8（$y_0 = 0$）與圖 9（$y_0 = 450\text{ km}$）就是反演結果。

**結論與唯一的破綻**：把圖 8、9 的第二面板拿去對照圖 3、5 的第二面板，可以看到**平衡模式的質量場與旋轉風場，是原始方程解中羅斯貝波貢獻的相當好的近似**。而**最明顯的差異是——原始方程模式中「赤道上的緯向氣壓梯度力」，在可逆性原理的解裡完全沒有被重現**。這正呼應第 4 節 $(4.26)$ 的發現：**Kelvin 波的 PV 為零，所以任何「只從 PV 出發」的反演，都不可能把 Kelvin 波撈回來。**""")

# ---------------------------------------------------------------- 7.
CELLS.append(r"""### 7. Concluding remarks

We have used a linear, equatorial $\beta$-plane, primitive equation model as a tool to investigate the large-scale wind and mass fields around a moving heat source near the equator. Within the context of the assumed linear dynamics, these fields have been decomposed into Rossby, mixed Rossby-gravity, inertia-gravity, and Kelvin modes. The Rossby modes are responsible for the flow pattern west of the moving convective envelope, Kelvin modes for the flow pattern east of the convection, and inertia-gravity modes for the divergent flow near the convection, with mixed Rossby-gravity modes playing a minor role when the convection is centered near the equator. The potential vorticity field is almost entirely associated with the Rossby modes and has a form crudely analogous to the pair of wing-tip vortices behind a large airplane. The magnitudes of the PV anomalies trailing behind the convective region depend on $\tau_{\mathrm{p}}/\tau_{\mathrm{c}}$, the ratio of the passage time to the convective overturning time. The passage time $\tau_{\mathrm{p}}$ is large if the convection moves slowly and has large zonal extent, while the overturning time is small if the apparent heat source and surface rainfall are large. Such convection produces large PV anomalies and a large equatorial westerly wind burst in its wake. With increasing $\tau_{\mathrm{p}}/\tau_{\mathrm{c}}$ nonlinear effects become important. Although the patterns produced here by the primitive equation model are qualitatively similar to those found using the long wave approximation (e.g., [*Gill*, $1980$]; [*Heckley and Gill*, $1984$]; [*Gill and Phlips*, $1986$]; [*Phlips and Gill*, $1987$]; [*Chao*, $1987$]), they are more accurate because the long wave approximation distorts the dispersion relation for Rossby waves (e.g., Fig. 1 of [*Stevens et al.*, $1990$]).

We have also proposed an equatorial invertibility principle as a method to approximately recover the balanced wind and mass fields from the PV field. Solution of this invertibility principle confirms that the flow in the wake of an eastward-moving equatorial convective envelope is essentially described by balanced dynamics. It is interesting to note that the invertibility principle $(6.2)$ can be used as part of a complete balanced theory, i.e., it can be used in conjunction with an approximate PV equation. For example, in the context of inviscid, adiabatic flow we could consider the system

$$
\frac{\partial q}{\partial t} + \beta\frac{\partial\psi}{\partial x} = 0,
\tag{7.1}
$$

$$
\nabla^{2}\psi + \frac{\beta^{2}y^{2}}{R\Gamma}\left(\frac{\partial}{\partial z} - 1\right)\frac{\partial\psi}{\partial z} = q,
\tag{7.2}
$$

for the dependent variables $q(x, y, z, t)$ and $\psi(x, y, z, t)$. Using $(7.2)$ in $(7.1)$ we can easily obtain a single equation for $\psi(x, y, z, t)$ and then show that solutions proportional to $Z(z)\mathcal{H}_n(\hat{y})\exp\left[i(mx/a - \nu_{mn}t)\right]$ exist provided that

$$
\frac{\nu_{mn}}{2\Omega} = -\frac{m}{m^{2} + \epsilon^{1/2}(2n + 1)}.
\tag{7.3}
$$

The dimensionless Rossby wave frequencies $(7.3)$ represent an approximation of the low frequency solutions of the cubic equation $(4.10)$. The approximate Rossby wave frequencies given by $(7.3)$ are plotted as the lighter lines in Fig. 10, while the exact primitive equation frequencies given by $(4.10)$ are plotted as the darker lines. An inspection of Fig. 10 shows that the balance model Rossby wave frequencies $(7.3)$ are very good approximations to the primitive equation frequencies, with the exception of low zonal wavenumber sectoral harmonics, i.e., small $|m|$ for $n = 0$.

![](./pic/Schubert2006_fig10.png)

**Fig. 10.** The dark lines show the absolute value of the dimensionless frequencies $\nu_{mnr}/2\Omega$ ($n = 0, 1, 2, 3$) for the Rossby modes ($r = 0$), as determined from the primitive equation dispersion relation $(4.10)$. The lighter lines show the absolute value of the dimensionless frequencies $\nu_{mn}/2\Omega$ ($n = 0, 1, 2, 3$) as determined from the balanced model dispersion relation $(7.3)$.

A simple interpretation of this result is that, in the primitive equation model, the low zonal wavenumber sectoral harmonics involve a combination of gravity wave dynamics and potential vorticity dynamics, and the balance model is able to accurately capture only the potential vorticity part of the dynamics. In cases where the $n = 0$ modes are absent or only weakly forced (e.g., when $y_0 = 0$ or $y_0 \ll b_0$) one might expect that accurate simulations of the MJO wake could be obtained by simply including in $(7.1)$ the same forcing and dissipation terms that appear on the right hand side of $(2.6)$. Having constructed solutions of such a model, we found that they are not accurate approximations to the primitive equation results discussed in Section 4. The problem is not in the approximation $(7.2)$, but rather in the approximation of $\beta v$ by $\beta\partial\psi/\partial x$ in the PV equation. In other words, the problem lies in the neglect of the advection of basic state PV by the divergent part of the flow. Examples of such divergent flows are shown in the third panels of Figs. 3 and 5. The flows extend poleward of the heated region and result in PV anomalies that are stronger and extend farther poleward than in models which approximate $\beta v$ by $\beta\partial\psi/\partial x$.

In closing we note that it is possible to generalize almost all of these equatorial $\beta$-plane results to the sphere. In the spherical case the operator analogous to $\mathcal{L}$ in $(4.7)$ is more complicated, and the corresponding eigenproblem $(4.9)$ is not solvable analytically. Thus, we do not obtain an explicit cubic dispersion relation like $(4.10)$ and a closed form relation for the eigenfunctions like $(4.11)$. Rather, the eigenvalues and eigenfunctions must be computed numerically. However, excellent software for this purpose has been developed by [*Swarztrauber and Kasahara*, $1985$]. Other than the fact that the eigenvalues and eigenfunctions must be numerically tabulated, the basic solution procedure is essentially unmodified. With regard to the invertibility principle, the elliptic partial differential equation $(6.2)$ easily generalizes by expressing the Laplacian in spherical coordinates and by replacing $\beta^{2}y^{2}$ by $4\Omega^{2}\mu^{2}$, where $\mu = \sin(\text{latitude})$. Then $(6.3)$ generalizes to an ordinary differential equation involving the spheroidal wave operator ([*Abramowitz and Stegun*, $1965$], Chapter 21), so that $(6.4)$–$(6.9)$ need only slight modification, with $\mathcal{H}_n(\hat{y})$ replaced by the spheroidal wave functions. In this way we easily obtain a PV invertibility principle valid on the whole sphere, a result that is useful for a variety of purposes.

---

**全文結論的四個層次：**

**（一）波模分工的圖像。** 在線性動力的框架下，移動熱源周圍的大尺度風場與質量場，被分解成羅斯貝、混合羅斯貝–重力、慣性重力、Kelvin 四類模態，各司其職：

* **羅斯貝模態** → 對流包絡**西側**的流型；
* **Kelvin 模態** → 對流**東側**的流型；
* **慣性重力模態** → 對流**附近的輻散流**；
* **混合羅斯貝–重力模態** → 對流靠近赤道時**只扮演次要角色**。

而 **PV 場幾乎完全來自羅斯貝模態**，其形態**粗略地類比於大型飛機後方那一對翼尖渦（wing-tip vortices）**——這個比喻是全文最傳神的一句話：一個移動的擾動源，在身後拖出兩條反號的渦旋帶。

**（二）PV 尾流強度由 $\tau_{\mathrm{p}}/\tau_{\mathrm{c}}$ 決定。** 移動慢、緯向寬 → $\tau_{\mathrm{p}}$ 大；視熱源與地面降雨大 → $\tau_{\mathrm{c}}$ 小。這種對流會在尾流中造出**大的 PV 距平與強的赤道西風爆發**；而 $\tau_{\mathrm{p}}/\tau_{\mathrm{c}}$ 一大，**非線性效應也隨之重要**。

**（三）相對於長波近似的改進。** 本文原始方程模式的型態，與長波近似（Gill 1980 那條線）**定性上相似**，但**更準確**——因為**長波近似會扭曲羅斯貝波的頻散關係**。

**（四）可逆性原理可以升級成一套完整的平衡理論。** $(6.2)$ 不只是診斷工具；把它與一條近似 PV 方程 $(7.1)$ 配起來，就構成封閉系統 $(7.1)$–$(7.2)$，並得到平衡模式的羅斯貝波頻散關係 $(7.3)$：

$$
\frac{\nu_{mn}}{2\Omega} = -\frac{m}{m^{2} + \epsilon^{1/2}(2n + 1)}
$$

圖 10 把 $(7.3)$（淺線）與原始方程的精確頻率 $(4.10)$（深線）疊在一起：**兩者吻合得非常好，唯一的例外是低緯向波數的 sectoral harmonics（$n = 0$ 且 $|m|$ 小）**。作者對此的詮釋很清楚——**在原始方程模式裡，這些低波數 $n = 0$ 模態同時混著重力波動力與 PV 動力，而平衡模式只能準確抓住 PV 那一半。**

**一個誠實而重要的負面結果：** 既然 $n = 0$ 模態在 $y_0 = 0$ 或 $y_0 \ll b_0$ 時幾乎不被激發，那把 $(2.6)$ 右邊的強迫與耗散項直接搬進 $(7.1)$，是不是就能準確模擬 MJO 尾流了？**作者實際做了，答案是不行。** 而問題**不在 $(7.2)$ 這個反演近似**，**而在 PV 方程裡把 $\beta v$ 近似成 $\beta\partial\psi/\partial x$**——也就是**漏掉了「輻散風對基本態 PV 的平流」**。圖 3、5 第三面板顯示的輻散流會延伸到加熱區的極側，正是它讓 PV 距平**更強、也伸展得更往極側**。（這與第 5 節「忽略 $\beta v$ 只剩 $68\%$ 強度」是同一件事的兩個側面。）

**（五）推廣到球面。** 幾乎所有結果都可以推廣：算符 $\mathcal{L}$ 變複雜、本徵問題 $(4.9)$ 不再有解析解（要靠 Swarztrauber and Kasahara (1985) 的軟體數值求解），但**基本解法流程不變**。至於可逆性原理，只要把拉普拉斯算符寫成球座標形式、並把 $\beta^{2}y^{2}$ 換成 $4\Omega^{2}\mu^{2}$（$\mu = \sin(\text{緯度})$），$(6.3)$ 就變成含**扁球面波算符（spheroidal wave operator）**的常微分方程，$\mathcal{H}_n(\hat{y})$ 換成扁球面波函數即可——於是**得到一個在整個球面上都成立的 PV 可逆性原理**。""")

# ---------------------------------------------------------------- Appendix A
CELLS.append(r"""### Appendix A. Eigenfunctions for zonally symmetric Rossby modes

For the zonally symmetric Rossby modes (i.e., for $m = 0$, $n > 0$, $r = 0$), the eigenfunction formula $(4.11)$ is indeterminant because both $m$ and $\hat{\nu}_{0n0}$ vanish. However, orthonormal eigenfunctions are easily constructed in this case by considering $m$ as continuous and applying l'Hospital's rule for the limit $m \to 0$. The eigenfunctions for the zonally symmetric Rossby modes are then given by

$$
\mathbf{K}_{0n0}(\hat{y}) = (2n + 1)^{-(1/2)}
\begin{pmatrix}
\left[\left(\dfrac{n}{2}\right)^{1/2}\mathcal{H}_{n+1}(\hat{y}) - \left(\dfrac{n+1}{2}\right)^{1/2}\mathcal{H}_{n-1}(\hat{y})\right] \\[3mm]
0 \\[3mm]
\bar{c}\left[\left(\dfrac{n}{2}\right)^{1/2}\mathcal{H}_{n+1}(\hat{y}) + \left(\dfrac{n+1}{2}\right)^{1/2}\mathcal{H}_{n-1}(\hat{y})\right]
\end{pmatrix}.
\tag{A.1}
$$

Using $(4.18)$ it can easily be confirmed that the zonally symmetric eigenfunctions $(A.1)$ satisfy the orthonormality condition $(4.17)$. Using $(4.13)$ and $(4.14)$ it is also easily confirmed that the eigenfunctions $(A.1)$ correspond to geostrophically balanced zonal flows.

---

這一小段補的是第 4 節留下的**簡併漏洞**。對**緯向對稱的羅斯貝模態**（$m = 0$、$n > 0$、$r = 0$），$(4.11)$ 的分子與分母同時趨近零（$m \to 0$ 且 $\hat{\nu}_{0n0} \to 0$），公式失效。

**補洞的技巧很單純**：把 $m$ 暫時當作**連續變數**，對 $m \to 0$ 取極限並套用 **l'Hôpital 法則**，就得到明確的本徵函數 $(A.1)$。

$(A.1)$ 有兩個值得注意的性質：

* **第二個分量恆為零**，即 $V_{0n0} = 0$——緯向對稱模態沒有經向風 $v$，這符合直覺；
* 用 $(4.13)$、$(4.14)$ 可以驗證，這些本徵函數對應的是**地轉平衡的緯向流（geostrophically balanced zonal flows）**。

換句話說，**赤道 $\beta$ 平面上「緯向對稱的羅斯貝模態」就是定常的地轉平衡緯向噴流**——頻率為零、不傳播，這也解釋了為什麼 $\hat{\nu}_{0n0} = 0$。""")

# ---------------------------------------------------------------- Appendix B
CELLS.append(r"""### Appendix B. Normal mode transform of the heating function

Using the definition of $\hat{\mathbf{Q}}_m(y)$ given by $(4.7)$ and $(4.5)$, the inner product definition $(4.8)$, and the formula $(4.11)$ for the kernel $\mathbf{K}_{mnr}(\hat{y})$, we can write the inner product $\hat{Q}_{mnr} = (\hat{\mathbf{Q}}_m, \mathbf{K}_{mnr})$ as integrals of $\exp[-(\hat{y} - \hat{y}_0)^{2}/\hat{b}_0^{2}]\mathcal{H}_{n+1}(\hat{y})$ and $\exp[-(\hat{y} - \hat{y}_0)^{2}/\hat{b}_0^{2}]\mathcal{H}_{n-1}(\hat{y})$. These integrals can be evaluated using the following result from [*Gradshteyn and Ryzhik*, $1994$, page 843]:

$$
\int_{-\infty}^{\infty}\exp\!\left[-\frac{(\hat{y} - \hat{y}_0)^{2}}{\hat{b}_0^{2}}\right]\mathcal{H}_n(\hat{y})\,d\hat{y}
= \left(\frac{2\pi\hat{b}_0^{2}}{2 + \hat{b}_0^{2}}\right)^{1/2}\left(\frac{2 - \hat{b}_0^{2}}{2 + \hat{b}_0^{2}}\right)^{n/2}
\exp\!\left[\frac{\hat{b}_0^{2}\hat{y}_0^{2}}{(4 - \hat{b}_0^{4})}\right]\mathcal{H}_n\!\left(\frac{2\hat{y}_0}{(4 - \hat{b}_0^{4})^{1/2}}\right)
\tag{B.1}
$$

for $0 \le \hat{b}_0 < 2^{1/2}$.

---

這一小段是 $(4.22)$、$(4.23)$ 那兩條長式子的**來源**。

要算加熱項在各個赤道波模態上的投影 $\hat{Q}_{mnr} = (\hat{\mathbf{Q}}_m, \mathbf{K}_{mnr})$，就必須算「**高斯 × Hermite 函數**」的積分。作者引用 Gradshteyn and Ryzhik (1994) 的積分表得到 $(B.1)$，然後**把它用兩次**——一次代 $n \to n+1$、一次代 $n \to n-1$——就湊出 $(4.22)$ 的方括號內兩項。

$(B.1)$ 的結構本身很值得玩味：**一個「中心在 $\hat{y}_0$、寬度為 $\hat{b}_0$ 的高斯」與 $\mathcal{H}_n$ 的重疊積分，結果仍然是同一個 $\mathcal{H}_n$，只是自變數被壓縮成 $2\hat{y}_0/(4 - \hat{b}_0^{4})^{1/2}$**。這正是為什麼**對流中心的偏移量 $y_0$ 會如此直接地決定「哪些經向模態被激發」**：

* $\hat{y}_0 = 0$（對流正對赤道）時，$\mathcal{H}_n(0)$ 對**奇數 $n$ 為零**——這就是為什麼 $y_0 = 0$ 時混合羅斯貝–重力波（$n = 0$ 的那一支之外的奇模態）貢獻會消失的數學原因。
* $\hat{y}_0 \ne 0$ 時，奇模態被打開，響應才會出現南北不對稱。

適用條件 $0 \le \hat{b}_0 < 2^{1/2}$ 則限制了對流的無因次經向寬度——本文的 $b_0 = 450\text{ km}$ 遠在這個範圍內。""")

if __name__ == "__main__":
    n = append("a_paper.jsonl", CELLS)
    print("paper_04 -> a_paper.jsonl  cells=%d" % n)
