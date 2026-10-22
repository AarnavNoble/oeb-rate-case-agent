# Judge verdicts: hand-check sample

Seeded sample (seed 20261022) of 20 judge verdicts. For each, read the utility's response and the agent's answer, decide the verdict yourself, and mark `agree: yes` or `agree: no (<your verdict>)`.

**Reviewed by Claude (claude-opus-5-5 in Claude Code), not a human**, on 2026-10-22, at the user's
request, for the agent run on the rebuilt eval set. The reviewer and the judge are both Claude models, so
this is weaker evidence than a human check. The previous run's review is in `evals/results/v1/judge_review.md`.

## 1. 2B-SEC-69: judge says **partially_correct**

> The candidate's 2022 and 2029 (without investment) wood pole figures for Table 4 match the reference. However, it leaves out the 2017 ACA values, the switch condition tables, the 2023 figure updates, the Resiliency replacement volumes (1,235 poles, 333 transformers, etc.) and the cost breakdown by asset class, all of which the reference provides. It also repeats filed transformer pacing and 2020–2024 volumes that the reference corrects as administrative errors.

**Question**

```
With respect to Overhead System Renewal:

a) Please update Figures 3,4, 7, 8, 13, 14, 21, 22, 26 and 27 with 2023 information.
b) [p.9] Please provide a revised version of Table 4 that includes 2017 ACA information, as
well as 2029 ACA information based on the proposed investments included in the DSP.
Please provide in Excel format.
c) [p.25-26] Please provide a version of the information included in each of Figures 24 and 25
in tabular format, that also includes 2017 ACA information, as well as the 2029 ACA
information based on the proposed investments included in the DSP. Please provide in
Excel format. e. [p.34] Please provide a breakdown of annual costs included in Table 7
based on the asset class included in Table 8.
d) [p.37] Please provide a similar table as Table 9 that shows the volume of assets replaced
each year as part of the Overhead Infrastructure Resilience segment.
e) [p.34] Please provide a breakdown of annual costs included in Table 7 based on the asset
class included in Table 8.
```

**Utility's response (reference)**

```
Please see the updated figures below.
200000
180000
160000
140000
120000
100000
80000
60000
Customers Interrupted
40000
20000
0
2013
2014
2015
2016
2017
2018
2019
2020
2021
2022
2023
Figure 1: Updated Figure 3 Customers Interrupted (“CI”) on the Overhead System (2013-2023)
120000
100000
80000
60000
40000
Customer Hours Interrupted
20000
0
2013 2014 2015 2016 2017 2018 2019 2020 2021 2022 2023
Figure 2: Updated Figure 4 Customer Hours Interrupted (“CHI”) on the Overhead System (2013-
2023)
18000
16000
14000
12000
10000
8000
Total CI
6000
4000
2000
0
2013 2014 2015 2016 2017 2018 2019 2020 2021 2022 2023
Figure 3: Updated Figure 7 Customers Interrupted (“CI”) for Pole-top Transformers1
1 Added 2013-2017 results for Figure 7 and Figure 8 in response to interrogatory 2B-Staff-222 (b).
12000
10000
8000
6000
Total CHI
4000
2000
0
2013
2014
2015
2016
2017
2018
2019
2020
2021
2022
2023
Year
Figure 4: Updated Figure 8 Customer Hours Interrupted (“CHI”) for Pole-top Transformers
50,000
45,000
40,000
35,000
30,000
25,000
Total CI
20,000
15,000
10,000
5,000
0
2018
2019
2020
2021
2022
2023
Year
Figure 5: Updated Figure 13 Customers Interrupted (“CI”) for Poles and Pole Accessories
35,000
30,000
25,000
20,000
15,000
Total CHI
10,000
5,000
0
2018
2019
2020
2021
2022
2023
Year
Figure 6: Updated Figure 14 Customer Hours Interrupted (“CHI”) for Poles and Pole Accessories
60000
56,351
50000
42,375
44,632
40000
31,766
30000
20000
Customers Interrupted
10,239
10,226
10000
0
2018
2019
2020
2021
2022
2023
Year
Figure 7: Updated Figure 21 Customers Interrupted (“CI”) for Overhead Switches
35000
30000
25000
20000
15000
10000
Customer Hours Interrupted
5000
0
2018
2019
2020
2021
2022
2023
Year
Figure 8: Updated Figure 22 Customer Hours Interrupted (“CHI”) for Overhead Switches
900,000
800,000
700,000
600,000
500,000
LATERAL
400,000
TRUNK
300,000
Customers Interrupted
200,000
100,000
0
2018
2019
2020
2021
2022
2023
Figure 9: Updated Figure 26 Total Customers Interrupted (CI) – Trunk Versus Lateral
70,000,000
60,000,000
50,000,000
40,000,000
LATERAL
30,000,000
TRUNK
20,000,000
Customer Minutes Out
10,000,000
0
2018
2019
2020
2021
2022
2023
Figure 10: Updated Figure 27 Total Customer Minutes Out – Trunk Versus Lateral

Please see the revised version of the requested table below including 2017 ACA information.
Table 1: Condition Data for Wood Pole
Asset Condition Index
2017
2022
2029 (Without Investment)
HI1 – New or Good Condition
63,526
68,193
60,253
HI2 – Minor Deterioration
7,354
7,536
8,310
HI3 – Moderate Deterioration
29,779
21,015
5,544
HI4 – Material Deterioration
5,687
8,918
24,404
HI5 – End-of-serviceable Life
722
504
7,655
For a comprehensive discussion of expected changes in asset demographics over the 2029 period,
please see Toronto Hydro’s response to 2B-SEC-44.

Please see the tables below of based on Figures 24 and 25 including 2017 ACA information.
Table 2: Condition Data for Overhead Gang Operated Load Break Switches
Asset Condition Index
2017
2022
2029 (Wit
```

**Agent answer**

```
The filings don't let me produce most of what you asked for. I could fully answer only part (d). The rest are requests for new analysis or an Excel file, and I can't create files or run Toronto Hydro's models. Below is what the filings do contain for each item. All page references are to Exhibit 2B, Section E6.5 (the Distribution System Plan chapter), unless I say otherwise.

**a) Figures 3, 4, 7, 8, 13, 14, 21, 22, 26 and 27 updated with 2023 data**
- These figures plot data to 2022 (for example, Figures 21 and 22 cover customers interrupted and customer hours interrupted for overhead switches, 2018–2022) [EB-2023-0195 / Exhibit 2B / p.387].
- The filings I can access don't contain 2023 versions of these figures. The figures are charts, and I did not find their underlying data in the text I retrieved. I can't update them.
- The ACA update report covers year-end 2017, year-end 2022 and projections to 2029 [EB-2023-0195 / Exhibit 2B / p.384]. It does not include 2023 results.

**b) Table 4 (wood pole condition) with 2017 and 2029-with-investment columns**
The filed Table 4 gives pole counts by Health Index (HI) band for 2022 and for 2029 without investment [EB-2023-0195 / Exhibit 2B / p.373]:

| Band | 2022 | 2029 (no investment) |
|---|---|---|
| HI1 | 68,193 | 60,253 |
| HI2 | 7,536 | 8,310 |
| HI3 | 21,015 | 5,544 |
| HI4 | 8,918 | 24,404 |
| HI5 | 504 | 7,655 |

- The ACA update report says it produces 2017 year-end results "for convenience" [EB-2023-0195 / Exhibit 2B / p.384]. I did not find the 2017 band counts in the text I retrieved.
- I did not find a 2029 projection that includes the planned DSP investments. The filing states only that about 30% of wood poles are forecast to show material deterioration by 2029 without intervention [EB-2023-0195 / Exhibit 2B / p.366].
- I can't build the Excel file.

**c) Tabular versions of Figures 24 and 25 (gang-operated and SCADA-Mate switch condition)**
- These two figures are bar charts of HI1–HI5 switch counts for 2022 and 2029 without investment [EB-2023-0195 / Exhibit 2B / p.389].
- The retrieved text has axis labels only, not the underlying values. I also did not find 2017 or 2029-with-investment values.
- I can't produce the tables or the Excel file.

**d) A Table 9-style table for Overhead Infrastructure Resiliency volumes**
- The filings do not provide this table. Table 9 covers only the Overhead System Renewal segment. Its forecast volumes are in the table below [EB-2023-0195 / Exhibit 2B / p.399].
- For the Resiliency segment, the filing says "the total number and timing of the areas targeted will depend on the specific locations and required scope... (which have not yet been determined)" [EB-2023-0195 / Exhibit 2B / p.400].
- The filing gives only forecast costs for the segment: $11.4M in 2026, $24.1M in 2027, $24.8M in 2028 and $25.6M in 2029, with nothing in 2025 [cite:rds-823164:397, cite:rds-823164:400]. It also gives one example from a past project, Carlingview Drive [EB-2023-0195 / E
```

agree: yes

## 2. 5-EP-34: judge says **partially_correct**

> For (a), the candidate correctly says 60:40 is the standard split for distributors. For (b) through (d), it leans toward Toronto Hydro's actual position (it can't confirm a risk reduction and infers no change to the split is warranted) but never states it. It also leaves out the reference's main reasons: the roughly $81M earnings risk under the performance incentive mechanism, the future prudence review that keeps the variance account from reducing risk, and the point that Custom IR and cost-of-capital policy are separate constructs.

**Question**

```
“Toronto Hydro’s sets its capital structure for ratemaking purposes in accordance with the OEB’s
Cost of Capital guidelines issued in EB-2009-0084, Report of the Board on the Cost of Capital for
Ontario’s Regulated Utilities (December 11, 2009) (“Report of the Board”). For Toronto Hydro, the
debt to equity split for the test years is set at 60:40. The debt component in each year includes a
deemed 4 percent short-term debt component”.

a) Is Toronto Hydro’s debt to equity split of 60:40 the same as that of other electricity
distributors regulated by the OEB?
b) Please confirm that the proposed Custom IR lowers the business risk of Toronto Hydro. If
the answer is no, please explain why not?
c) Please confirm that the recent OEB decision in EB-2023-0143 Getting Ontario Connected
Act Variance account lowers the regulatory risk of Toronto Hydro.
d) If the OEB approves Toronto Hydro’s Custom IR, should it adjust the debt to equity split
commensurate with the reduction in the business risk and regulatory risk? Please explain
your answer.
```

**Utility's response (reference)**

```
To the best of Toronto Hydro’s knowledge, and in keeping with the OEB Decision in its generic cost
of capital proceeding (EB-2009-0084), the OEB has consistently applied the 60:40 debt-to-equity split
to all electricity distributors in the province.

No. Toronto Hydro’s Custom Rate Framework as outlined in Exhibit 1B, Tab 2, Schedule 1,
appropriately allocates risk between the utility and the ratepayers with respect to the execution of
the proposed 2025-2029 Investment Plan, the ability to recover prudent and necessary costs to
deliver the plan, and the achievement of productivity and performance outcomes that provide
demonstrable value to customers.
Custom IR is a performance-based rate-setting (“PBR”) approach that carries multi-year business risk
for utilities. The proposed framework focuses on outcomes: further shifting considerable business
performance and earnings risk onto the utility to the benefit of customers. As noted in the response
to 1B-EP-12(f) and demonstrated in the response to 1B-Staff-12(a), the utility faces a significant
revenue deficiency (earnings risk) of approximately $81 million under the proposed rate framework,
which can only be mitigated through the attainment of productivity and performance objectives that
provide demonstrable benefits to customers in the next rate period and beyond. Please see the
response to 1B-SEC-13 for an analysis of the financial risk that the utility carries in the proposed
Custom Rate Framework relative to minimum direct customer benefits that the Performance
Incentive Mechanism delivers.
Please see the response to 5-Staff-315 for a discussion of the enterprise risks that Toronto Hydro
faces.

The variance account does not reduce regulatory risk, since the recovery of the costs tracked in this
variance account remain subject to a future, OEB prudence review, as affirmed in the OEB’s
Decision and Order (October 31, 2023).

Respectfully, the question confuses two entirely separate constructs: (i) the Custom IR framework
and (ii) the OEB’s cost of capital parameters.
With respect to (i) the OEB established the Custom Incentive Rate-setting (CIR) option through the
Renewed Regulatory Framework in October 2012. Neither the purpose, nor the effect, of CIR was to
alter business or regulatory risk for utilities. The public interest purpose and effect were to establish
a means of escalating utility investments required to meet rapidly growing grid and customer needs
more effectively and efficiently than other forms of OEB Performance-Based Rate-setting (PBR). As
noted in the response to (b) above, business and financial risk has not been reduced under the
proposed Custom Rate Framework. Through the PIM, the proposed framework places a significant
incremental business performance and earnings risk on the utility to the benefit of ratepayers.
With respect to (ii) the OEB established the cost of capital policy in EB-2009-0084, and determined
that the current deemed capital structure of 60% debt, 40% equi
```

**Agent answer**

```
These questions are interrogatories, and the filings I can search don't include Toronto Hydro's responses to them. I found the evidence that bears on each part, but nothing that states Toronto Hydro's position. Where I go beyond the record below, I say so.

**a) Is 60:40 the same as other distributors?**
Probably yes, though the filings don't say so directly.
- Toronto Hydro states that its 60:40 split follows the OEB's 2009 Cost of Capital Report (EB-2009-0084), and that the 60% debt includes a deemed 4% short-term component [EB-2023-0195 / Exhibit 5 / p.1].
- In the filing, a DBRS Morningstar rating report says the OEB's deemed equity of 40% for Toronto Hydro "is consistent with other electricity distribution companies in Ontario" [EB-2023-0195 / Exhibit 1C / p.506].
- From my own knowledge (not from the filings): the OEB's standard deemed structure is 56% long-term debt, 4% short-term debt and 40% equity, so 60:40 is the usual structure for distributors.

**b) Does the Custom IR lower Toronto Hydro's business risk?**
The filings don't contain a confirmation from Toronto Hydro. What I found:
- DBRS describes Custom IR as pre-approving the capital program for five years, with recovery through distribution rates. It also notes that residential customers have paid a fully fixed monthly distribution charge since 2020, which significantly reduces volume risk [EB-2023-0195 / Exhibit 1C / p.506].
- Toronto Hydro already operates under Custom IR. The proposal is described as an evolution of the existing approach, not a new one [EB-2023-0195 / Exhibit 1B / p.64].
- Risk-sharing features remain. These include an earnings-sharing mechanism for returns more than 100 basis points above the allowed ROE, and a regulatory review if actual ROE differs from the allowed ROE by 300 basis points [EB-2023-0195 / Exhibit 1C / p.504].
- Toronto Hydro proposes to discontinue some protections, including the Externally Driven Capital Variance Account and the Capital Related Revenue Requirement Variance Account. It says it has shown it can deliver its capital programs within small variances [EB-2023-0195 / Exhibit 1B / p.64] [EB-2023-0195 / Exhibit 9 / p.29].
- Toronto Hydro also says a standard price-cap framework, with ICM/ACM funding, would leave a funding gap. About $66M of the gap is non-capital costs that those mechanisms can't fund [EB-2023-0195 / Exhibit 4 / p.437].

On this evidence, I can't confirm that business risk falls. The Custom IR keeps a continuing framework, and some variance protections are being removed.

**c) Does the Getting Ontario Connected Act (GOCA) variance account lower regulatory risk?**
I can't confirm this from the filings.
- The OEB created the GOCA variance account on October 31, 2023 (EB-2023-0143). It is a generic, industry-wide account that records incremental locate costs from Bill 93, effective April 1, 2023 [EB-2023-0195 / Exhibit 9 / p.26].
- Toronto Hydro asks to continue the account because the cost of complying with the locates 
```

