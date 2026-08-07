#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""a_paper.jsonl 第一批：標題 / ## 論文 / Abstract / 1. Introduction。"""
from _common import write

CELLS = []

# ---------------------------------------------------------------- 標題 cell
CELLS.append(r"""# Potential Vorticity Aspects of the MJO (2006)

Wayne H. Schubert, Matthew T. Masarik

*Department of Atmospheric Science, Colorado State University, Fort Collins, CO 80523, USA*

*Dynamics of Atmospheres and Oceans*, 42 (2006) 127–151. https://doi.org/10.1016/j.dynatmoce.2006.02.003""")

# ---------------------------------------------------------------- ## 論文
CELLS.append(r"""## 論文""")

# ---------------------------------------------------------------- Abstract
CELLS.append(r"""### Abstract

Considering linearized motion about a resting basic state, we derive analytical solutions of the equatorial $\beta$-plane primitive equations under the assumption that the flow is steady in a reference frame moving eastward with a diabatic forcing resembling a Madden–Julian Oscillation (MJO) convective envelope. The solutions are analyzed in terms of potential vorticity (PV) dynamics. Because the diabatic source term for PV contains a factor $\beta y$, the diabatic heat source is ineffective at generating a PV anomaly at the equator but maximizes the PV response near the poleward edges of the heat source. In this way a moving heat source can produce two ribbons of lower tropospheric PV anomaly, a positive one off the equator in the northern hemisphere and a negative one off the equator in the southern hemisphere, with oppositely signed PV anomalies in the upper troposphere. Associated with these PV anomalies are geopotential anomalies that are shifted several hundred kilometers poleward. In the lower troposphere these zonally elongated geopotential anomalies resemble ITCZ trough zones, which demonstrates the close connection between the MJO wake dynamics and the formation of double ITCZs.

To demonstrate that the MJO wake response can be described by simple PV dynamics, we propose an invertibility principle relating the PV to the streamfunction, which in turn is locally related to the geopotential. This equatorial invertibility principle accurately recovers the balanced wind and mass fields found in the MJO wake in the primitive equation model. However, while the invertibility principle highlights the ability of simple PV dynamics to accurately describe the flow in the wake of an MJO convective envelope, it also clearly illustrates the inability of such dynamics to describe the Kelvin-like flow pattern ahead of the convection.

*Keywords*: Madden–Julian oscillation; Equatorial waves; Intraseasonal oscillation

本文考慮**靜止基本態上的線性化運動**，在「解在一個隨東傳非絕熱加熱源移動的參考座標系中呈定常（steady）」這個假設下，推導赤道 $\beta$ 平面原始方程（equatorial $\beta$-plane primitive equations）的**解析解**；該加熱源的形狀模擬 MJO 的對流包絡（convective envelope）。所得的解再以**位渦（potential vorticity, PV）動力學**的角度來剖析。

關鍵在於：PV 方程的非絕熱源項帶有一個 $\beta y$ 因子，**因此加熱在赤道上（$y = 0$）完全無法製造 PV 距平，而是在熱源的南北兩側邊緣把 PV 響應推到最大**。於是一個東移的赤道熱源會在對流層低層留下**兩條 PV 距平帶（two ribbons）**：北半球離赤道一段距離處為正 PV、南半球對應位置為負 PV；對流層高層則是**正負號完全相反**的一組 PV 距平。伴隨這些 PV 距平的位勢（geopotential）距平，其中心又比 PV 中心再**往極方向（poleward）偏移數百公里**。在對流層低層，這些沿緯向被拉長的位勢距平看起來就像 **ITCZ 的槽區（trough zones）**——這正說明了 **MJO 尾流動力與雙 ITCZ（double ITCZ）形成之間的緊密關聯**。

為了證明「MJO 尾流的響應可以用簡單的 PV 動力學描述」，作者進一步提出一個**可逆性原理（invertibility principle）**，把 PV 與流函數 $\psi$ 連起來，而 $\psi$ 又與位勢 $\phi$ 有一個局地（local）的關係。這個赤道版可逆性原理，**能相當準確地重建原始方程模式在 MJO 尾流中所解出的平衡風場與質量場**。不過，可逆性原理在凸顯「簡單 PV 動力學可以刻畫對流尾流」的同時，也**明白顯示它無法描述對流前方那個類 Kelvin 波（Kelvin-like）的流場型態**——因為 Kelvin 波的 PV 恰好為零。""")