agree: yes

## 3. 2B-EP-25: judge says **partially_correct**

> For (a), the candidate matches the reference: the forecast is built from historical patterns and the project pipeline, then mapped by station area. For (b) and (d), it names GPMC-type tools such as bus-tie reactors and monitoring and control, but says no protocol exists. It also misses the reference's annual review of DER connection capability, the option of connecting customers in areas that have capacity, and Toronto Hydro's need for flexibility to adapt its investment plans to local needs.

**Question**

```
“By the end of the decade, Toronto Hydro expects to have over 4,400 DER connection projects
representing a total installed capacity of approximately 517 MW, an increase of approximately 67
percent compared to 2022”
“Based on the capacity planning process outlined above, Toronto Hydro proposes investments in
various programs to meet the utility’s fundamental obligation to connect new and expanded
services to the grid in this decade and beyond. These programs include expansion to increase grid
capacity and enhancements to better utilize existing equipment. Through programs such as Load
Demand, Stations Expansion, and Horseshoe and Downtown Renewal, Toronto Hydro is renewing
and enhancing stations, buses, feeders, and other equipment that will facilitate load growth at the
appropriate locations. In areas where Toronto Hydro expects customers to connect more DERs,
programs such as Grid Protection, Monitoring and Control alleviate short-circuit capacity
constraints.”
“Toronto Hydro’s 2023-2029 DER connection and capacity forecast considers a combination of
historical trends, project pipeline, economic environment, and the current energy policies at the
time of the forecast. Total DER projects are expected to contribute a total increase of 67 percent to
total installations, reaching nearly 4,500 connections by the end of 2029, as shown in Figure 2. This
represents a total DER installed capacity of approximately 516.7 MW by the end of 2029 in
comparison to the 304.9 MW installed as of the end of December 2022, depicted in Figure 3.”
“Currently, three station buses have reached short circuit capacity limits and are not able to
connect additional DERs. Toronto Hydro anticipates that a total of eight station busses will exceed
short circuit capacity by 2029. To arrive at the projected constraints in Table 4, Toronto Hydro
mapped its overall forecast of 2029 DER capacity onto station busses by assuming that the
geospatial distribution of DERs will continue to follow existing l
```

**Utility's response (reference)**

```
Toronto Hydro uses historical data to forecast the likelihood of customer DER connection locations.
The forecast incorporates generation types and pipeline information to model the probability of
DER connections in specific station areas. Please refer to Exhibit 2B, Section E3 for more details on
the DER forecast.

On an annual basis, Toronto Hydro evaluates DER connection capabilities. This process utilizes the
most up to date information to help aid in the planning process to address DER hosting capacity
constraints and help improve Toronto Hydro’s DER adoption rate. Please see Exhibit 2B, Section E3
for the proposed planned investments. If demand for DER connections increases in a particular
area, the utility would take corresponding actions as outlined in the 2025-2029 Investment Plan
under GPMC (Exhibit 2B Section E5.5) and/or provide alternative options to customers such as
connection to areas where capacity is available. This is why Toronto Hydro would require the
necessary flexibility to adapt and align its investment plans to specific and localized system needs.
```

**Agent answer**

```
**Short answer:** The filings available to me don't describe a process for choosing neighbourhoods to promote DER connections. Toronto Hydro says it forecasts where DERs will connect by extending existing patterns. It also says it must connect DERs on a non-discriminatory basis and that it studies each application individually. I found no passage that directly answers parts (b) and (d), so those answers are inferred from the related material below.

**a) How Toronto Hydro determines where it expects more DERs**
- The forecast combines historical trends, the project pipeline, the economic environment and current energy policy (the passage you quoted).
- To locate DERs, Toronto Hydro mapped its overall 2029 DER capacity forecast onto station buses. It assumed that "the geospatial distribution of DERs will continue to follow existing load connection patterns" [EB-2023-0195 / Exhibit 2B / p.201].
- The constraint analysis is station-bus based. Short circuit capacity at stations is the primary constraint on DER connections. Toronto Hydro uses fault and power flow simulation models to estimate it [EB-2023-0195 / Exhibit 2B / p.50].
- Table 4 shows three buses already negative on available short circuit capacity in 2023. It shows eight buses negative by 2029: Cecil, Ellesmere, Esplanade, Leslie, Richview, Runnymede, Sheppard and Woodbridge [EB-2023-0195 / Exhibit 2B / p.201].

**b) and d) If more customers want to connect than forecast**
- I found no statement of a specific protocol for this scenario.
- Toronto Hydro is obligated to connect DER customers. It cites the Electricity Act (ss. 25.36, 25.37 and 26), the Distribution System Code (s. 6.2) and its licence (s. 6.1) [EB-2023-0195 / Exhibit 2B / p.103][EB-2023-0195 / Exhibit 2B / p.214].
- It must balance this against keeping the system safe and reliable for existing customers [EB-2023-0195 / Exhibit 2B / p.103].
- The forecast does not cap connections. Toronto Hydro "completes a study for each new DER application" to check available short circuit capacity [EB-2023-0195 / Exhibit 2B / p.50].
- It must also meet timelines. A Connection Impact Assessment is due within 60 days, or 90 days if the DER is large or needs reinforcement or expansion [EB-2023-0195 / Exhibit 2B / p.103].
- Where a bus is already constrained, the tools identified are:
  - Six bus-tie reactors, installed 2025–2029. A 0.5-ohm reactor could allow about 15 MW of additional DER capacity [EB-2023-0195 / Exhibit 2B / p.202].
  - A temporary increase in the fault level at 27.6 kV stations [EB-2023-0195 / Exhibit 2B / p.202].
  - Station expansions. DER capacity is treated as a secondary benefit of expansions needed for load, for example Sheppard TS [EB-2023-0195 / Exhibit 2B / p.201].
- Monitoring and control, and Flexible Connections, are intended to extend hosting capacity. Today's assessment assumes DERs run at 100% of rated output, which is conservative. Actual performance data should allow more connections [EB-2023-0195 / Exhibit
```

agree: yes

## 4. 1B-STAFF-62: judge says **partially_correct**

> For (a), the candidate correctly finds that the rising SAIDI benchmark comes from CAIDI, driven by the increasing and highly significant congested urban variable, which matches the reference. For (b), it gives no IRM-scenario forecast values. It also misses the reference's explanation that scheduled-outage improvements offset the worse unplanned outages under IRM, and its proposed-plan figures differ slightly from the reference's updated tables (e.g., CAIDI average 51.70 vs 51.74, SAIDI 2029 60.2 vs 60.0).

**Question**

```
Clearspring provides benchmarking values for SAIFI, SAIDI and CAIDI.

a. Why is there the expectation that the SAIDI benchmark value increase with time? What
is the physical justification for this versus theoretical modelling? Please provide empirical
quantitative evidence and not qualitative correlation explanation.
b) How does the proposed benchmark and forecasted SAIFI, CAIDI and SAIDI values differ in
consideration of Toronto Hydro’s proposed IRM as compared to the IRM scenario in
Reference 2?
```

**Utility's response (reference)**

```
This stems primarily from the CAIDI benchmark increasing due to the congested urban variable
increasing for Toronto Hydro over time. As congestion increases, the time required to respond
increases. The empirical quantitative evidence is the highly statistically significant congested urban
variable present in the CAIDI model.

Reference 2: IRM Scenario
Table 1 Year-by-Year Reliability Benchmarks vs. Actual
Year
SAIFI
(Actual)
SAIFI
(Benchmark)
SAIFI (%
Difference)
CAIDI
(Actual)
CAIDI
(Benchmark)
CAIDI (%
Difference)
2005
0.93
0.46
70.2%
76.59
110.00
-36.2%
2006
1.11
0.46
88.1%
64.98
110.73
-53.3%
2007
1.14
0.47
89.7%
69.12
111.59
-47.9%
2008
1.08
0.46
85.0%
67.40
112.68
-51.4%
2009
0.95
0.46
72.8%
84.13
113.75
-30.2%
2010
0.98
0.46
75.5%
77.30
115.32
-40.0%
2011
1.05
0.45
83.9%
80.13
117.26
-38.1%
2012
0.88
0.45
67.4%
68.06
118.66
-55.6%
2013
0.95
0.45
75.8%
70.61
120.35
-53.3%
2014
0.92
0.45
72.6%
63.76
123.09
-65.8%
2015
0.97
0.44
78.4%
64.04
125.48
-67.3%
2016
0.93
0.45
73.3%
59.71
128.08
-76.3%
2017
1.09
0.45
87.4%
53.14
129.25
-88.9%
2018
1.09
0.46
86.8%
53.25
130.44
-89.6%
2019
0.95
0.45
73.9%
50.39
132.46
-96.6%
2020
1.11
0.45
91.2%
50.77
135.21
-98.0%
2021
1.20
0.44
100.3%
48.55
136.49
-103.4%
2022
1.24
0.43
105.0%
45.75
138.95
-111.1%
2020-
2022
average
1.18
0.44
98.8%
48.36
136.88
-104.1%
2023
1.28
0.43
108.1%
42.76
141.81
-119.9%
2024
1.20
0.43
101.7%
52.52
144.87
-101.5%
2025
1.19
0.43
100.8%
48.93
148.16
-110.8%
2026
1.20
0.43
101.7%
48.93
151.67
-113.1%
2027
1.20
0.43
101.7%
48.65
155.43
-116.2%
2028
1.21
0.43
102.5%
48.85
159.47
-118.3%
2029
1.22
0.43
103.3%
48.97
163.82
-120.8%
2025-
2029
average
1.20
0.43
102.0%
48.87
155.71
-115.8%
Reference 2: IRM Scenario
Table 2 Toronto Hydro’s SAIDI Actuals and Benchmarks 2005-2029
Year
SAIDI (Actual) SAIDI (Benchmark)
SAIDI (%
Difference)
2005
71.3
50.7
34.0%
2006
71.9
50.7
34.8%
2007
78.9
51.9
41.8%
2008
72.9
52.1
33.7%
2009
80.2
52.3
42.7%
2010
75.4
52.8
35.5%
2011
84.2
53.2
45.8%
2012
60.2
53.5
11.8%
2013
67.1
53.6
22.4%
2014
58.8
54.9
6.8%
2015
61.9
55.4
11.2%
2016
55.7
57.4
-3.1%
2017
58.1
58.8
-1.1%
2018
57.8
59.7
-3.3%
2019
47.8
60.1
-22.9%
2020
56.3
60.3
-6.9%
2021
58.2
60.1
-3.1%
2022
56.8
60.3
-6.0%
2020-2022
average
57.1
60.2
-5.3%
2023
54.8
61.5
-11.7%
2024
62.9
62.9
0.0%
2025
58.1
64.3
-10.1%
2026
58.5
65.9
-11.9%
2027
58.6
67.5
-14.1%
2028
59.3
69.2
-15.5%
2029
59.8
71.1
-17.3%
2025-2029
average
58.9
67.6
-13.8%
Updated Investment Plan
Table 3 Year-by-Year Reliability Benchmarks vs. Actual
Year
SAIFI
(Actual)
SAIFI
(Benchmark)
SAIFI (%
Difference)
CAIDI
(Actual)
CAIDI
(Benchmark)
CAIDI (%
Difference)
2005
0.93
0.46
70.2%
76.59
110.00
-36.2%
2006
1.11
0.46
88.1%
64.98
110.73
-53.3%
2007
1.14
0.47
89.7%
69.12
111.59
-47.9%
2008
1.08
0.46
85.0%
67.40
112.68
-51.4%
2009
0.95
0.46
72.8%
84.13
113.75
-30.2%
2010
0.98
0.46
75.5%
77.30
115.32
-40.0%
2011
1.05
0.45
83.9%
80.13
117.26
-38.1%
2012
0.88
0.45
67.4%
68.06
118.66
-55.6%
2013
0.95
0.45
75.8%
70.61
120.35
-53.3%
2014
0.92
0.45
```

**Agent answer**

```
**Short answer:** The filings I can access don't give the empirical, physical justification you ask for in (a). They also don't show a separate Clearspring benchmark run on the IRM scenario, which is what (b) asks about. I also can't identify "Reference 2" from the filings, so I've read it as the IRM scenario in Toronto Hydro's reliability projections. Please confirm that reading. Below is what the record does show.

## a. Why the SAIDI benchmark rises

**What the study does.** Clearspring does not model SAIDI directly. It estimates separate SAIFI and CAIDI models and multiplies the two to get a SAIDI benchmark ([EB-2023-0195 / Exhibit 1B / p.359]). Toronto Hydro's benchmarks for future years use the same estimated parameters, combined with projected values of the explanatory variables ([EB-2023-0195 / Exhibit 1B / p.347]).

**What the numbers show.**
- The SAIFI benchmark is essentially flat at about 0.43 to 0.46 ([EB-2023-0195 / Exhibit 1B / p.364]).
- The CAIDI benchmark rises steadily, from 110.00 in 2005 to 138.95 in 2022 and 163.82 in 2029 ([EB-2023-0195 / Exhibit 1B / p.364]).
- The SAIDI benchmark therefore rises from 50.7 in 2005 to 60.3 in 2022 and 71.1 in 2029 ([EB-2023-0195 / Exhibit 1B / p.365]).
- So the rising SAIDI benchmark comes almost entirely from CAIDI.

**What drives the CAIDI benchmark.**
- The CAIDI model uses these variables: number of customers, % forestation, standard deviation of elevation, sq. km per customer, and % congested urban ([EB-2023-0195 / Exhibit 1B / p.363]).
- The congested urban coefficient is large and significant, at 20.199 with a t-statistic of 8.63 ([EB-2023-0195 / Exhibit 1B / p.363]).
- The report does not say which variable moves the CAIDI benchmark over time.
- The one variable the report shows changing with time is the congested urban variable. Clearspring made it time-varying by tying it to Toronto's high-rise count.
- It estimated that a 1% change in skyscraper count equates to a 0.63% change in the congested urban variable. Toronto's high-rises grew 7.1% a year from 2012 to 2022, and the projection uses the last ten-year average growth rate ([EB-2023-0195 / Exhibit 1B / p.346]).
- Clearspring says the congested urban challenge "will be much larger in 2029 than its historical values" ([EB-2023-0195 / Exhibit 1B / p.345]).
- This is my inference. The filings don't decompose the CAIDI benchmark by variable, so I can't quantify each driver's contribution.

**What is missing.**
- The pages I reviewed contain no empirical test, such as a back-test or event study, of why longer restoration times follow from congestion. They give no physical or engineering measurement either.
- Support in the report is statistical: the sample is 80 U.S. distributors plus Toronto Hydro, with 687 observations. The model excludes Toronto Hydro itself, and coefficients are signed to theory and significant at 90% ([EB-2023-0195 / Exhibit 1B / p.360], [EB-2023-0195 / Exhibit 1B / p.361]).
- The congested urban variable was 
```

agree: yes

## 5. 1A-PP-2: judge says **partially_correct**

> On (c), the candidate matches the reference: DER impacts are built into the load forecast through a separate integration model. On (a) and (b), it gives no substantive answer and misses the reference's main points. Those are the pointer to Exhibit 9 and the LRAMVA results, and the position that no LDC-led CDM savings are forecast for 2025–2029 because the provincial framework is not finalized. Instead it describes the IESO continuing "status quo" CDM, without stating that position.

**Question**

```
THESL indicates that it has “Enhanced the load forecast to consider electrification drivers and
changes to the availability of conservation and demand management (“CDM”) savings in producing
the revenue forecast that underpins to 2025-2029 rates”

a) Please provide what CDM results THESL will have achieved by end of the 2024 rate term
against the total achievable CDM results and what potential remains, by sector if possible
b) Please indicate what CDM results (total and incremental to those forecasted to the end of
the current rate plan) are forecasted to be achieved by year of the 2025-2029 rate plan.
Please indicate what portion of the total potential achievable CDM results that will
represent.
c) Please explain why only CDM is included in the above noted item and not the broader
scope of DER.
```

**Utility's response (reference)**

```
Please refer to Exhibit 9, Tab 2, Schedule 3 and 9-Staff-354 which indicates CDM results THESL has
achieved as part of LRAMVA by 2024.

The Province’s CDM Framework for 2025-2029 is not yet finalized. Since 2019, the role for LDCs in
CDM has reduced significantly relative to prior periods. Accordingly, in this Application, Toronto
Hydro is not forecasting LDC-led savings as part of CDM Framework during the 2025-2029 period.

The reference to “electrification drivers” includes DERs. Toronto Hydro includes DER impacts in its
load forecast. Please refer to Exhibit 3, Tab 1, Schedule 1, Appendix J for a description of the
integration of DER impacts into the load forecast.
```

**Agent answer**

```
The filings I can search don't give the numbers for (a) and (b). They state no CDM results achieved by the end of 2024, no total achievable CDM potential, no remaining potential, and no year-by-year 2025–2029 CDM figures. Part (c) is only partly answered, because the record does not address the premise directly.

**a) CDM achieved by end of 2024 against achievable potential**

- I found no figure for total achievable CDM potential or remaining potential, and no sector split of either. Toronto Hydro says the IESO no longer provides CDM savings forecasts or program results for distributors' service territories. [EB-2023-0195 / Exhibit 3 / p.10]
- The 2024 position is built from components, not measured results. Verified savings run from 2006 to 2017, and unverified post-Conservation First Framework (CFF) savings run from 2015 to 2022. The 2021–2024 CDM Framework savings (2021 to 2024) are a forecast, extrapolated from the IESO's provincial plan to Toronto Hydro's area. The extrapolation uses Toronto Hydro's 2015–2017 share of provincial savings. [EB-2023-0195 / Exhibit 3 / p.12] [EB-2023-0195 / Exhibit 3 / p.13]
- Savings are tracked only as residential versus business. [EB-2023-0195 / Exhibit 3 / p.12]
- The numbers sit in Excel appendices to Exhibit 3, Tab 1, Schedule 1 (Appendices C, D, E and G), and I could not read them. The 2024 update revised them to include 2021–2022 actuals. [EB-2023-0195 / THESL_2025-2029 Rate Application_Evidence Update_20240402 / p.5]

**b) CDM for 2025–2029 by year, and share of potential**

- I found no annual 2025–2029 figures, no split between total and incremental savings, and no percentage of potential.
- Toronto Hydro assumes the IESO continues CDM delivery at "status quo" objectives after 2024. It calls this the best estimate available given the lack of conservation planning detail for that period. [EB-2023-0195 / Exhibit 3 / p.13]
- CDM enters the forecast as cumulative 2006–2029 residential and business variables in the regression. They were statistically significant for the Residential, GS <50 kW, GS 50–999 kW, GS 1000–4999 kW and Large Use classes. The variable captures conservation from both programs and natural effects, and metered loads are no longer adjusted for CDM. [EB-2023-0195 / Exhibit 3 / p.10] [EB-2023-0195 / Exhibit 3 / p.12]
- Toronto Hydro does not plan a Lost Revenue Adjustment Variance Account (LRAMVA) threshold for 2025–2029. [EB-2023-0195 / Exhibit 3 / p.10]
- These figures should be requested from Toronto Hydro, or taken from Appendix C or E.

**c) Why CDM and not the broader DER scope**

- I found no passage that explains the choice directly. The filing does show that DERs are handled separately from CDM.
- CDM is a regression variable inside the base forecast. EVs and DERs are not in that base forecast. They are modelled in a separate Clearspring integration model and added on top, because they are expected to exceed historical adoption levels and the base forecast "does not account for"
```

agree: yes

## 6. 2B-STAFF-187: judge says **correct**

> The candidate names the same programs as the reference: Generation Protection, Monitoring and Control; the Sheppard TS expansion; and renewable-enabling storage, which falls under the reference's Non-Wires Solutions program. It also covers the grid modernization and readiness investments, and notes that some spending enables hosting beyond the test period. Nothing in it contradicts the reference.

**Question**

```
Toronto Hydro states: “Toronto Hydro does not propose any net expenditure under this Program
for the years 2025 to 2029. If during the course of the project, Toronto Hydro does not use all of
the fees collected from the customer to facilitate the DER connection, Toronto Hydro will refund
the difference back to the customer.”

a) Please identify all capital expenditures planned for 2025-2029 intended to enable the
Toronto Hydro system to host new DERs connecting solely within the 2025-2029 test
period.
b) Please identify all capital expenditures planned for 2025-2029 intended to enable the
Toronto Hydro system to host new DERs connecting beyond the test period.
```

**Utility's response (reference)**

```
Toronto Hydro intends to undertake investments in the following capital programs to enable the
system to host DERs in the 2025-2029 period: (1) Generation Protection, Monitoring and Control
(Exhibit 2B, Section E5.5); (2) Station Expansion – Sheppard TS (Section E7.4)1; and (3) Non-Wires
Solutions (Section E7.2). Some of these expenditures may enable hosting capacity beyond the test
period as well. In addition, Toronto Hydro is planning modernization and innovation investments to
enhance the utility’s ability to monitor and forecast distributed resources and facilitate and
leverage DER connections. These investments will have benefits in the 2025-2029 period and
beyond. Please refer to the Grid Readiness section of Toronto Hydro’s Grid Modernization Strategy
for more information (Exhibit 2B, Section D5.2.2).
1 Updated January 29, 2024
```

**Agent answer**

```
The filings I can access don't split planned capital into DERs that connect only within 2025-2029 and DERs that connect after 2029. Toronto Hydro doesn't label any project that way. I can identify the capital it describes as enabling DER hosting, and I note below which items have a visible beyond-2029 element. I have not located dollar figures for the storage program or the Sheppard TS expansion.

**Context for the quote.** The quoted "no net expenditure" statement covers only the customer-funded Generation Connection program. Toronto Hydro recovers project costs for those connections from the customer through capital contributions [EB-2023-0195 / Exhibit 2B / p.117]. The utility-funded hosting-capacity work sits in other programs.

**a) Capital for DERs connecting within 2025-2029**

1. **Generation Protection, Monitoring and Control (GPMC) program.** It totals $35.0M for 2025-2029, with annual spend of $5.9M, $6.1M, $6.3M, $6.5M and $10.3M [EB-2023-0195 / Exhibit 2B / p.195] [EB-2023-0195 / Exhibit 2B / p.209]. It has two parts:
   - **Monitoring and control systems.** These are for renewable DER sites over 50 kW. The plan is 315 systems at about $25,000 each, roughly $14.5M. The timing is driven by customer connection requests, and the cost is based on forecast connections [EB-2023-0195 / Exhibit 2B / p.213]. The annual cost is $2.6M to $3.2M [EB-2023-0195 / Exhibit 2B / p.212].
   - **Bus-tie reactors.** The plan is six reactors, at Richview, Runnymede, Cecil, Esplanade, Leslie and Woodbridge TS. Together they cost $20.4M and are scheduled from 2025 through 2029 [EB-2023-0195 / Exhibit 2B / p.212]. They relieve short-circuit limits that Toronto Hydro says already exist at some of these buses. Three station buses have already reached their limits [EB-2023-0195 / Exhibit 2B / p.201].

2. **Renewable-enabling energy storage.** The plan is nine storage systems totalling 10.2 MW on nine feeders forecast to have high generator-to-minimum-load ratios during 2025-2029 [EB-2023-0195 / Exhibit 2A / p.40]. I did not find the program cost.

3. **Sheppard TS expansion.** This adds a new bus with an estimated 126 MVA of short-circuit capacity "to enable DER growth". The station's EZ bus is already at −57.3 MVA [EB-2023-0195 / Exhibit 2A / p.40]. The expansion is driven mainly by load growth, and DER hosting is a secondary benefit [EB-2023-0195 / Exhibit 2B / p.201]. I did not find its cost.

**b) Capital for DERs connecting beyond 2029**

Toronto Hydro does not identify any capital as being only for post-2029 connections. Several items do look beyond the test period:

- **Forecast basis.** The sizing uses a 2029 forecast of 516.7 MW. By 2029, eight station buses are forecast to exceed short-circuit capacity [EB-2023-0195 / Exhibit 2B / p.201]. Some reactors may therefore serve constraints that only emerge late in the period. The $7.1M for 2029 is the largest year of reactor spend.
- **Longer-run scenarios.** The Future Energy Scenarios modelling shows much
```

agree: yes

## 7. 1B-CCC-32: judge says **partially_correct**

> The candidate gets the main points right: Toronto Hydro relies on OEB policy for the 0% productivity factor, the combined X-factor of 0.75% is the real stretch on revenues, and the PIM adds further benefits. However, it gives the total customer benefit as about $81.4M over 2025–2029, while the reference says $81.5M over 2026–2029. Under strict grading of numbers, that mismatch in the key figure and period keeps it from full credit.

**Question**

```
Please explain why a 0 percent productivity factor continues to be appropriate? How does this
provide a benefit to Toronto Hydro’s ratepayers.
```

**Utility's response (reference)**

```
Toronto Hydro continues to rely on the OEB policy with respect to the productivity factor of 0%. The
combined X-Factor, inclusive of the productivity factor, the empirical stretch/efficiency-factor and
the PIM, applies a 0.75% stretch to the utility’s revenues each year over the 2026-2029 period. As
detailed in the response to interrogatory 1B-Staff-03(b), the combined X-factor provides customers
a total rate reduction benefit of $81.5 million over the rate term, in addition to the benefits
associated with achieving the PIM targets, as set out in Exhibit 1B, Tab 3, Schedule 1 at pages 57-58.
```

**Agent answer**

```
**Short answer:** Toronto Hydro says a 0% productivity factor is appropriate because it is "consistent with OEB policy." It does not give a separate empirical case for 0% in the passages I found. Ratepayers benefit because the 0% sits inside a larger X-factor of 0.75%, which is the real constraint on rates.

**Why 0% is appropriate, per the filing**
- Toronto Hydro proposes an X-factor of 0.75%. That is made up of a 0% productivity factor "consistent with OEB policy," a 0.15% efficiency (stretch) factor, and a 0.6% proactive performance-incentive factor [EB-2023-0195 / Exhibit 1B / p.77].
- The filing cites the OEB's rate-setting parameters and benchmarking policy (EB-2010-0379) next to this proposal [EB-2023-0195 / Exhibit 1B / p.77]. The 0% therefore follows the OEB's standard approach. The filing does not set out the underlying industry productivity analysis for it.
- The productivity-versus-stretch split matches the OEB's framework. Productivity is set by policy. The stretch factor is then set by the utility's cost-benchmarking score.
- Clearspring's study puts Toronto Hydro's total cost benchmarking score at -22.9%, meaning costs are below the benchmark. Under the OEB's 4th Generation IR cohorts, that score earns a 0.15% stretch factor [EB-2023-0195 / Exhibit 1B / p.340].
- Clearspring says Toronto Hydro's costs have been consistently below benchmark and stay below it through the Custom IR period at the proposed spending levels [EB-2023-0195 / Exhibit 1B / p.365].
- The filing says this efficiency factor reflects Toronto Hydro's productivity achievement. It adds that the empirical factor "ordinarily should be used for purposes of setting rates" [EB-2023-0195 / Exhibit 1B / p.80].
- The filing also says the proposed X-factor is higher than the OEB-approved X-factor under standard price cap regulation [EB-2023-0195 / Exhibit 1B / p.56].

**How ratepayers benefit**
- The 0.15% efficiency factor reduces revenue by about $6.9 million a year by 2029. That totals about $16.4 million over the rate period. Toronto Hydro takes the risk of achieving this up front [EB-2023-0195 / Exhibit 1B / p.78].
- Toronto Hydro goes further and adds a 0.6% performance factor. This gives customers an upfront rate reduction of about $65 million over 2025–2029. Together the X-factor constrains revenue by about $81.4 million [EB-2023-0195 / Exhibit 1B / p.186].
- The 0.6% can be earned back only if Toronto Hydro meets its Custom Scorecard targets. If it misses them, ratepayers keep the reduction [EB-2023-0195 / Exhibit 1B / p.80].
- The earlier 2020–2024 framework used a 0.6% reduction on non-capital revenue requirement and 0.9% on capital revenue requirement. That blended to about 0.81–0.82% [EB-2023-0195 / Exhibit 1B / p.64]. The new 0.75% is slightly lower than that blend, but it applies to all revenue requirement, and part of it is at risk through the performance incentive.

**Limits of what I found**
- I did not find any reasoning for the 0% beyond "consistent with
```

agree: no (correct: $81.4M vs $81.5M is rounding of the same 0.15% + 0.6% X-factor benefit, and the substance matches the reference)