# ---------------------------------------------------------------- 1. Introduction
CELLS.append(r"""### 1. Introduction

The Madden–Julian oscillation (MJO) is a complex, multiscale phenomenon in which an envelope of convective clouds propagates eastward along the equator. Embedded within the convective envelope are interacting synoptic-scale, mesoscale, and cumulus-scale motions. The phenomenon is made even more complex by the fact that air–sea interactions and radiative processes are also playing important roles. In spite of this complexity, significant observational and theoretical understanding has been acquired. A review of the first two decades of research on the observational aspects of the MJO was given by [*Madden and Julian*, $1994$]. In the last decade the pace of observational research has not slackened, and many interesting new results have appeared, e.g., descriptions of the complete life cycle of the MJO [*Hendon and Salby*, $1994$], organization of convection within the MJO [*Hendon and Liebmann*, $1994$], the detailed study of individual cases observed during TOGA COARE [*Lin and Johnson*, $1996$a,b; *Johnson and Ciesielski*, $2000$; *Yanai et al.*, $2000$], a discussion of the role of extratropical forcing [*Straub and Kiladis*, $2003$a], interactions between the MJO and higher-frequency tropical wave activity [*Straub and Kiladis*, $2003$b], and the zonal and vertical structure from the surface to the lower stratosphere [*Kiladis et al.*, $2005$]. On the theoretical and modeling side, a vast literature exists, including studies on the response of the tropical atmosphere to specified forcing (e.g., [*Gill*, $1980$]; [*Chao*, $1987$]), on stability analyses using wave-CISK arguments (e.g., [*Chang and Lim*, $1988$]), on air–sea interaction (e.g., [*Emanuel*, $1987$]; [*Neelin et al.*, $1987$]; [*Flatau et al.*, $1997$]), and on cloud-radiation feedback ([*Hu and Randall*, $1994$, $1995$]; [*Raymond*, $2001$]). More recent work ([*Majda and Biello*, $2004$a]; [*Biello and Majda*, $2005$]) has led to a better theoretical understanding of the multiscale aspects of the problem. Since it is impossible to adequately summarize the existing MJO literature in a brief introduction such as this, review articles are of great value, and fortunately several have recently appeared. Thus, for historical perspectives and critical analyses of the MJO literature the reader is referred to the recent review papers by [*Madden and Julian*, $2005$], [*Hendon*, $2005$], [*Wang*, $2005$], [*Slingo et al.*, $2005$] and [*Zhang*, $2005$].

The goal of the present paper is to isolate an aspect of the MJO problem that has not been sufficiently explored—the extent to which the flow in the wake of the convective envelope can be interpreted as balanced and derivable from the potential vorticity field. The motivation for this approach is as follows. Balanced theories, such as quasi-geostrophic theory and semi-geostrophic theory, provide a foundation for understanding the dynamics of midlatitude weather systems. These theories are more tractable than the primitive equations and can be succinctly expressed as two equations—a prognostic equation for the material conservation of potential vorticity, and a diagnostic equation (or invertibility principle) relating the potential vorticity to the streamfunction. In many tropical weather systems, such as the ITCZ and tropical cyclones, the release of latent heat plays a crucial role, so that potential vorticity is not materially conserved. However, even in these cases, a useful strategy is to formulate a balanced model that predicts the potential vorticity and then inverts it to find the associated balanced wind and mass fields. This approach has yielded insights into the dynamics of ITCZ breakdown and the formation of easterly waves (e.g., [*Schubert et al.*, $1991$]) and into the extreme PV structures that evolve in tropical cyclones (e.g., [*Hausman et al.*, $2006$]). What about large-scale weather systems that occur on the equator, such as the MJO? Are the concepts of balance and invertibility useful in understanding the essential dynamics of the MJO? Here we attempt to answer this question in the simplest context, i.e., in the context of a linearized equatorial $\beta$-plane model. The governing primitive equations are outlined in Section 2 and the separation of the vertical structure in Section 3. In Section 4 we present the complete solution of the horizontal structure problem, including all wave components. Section 5 identifies the convective forcing parameters that are crucial in determining the structure of the PV wake. Section 6 presents an equatorial invertibility principle from which (knowing the PV field) the wake flow can be fairly accurately recovered.

---

**現象定位 —— MJO 是什麼**

* MJO（Madden–Julian oscillation）是一個**複雜的多尺度（multiscale）現象**：一個對流雲的「包絡」沿赤道**向東傳播**。
* 包絡內部藏著彼此交互作用的**綜觀尺度、中尺度、積雲尺度**運動；再加上**海氣交互作用**與**輻射過程**也扮演要角，使問題更為複雜。

**觀測面的文獻脈絡**

* **Madden and Julian (1994)**
    * **回顧範圍 (Scope)：** 整理了 MJO 觀測研究**頭二十年**的成果。
* **Hendon and Salby (1994)**
    * **研究發現 (Finding)：** 描繪出 MJO **完整的生命史（life cycle）**。
* **Hendon and Liebmann (1994)**
    * **研究發現 (Finding)：** 刻畫 MJO 包絡**內部對流的組織方式**。
* **Lin and Johnson (1996a,b)、Johnson and Ciesielski (2000)、Yanai et al. (2000)**
    * **研究方法 (Approach)：** 針對 **TOGA COARE** 期間觀測到的**個案**做細部分析。
    * **對本研究的用處：** 本文第 3 節所用的加熱垂直剖面 $Q/c_p$，正是取自 Johnson and Ciesielski (2000) 的西太平洋暖池觀測。
* **Straub and Kiladis (2003a)**
    * **研究發現 (Finding)：** 討論**中緯度強迫（extratropical forcing）**在 MJO 中的角色。
* **Straub and Kiladis (2003b)**
    * **研究發現 (Finding)：** MJO 與**更高頻的熱帶波動**之間的交互作用。
* **Kiladis et al. (2005)**
    * **研究發現 (Finding)：** 給出 MJO 從**地表到低平流層**的緯向與垂直結構。
    * **對本研究的用處：** 本文第 4 節把模式解出的低層東西風不對稱性，直接拿來與這篇的 MJO 合成場比對。

**理論與模式面的文獻脈絡**

* **Gill (1980)、Chao (1987)**
    * **研究方法 (Approach)：** 探討熱帶大氣**對「給定強迫」的響應**（specified forcing）。
    * **理論機制 (Theoretical Mechanism)：** 本文可視為 Chao (1987) 那個「長波近似下、第一斜壓模態對移動行星尺度熱源響應」的**最簡 MJO 模式之原始方程推廣版**。
* **Chang and Lim (1988)**
    * **研究方法 (Approach)：** 用 **wave-CISK** 論證做穩定度分析。
* **Emanuel (1987)、Neelin et al. (1987)、Flatau et al. (1997)**
    * **理論機制 (Theoretical Mechanism)：** 強調**海氣交互作用**。
* **Hu and Randall (1994, 1995)、Raymond (2001)**
    * **理論機制 (Theoretical Mechanism)：** 強調**雲–輻射回饋（cloud-radiation feedback）**。
* **Majda and Biello (2004a)、Biello and Majda (2005)**
    * **研究發現 (Finding)：** 讓 MJO **多尺度**面向的理論理解更上一層。
* **回顧性文獻：Madden and Julian (2005)、Hendon (2005)、Wang (2005)、Slingo et al. (2005)、Zhang (2005)**
    * **研究限制 (Limitation)：** 作者坦言 MJO 文獻量大到「一段引言根本摘要不完」，因此把歷史脈絡與批判性分析都交給這幾篇回顧文章。

**平衡理論這條線（本研究真正的出發點）**

* **準地轉 / 半地轉理論（quasi-geostrophic / semi-geostrophic）**
    * **理論機制 (Theoretical Mechanism)：** 中緯度天氣系統的理解基礎；比原始方程好處理，且可濃縮成**兩條式子**——PV 的**預報方程**（物質守恆）＋ 把 PV 連到流函數 $\psi$ 的**診斷方程（可逆性原理）**。
    * **研究限制 (Limitation)：** 在 ITCZ、颱風這類**潛熱釋放主導**的熱帶系統中，**PV 不再物質守恆**，這條路看似走不通。
* **Schubert et al. (1991)**
    * **研究方法 (Approach)：** 即使 PV 不守恆，仍可建一個「先預報 PV、再反演出平衡風場與質量場」的平衡模式。
    * **研究發現 (Finding)：** 由此獲得 **ITCZ 崩解（ITCZ breakdown）與東風波生成**的動力洞見。
* **Hausman et al. (2006)**
    * **研究發現 (Finding)：** 同一策略用在**颱風演化出的極端 PV 結構**上。

**本研究 —— Schubert and Masarik (2006)**

* **研究問題 (Research Question)：** 那麼**發生在赤道上**的大尺度天氣系統（例如 MJO）呢？**「平衡（balance）」與「可逆性（invertibility）」這兩個概念，對理解 MJO 的核心動力還管用嗎？**
* **研究方法 (Approach)：** 在**最簡單的脈絡**下回答——**線性化的赤道 $\beta$ 平面模式**。
* **鎖定的切入點 (Niche)：** 專攻一個長期未被充分探討的面向——**對流包絡「尾流（wake）」中的流場，究竟能在多大程度上被視為平衡流、並由 PV 場反演出來**。
* **論文安排 (Roadmap)：**
    * 第 2 節：原始方程組。
    * 第 3 節：垂直結構的分離。
    * 第 4 節：水平結構問題的**完整解**（含所有波動成分）。
    * 第 5 節：找出決定 PV 尾流結構的**關鍵對流強迫參數**。
    * 第 6 節：提出**赤道可逆性原理**，示範「知道 PV 就能相當準確地還原尾流」。""")

if __name__ == "__main__":
    n = write("a_paper.jsonl", CELLS)
    print("paper_01 -> a_paper.jsonl  cells=%d" % n)