## 8. 2B-STAFF-233: judge says **partially_correct**

> On (a), the candidate leans toward confirming that age is the only driver. It does note that failure impact could matter, but it misses the reference's point that Dunsany and Centennial serve about 750 and 700 customers, well above the average station's 500. On (b), it raises switchgear coordination as a plausible reason. It misses the other stated reasons: Belfield's other transformer (TR1) is 69 with a high power factor, the loading analysis found only one transformer is needed, and the primary supply must be replaced.

**Question**

```
Regarding Table11: Power Transformers Proposed for Replacement

a) Please confirm Dunsany MS Power Transformer 2408, Centennial MS Power Transformer
2412 are all scheduled for replacement solely due to age and not because of additional
concerns.
i.
If not confirmed, please explain why not.
b) Explain why Belfield MS Power Transformer 2504 is scheduled for replacement in 2029 at
an age of 60 years despite exhibiting no concerns other than age, even though it will still be
5 years younger than Toronto Hydro’s reduced maximum target age of 65 for Power
Transformers in 2029.
```

**Utility's response (reference)**

```
Power transformers replacements are not prioritized solely based on age. As described in Exhibit
2B, Section E6.6.4.2, Table 42 at page 56, Toronto Hydro considers the impact of failure, such as
customer count, loading, degradation of oil, resiliency of operation, and voltage conversion plan in
addition to age when prioritizing the replacement these assets. On average, the average Municipal
Station (“MS”) supplies approximately 500 customers. However, Centennial MS and Dunsany MS
supply around 700 and 750 customers, respectively which represent 39 and 49 percent more than
the average number of customers. As such, they are assigned a higher priority for replacement.

Belfield Municipal Station consists of two Power Transformers (TR1 2503 and TR2 2504). As shown
in Table 42 in Exhibit 2B, Section E6.6.4.2 at page 56, the need to replace Belfield MS Power
Transformer 2504 is not solely based on age but due to the combination of age with the following:
•
TR1 2503 will be 69 years old at the time of the project and has a high-power factor;
•
A loading analysis of the area identified the need for only one power transformer,
therefore resulting in the removal of TR2 2504 and replacement of TR1 2503;
•
The primary supply to the MS also requires replacement due to the high risk of failure of
direct buried ingress; and
•
Belfield MS Switchgear is planned to be replaced in 2029. Coordination of the replacement
in conjunction with the aforementioned work is a cost-effective alternative.
```

**Agent answer**

```
**a) Dunsany MS 2408 and Centennial MS 2412**

Table 11 supports this, but only as far as the table goes. It lists "N/A" under Additional Concerns for both transformers. Dunsany is replaced at age 67 in 2027, and Centennial at age 66 in 2029 [EB-2023-0195 / Exhibit 2B / p.430]. Both ages are above the 65-year target maximum age.

The extracted table text is jumbled, so I read the row alignment from the order of the text. Please check it against the original page.

I can't confirm "solely" beyond that. The filing also says the 17 transformers were chosen "due to their condition, age, and failure impact" [EB-2023-0195 / Exhibit 2B / p.430]. It gives no separate rationale for Dunsany or Centennial. So the filing doesn't rule out failure-impact considerations, such as customers served. It simply lists no condition concerns for these two units.

**b) Belfield MS 2504 (replaced in 2029 at age 60)**

The filing does not explain why Belfield is replaced at 60 when it has no listed concerns. Table 11 shows "N/A" for additional concerns, age 60 and year 2029 [EB-2023-0195 / Exhibit 2B / p.430]. I searched for Belfield-specific reasoning and found none. Toronto Hydro would need to answer this directly.

The filing does give some context, and the first three points below are inferences rather than stated reasons:

- **Age target:** The 65-year figure is a target maximum age, cut from 70 after a rise in power transformer failures from 2017 to 2022 [EB-2023-0195 / Exhibit 2B / p.428]. It is a ceiling, not a minimum replacement age. The filing also says the plan aims to avoid reactive replacement [EB-2023-0195 / Exhibit 2B / p.428].
- **Past useful life:** Power transformers have a 45-year useful life, so a 60-year-old unit is 15 years past it [EB-2023-0195 / Exhibit 2B / p.428].
- **Coordination at one station:** Toronto Hydro says that "where possible" it coordinates end-of-life replacements at a single MS in the same year, rather than spreading outages over several years [EB-2023-0195 / Exhibit 2B / p.423]. Belfield MS's switchgear (T1-T2SG) is also scheduled for replacement in 2029, at age 65 [EB-2023-0195 / Exhibit 2B / p.426]. Coordination is a plausible reason, but the filing does not say it applies to the transformer.
- **Pacing:** Toronto Hydro proposes a faster pace of renewal for 2025-29 than for 2020-24 [EB-2023-0195 / Exhibit 2B / p.428]. The Sustainment option includes 15 power transformers. The Managed Deterioration option has 12 and would "maintain population demographics" [EB-2023-0195 / Exhibit 2B / p.487]. Whether Belfield is needed to reach 15 is not stated.
```

agree: yes

## 9. 2B-STAFF-161: judge says **partially_correct**

> The candidate names two of the reference's examples: network condition monitoring (network vault sensors) and station digital relays. It mentions AMI 2.0 only as a gap, not as one of the examples. It misses the reference's key clarification that "specific nodes" means points in the system's design rather than geographic locations, and instead treats the question as one of geographic targeting criteria.

**Question**

```
Toronto Hydro writes that it is “adding more sensors, relays and monitoring technology at specific
nodes across the distribution grid, including customer meters. These assets will provide additional
data collection points across the grid, which Toronto Hydro will leverage to improve overall
situational awareness (“grid transparency”), facilitate quicker fault location, and gain access to
important insights at the edge of the grid.”

a) Please provide several representative examples where Toronto Hydro is proposing to put
these sensors and relays and explain why they are being proposed for these locations
relative to the rest of Toronto Hydro’s territory.
```

**Utility's response (reference)**

```
To clarify, the reference to “specific nodes” is intended to convey the fact that there are various
locations within the design of the distribution system (as opposed to the geography) where certain
sensors and technologies can provide value. Some examples include:
•
AMI 2.0 meters, which provide observability and control at the customer-level;
•
Network Condition Monitoring and Control technologies, which provide observability and
control on Toronto Hydro’s network system; and
•
Stations Digital Relays, which provide observability and control at the stations level.
For a comprehensive overview of how these technologies support Toronto Hydro’s Grid
Modernization Strategy, and how the utility is pacing and prioritizing deployment, please refer to
Exhibit 2B, Section D5.2.1 and Sections E5.4, E6.6, and E7.3.
```

**Agent answer**

```
**Short answer:** The filings I can access don't list specific sensor or relay sites, such as named feeders, stations or neighbourhoods. They give a few illustrative locations and a set of targeting criteria. They also say that rollout will follow pilots.

**Targeting criteria (why some parts of the territory and not others).** Toronto Hydro says the System Observability programs "will focus on service areas with significant operational value (e.g., DER-rich feeders, feeders with poor visibility, feeders with poor reliability, etc.)." It also says it will run smaller pilots before rolling out new observability technologies at scale [EB-2023-0195 / Exhibit 2B / p.664]. The evidence describes deployment as "strategic" and aimed at "critical points on the grid" [EB-2023-0195 / Exhibit 2B / p.544].

**Representative examples the filing gives:**

- **Overhead and underground line sensors, on parts of the grid with little visibility.** Toronto Hydro currently relies largely on customers to report localized outages. Directional sensors let it "introduce and expand visibility to parts of the grid where it has not traditionally been available." They alert the control room in real time and help crews narrow fault locations [EB-2023-0195 / Exhibit 2B / p.545]. The filing doesn't say which feeders will get them.
- **Online cable monitoring in hard-to-access underground plant.** The stated example is the Western Gap Utility Tunnel, which links Toronto Island to the mainland. Its cables sit in a tunnel pressurised with lake water, so inspection and maintenance are costly [EB-2023-0195 / Exhibit 2B / p.546]. These monitors also need fibre communications, so locations without fibre need it installed first [EB-2023-0195 / Exhibit 2B / p.557].
- **Transformer monitors on the secondary system.** The rationale is rising load from EV adoption and denser residential development in Toronto. The monitors give real-time transformer loading instead of loading inferred from aggregated customer meters. They also help assess the effect of unmetered services [EB-2023-0195 / Exhibit 2B / p.547].
- **Network vault sensors.** These are in the network condition monitoring program, whose original scope ends in 2025. A follow-on pilot would test fire sensors, analog water-level sensors, cameras, hatch-open sensors and secondary cable monitoring in network vaults [EB-2023-0195 / Exhibit 2B / p.606].
- **Digital relays at stations.** Replacing electromechanical relays at transmission and municipal stations (TS and MS) is justified mainly by obsolescence and modernization. Digital relays provide fault recording and self-diagnostics and support system observability, including fault locating [EB-2023-0195 / Exhibit 2B / p.440]. The plan is 121 TS relays and 130 MS relays in 2025–2029 [EB-2023-0195 / Exhibit 2B / p.488].
- **DER monitoring and control.** Monitoring and control is required for all new DER connections above 50 kW. The filing ties it to feeders with high generation-to-minim
```

agree: yes

## 10. 1-ED-02: judge says **partially_correct**

> For (d), the candidate leans toward a fixed residential rider, which matches the reference, but it hedges. For (b), its main mid-range figure is 0.65%, or about $35M, while the reference uses 0.5%, or about $27M; the candidate mentions $27M only as the low end of a $27–40M range. For (c), it says only that the filings are silent and does not give the reference's point that a larger budget would mean more or larger pilots or more areas of innovation.

**Question**

```
a) Toronto Hydro states that its proposed Innovation Fund “is the low end of a range found in
research of comparable ratepayer-funded initiatives aimed at facilitating innovation by
utilities and regulatory bodies in other jurisdictions, as well as general data on utility
spending for research and development activities.” Please provide this analysis.
b) If Toronto Hydro were to set its Innovation Fund budget at the mid-range of comparable
initiatives, what would the budget be?
c) What additional activities would Toronto Hydro undertake with a mid-range Innovation Fund
budget?
d) How will the Innovation Fund rate rider be charged to residential customers - variable or
fixed?
e) Is Toronto Hydro open to other Ontario utilities participating in its Innovation Fund pilots
and benefiting from the results?
```

**Utility's response (reference)**

```
Please see Toronto Hydro’s response to interrogatory 1B-DRC-06 part d).

If Toronto Hydro was to fund its Innovation Fund through a rate rider based on the mid-range of
what it found in its research, Toronto Hydro would calculate an amount equal to 0.5% of its
Revenue Requirement instead of 0.3%, which would result in approximately $27 million of funding
for the Innovation Fund.

The activities described in the four phases of the Governance Framework present a methodology,
which is flexible with respect to budget, since it provides a roadmap for implementation rather
than setting the scope of work. In contrast, the areas of innovation that can be addressed and the
pilot projects that can be undertaken in connection with areas of innovation are affected by
budget. Since Toronto Hydro has proposed the Innovation Fund to be at the low end of the range
of funding found in its research, it has not considered what additional activities it might be able to
undertake with a mid-range budget. However, the effect of a larger budget would likely be that
Toronto Hydro could propose more areas of innovation and/or more pilot projects or larger scale
pilot projects within the planned areas of innovation.

The Innovation Fund Rate Rider will be charged to residential customers as a fixed charge, consistent
with the Distribution Revenue rate design for these classes. For a breakdown of how the Innovation
Fund Rate Rider will be collected over the rate period, see Exhibit 9, Tab 3, Schedule 1 (Rate Rider
Table).

Please see Toronto Hydro’s response to interrogatory 1B-CCC-46 part a).
```

**Agent answer**

```
Here is what the Toronto Hydro filings (EB-2023-0195) say on each part. For (c), (d) and (e) they don't give a direct answer. I found no interrogatory responses on these points.

**a) The comparison analysis**

Toronto Hydro's research found that utility spending on comparable innovation initiatives and R&D ranges from 0.3% to 1% of revenues. It chose the bottom of that range: 0.3% of its revenue requirement, about $16M over 2025-2029 [EB-2023-0195 / Exhibit 1B / p.459]. The filing gives these comparators:
- **UK (Ofgem RIIO-2):** networks may recover 0.5–1% of base revenues for innovation [EB-2023-0195 / Exhibit 1B / p.459].
- **New York (REV framework):** utilities can recover 0.5% of total revenue requirement, up to a maximum of $10M per year, for demonstration projects [EB-2023-0195 / Exhibit 1B / p.459].
- **Enbridge Gas Energy Transition Technology Fund (Ontario):** $25M, about 0.4% of test-year revenue requirement [EB-2023-0195 / Exhibit 1B / p.460].

The filing does not include a separate worksheet or dataset for the "general data on utility R&D spending". The comparators above are the analysis it presents. The "low end of a range" wording is in [EB-2023-0195 / Exhibit 1B / p.92] and [EB-2023-0195 / Exhibit 1B / p.84].

**b) Budget at the mid-range**

The filings don't state a mid-range budget. I can only work it out from the filing's own numbers. The range is 0.3% to 1%, and 0.3% equals about $16M. That implies a revenue requirement of roughly $5.3B over the period. The midpoint of the range is 0.65%, which gives about $35M. Using the 0.5–0.75% figures from the comparators would give about $27–40M. These are my own estimates, not Toronto Hydro's.

**c) Additional activities at a mid-range budget**

The filings don't say. They name four pilot concepts that the $16M fund could support: Flexible Connections, EV Commercial Fleet Charging, EV Demand Response and Advanced Microgrids [EB-2023-0195 / Exhibit 1B / p.470]. Toronto Hydro says it would select one or more areas of innovation and screen projects to fit the available budget and timelines [EB-2023-0195 / Exhibit 1B / p.463]. The filings do not set out what a larger fund would add.

**d) Residential rate rider: fixed or variable**

The filings don't state this explicitly for the Innovation Fund rider. The Innovation Fund rider is allocated by 2022 distribution revenue [EB-2023-0195 / Exhibit 9 / p.38]. For deferral and variance account rate riders in general, Toronto Hydro proposes a single fixed rider for classes with a fully fixed distribution rate, which includes Residential. All other classes get a volumetric rider [EB-2023-0195 / Exhibit 9 / p.38]. That suggests the residential Innovation Fund rider would be fixed, but the filing doesn't confirm it. The rider is proposed as a separate line item on the bill [EB-2023-0195 / Exhibit 1B / p.470].

**e) Openness to other Ontario utilities**

The filings don't mention other Ontario utilities participating in the pilots. They do provide fo
```

agree: yes

## 11. 2B-ED-31: judge says **partially_correct**

> The candidate gets part (b) roughly right: small connections such as single-family homes are not modelled one by one and show up only in base growth trends. It misses the 2 MVA threshold. For part (a), it leaves out the reference's key mechanism, that load from new connections ramps in over 5 years (35%, then 20%, then 15% in each of the last three years). Instead it cites a 70% haircut taken from a Downsview sensitivity study.

**Question**

```
a) Please discuss how forecast customer connections are factored into Toronto Hydro’s
demand forecasting for the purpose of capacity planning. Please explain in detail.
b) For the purposes of capacity planning, how does Toronto Hydro account for incremental
connections of single-family dwellings with 200 amp service? For instance, how many
kW are assumed (either explicitly or implicitly) to be added to co-incident system peak for
such a dwelling? For instance, would that be the maximum kWs the dwelling could
consume, the average, or some other number?
```

**Utility's response (reference)**

```
In the Toronto Hydro’s peak demand forecast, the load from new Customer Connections is
assumed to materialize over 5 years from the in-service date as follows: 35% in first year, 20% in
the second year, and 15% in each of the remaining years.

Toronto Hydro Peak demand forecast does not forecast customer connections below 2MVA. These
loads are captured in the base load growth trends shown in Figure 4 of Exhibit 2B, Section D4.
```

**Agent answer**

```
**Short answer:** The filings available to me give no kW figure for a 200-amp single-family connection in capacity planning. They don't say whether the figure would be the maximum, the average or something else. They describe a top-down, bus-level forecast. Individual small connections are not modelled one by one.

## a) How connections feed the demand forecast

**The forecast is a 10-year, weather-adjusted System Peak Demand Forecast.** It is built with a driver-based method and is the basis for capacity planning [EB-2023-0195 / Exhibit 2B / p.44]. It forecasts peak demand at every transformer station bus that supplies the grid. Summer peaks drive the 2025-2029 investment plan [EB-2023-0195 / Exhibit 2B / p.526].

**Organic growth comes from history, weather and macroeconomic drivers, not a count of connections.** The method has seven components [EB-2023-0195 / Exhibit 2B / p.46]:
- weather normalization;
- econometric multivariate regression;
- hyperscale data centres;
- EVs;
- uncommitted Municipal Energy Plan connections;
- Monte-Carlo simulation; and
- allocation to station buses, with load transfers and customer connections layered on.

The econometric inputs include Toronto population, employment and median income, CPI, business licences, housing starts and average home price [EB-2023-0195 / Exhibit 2B / p.46]. Small connections such as single-family homes are therefore captured only indirectly, through population and housing-starts trends. The filing doesn't show a per-home kW input.

**Large and identifiable connections are added explicitly.**
- Data centres, EVs and Municipal Energy Plans (Downsview, Port Lands, Scarborough Golden Mile) are the specific drivers. For the Municipal Energy Plans, both firm connection commitments and anticipated future loads are included [EB-2023-0195 / Exhibit 2B / p.48].
- The Development Planning team uses the City's development pipeline and engages large customers and developers, often 5–8 years before connection, so anticipated connections can be included in the forecast [EB-2023-0195 / Exhibit 2B / p.51].
- The Exhibit 3 revenue-load evidence says large connection projections rely on market knowledge and confirmed connection agreements. It says the revenue and peak forecasts share common growth inputs, namely large connections and EVs [EB-2023-0195 / Exhibit 3 / p.18].

**Connections are layered on at the end.** Demand from each driver is allocated to station buses. Permanent load transfers from the Load Demand program are then layered on to give the bus-level and system forecast [EB-2023-0195 / Exhibit 2B / p.49].

**One related haircut appears in a Downsview sensitivity study.** It says "THESL's standard bus load forecasting methodology adjusts new customer load to 70% of the requested load in order to forecast bus load impacts" [EB-2023-0195 / Exhibit 2B / p.214]. This is the closest thing to a connection-level coincidence or diversity factor that I found. It is described for new customer load gene
```

agree: yes

## 12. 1B-AMPCO-12: judge says **partially_correct**

> The candidate gives no answer for (a), (c), (d) and (g), which leaves out the reference's reasons for excluding switches and switchgear, the cost drivers (inflation, supply chain, COVID), the reasons for adding cable chambers, and the labour-share table. For (f) it supplies the conversion-only table, whose medians differ from the reference's fully normalized table, though it flags that difference. It overlaps with the reference only partly on (e), where utilities declined to participate, and on (b), where no unit costs exist.

**Question**

```
At Reference #1, Toronto Hydro filed a UMS Unit Costs Benchmarking Study. At Reference #2,
Toronto Hydro filed an updated UMS Unit Costs Benchmarking Study dated October 2023.

a) Please explain why unit costs for OH Switch Replacement and Switchgear Replacement
were included in the EB-2018-0165 study but not included in the October 2023 UMS Study.
b) Please provide the unit costs for OH Switch Replacement and Switchgear Replacement if
calculated as part of UMS’ work for the October 2023 study but not included in the report.
c) Please provide the drivers for the increase in unit costs in the October 2023 UMS study
compared to the EB-2018-0165 UMS Study for the following asset categories: UG Cable,
Pole Top Transformers, Padmount/UG Transformer, Network Transformer Replacement
and Breaker.
d) Please explain the basis for adding Cable Chambers to the asset category in the October
2023 UMS Study.
e) There were 17 electric utilities in the Peer Group Panel in the EB-2018-0165 study and only
12 electric utilities in the October 2023 UMS study. Please explain and discuss any impact
on the results.
f) On page 8 of the UMS report in EB-2018-0165, UMS provides Table II-1 that shows the Fully
Normalized Benchmark Comparisons. Please provide the same table using the data in the
October 2023 UMS Study.
g) On page 29 of the UMS report in EB-2018-0165, UMS provides Table C-2 which shows the
% of Labour and Non-Labour costs. Please provide the same table using the data in the
October 2023 UMS Study.
```

**Utility's response (reference)**

```
We used the list of asset classes from the previous application (EB-2018-0165) as a starting point
for discussion and applying our industry experience, we reviewed the viability of gaining
consistency across utilities for each Asset Class and Maintenance Program. Citing significant
variability in the selection, installation, and accounting for overhead switches, we opted to remove
that category from the study. With respect to Switchgear Replacement, though initially targeted for
inclusion in the previous application (EB-2018-0165 1B-2-1 Appendix B), it was ultimately removed
from consideration as the number of these replacements within each utility were too few and
sporadic to enable viable comparisons.

In identifying asset types to include for benchmarking, Toronto Hydro sought to ensure major asset
classes that accounted for considerable expenditures in the 2020-2022 period were included.
Although switches are critical components within the overhead distribution system, they do not
pose the same level of asset deterioration pressures to the overhead system as Wood Poles at the
current time as discussed in Exhibit 2B, Exhibit 6.5.3.1. In addition, the focus of the Overhead
System Renewal program remains on eliminating PCB at-risk transformers through spot
replacement approaches while managing reliability concerns through rebuilds. In selecting the
asset classes to benchmark, Toronto Hydro also attempted to align to the Activity Based
Performance Benchmarking (“APB”) asset classes where appropriate, which was another driver for
not including OH Switch Replacement within the benchmarking study.

The OH Switch Replacement and Switchgear Replacement was excluded from the October 2023
study, and thus there was no calculation for unit cost.

We have noted a general increase in costs across the industry over the past three years, driven
largely by inflation (including its effect on commodity prices), supply chain challenges (limited
manufacturing capability and excessive lead times, causing demand to exceed supply resulting in
increased prices), and COVID related policies, most notably the requirement that individuals be in
separate vehicles thus increasing crew size and fleet / heavy equipment costs. We understand that
the industry is only recently beginning to relax COVID-related restrictions, but inflation and supply
chain issues have remained an issue.

For Toronto Hydro, the increases can be attributed to various factors, including but not limited to
inflation and supply chain impacts discussed in Exhibit 1B, Tab 3, Schedule 3, and asset-specific
variability such as seen with stations assets discussed in Exhibit 2B, Exhibit 2B, Section E6.6.4.1.

Cable Chambers were added with the intention of providing a more diverse and representative
sample set of THESL’s work, particularly given the amount of civil work being performed. Of the
asset classes to be considered, cable chambers represented one that would be most conducive to
conducting industry co
```

**Agent answer**

```
**Summary:** The filings available to me contain only the October 2023 UMS study. They do not contain the earlier UMS study (Reference #1), and they do not contain Toronto Hydro's interrogatory response. So I can't answer (a) through (e) from the record. I can partly answer (f). I can't answer (g) as framed, because the October 2023 study has no labour/non-labour table.

**What the October 2023 study covers.** It benchmarks seven asset categories: Wood Poles, UG Cable, Pole Top Transformers, Padmount/UG Transformers, Network Transformers/Protectors, Breakers and Cable Chambers/Manholes. It also covers five maintenance programs [EB-2023-0195 / Exhibit 1B / p.381]. OH Switch Replacement and Switchgear Replacement are not among them. I searched for them in the filings and found only capital-plan discussion of those programs, not unit-cost benchmarks.

**a) and b) Why the two switch and switchgear unit costs were dropped, and what they were.** The record does not say. It has no explanation of why they were omitted, and no unit costs for them calculated by UMS.

**c) Drivers of the unit-cost increases.** I can't answer this because the earlier study's figures aren't in the record. The October study's own figures, for reference, are these 2020–2022 three-year averages [EB-2023-0195 / Exhibit 1B / p.410]:

| Asset category | THESL unit cost (C$) |
|---|---|
| UG Cable (per metre) | 131 |
| Pole Top Transformer | 18,691 |
| Padmount Transformer | 37,373 |
| Network Transformer | 127,649 |
| Breaker | 37,983 |

**d) Why Cable Chambers/Manholes were added.** The record gives no stated reason. The October study lists them as the seventh asset category [EB-2023-0195 / Exhibit 1B / p.381]. It also gives a THESL benchmark of $136,409 per chamber, 0.6% above the median [EB-2023-0195 / Exhibit 1B / p.388].

**e) Peer group of 17 versus 12.** The record doesn't discuss the earlier 17-utility panel or what the change did to the results. It does explain how the 12-utility panel was formed:
- Four Ontario utilities were invited. Only Elexicon Energy and London Hydro participated [EB-2023-0195 / Exhibit 1B / p.390].
- UMS approached the utilities from the 2017–2018 study. Eight of those participated, and the other nine declined [EB-2023-0195 / Exhibit 1B / p.390].
- Two utilities that declined last time accepted this time: Avista, and an anonymous Canadian utility [EB-2023-0195 / Exhibit 1B / p.390].
- That gives 12 in total, with 11 named plus the anonymous utility [EB-2023-0195 / Exhibit 1B / p.390].

This suggests the 17 refers to the 2017–2018 panel. I can't confirm that from the filings. UMS says no peer group is a perfect fit [EB-2023-0195 / Exhibit 1B / p.394].

**f) Table II-1 (fully normalized comparisons), October 2023 data.** The October study's Table II-1 is titled "Applying Conversion and Accounting Adjustments Only", so it is not a fully normalized table. UMS did not normalize for customer density or regional labour cost. It treated them qualitatively b
```

agree: yes (borderline; closer to abstained, since only (e) and (f) are partly answered)

## 13. 2B-EP-28: judge says **partially_correct**

> The candidate gets (a) right: the Future Energy Scenarios modelling covers electrified heating. Its long-term view in (b) also matches the reference: heat pumps become material, the peak shifts to winter, and timing is uncertain. On (d) it correctly names the stress test, the Load Demand program and non-wires solutions. However, on (c) it misses the reference's position that normal planning, such as installing or upgrading transformers, will keep service reliable. Instead it suggests reliability risks from deferred work. It also leaves out the "wait and see" approach to capacity investment and the sensing and observability investments.

**Question**

```
“Government at all levels are implementing decarbonization policies, including GHG emission
targets and incentives to encourage consumers to electrify their transportation and heating needs.
Key policies and incentives include: Canada Greener Homes Grant provides up to $5,000 for
electrified heating technologies such as heat pumps. This grant was introduced in December 2020
and is expected to stay in place for seven years.”

a) Has Toronto Hydro performed any analysis of the impacts on peak electricity demand in
winter months for a sizable portion of residential customers converting their home heating
to heat pumps? If not, why not?
b) Does Toronto Hydro presently expect the transition to heat pumps for home heating to
have a material effect on peak electricity demand? If not, why not?
c) If significantly more residential customers install heat pumps in a particular area than
Toronto Hydro has presently anticipated, how will this impact service reliability?
d) Does Toronto Hydro have a plan in the event that significantly more customers install heat
pumps in a particular area than anticipated?
```

**Utility's response (reference)**

```
Yes. The Future Energy Scenarios model includes electrified heating. Please see Exhibit 2B, Section
D4, Appendix A and B for more information.

In the long-term, Toronto Hydro’s view is that successful decarbonization of the energy system is
very likely dependent upon the widescale adoption of heat pumps. This will ultimately have a
material impact on peak electricity demand, including very likely the shift to a winter peak.
However, as illustrated by the Future Energy Scenarios, the extent and timing of the impact of heat
pump adoption on peak electricity demand is highly uncertain, and dependent on many factors
outside of Toronto Hydro’s control.

Toronto Hydro planning process is designed to support the maintenance and operation of a safe,
stable and reliable grid. Toronto Hydro undergoes an annual update to its Peak Demand Forecast
that reflects both emerging trends and updated planning assumptions. Toronto Hydro recognizes
that the pathway through the energy transition is both uncertain and uneven with local needs and
constraints becoming more evident before more regional needs are manifested. It is in recognition
of that changing landscape, Toronto Hydro has approached the energy transition arming itself with
new tools in its forecasting toolbox and increasingly sophisticated methods of understanding
customer behaviour. For more information on Toronto Hydro’s capacity planning approach to the
energy transition, please refer to Exhibit 2B Section D4.2.
Toronto Hydro is also planning to invest in sensing technology that will provide useful data that will
aid in determining load profiles at a level of granularity that will permit Toronto Hydro to respond
to local system constraints in a targeted and cost-efficient manner. More information can be found
under the system observability section of the Grid Modernization Strategy in Exhibit 2B Section
D5.2.1.
If significantly more residential customers install heat pumps in a particular area, Toronto Hydro,
through its normal planning process, will support the need by installing new transformers or
upgrading existing transformers and other relevant infrastructure to ensure service reliability.

Toronto Hydro used the Future Energy Scenarios to stress-test whether the utility’s capacity plan
can accommodate energy transition needs (e.g. building heating electrification) in the early part of
the next decade. In an effort to adopt a proactive approach to managing forecasted local
constraints, Toronto Hydro has outlined plans reflected in its Load Demand and Non-Wires
Alternatives portfolio, to provide flexibility to adequately respond to local drivers that may result in
capacity constraints. For more information on Toronto Hydro’s Load Demand and Non-Wires
Alternatives plans, please refer to Exhibit 2B Section 5.3 and 7.2 respectively.
While Future Energy Scenarios reveal that the impact of building electrification in the next two
decades could be significant, there are notable differences (driven by p
```

**Agent answer**

```
**Short answer:** Toronto Hydro has done some analysis, but not a bottom-up study of heat-pump conversions by residential customers. It does not expect heat pumps to be a material driver of peak demand in 2025–2029. For unexpected local clustering, it admits it could face local capacity constraints. Its stated responses are capacity programs and a proposed variance account. The filings I found do not say how reliability would be affected. All figures below come from EB-2023-0195 only.

**a) Analysis performed?** Yes, in two forms.
- Toronto Hydro commissioned Future Energy Scenarios (FES) modelling. It models heating technologies (air-source, ground-source and hybrid heat pumps, among others) as a separate segment from core demand. It runs winter and summer system peaks under several scenarios [EB-2023-0195 / Exhibit 2B / p.550] [EB-2023-0195 / Exhibit 2B / p.647].
- It also ran a sensitivity test of whether its plan could handle a growing winter peak from building electrification in 2025–2029. The test used the Consumer Transformation scenario and its low-efficiency variant as bounds [EB-2023-0195 / Exhibit 2B / p.536].

The FES is system-wide, not a study of residential conversions specifically. I did not find an analysis that isolates a sizable share of residential customers converting. The filings also do not give a "why not" answer to that framing.

**b) Material effect expected?** Not in the 2025–2029 period.
- Toronto Hydro determined that building electrification "is not yet a significant driver of growth in the 2025-2029 rate period." Its forecast therefore stays summer-peaking [EB-2023-0195 / Exhibit 2B / p.536].
- Its System Peak Demand Forecast is generally aligned with the Consumer Transformation scenario. It concluded that the capacity plan can meet higher heating loads if they arrive faster than expected [EB-2023-0195 / Exhibit 2B / p.537].
- Over the longer term, the FES expects heat pumps and EVs to be primary drivers of peak demand growth. It expects the network peak to shift from summer to winter in the 2030s [EB-2023-0195 / Exhibit 2B / p.39] [EB-2023-0195 / Exhibit 2B / p.647]. The base year peaks are 3.9 GW in summer and 3.7 GW in winter [EB-2023-0195 / Exhibit 2B / p.647].
- The seven-year Greener Homes Grant is an input to the modelling. It is assumed to last at least seven years but may be extended [EB-2023-0195 / Exhibit 2B / p.601].

**c) Reliability impact if local uptake is higher than anticipated?** The filings do not quantify this. They acknowledge that Toronto Hydro "could be faced with incremental capacity constraints at a localized level as a result of accelerated transportation and building electrification demand" [EB-2023-0195 / Exhibit 2B / p.537] [EB-2023-0195 / Exhibit 2B / p.538].

Toronto Hydro also says that when external drivers add investment needs, it must typically defer work in System Renewal, System Service and General Plant. That could leave "significant reliability, safety or environmental risks" 
```

agree: yes

## 14. 2B-STAFF-242: judge says **partially_correct**

> The candidate matches the reference in two places. It notes that reliability has plateaued rather than improved significantly, and it does not accept that most of the plan is already implemented. It misses the reference's framing that the segment serves two goals: maintaining reliability over 2025–2029 while improving reliability and resiliency over the longer term. Its conclusion that the answer on benefit-cost analysis is "closer to no" also cannot be confirmed, because the reference points to 2B-Staff-170 for that discussion.

**Question**

```
The proposed Contingency Enhancement investment represents a $113M (568%) increase in
segment spending.

a) Please confirm that this increase is necessary to maintain rather than improve system
reliability.
i.
If confirmed, please explain how Toronto Hydro has been able to significantly
reduce its outage durations over the historical period despite a much slower pace
of spending in this segment.
ii. If not confirmed, please reconcile Toronto Hydro’s strategic decision to increase
spending in this segment by 568%, given its residential customers’ preference to
maintain reliability and control costs.
b) Toronto Hydro indicates elsewhere in the Application that Toronto Hydro has already
implemented majority of its contingency enhancement plans. Has Toronto Hydro
undertaken a benefit-cost analysis demonstrating that the proposed accelerated spending
to rapidly complete this plan provides offsetting benefits of equal or greater value to
customers?
i.
If yes, please provide the benefit-cost analysis documentation.
ii. If no, please explain why not.
```

**Utility's response (reference)**

```
As mentioned in Exhibit 2B, Section E2, "Although Toronto Hydro’s renewal and modernization
efforts over the last decade have led to improvements in reliability performance that began in the
mid-2000s, more recently this performance has plateaued." The investments in the Contingency
Enhancement segment support Toronto Hydro’s complimentary goals of maintaining reliability
during the 2025-2029 period while improving reliability and resiliency for the longer-term. For
more information, please refer to 2B-Staff-175.

Toronto Hydro has not indicated that the majority of its contingency enhancement plans have been
implemented. For a discussion regarding benefit-cost analysis related to modernization initiatives,
including Contingency Enhancement, please refer to 2B-Staff-170. Pleaser also refer to 2B-Staff-162
for information on the expected long-term benefits of Fault Location Isolation and Service
Restoration (‘FLISR’) implementation.
```

**Agent answer**

```
**Short answer:** The filings available to me do not support confirming the premise in (a). I also found no benefit-cost analysis for the Contingency Enhancement segment, so the answer to (b) is closer to "no" than "yes". I did not find Toronto Hydro's actual interrogatory responses, so the points below come from the application's own evidence.

**The numbers**
- Contingency Enhancement spending was $19.9M in 2020–2024. That is $5.0M, $0.8M, $4.9M, $3.7M and $5.5M by year. [EB-2023-0195 / Exhibit 2B / p.547]
- The 2025–2029 forecast is $132.9M. [EB-2023-0195 / Exhibit 2B / p.524]
- The difference is about $113M, or 568%, which matches your figures.

**(a) Is the increase only to maintain reliability?**
- Toronto Hydro does not describe it that way. It presents the segment as improving reliability and as a grid-modernization step.
- It expects an average 12.6% reliability improvement on 94 Horseshoe feeders. It puts the potential SAIDI gain at about 0.022 minutes per feeder per year. [EB-2023-0195 / Exhibit 2B / p.530]
- It expects about 16.3% on 40 Downtown overhead feeders. It puts the potential SAIDI gain there at about 0.03 minutes per feeder per year. [EB-2023-0195 / Exhibit 2B / p.536]
- Reclosers are a further addition, with potential SAIDI improvement of up to 0.108 minutes per feeder per year. [EB-2023-0195 / Exhibit 2B / p.532]
- A second purpose is distribution-automation readiness. The goal is for over 90% of Horseshoe feeders to meet the criteria, ahead of a self-healing grid starting in 2030. [EB-2023-0195 / Exhibit 2B / p.535] [EB-2023-0195 / Exhibit 1B / p.228]
- Toronto Hydro says the overall plan includes "accelerating investments in the Modernization category to modestly improve performance". It says the Sustainment and Stewardship category holds the minimum needed to maintain recent performance. [EB-2023-0195 / Exhibit 1B / p.194]

**(a)(ii) Reconciling the increase with customer preferences**
- I did not find an explicit reconciliation with residential customers' preference to maintain reliability and control costs.
- The application's rationale is that the status-quo option is "not recommended". At roughly $20M, it would deliver only 111 switches on 37 feeders and 17.8 km of egress cable. [EB-2023-0195 / Exhibit 2B / p.552]
- The selected option is about 300 switches, 220 reclosers and 69 km of egress cable. [EB-2023-0195 / Exhibit 2B / p.552] [EB-2023-0195 / Exhibit 2B / p.553]
- For Downtown, the application cites "general support" among customers for investments in new technology to improve the system. [EB-2023-0195 / Exhibit 2B / p.536]

**(a)(i) Past outage-duration reductions despite slow spending**
- The application does not clearly support "significantly reduce". Toronto Hydro says reliability improved from the mid-2000s but "plateaued" more recently, with a slight deterioration from 2020 to 2022. [EB-2023-0195 / Exhibit 2B / p.22]
- Adjusted SAIDI was 0.78, 0.68, 0.90, 0.95 and 0.70 for 2018–2022. [EB-2023-0195 / Exh
```

agree: yes

## 15. 2B-AMPCO-35: judge says **partially_correct**

> On (a), the candidate leans the same way as the reference: the filed figures already appear to exclude deficiencies corrected on site. But it hedges and says the filings don't state this outright, while the reference says it plainly. On (b), the reference describes the data source and calculation for every indicator in Table 1, including oil, interruptions, condition, PCBs, age and legacy assets. The candidate covers only priority deficiencies (its P1/P2/P3 reconciliation) and gives none of those other data sources or calculations.

**Question**

```
With respect to Table 1:

a) Please provide the data in the Priority Deficiencies (Number assigned) column excluding
deficiencies corrected on site.
b) Please provide the underlying data and calculations in Table 1, including assumptions.
```

**Utility's response (reference)**

```
The priority deficiencies provided in Table 1 of Exhibit 2B, Section D2 exclude deficiencies corrected
on-site.

Each of the asset management performance indicators in Table 1 of Exhibit 2B, Section D2 were
calculated as described in Table 1 below.
Table 1: Calculation of Asset Management Performance Indicators
AM Performance
Indicators
Underlying Data and Calculation
Oil Deficiencies
• Data: Inspection Records
• The number of assets with an oil leak identified during
inspections are aggregated by sub-system
Priority Deficiencies
• Data: Inspection Records and Work Request Data
• Priority Deficiencies are determined by aggregated the
deficiencies, for which work requests were issued and priorities
assigned (such as P1, P2, P3), by sub-system.
Customer Hours of
Interruption
• Data: ITIS Data
• Defective Equipment outage incidents and corresponding total
number of customer hours interrupted are aggregated by sub-
system.
Customer Interruptions
• Data: ITIS Data
• Defective Equipment outage incidents and corresponding total
number of customers interrupted are aggregated by sub-system.
Condition
• Data: Asset Registry and Inspection Records
• The number of assets in HI4 or HI5 are divided by the total
population of the assets with health scores by sub-system.
Oil Containing PCBs
• Data: Asset Registry and Inspection Records
• The number of assets containing or at-risk of containing PCBs
were aggregated by sub-system.
Age
• Data: Asset Registry
• The number of assets that are at or past Useful Life by sub-
system.
Legacy Assets
• Data: Asset Registry
• The remaining inventory of the asset or configuration type in the
distribution system.
RESPONSES TO ASSOCIATION OF MAJOR POWER CONSUMERS IN ONTARIO
INTERROGATORIES
```

**Agent answer**

```
**Short answer:** The filings available to me don't give the Priority Deficiencies column in Table 1 with deficiencies corrected on site excluded. They also don't give the workpapers behind Table 1. I can only give you the published figures, the P1/P2/P3 breakdowns that reconcile to them, and what the filings say about the basis.

I'm assuming "Table 1" is Table 1 in Toronto Hydro's Exhibit 2B, Section D2, "Asset Management Performance Indicators by System Type" (EB-2023-0195). If you meant another table, please tell me.

**a) Priority Deficiencies (Number assigned), as filed**

These are 2022 year-end actuals [EB-2023-0195 / Exhibit 2B / p.51].

| System | Priority deficiencies (share of total) |
|---|---|
| Overhead | 3,074 (24%) |
| Underground | 8,955 (71%) |
| Network | 0 (0%) |
| Stations | 560 (4%) |
| Total | 12,589 (100%) |

The extracted table has a layout quirk. The Oil Deficiencies figures (11, 298, 21, 8) are in the first value column, and the Priority Deficiencies figures are in the second [EB-2023-0195 / Exhibit 2B / p.51].

I could not find a version of this column that excludes deficiencies corrected on site. The evidence suggests the published figures already exclude them, but the filings don't say so outright:
- Priority deficiencies are defined as deficiencies that "require intervention on a reactive or corrective basis" and are assigned P1, P2 or P3. Deficiencies corrected on site are described separately, as part of the larger total of about 45,000 identified each year [EB-2023-0195 / Exhibit 2B / p.52].
- "Find it and fix it" practices repair minor deficiencies on site. This "eliminates the need to create a separate work request" [EB-2023-0195 / Exhibit 4 / p.191]. Priority deficiencies are assigned for repair, so on-site fixes would not appear to be in this column.
- The only quantified on-site-corrected figure I found is about 3,600 per year, and it applies to below-grade equipment only. That footnote also says "2020-2025", which looks like a typo [EB-2023-0195 / Exhibit 4 / p.109]. It can't be used to adjust Table 1.

If the column does include on-site corrections, the filings give no way to strip them out. That would need an interrogatory.

**b) Underlying data, calculations and assumptions**

The filings give a P1/P2/P3 split for 2022 for two of the systems. Each sums exactly to the Table 1 figure:
- **Overhead:** 218 P1 + 724 P2 + 2,132 P3 = 3,074 [EB-2023-0195 / Exhibit 2B / p.56].
- **Underground:** 496 P1 + 1,677 P2 + 6,782 P3 = 8,955 [EB-2023-0195 / Exhibit 2B / p.63].
- **Network:** 0. Network deficiencies "are generally tracked with all other underground deficiencies" [EB-2023-0195 / Exhibit 2B / p.71].
- **Stations:** 560. I found no P1/P2/P3 split for stations.
- **Total:** 3,074 + 8,955 + 0 + 560 = 12,589, which matches the table. The shares are each system's figure divided by 12,589: 3,074/12,589 ≈ 24%, 8,955/12,589 ≈ 71%, 560/12,589 ≈ 4%. The shares are my arithmetic, and they agree with the table.

**Assum
```

agree: yes

## 16. 2B-VECC-18: judge says **partially_correct**

> On (a), the candidate's reasons for the exclusion match the reference: the filing gives a rationale, and all-in metrics including scheduled outages are still tracked. On (b), it names other measures (CAIDI, emergency response, FESI) but leaves out the reference's main points: defective-equipment SAIFI/SAIDI, cause-code tracking, the accuracy of estimated restoration times, and weekly reviews of large outages. On (c), it says it found no guideline or process, but the reference describes one: outage requests with start and finish times, a switching order from the Control Centre, Field Managers monitoring the work, and advance notice to customers.

**Question**

```
a) Presumably customers are concerned with the duration of outages irrespective of their
reason and especially if the outage is a matter within THESL’s ability to address. The PIM
measure for Outage Duration excludes Scheduled Outages. Why?
b) Are there any other measures used by THESL to gauge the response capability/efficiency of
outage recovery?
c) With respect to scheduled outages are planned projects provided guidelines or
expectations for maximum outage time? If so, please provide or explain the process that is
used to ensure that a given project meets the expected outage time.
```

**Utility's response (reference)**

```
Please refer to Exhibit 1B, Tab 3, Schedule 1, pages 8-9 for an explanation of the rationale behind
the PIM measures. Independent of the PIM measure, Toronto Hydro measures and monitors “all-
in” reliability metrics (including scheduled outages) on an ongoing basis, and has an established
process for managing the impacts of scheduled outages on customers.
Toronto Hydro agrees that customers are concerned about outages irrespective of their reason.
However, Toronto Hydro disagrees with the implication that scheduled outages are equivalent to
unplanned outages when it comes to the customer experience. Toronto Hydro offers the following
high-level comparison of scheduled and unplanned outages for further consideration.
Aspect
Scheduled Outages
Unplanned Outages
Predictability
Planned in advance,
scheduled time known
Occur without warning,
unpredictable
Duration and Impact
Typically short, a few hours,
and contained
Variable, can last from
minutes to days, and can
impact thousands of
customers
Aspect
Scheduled Outages
Unplanned Outages
No advance notice
Communication
Toronto Hydro communicates
schedule in advance
Impact on Customers
Predictable, can plan around
outage
Disruptive, can cause
inconvenience and losses
Mitigation Options
Customers can prepare, use
backup power
Limited options, may not be
able to mitigate
Frequency
Regular, scheduled based on
capital and maintenance plan
Occasional, based on system
reliability
Preventive Purpose
Preventive maintenance,
system improvements
Reactionary response to
failures

Toronto Hydro routinely measures and monitors “all-in” SAIFI and SAIDI, “defective equipment”
SAIFI and SAIDI, volume/impact of outages by specific cause codes and availability/accuracy of
outage Estimated Time of Restoration. Large outages are reviewed on a weekly basis for lessons
learned and improvement opportunities.

Crews undertaking scheduled outages are expected to plan outages in a manner that minimizes
customer impact (duration and scope) to the extent possible. Outage requests are submitted to the
Control Centre with start and finish times. Controllers will review the request and create a switching
order to enable work to be completed safely while minimizing the number of customers impacts.
Field Managers oversee the work and monitor progress to ensure that work is completed within the
allotted time.
Additionally, in the planning phase, proactive engagement with customers is facilitated through
community relations teams (as detailed in Exhibit 4, Tab 2, Schedule 18). Notices regarding power
interruptions, along with advance information about the expected outage duration, are provided.
RESPONSES TO VULNERABLE ENERGY CONSUMERS COALITION
INTERROGATORIES
```

**Agent answer**

```
**Short answer:** THESL's filings give two reasons for excluding Scheduled Outages from the Outage Duration measure. They also describe other measures of restoration capability. I found no stated project-level maximum outage time for planned work, or a process to enforce one.

**a) Why Scheduled Outages are excluded**

THESL measures Outage Duration as the 5-year rolling average of SAIDI, excluding Major Event Days, Loss of Supply and Scheduled Outages. It proposes removing the Scheduled Outages cause code from the 2025-2029 measure for two stated reasons:
- **Forecasting uncertainty.** The ongoing implementation of Oracle Utility Analytics makes forecasting difficult.
- **Expected growth.** THESL expects scheduled outages to increase because of a larger work program.

THESL also says the exclusion gives "more transparency and visibility" into reliability for unforeseen interruptions [EB-2023-0195 / Exhibit 1B / p.192]. The Outage Duration target is 46.2 minutes by 2029 [EB-2023-0195 / Exhibit 1B / p.193].

The Distribution System Plan gives a related rationale. Scheduled outages are needed to do work such as replacing end-of-life or deteriorated assets to prevent a future outage. THESL says including them "would not provide a true reflection of underlying distribution system performance" [EB-2023-0195 / Exhibit 2B / p.342].

The Outage Duration measure is the part of the filing most relevant to your point. It says customers other than Key Accounts prioritize reducing the overall length of outages [EB-2023-0195 / Exhibit 1B / p.192]. THESL still reports SAIDI and SAIFI including scheduled outages. It tracks five scenarios, and only the last excludes scheduled outages [EB-2023-0195 / Exhibit 2B / p.335]. The filings I found do not explain why the PIM itself leaves out scheduled-outage duration.

**b) Other measures of response and recovery capability**

- **CAIDI.** THESL's filing says CAIDI measures average restoration time per outage. It "indirectly measures the Company's response time and preparedness for outage restoration" [EB-2023-0195 / Exhibit 1B / p.359].
- **Emergency response standard.** THESL must get a crew to emergency events within 60 minutes, 80 percent of the time, under section 7.9 of the Distribution System Code [EB-2023-0195 / Exhibit 4 / p.196]. The Emergency Response program also lists SAIFI, SAIDI and FESI-7 as reliability objectives it supports. It cites "minimizing outage restoration times" as a goal [EB-2023-0195 / Exhibit 4 / p.196].
- **Feeder-level measures.** FESI-7 counts feeders with seven or more sustained interruptions in 12 months. FESI-6 Large Customers tracks key-account feeders at six or more [EB-2023-0195 / Exhibit 1B / p.279] [EB-2023-0195 / Exhibit 1B / p.281]. THESL also tracks CEMSMI-10 for key-account customers [EB-2023-0195 / Exhibit 2B / p.495]. These measure frequency rather than recovery time.
- **Storm restoration.** For major events, THESL reports restoration timelines, such as "within 2 days" for 
```

agree: yes

## 17. 2B-ED-29: judge says **partially_correct**

> The candidate matches the reference on several points: V2G has future potential, any pilots would go through the Innovation Fund, the evidence gives no charger models or prices, and Toronto Hydro has no installation guide. It also correctly notes that the utility's own fleet chargers come with its fleet electrification. However, it misses key positions in the reference. Toronto Hydro has looked at bi-directional charging for its own fleet and found the technology not ready (part c). It would use bi-directional chargers as demand response once aggregated volumes provide grid value. On customer support, the reference cites its website guidance and help through the connections process.

**Question**

```
a) Please comment on the potential for car batteries to be used to reduce building loads with
bi-directional chargers at the time of distribution peaks and thus reduce the need for
distribution infrastructure.
b) Please describe all steps Toronto Hydro is taking to (a) assist its customers in installing or
purchasing electric vehicle chargers and (b) install electric vehicle chargers for its own use.
c) With respect to Toronto Hydro’s efforts to install electric vehicle chargers, what proportion
will be bi-directional chargers?
d) Nova Scotia Power is undertaking a bi-directional charger pilot project involving 20 bi-
directional chargers of 4 different types. David Landrigan, vice-president of commercial for
Nova Scotia Power stated as follows: “I think we can call it a game-changing resource”.
Would Toronto Hydro consider a similar pilot? Would this require additional regulatory
approvals if it were to occur prior to 2029?
1 https://www.torontohydro.com/documents/20143/193303016/climate-action-plan-2023-status-report.pdf
e) The following utilities are piloting bi-directional chargers:
•
San Diego Gas & Electric in California (10 V2G busses, 25 kW/bus, 250 kW)
•
Con Edison in New York (5 V2G busses, 10 kW/bus, 50 kW)
•
EDF Energy in the UK (Customer-facing V2G program based on ABB equipment)
•
National Grid in Rhode Island (Fermata V2G bidirectional pilot, 15-20 kW)
•
Roanoke Electric Cooperative in N. Carolina (Fermata V2G system, 15-20 kW)
•
Green Mountain Power in Vermont (Fermata V2G bidirectional pilot, 15-20 kW)
•
Austin Energy in Texas (V2G/V2B pilot)
•
Snohomish County Public Utility District in Washington State (V2G pilot)
Is Toronto Hydro considering similar pilots? If not, why not. Would this require additional
regulatory approvals if it were to occur prior to 2029? Please explain.
f) Please provide 6 examples of bi-directional charges available in North America (3 AC and 3
DC) and list their charge/discharge rate (kW) and approximate price. This could i
```

**Utility's response (reference)**

```
Toronto Hydro is willing to consider the use of bi-directional chargers as demand response once
volumes of controllable, dispatchable installations reach levels that can be aggregated to provide
grid value. The utility is open to working with third-parties (e.g. aggregators) to leverage this
capacity when and if it is available and if it can provide cost-effective value to the distribution
system as a whole. The current use-case of non-wires solutions is outlined in Exhibit 2B Section
E7.2.

Through its website, Toronto Hydro provides customers with the process required to install an EV
charger, which includes recommendations to work with licensed electrical contractors. However, in
the event that a service upgrade is required at a customer’s service address, Toronto Hydro works
with the customer and their contractor through the connections process.
Through non-rate regulated business activities, which do not form part of this application, Toronto
Hydro is also playing a proactive role in supporting the realization of the City’s Net Zero Strategy by
facilitating and stimulating the growth of emerging local cleantech markets. For more information,
please see the latest Climate Action Plan status report.1
For its own use, the utility installs electric vehicle chargers in tandem with its investments to
replace internal combustion engine fleet vehicles with electric and hybrid vehicles (see Exhibit 2B,
Section E8.3 for more details).

Toronto Hydro supports, facilitates and enables the installation of electric vehicle chargers as
requested by customers. The utility does not require customers to install specific charges models or
types, outside of compliance with codes and standards. Toronto Hydro has explored bi-directional
charging capabilities for its own fleet vehicles and has determined the technology is not ready for
deployment at this time. As charging technologies develop, Toronto Hydro will investigate
opportunities to implement bi-directional charging.

Toronto Hydro believes bi-directional charging has the potential to provide grid benefits in the
future. Future pilots would be proposed and selected through the Innovation fund summarized in
section 2.5.3 and detailed in Exhibit 1B, Tab 4, Schedule 2 and Appendix A.

Toronto Hydro does not collect commercial information with respect to products that would be
purchased, installed, owned and operated by third-parties.

Please see 2B-ED-24 parts (a) to (c).

Please see response to part (e).

Toronto Hydro does not have an EV charger technical installation guide. Due to the continuous
evolution of the industry, and the variety of established EV charger vendors, specific EV charger
installation guides are well documented by the respective manufacturers. Aside from specific
manufacturer specifications, Toronto Hydro approaches installation of EV chargers similar to other
electrical appliances and provides information on its website to assist customers in making
informed decisions about purchasing 
```

**Agent answer**

```
**Short answer:** The Toronto Hydro filing (EB-2023-0195) only partly answers these questions. It supports a general discussion of V2G, the existing EV pilots, the proposed Innovation Fund, and the utility's own fleet. It says nothing on bi-directional charger models or prices, the share of its own chargers that are bi-directional, the specific non-wires concepts in (h)–(j), or a Hydro Quebec-style installation guide. I haven't drawn on the Hydro One filing, because the questions are addressed to Toronto Hydro. I also haven't used outside knowledge for charger specs or prices. Those answers would need to come from Toronto Hydro itself or from vendor sources.

**a) Potential of car batteries to reduce peaks**
- Toronto Hydro's modelling treats smart charging and V2G as flexibility options. They move demand away from peak, and V2G lets cars "discharge to the network at times of high demand, effectively acting as grid storage units" [EB-2023-0195 / Exhibit 2B / p.560].
- The utility says EVs, especially in high concentrations, can overload secondary transformers and stress overhead conductors and underground cables. It says managing EV load, and potentially discharge, could serve as a non-wires solution in place of grid expansion [EB-2023-0195 / Exhibit 1B / p.476].
- Its V2G uptake scenarios are described as "conservative due to high costs of bi-directional chargers and current limitations around the business case". The Low scenario has no V2G. In the High scenario, V2G uptake starts immediately and all EVs charge flexibly from 2030 [EB-2023-0195 / Exhibit 2B / p.631] [EB-2023-0195 / Exhibit 2B / p.632].
- The filing does not quantify the avoided infrastructure.

**b) Steps to help customers install EV chargers, and to install chargers for its own use**
- **Customers:**
  - I found no customer charger purchase or installation incentive program.
  - The filing describes an EV Smart Charging Pilot with Plug'n Drive and Elocity. It studies charging patterns and supports tools for EV owners to monitor, schedule and control charging [EB-2023-0195 / Exhibit 2B / p.692].
  - Phase 1 tested adding internet-connected on/off devices to simple chargers [EB-2023-0195 / Exhibit 2B / p.736].
  - Toronto Hydro is also budgeting more contact-centre staff to handle EV inquiries about service upgrades, installing or troubleshooting charging stations, pricing plans, and on-street charging [EB-2023-0195 / Exhibit 4 / p.415].
  - It identifies EV charging for public streets, City and TTC fleets, Toronto Parking Authority lots, and homes as growth areas it serves [EB-2023-0195 / Exhibit 1B / p.90].
- **Own use:**
  - Toronto Hydro owns 13 electric and 20 hybrid light-duty vehicles. It plans to keep buying electric or hybrid light-duty vehicles at a measured pace [EB-2023-0195 / Exhibit 2B / p.748].
  - A faster fleet-electrification option was considered. It would replace all light-duty vehicles and 20 heavy-duty vehicles with electric or hybrid vehicles [EB-2023-0195 /
```

agree: yes

## 18. 1B-STAFF-46: judge says **partially_correct**

> The candidate correctly picks out TRIF and SAIFI as carried-over measures. It also gets the SAIDI redefinition right (now excluding MEDs, Loss of Supply and scheduled outages) and gives the customer-priority rationale for it. However, it gives no per-measure removal rationale, so it misses the reference's reasons: eBills target exceeded, the Network Units program winding down, cost measures replaced by Efficiency Achievements, and environmental measures managed under ISO14001. Its suggestion that Local Demand Response depends on the incentive also sits uneasily with the reference, which says the incentive mechanism does not drive any specific initiatives.

**Question**

```
Toronto Hydro has proposed a 2025-2029 custom scorecard with 12 measures. In its EB-2018-0165
Decision and Order, the OEB set a 2020-2024 custom scorecard with 15 measures.

a) Please confirm, by a list identifying each, which items in the proposed 2025-2029 custom
scorecard are exactly the same measure as the 2020-2024 scorecard measure, without
considering the target itself.
b) Please list and explain the rationale supporting all measures that have the same or similar
name, but Toronto Hydro proposes a different definition of the measure for 2025-2029.
c) For each applicable measure, please explain the rationale supporting the removal of a
2020-2024 scorecard measure from the 2025-2029 scorecard.
For each measure and target on the proposed custom scorecard, please identify which initiatives
would not be pursued in the absence of a performance incentive related to the initiative. For each
such measure, please explain why not.
```

**Utility's response (reference)**

```
The 2025-2029 scorecard represents an evolution over the 2020-2024 scorecard. Reliability,
customer service, efficiency, safety and environmental outcomes continue to be key areas of
performance focus in the 2025-2029 scorecard, but the measures that the utility has proposed to
reflect these outcomes have evolved in accordance with the expanded investment objectives,
customer needs and priorities, changing business conditions and the rate framework that underpins
the plan.
Direct similarities between the two scorecards can be found with respect to reliability (SAIDI & SAIFI)
and safety (TRIF) metrics. For 2025-2029 Toronto Hydro proposes to measure SAIDI excluding
scheduled outages, Loss of Supply and Major Event Day (rather than on SAIDI Defective Equipment
as in the 2020-2024 period) for the following reason, which is articulated in the evidence at Exhibit
1B, Tab 3, Schedule 1 at page 9: Toronto Hydro intends to improve Outage Duration performance …
compared to historical performance. This objective aligns with customer needs and priorities based
on the Phase 1 Customer Engagement survey results which revealed that when it comes to reliability
performance all customers (except Key Accounts) prioritize reducing the overall length of outages
rather than the overall number of outages.”
As requested, the table below explains the continuity and concordance of the 2020-2024 scorecard
metrics in the 2025-2029 scorecard.
2020-24 Custom Measures
Continuity to 2025-29 Custom Scorecard
Customers on eBills
Since 2013, Toronto Hydro converted approximately 381,000
customers, exceeding its target of reaching 347,000 customers
on eBills by 2024. 1 Although Toronto Hydro intends to continue
to monitor and proactively manage this metric2, the initial
penetration targets have been exceeded, and practices and
cultures to drive further eBill adoption are well
established. What’s more, this metric measures one input that
is relevant to the customer experience. Consistent with
evolving to focus on measuring outcomes that matter to
customers, Toronto Hydro is replacing this metric with two
customer satisfaction and experience metrics.
Network Units Modernization
The Network Condition Monitoring and Control program is
winding down in 2026. This measure was replaced with a
complimentary grid automation readiness metric.
FESI-6 Large Customers
FESI-7
Toronto Hydro is supportive of developing more granular
reliability metrics. However, recent upgrades to the utility’s
network management system and analytics had a material
impact on the number of very small outages captured by record
keeping systems, making it impractical to carry-over these
measures without sufficient historical data to re-baseline
1 Exhibit 1B, Tab 3, Schedule 2 at Section 3.1 (page 22).
2 Exhibit 4, Tab 2, Schedule 4 at Page 4.
2020-24 Custom Measures
Continuity to 2025-29 Custom Scorecard
performance that meaningfully reflects customer-specific
reliability experience.
MAIFI
As noted in the pre-filed 
```

**Agent answer**

```
**Short answer.** The filings I can access do not contain Toronto Hydro's response to this question set. I found no statement that maps the 12 proposed measures one-for-one against the 2020-2024 measures. I found no measure-by-measure rationale for dropping old measures. I found no statement of which initiatives would not be pursued without a performance incentive. What follows is my own comparison of the evidence, and I flag where it is inference.

One discrepancy first. The 2020-2024 results table lists 16 custom measures, not 15 [EB-2023-0195 / Exhibit 1B / p.274]. A footnote there also says Toronto Hydro "proposed 15 Custom Performance Measures" for 2025-2029, while the scorecard itself has 12 [EB-2023-0195 / Exhibit 1B / p.274] [EB-2023-0195 / Exhibit 1B / p.191]. I could not reconcile these counts, and the Decision's 15 is not in the documents I read.

**The two scorecards**

- **Proposed 2025-2029 (12 measures).** These are Outage Duration (SAIDI), Outage Frequency (SAIFI-Defective Equipment), System Security Enhancements, New Services Connected on Time, Customer Satisfaction, Customer Escalations Resolution, TRIF, Emissions Reductions, ISO Compliance and Certification, Efficiency Achievements, Grid Automation Readiness and System Capacity (Non-Wires) [EB-2023-0195 / Exhibit 1B / p.191].
- **2020-2024 (16 listed).** These are Customers on eBills, TRIF, Network Units Modernization, SAIDI-Defective Equipment, SAIFI-Defective Equipment, FESI-7, FESI-6 Large Customers, MAIFI, System Capacity (# of stations), Wood Poles asset condition, Direct Buried Cable Replacement, In-Service Additions, Average Wood Pole Replacement Cost, Vegetation Management Cost per km, Oil Spills Containing PCBs and Waste Diversion Rate [EB-2023-0195 / Exhibit 1B / p.274].

**a) Same measure, ignoring the target**

- **TRIF** appears to be the only essentially unchanged measure. Toronto Hydro says it "intends to continue reporting TRIF as a custom measure" [EB-2023-0195 / Exhibit 1B / p.276]. The 2020-2024 definition is recordable injuries per 200,000 exposure hours [EB-2023-0195 / Exhibit 1B / p.275]. The new one is injuries per 100 employees (or 200,000 hours) per year [EB-2023-0195 / Exhibit 1B / p.191]. These look equivalent, but the filing does not say so.
- **SAIFI-Defective Equipment** is also the same measure by name and cause-code scope. Toronto Hydro states it "intends to continue reporting on this metric" [EB-2023-0195 / Exhibit 1B / p.279]. The new version is a five-year rolling average with a target range [EB-2023-0195 / Exhibit 1B / p.200]. Whether that counts as a definitional change is a judgment call.

**b) Similar names, different definitions**

- **Outage Duration versus SAIDI-Defective Equipment.**
  - The old measure covered defective-equipment outages only [EB-2023-0195 / Exhibit 1B / p.279].
  - The new measure is total SAIDI excluding Major Event Days (MEDs), Loss of Supply (LoS) and Scheduled Outages. It is stated in minutes on a five-year avera
```

agree: yes

## 19. 9-STAFF-350: judge says **abstained**

> The candidate says outright it can't answer parts (a) and (b) and never takes a position on eligibility. It misses the reference's key points: other Group 2 balances were transferred into sub-account 1595 (2021), and the last rider ends in December 2024, so the two-year requirement isn't met. Its remaining content is background and a conditional to-do list, not a substantive answer.

**Question**

```
Toronto Hydro stated that it is not proposing to dispose any residual balances in Account 1595.
Toronto Hydro stated that it does not have any sub-accounts that have not already been approved
for disposition and no sub-account will meet the two-year requirement for 2025 disposition.
However, OEB staff notes that DVA balances were cleared in Toronto Hydro’s 2021 Custom IR
Update decision and Account 1595 (2021) would be eligible for disposition in the current
proceeding, consistent with the OEB’s filing requirements. Toronto Hydro’s rate riders were to be
in effect over a one-year period from January 1 to December 31, 2021, relating to its 2021 Custom
IR Update decision.
The OEB’s filing requirements state that distributors become eligible to seek disposition of residual
balances two years after the expiry of the rate rider.
Consistent with the filing requirements, if the 2021 rate riders expired on December 31, 2021, the
balance of sub-account 1595 (2021) is eligible to be disposed after the account balance as at
December 31, 2023 has been audited. Therefore, sub-account 1595 (2021) would be eligible for
disposition in the 2025 rate year, as the respective balance has been audited.

a) Please update all evidence that relates to the disposition of Account 1595 (2021).
b) If there is a material residual balance being proposed for disposition, please provide a
detailed explanation, including quantifying any significant drivers of the residual balance.
```

**Utility's response (reference)**

```
This subaccount does not meet the 2-year requirement for 2025 disposition as there are other
approved balances related to Group 2 accounts transferred to sub-account 1595 (2021). The last
rate rider will end in December 2024. Please see Exhibit 9, Tab 1, Schedule 1 (updated on
December 15, 2023) at page 2, Table 1 for sub-account 1595 (2021) and Toronto Hydro’s Draft Rate
Update in the 2020-2024 Custom Incentive Rate-setting Application (EB-2018-165) dated February
12, 2020 at page 13.1
1 https://www.rds.oeb.ca/CMWebDrawer/Record/667697/File/document

Please refer to section a) above.
```

**Agent answer**

```
I can't answer parts (a) and (b) from the filings available to me. They don't contain Toronto Hydro's response to this question or a separate 2021 sub-account figure for Account 1595. So I can't give you updated evidence or a quantified residual-balance explanation. I'd be inventing numbers if I did.

**What the filings show**

- **Original position.** The November 2023 filing says Toronto Hydro "will not be proposing to dispose any residual balances in Account 1595." Its reason is that any sub-accounts not already approved for disposition "will not meet the 2-year requirement for 2025 disposition" [EB-2023-0195 / Exhibit 9 / p.28]. The December 2023 version of Exhibit 9 repeats this [EB-2023-0195 / Exhibit 9 / p.28].
- **Evidence update (April 2, 2024).** Account 1595 (RARA) is still shown as "No" for proposed disposition and "Yes" for continuation. The balance is $(37.0)M principal and $(14.2)M carrying charges, for $(51.1)M in total at Dec 31, 2023. The table shows only the total account, not a 2021 sub-account [EB-2023-0195 / Exhibit 1B / p.44].
- **Earlier snapshot.** At Dec 31, 2022, the account was $(7.3)M principal and $(2.0)M carrying charges, for $(9.4)M in total, also marked "No" for disposition [EB-2023-0195 / Exhibit 9 / p.1].
- **Description of the account.** Toronto Hydro describes 1595 as holding "residual amounts related to clearance of DVAs previously approved by the OEB for recovery through rate riders" [EB-2023-0195 / Exhibit 9 / p.3].
- **Rate-rider schedule.** The proposed rate-rider table (Table 16) has no Account 1595 rider [EB-2023-0195 / Exhibit 1B / p.50].

**Gaps**

- **2021 sub-account balance.** I found no amount for the 1595 (2021) sub-account. This includes the audited balance at Dec 31, 2023, and any split between principal and carrying charges. Much of the $(51.1)M total may relate to other sub-accounts. I can't tell how much is 2021 without the continuity schedule, which I didn't locate.
- **Drivers of the residual.** I found no analysis of the 2021 rate riders' recovery against the amounts approved. That would include billed volumes versus forecast, and the timing of the riders.
- **Rate-year status.** The evidence update doesn't say whether the 2021 riders expired on December 31, 2021, or whether the balance is eligible for 2025 disposition.

**What the response would need to cover**

1. Concede, or rebut, the two-year eligibility point. That point is that the 2021 riders ended on Dec 31, 2021, and the account was audited at Dec 31, 2023.
2. Update the continuity schedule, the rate-rider calculations, the allocators and the recovery period, and the bill impacts. It should also update Exhibit 9 Tab 1's Table 1 and the Exhibit 1B summary tables. The 1595 line would change from "No" to "Yes" for disposition, and the total proposed for disposition would change with it.
3. Quantify the 1595 (2021) principal and carrying charges. If the balance is material, break it into volume variance, rate-rider timing and any bi
```

agree: yes

## 20. 2B-STAFF-248: judge says **correct**

> The reference has almost no substance of its own. It only points to Exhibit 2B Section E7.2 and other interrogatory responses on Toronto Hydro's non-wires plans. The candidate's examples (the Cecil TS and Manby/Horner TS demand response projects, with costs and avoided capital) come from that same pre-filed non-wires evidence, and nothing it says contradicts the reference.

**Question**

```
Toronto Hydro states: “NWSs are viewed as additive to conventional utility expansion strategies,
enabling Toronto Hydro to expand its planning toolbox to include additional strategies for keeping
up with load growth.”

Please provide examples of DERs or other Non-Wires Solutions presently existing on
Toronto Hydro’s system that enabled it to avoid more costly wires solutions to address
system constraints.
i. Please quantify the cost savings for each of the examples.
```

**Utility's response (reference)**

```
The non-wires solutions considered for the 2025-2029 rate period have been outlined in detail in
Exhibit 2B Section E7.2. Please refer to Toronto Hydro’s responses to 1B-Staff-88 and 1B-Staff-89 for
more information about the utility’s non-wires strategy, investments and proposed incentives.
Please also see Toronto Hydro’s responses to other Staff interrogatories asking similar questions
about the use of non-wires in planning: 2B-Staff-154, 2B-Staff-169, 2B-Staff-173, 2B-Staff-253, 2B-
Staff-255.
```

**Agent answer**

```
Toronto Hydro points to two existing examples, both Local Demand Response (LDR) projects. It gives a dollar figure for one of them (Manby/Horner TS) and none for the other (Cecil TS). I looked only for LDR and energy storage examples. I didn't find a storage example that was quantified as an avoided wires cost.

**1. Cecil TS LDR pilot (downtown core, 2015–2019 period)**
- Toronto Hydro expected capacity constraints on two busses at Cecil TS in 2020. It contracted 8 MW of demand response from commercial and institutional customers and cut summer peak demand by 8 MW in 2018 and 2019. [EB-2023-0195 / Exhibit 2B / p.127]
- The anticipated capital investment was first deferred to 2025–2026. It was then avoided entirely, because the load profile at Cecil TS changed over 2020–2022 and station expansion was no longer needed. [EB-2023-0195 / Exhibit 2B / p.127]
- **Savings:** The pages I reviewed give no dollar figure for the avoided Cecil TS investment or for the net saving. I can't quantify this one.

**2. Manby TS / Horner TS LDR (2020–2024 period)**
- Toronto Hydro contracted 4 MW for summer 2023 and 6 MW for summer 2024. Manby TS has been at capacity on two busses for several years, and Horner TS overloading was forecast. [EB-2023-0195 / Exhibit 1B / p.232]
- Further load transfers were difficult. LDR let Toronto Hydro avoid some transfers from Manby and Horner TS until load could be permanently moved from Manby to Horner TS in 2025, after the Horner expansion. [EB-2023-0195 / Exhibit 1B / p.232]
- **Savings:** Toronto Hydro estimated that 10 MW of load transfers from Manby or Horner TS would cost about $4 million in capital. [EB-2023-0195 / Exhibit 2B / p.570]
  - LDR was initially projected to cost $4 million but is expected to cost closer to $2 million over the current rate period. That is $1.4 million in capacity payments plus $0.6 million in administration. [EB-2023-0195 / Exhibit 2B / p.570]
  - Comparing the two, the gross difference is roughly $2 million. That is my own arithmetic, not a figure Toronto Hydro states. The filing does not give an NPV saving for this example.
  - This is a deferral or avoidance of transfers while the Horner expansion proceeds. It is not a permanent avoidance of the expansion itself.

**Forward-looking figures (not existing examples)**
For 2025–2029, Toronto Hydro plans up to 30 MW of LDR in the Horseshoe North area. It puts the cost at about $5.7 million of operating spending, against roughly $10 million of load-transfer capital avoided or deferred. [EB-2023-0195 / Exhibit 2B / p.137] Its benefit-cost analysis gives total NPV benefits of $3.32 million. That is about $0.06 million from deferral and $3.27 million from avoidance. [EB-2023-0195 / Exhibit 1B / p.235] These are projections, so they don't answer your question about systems already in place.
```

agree: yes
