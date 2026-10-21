# Judge verdicts: hand-check sample

Seeded sample (seed 20261022) of 20 judge verdicts. For each, read the utility's response and the agent's answer, decide the verdict yourself, and mark `agree: yes` or `agree: no (<your verdict>)`.

**Reviewed by Claude (claude-opus-5-5 in Claude Code), not a human**, on 2026-10-21, at the user's request.
The judge is also a Claude model, so this agreement is weaker evidence than a human check.

## 1. 2B-SEC-69: judge says **abstained**

> The candidate says the evidence has no 2023 data and that it cannot update the figures. It gives only 2018–2022 context and no 2023 values. The reference supplies the updated figures with 2023 data.

**Question**

```
With respect to Overhead System Renewal:

a) Please update Figures 3,4, 7, 8, 13, 14, 21, 22, 26 and 27 with 2023 information.
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
QUESTION (B):
b) [p.9] Please provide a revised version of Table 4 that includes 2017 ACA information, as
well as 2029 ACA information based on the proposed investments included in the DSP.
Please provide in Excel format.

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
please see Toronto Hydro’s resp
```

**Agent answer**

```
**The filings available to me do not contain 2023 data for these figures, so I can't update them.** The Overhead System Renewal evidence (Exhibit 2B, Section E6.5, filed 17 Nov 2023) stops at 2022 actuals. Its tables show 2023 only as a bridge-year cost forecast. I searched for an interrogatory response or any updated version of these figures and found none.

The figure numbers in your request match the Section E6.5 numbering in Exhibit 2B, Part 3 of 3 (rds-823164). I could not locate Figures 3, 4, 7, 8 or 26 directly, so those matches are inferred. Here is what I found for each figure, all of it ending at 2022:

- **Figures 13 and 14** show customers interrupted (CI) and customer hours interrupted (CHI) for poles and pole accessories, 2018–2022 [EB-2023-0195 / Exhibit 2B / p.379]. The text gives only five-year averages of 6,627 CI and 4,700 CHI for poles alone. With accessories, the averages are 30,740 CI and 18,018 CHI.
- **Figures 21 and 22** in Section E6.5 show CI and CHI for overhead switches, 2018–2022 [EB-2023-0195 / Exhibit 2B / p.387]. The filing gives 37,070 CI and about 20,264 CHI per year on average [EB-2023-0195 / Exhibit 2B / p.385].
- **Figures 3, 4, 7, 8, 26 and 27** are in the same section. I did not retrieve them, and they would also need 2023 data from Toronto Hydro. Other figures in the section, such as Figure 19 (wood pole health, 2018–2022), use the same period [EB-2023-0195 / Exhibit 2B / p.383].

Section E6.5's only 2023 value is the segment cost: Overhead System Renewal for 2023 is $32.5M, shown as a bridge-year forecast [EB-2023-0195 / Exhibit 2B / p.397]. It is not a 2023 actual, and it is not the CI, CHI, or condition data these figures plot.

Updating these figures would require Toronto Hydro's 2023 outage records and asset condition data. Those would have to come from the utility, for example through an interrogatory response, and they are not in the documents I can access. I can read the page text for the other figures if you want me to check them individually.
```

agree: yes

## 2. 4-VECC-71: judge says **abstained**

> The candidate says it can't identify the segment or find the FTE, compensation or customer data, and asks the user to clarify. It doesn't give the Customer Relationship Management FTE or compensation figures that are in the reference. The only figures it mentions are unrelated context, not an answer to the question.

**Question**

```
a) For each year 2020 to 2025 (forecast) please provide a table showing the
number of FTEs in this segment, the total compensation and, separately, the number of
residential, GS<50, GS>50 customers in each year (year average).
```

**Utility's response (reference)**

```
This response should be considered in conjunction with Exhibit 4, Tab 2, Schedule 14, Pages 34-46,
which detail a number of functions within this segment where staffing is not directly related to the
changes in the utility’s customer count over the period.
Cost in $ millions
Segment
Actual
Bridge
Forecast
Expense Type
2020
2021
2022
2023
2024
2025
Compensation
5.5
5.2
5.6
6.4
7.8
8.6
Customer Relationship
Management
# of FTEs
Segment
Actual
Bridge
Forecast
2020
2021
2022
2023
2024
2025
Total
37.3
35.2
36.8
41.5
48
50.5
Customer Relationship
Management
For customer numbers by rate class, please refer to Table 2 in Exhibit 3, Tab 1, Schedule 1, at Page
3.
QUESTION (B):
b) What is the assumed customer growth (residential + GS<>50) for the years 2026 through
2029.

Please refer to Table 2 in Exhibit 3, Tab 1, Schedule 1, at Page 3.
Year
Residential
Large
Use
Total
Absolute
Growth
General
Service
<50 kW
%
Growth
Rate
Competitive
Sector
Multi-Unit
Residential
General
Service
50-999
kW
General
Service
1,000-
4,999
kW
2026
Forecast
618,292
100,404
73,632
9,712
462
48
802,551
2,969
0.37%
2027
Forecast
618,985
102,150
73,857
9,725
460
47
805,224
2,674
0.33%
2028
Forecast
619,849
103,674
74,165
9,740
463
46
807,938
2,713
0.34%
2029
Forecast
620,742
104,994
74,455
9,754
461
46
810,452
2,515
0.31%
Note: This table is excluding Streetlighting and Unmetered load customer numbers.
RESPONSES TO VULNERABLE ENERGY CONSUMERS COALITION
INTERROGATORIES
```

**Agent answer**

```
I can't build this table yet. Your question refers to "this segment", and I don't know which segment you mean. I also haven't found the segment-level data it asks for.

- **Segment-level FTEs and compensation:** The Toronto Hydro Exhibit 4 segment write-ups, such as Billing, Remittance and Meter Data Management, give only annual segment costs in $ millions for 2020–2029. Billing, for example, runs from 19.4 in 2020 to 23.7 in 2025 [EB-2023-0195 / Exhibit 4 / p.426]. Those figures cover all costs, not FTEs or total compensation. I haven't found a segment-by-segment FTE or compensation breakdown.
- **Utility-wide FTEs and compensation:** Toronto Hydro's Appendix 2-K (Exhibit 4, Tab 4, Schedule 2) reports FTEs and total compensation for the whole utility, not by segment. The evidence says staffing hit a low of 1,203 FTEs in 2021 [EB-2023-0195 / Exhibit 4 / p.90]. I haven't retrieved the year-by-year numbers.
- **Average customers by class:** I haven't located a table of year-average customer counts for Residential, GS<50 and GS>50 across 2020–2025. The Exhibit 3 load forecast uses customer counts as regression variables [EB-2023-0195 / Exhibit 3 / p.17]. The searches mostly returned the DER and EV forecast tables instead.
- **Hydro One:** I haven't searched the Hydro One application (EB-2026-0164) for this.

Could you tell me one of these?
1. Which segment you mean, and whether it's Toronto Hydro or Hydro One. It may be the Billing, Remittance and Meter Data Management segment or another one.
2. Whether utility-wide Appendix 2-K FTEs and compensation would do instead, with the customer counts shown next to them.

With either answer I can pull the Appendix 2-K and customer-count tables and set them out year by year.
```

agree: yes

## 3. 2B-EP-25: judge says **partially_correct**

> The candidate matches the reference on historical data: it says DER locations are projected from past patterns, by mapping the forecast onto station buses along existing load connection patterns. But the reference says the location forecast also uses generation types and pipeline information to model how likely DER connections are in specific station areas. The candidate leaves out generation types and says the overall forecast (pipeline included) is not location-specific, which undercuts that point.

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
QUESTION (B) - (D):
b) Please describe how Toronto Hydro would act in the event that more customers want to
connect DERs than Toronto Hydro expects in a particular area.
c) How will Toronto Hydro ensure that it is not picking certain neighborhoods, such as only
those that have previously shown demand to connect DERs, at the expense of other
neighbourhoods for being able to benefit from connecting DERs?
d) If a neighbourhood ends up having greater demand for connecting DERs in the future than
Toronto Hydro has planned for, please describe the approach Toronto Hydro would take to
service those customers?

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
Toronto Hydro doesn't pick DER locations by detailed siting. It assumes DERs will connect where load has historically connected.

**Method.** To project where DER capacity will land, Toronto Hydro takes its overall 2029 DER capacity forecast and maps it onto station buses. It assumes that "the geospatial distribution of DERs will continue to follow existing load connection patterns" [EB-2023-0195 / Exhibit 2B / p.201]. This mapping produces the projected short-circuit constraints in Table 4. Those constraints are the basis for expecting that eight station buses will exceed short-circuit capacity by 2029, up from three today [EB-2023-0195 / Exhibit 2B / p.201]. The areas where it expects more DER connections are therefore the buses and feeders that carry the most existing load connections. Grid Protection, Monitoring and Control then addresses short-circuit constraints in those areas.

**Overall forecast.** The overall DER forecast that gets mapped is not location-specific. It rests on historical trends, the project pipeline, the economic environment and current energy policy. That is the basis for the 67% increase you quoted, from 304.9 MW at the end of 2022 to about 516.7 MW at the end of 2029. I did not find that passage in my searches, so it comes from your quote, not a cited page.

**Supporting analysis.**
- Toronto Hydro uses fault and power-flow simulation models to determine short-circuit capacity at stations and other points on the system. These models predict how much fault current will flow to a location from generators across the system. It also runs a study for each new DER application [EB-2023-0195 / Exhibit 2B / p.532].
- The Hydro One and IESO regional planning outlook says it is difficult to predict where future DERs will be located. It therefore makes no further assumptions about future DER growth in its demand outlook [EB-2023-0195 / Exhibit 2B / p.225].
- Toronto Hydro plans to develop a Hosting and Load Capacity Map. It would show estimated available DER capacity at different locations, based on automated analysis [EB-2023-0195 / Exhibit 2B / p.681].
- Monitoring and control data from connected DERs would feed hosting capacity analyses. Currently, connection potential is assessed using conservative estimated thermal loading, which assumes DERs generate at 100% of rated capacity [EB-2023-0195 / Exhibit 2B / p.207].

**Limitation.** The location forecast is an assumption that the future will resemble the past. It is not based on site-specific customer siting data.
```

agree: yes

## 4. 1B-STAFF-62: judge says **correct**

> Like the reference, the candidate traces the rising SAIDI benchmark to the rising CAIDI benchmark, driven by the increasing congested-urban variable. It also cites that variable's high statistical significance in the CAIDI model (t-stat 8.63), which is the empirical evidence the reference relies on. It presents the link as an inference and says it found no physical evidence, but it does not contradict the reference.

**Question**

```
Clearspring provides benchmarking values for SAIFI, SAIDI and CAIDI.

a. Why is there the expectation that the SAIDI benchmark value increase with time? What
is the physical justification for this versus theoretical modelling? Please provide empirical
quantitative evidence and not qualitative correlation explanation.
```

**Utility's response (reference)**

```
This stems primarily from the CAIDI benchmark increasing due to the congested urban variable
increasing for Toronto Hydro over time. As congestion increases, the time required to respond
increases. The empirical quantitative evidence is the highly statistically significant congested urban
variable present in the CAIDI model.
QUESTIONS (B)
b) How does the proposed benchmark and forecasted SAIFI, CAIDI and SAIDI values differ in
consideration of Toronto Hydro’s proposed IRM as compared to the IRM scenario in
Reference 2?

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

```

**Agent answer**

```
The filings I can access don't give the empirical, physical justification you're asking for. They show that the rising SAIDI benchmark is a mechanical output of the model. I found no outage-physics evidence, and no separate test showing that benchmark SAIDI should rise.

**What the filing shows**

- Clearspring's SAIDI benchmark for Toronto Hydro rises from 50.7 in 2005 to 60.3 in 2022. It then rises to 71.1 by 2029, which is 64.3 in 2025 and 71.1 in 2029 within the Custom IR period [EB-2023-0195 / Exhibit 1B / p.365].
- SAIDI is not modelled directly. It is the product of the SAIFI and CAIDI benchmarks, because SAIDI = SAIFI × CAIDI [EB-2023-0195 / Exhibit 1B / p.359]. The study estimates only SAIFI and CAIDI models [EB-2023-0195 / Exhibit 1B / p.359].
- The SAIFI benchmark is roughly flat to slightly falling, from 0.46 in 2005 to 0.43 in 2022 [EB-2023-0195 / Exhibit 1B / p.339].
- The CAIDI benchmark is what rises, from 110.0 in 2005 to 138.95 in 2022 [EB-2023-0195 / Exhibit 1B / p.339]. So the upward SAIDI benchmark comes from the CAIDI side.

**What drives the CAIDI benchmark**

- The CAIDI model's variables are customers, % forestation, standard deviation of elevation, sq. km per customer, and % congested urban. The congested-urban coefficient is 20.199 with a t-statistic of 8.63 [EB-2023-0195 / Exhibit 1B / p.363].
- Only some of these inputs change over time for Toronto Hydro. The congested-urban variable is the one the filing explicitly makes time-varying in the cost study. I did not confirm that the same time-varying variable feeds the reliability models.
- In the cost study, Clearspring scales the variable using high-rise (100 m+) building counts from the Council on Tall Buildings and Urban Habitat (CTBUH). A 1% change in the number of high-rises is estimated to change the congested-urban variable by 0.63% [EB-2023-0195 / Exhibit 1B / p.345] [EB-2023-0195 / Exhibit 1B / p.346].
- Toronto's high-rise count grew at an average of 7.1% a year from 2012 to 2022. Future years are projected using that 10-year growth rate [EB-2023-0195 / Exhibit 1B / p.346].
- I infer, but the filing doesn't say outright, that this projected growth is the likely driver of the rising CAIDI and SAIDI benchmarks. I did not find a decomposition that confirms it.

**What I did not find**

- I found no empirical outage data, such as restoration-time studies for underground or congested networks, that tests the claim that benchmark SAIDI should rise.
- I found no out-of-sample test of the projected benchmark values.
- The sample is 80 U.S. distributors plus Toronto Hydro. The U.S. reliability data comes from EIA Form 861, which starts in 2013. The model estimates exclude Toronto Hydro itself [EB-2023-0195 / Exhibit 1B / p.359] [EB-2023-0195 / Exhibit 1B / p.360]. The benchmarks before 2013 and after 2021 therefore rest on extrapolated variable values. They do not rest on observed U.S. outcomes in those years.

Your question reads like an interrogatory, so the answer m
```

agree: yes

## 5. 1A-PP-2: judge says **abstained**

> The reference says THESL's CDM results achieved by 2024 are set out in the LRAMVA evidence (Exhibit 9, Tab 2, Schedule 3) and in 9-Staff-354. The candidate says the filings don't give these results and points instead to the load-forecast appendices. It adds methodology and provincial background but gives no Toronto Hydro achieved-results figures, so it is effectively an abstention.

**Question**

```
THESL indicates that it has “Enhanced the load forecast to consider electrification drivers and
changes to the availability of conservation and demand management (“CDM”) savings in producing
the revenue forecast that underpins to 2025-2029 rates”

a) Please provide what CDM results THESL will have achieved by end of the 2024 rate term
against the total achievable CDM results and what potential remains, by sector if possible
```

**Utility's response (reference)**

```
Please refer to Exhibit 9, Tab 2, Schedule 3 and 9-Staff-354 which indicates CDM results THESL has
achieved as part of LRAMVA by 2024.
QUESTION (B):
b) Please indicate what CDM results (total and incremental to those forecasted to the end of
the current rate plan) are forecasted to be achieved by year of the 2025-2029 rate plan.
Please indicate what portion of the total potential achievable CDM results that will
represent.

The Province’s CDM Framework for 2025-2029 is not yet finalized. Since 2019, the role for LDCs in
CDM has reduced significantly relative to prior periods. Accordingly, in this Application, Toronto
Hydro is not forecasting LDC-led savings as part of CDM Framework during the 2025-2029 period.
QUESTION (C):
c) Please explain why only CDM is included in the above noted item and not the broader
scope of DER.

The reference to “electrification drivers” includes DERs. Toronto Hydro includes DER impacts in its
load forecast. Please refer to Exhibit 3, Tab 1, Schedule 1, Appendix J for a description of the
integration of DER impacts into the load forecast.
```

**Agent answer**

```
I'm wrapping up the search. The filings don't seem to hold a Toronto Hydro-specific answer, so I'm writing up what they do contain.

**Short answer:** The filings available to me don't state what CDM results Toronto Hydro (THESL) will have achieved by the end of 2024. They also don't give a "total achievable" CDM figure, a remaining-potential figure, or a split of either by sector. I found no achievable-potential study for its service territory.

**Why the numbers aren't there**
- The IESO no longer provides CDM savings forecasts or program results for distributors' service territories. Since the Conservation First Framework ended in 2019, CDM delivery has been provincially centralized under the IESO [EB-2023-0195 / Exhibit 3 / p.10].
- Toronto Hydro now enters CDM as a variable in its load-forecast regression. It does not track CDM against a target. It builds the variable from cumulative savings for 2006–2029, split into residential savings (used in the Residential class model) and business savings (used in the General Service models) [EB-2023-0195 / Exhibit 3 / p.12].
- The variable has four components [EB-2023-0195 / Exhibit 3 / p.12]:
  - Verified IESO results for 2006–2017.
  - Unverified post-CFF savings for 2015–2022.
  - 2021–2024 savings extrapolated from the IESO's provincial plan.
  - 2025–2029 savings, assumed to continue at "status quo" delivery.
- The 2021–2024 portion is a scaled-down share of the provincial plan, based on Toronto Hydro's 2015–2017 ratio of its savings to provincial savings [EB-2023-0195 / Exhibit 3 / p.13][EB-2023-0195 / Exhibit 3 / p.14]. The year-by-year Toronto Hydro numbers are in Exhibit 3, Tab 1, Schedule 1, Appendices C, D and E. Those appendices did not come up in my searches or table queries.
- The April 2024 evidence update says Appendices C, D and E were revised to include 2021–2022 actuals under the 2021–2024 framework [EB-2023-0195 / THESL_2025-2029 Rate Application_Evidence Update_20240402 / p.5]. So even the 2021–2022 portion is partly actuals, and 2023–2024 remain forecasts.

**Provincial context (not Toronto Hydro-specific)**
- The IESO's 2021–2024 CDM Framework plan targets about 725 MW of peak demand savings and 3.8 TWh of energy savings by 2026. The budget is up to $1.034 billion [EB-2023-0195 / Exhibit 3 / p.54][EB-2023-0195 / Exhibit 3 / p.56].
- The plan's annual provincial energy savings rise from about 357 GWh in 2021 to about 1,575 GWh in 2024. The table is only partly legible, so I'm reading these as running totals [EB-2023-0195 / Exhibit 3 / p.56].
- The plan breaks savings out by program, such as Retrofit, Small Business and Energy Affordability, not by residential versus business sector. I can't turn this into a Toronto Hydro share or a remaining-potential number without inventing one.
- The 2019–2020 Interim Framework hit 106% of its energy target provincially (1,516.9 GWh against 1,429.4 GWh) [EB-2023-0195 / Exhibit 3 / p.51]. That is a past result and says nothing about 2024.

**Wh
```

agree: yes

## 6. 2B-STAFF-187: judge says **partially_correct**

> The candidate correctly identifies GPMC and Non-Wires Solutions as DER-hosting capital and covers the grid modernization investments. However, it says DER-hosting capital is limited to two programs and treats Sheppard TS only as a side benefit of a load-driven expansion, so it misses the reference's third program (Station Expansion – Sheppard TS). Its answer to part (b) also differs from the reference, which says some of these expenditures may enable hosting capacity beyond the test period.

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
**Short answer:** The filings available to me don't split capital between DERs that connect within 2025–2029 and DERs that connect after 2029. No program is labelled that way. The only DER-hosting capital I found is in two programs. Toronto Hydro describes both as serving DER growth forecast through 2029, and says nothing about connections after 2029.

**Context for the quoted statement.** The "no net expenditure" sentence applies only to the Generation Connection segment. Customer capital contributions recover the project costs of connecting DERs [EB-2023-0195 / Exhibit 2B / p.117]. The hosting-capacity investments below sit in separate programs and are funded by the utility.

**a) Capital for DERs connecting within 2025–2029**

- **Generation Protection, Monitoring and Control (GPMC) program, $35.0M over 2025–2029** [EB-2023-0195 / Exhibit 2B / p.212]. It is customer-driven, and the investment is sized to the 2023–2029 DER connection forecast. That forecast reaches about 516.7 MW by 2029 [EB-2023-0195 / Exhibit 2B / p.198].
  - **Monitoring and control systems (MCS), about $14.5M.** These are installed at renewable DER sites as connections occur, at about $25,000 per site [EB-2023-0195 / Exhibit 2B / p.213].
  - **Bus-tie reactors, $20.4M.** They mitigate short-circuit limits at six Hydro One-owned transformer stations, with one installed per year from 2025 [EB-2023-0195 / Exhibit 2B / p.212]:

| Year | Station |
|---|---|
| 2025 | Richview |
| 2026 | Runnymede |
| 2027 | Cecil |
| 2028 | Esplanade |
| 2029 | Leslie and Woodbridge |

  The bus-tie reactors address eight stations that Toronto Hydro expects to exceed short-circuit capacity by 2029 [EB-2023-0195 / Exhibit 2B / p.201]. Annual program costs run $5.9M, $6.1M, $6.3M, $6.5M and $10.3M for 2025–2029 [EB-2023-0195 / Exhibit 2B / p.212].

- **Renewable-enabling energy storage systems (Non-Wires Solutions program), $22.5M.** Toronto Hydro plans nine systems totalling 10.2 MW on nine feeders. The feeders were chosen because of forecast generation-to-minimum-load ratios over 2025–2029 [EB-2023-0195 / Exhibit 2B / p.687] [EB-2023-0195 / Exhibit 2A / p.380].

**b) Capital for DERs connecting beyond the test period**

The filings don't identify any capital intended specifically for post-2029 connections. These are the nearest items:

- Toronto Hydro says MCS data will feed hosting-capacity analysis and "lay the foundation" for longer-term DER management. It also says this has "long-term value" for planning future DER connections [EB-2023-0195 / Exhibit 2B / p.207] [EB-2023-0195 / Exhibit 2B / p.198]. The spending is still part of the GPMC program above.
- Toronto Hydro notes that the Future Energy Scenarios high case (Net Zero by 2040) could reach 1,249 MW by 2029 and "could require significant investment in hosting capacity expansion, grid modernization, and innovation." No funding is requested for that scenario in this passage [EB-2023-0195 / Exhibit 2B / p.198].
- Toronto Hydro says it won't
```

agree: yes

## 7. 1B-CCC-32: judge says **correct**

> The candidate matches the reference's main points. It says the 0% productivity factor rests on OEB policy, gives the combined X-factor as 0.75%, and puts the total customer rate reduction at about $81.4M, which is a rounding-level difference from the reference's $81.5M. It also notes the added benefits from meeting the Performance Incentive Mechanism (PIM) targets. Nothing in it contradicts the reference.

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
A 0% productivity factor is appropriate, in Toronto Hydro's filing, because it follows OEB policy. The filing does not set out the OEB's reasoning for that policy in the pages I retrieved. Toronto Hydro's X-factor is 0.75%, and ratepayers get their benefit from the two components added on top of the 0% [EB-2023-0195 / Exhibit 1B / p.77].

**Why 0% is appropriate**
- The 0% is described as "consistent with OEB policy" [EB-2023-0195 / Exhibit 1B / p.77]. The OEB's usual (standard) approach to setting the X-factor is the Rate Handbook framework, which the filing cites as EB-2010-0379 [EB-2023-0195 / Exhibit 1B / p.77].
- I did not find the underlying industry productivity study or OEB reasoning for the 0% value in these pages. I can't say more than that Toronto Hydro relies on policy.
- Company-specific performance is dealt with through the other two components. A Clearspring total cost benchmarking study found Toronto Hydro's costs were about 22.9% below benchmark over 2025–2029. That score falls in the OEB's 0.15% stretch cohort (scores between -25% and -10%) [EB-2023-0195 / Exhibit 1B / p.340].

**How ratepayers benefit**
- The X-factor is 0.75%, made up of 0% productivity, a 0.15% efficiency factor from the benchmarking, and a 0.6% proactive performance factor [EB-2023-0195 / Exhibit 1B / p.77].
- Toronto Hydro says the benchmarking supports only 0.15% and that this "ordinarily should be used" for setting rates. It proposes the higher 0.75% anyway [EB-2023-0195 / Exhibit 1B / p.80].
- The 0.15% efficiency factor reduces revenue by about $16.4 million over the rate period. Toronto Hydro takes that risk up front, so customers get the rate reduction during the period [EB-2023-0195 / Exhibit 1B / p.77].
- The 0.6% factor gives customers an upfront rate reduction of about $65 million. Together, the X-factor constrains revenue by about $81.4 million over the term [EB-2023-0195 / Exhibit 1B / p.186].
- Toronto Hydro can earn back the $65 million only by meeting targets on its Custom Scorecard through the Performance Incentive Mechanism. If targets are missed, ratepayers keep some or all of the reduction, and the utility can't earn its approved return on equity [EB-2023-0195 / Exhibit 1B / p.80].
- The Scorecard and investment plan are said to deliver quantified customer benefits of roughly $90 million to $216 million (nominal) over 2025–2029 [EB-2023-0195 / Exhibit 1B / p.186].
- The 0.75% is higher than the OEB-approved X-factor under standard price cap regulation [EB-2023-0195 / Exhibit 1B / p.56].
- Under the prior 2020–2024 framework, the blended X-factor was about 0.81–0.82% [EB-2023-0195 / Exhibit 1B / p.64]. The new 0.75% is slightly lower, but it applies to all revenue requirement, with a possible earn-back of up to 0.6% [EB-2023-0195 / Exhibit 1B / p.64].

All of this is Toronto Hydro's own evidence. I did not look for OEB staff or intervenor positions, or for any decision on the point.
```

agree: yes

## 8. 2B-STAFF-231: judge says **correct**

> The reference says Toronto Hydro hasn't specifically assessed how a summer or winter peak affects transformer useful life, and that it remains summer-peaking for this rate period. The candidate matches both points: the filings don't tie the 45-year life to the season of the peak, and Toronto Hydro is summer-peaking today, with a shift to winter peaking expected later. Its suggestion that a winter peaker could see a longer life is clearly labelled as general reasoning and doesn't contradict the reference.

**Question**

```
Toronto Hydro states: “The useful life of a power transformer is 45 years.”

a) Would the same useful life apply to a transformer in a winter peaking system?
```

**Utility's response (reference)**

```
Toronto Hydro has not specifically assessed the impact of summer vs. winter peak on the useful life
of transformers. Based on the System Peak Demand Forecast in Exhibit 2B, Section D4 (updated
January 29, 2024), Toronto Hydro remains a summer peaking utility for this rate period.
QUESTION (B):
b) Toronto Hydro forecasts that it will become a winter peaking system. Should it be
modifying the planning criteria it applies to make station asset investment decisions, since
most station asset types will have higher capacity ratings in winter peak ambient
temperature conditions than they will in summer peak ambient temperature conditions.

As noted in the response to part (a), Toronto Hydro remains a summer peaking utility for this rate
period. The planning criteria used assesses the maximum ratio of load to transformer capacity, and
considers all seasons. If and when Toronto Hydro’s system evolves to a winter-peaking system, this
criteria will not be affected.
```

**Agent answer**

```
**Short answer:** The filings don't say. I found nothing that sets a different useful life for a transformer in a winter-peaking system. I also couldn't find the exact sentence you quote.

**What the filings do say**
- Toronto Hydro's depreciation study sets one life for power transformers in its stations: about 45 years (Iowa 45-R3). The study bases it on three inputs:
  - an observed retirement-rate analysis;
  - peer and Kinetrics ranges of 30–55 or 30–60 years;
  - Toronto Hydro staff's view that about 45 years is reasonable, with engineering planning at 44 years.
  
  [EB-2023-0195 / Exhibit 2A / p.42] [EB-2023-0195 / Exhibit 2A / p.44]
- The study says nothing about the season of the system peak. It does not tie the life to summer or winter loading. The 45 years is a statistical average-service-life assumption for the asset class. It is not a thermal or loading-based rating.
- Toronto Hydro describes itself as summer-peaking today. Its climate-risk work puts the base-year peak at 3.9 GW in summer against 3.7 GW in winter. It expects the system to shift to winter peaking in the 2030s as heat pumps and electric vehicles grow. [EB-2023-0195 / Exhibit 2B / p.647]
- In the climate-risk assessment, high ambient temperature is the stress on station power transformers. It raises air-conditioning load and reduces cooling effectiveness. That assessment uses an "expected service life" of 20.55 years (180,000 hours) at a 110 °C hot-spot limit and 30 °C ambient. [EB-2023-0195 / Exhibit 2B / p.173] [EB-2023-0195 / Exhibit 2B / p.311]

**What this means for your question**
- Cooler winter ambient temperatures generally ease transformer thermal stress, so a winter peaker could plausibly see a longer physical life. That is general engineering reasoning, not something the filings state.
- The filings also don't say Toronto Hydro would adjust the 45-year accounting life for a winter-peaking utility. The life is set from retirement experience, peer ranges and judgment. Actual life also depends on loading, condition and maintenance. Toronto Hydro says it replaces station transformers "based on age and asset health condition assessments." [EB-2023-0195 / Exhibit 2A / p.42]

To confirm the exact wording and context of your quote, please give me the exhibit or interrogatory it comes from. If it's an interrogatory response, it may add context that I haven't found.
```

agree: yes

## 9. 2B-STAFF-161: judge says **partially_correct**

> The candidate covers two of the reference's examples: network condition monitoring and control, and station digital relays. It misses the reference's key clarification that "specific nodes" means positions in the system's design rather than geography, and it does not present AMI 2.0 meters as the customer-level example. Instead it frames the answer around geographic and feeder-level targeting.

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
The filings I can access do not give a site-by-site list of where Toronto Hydro will install these sensors and relays. They also do not explain why those sites differ from the rest of the territory. What they give is a set of example locations and the selection criteria below.

**Selection criteria**
- The Grid Modernization Strategy says System Observability programs will "focus on service areas with significant operational value (e.g., DER-rich feeders, feeders with poor visibility, feeders with poor reliability, etc.)" [EB-2023-0195 / Exhibit 2B / p.664].
- Toronto Hydro says it will run smaller pilots before any large-scale rollout. It intends to develop a "fully formed observability strategy" for 2030-2034 [EB-2023-0195 / Exhibit 2B / p.664].
- The capital plan describes the deployment as "strategic" and aimed at "critical points on the grid" [EB-2023-0195 / Exhibit 2B / p.544]. It also refers to visibility "at strategic locations" [EB-2023-0195 / Exhibit 2B / p.555].

**Representative examples and the reasons given**
1. **Overhead and underground line sensors, in parts of the grid that have no visibility today.**
   - Toronto Hydro currently depends largely on customer calls to learn of a localized outage. Directional sensors would alert the control room in real time and help narrow fault locations [EB-2023-0195 / Exhibit 2B / p.545].
   - They would "introduce and expand visibility to parts of the grid where it has not traditionally been available" [EB-2023-0195 / Exhibit 2B / p.545].
   - The underground system is where outage causes are harder to identify and restoration can take longer, because the assets are not visible to crews [EB-2023-0195 / Exhibit 2B / p.61].

2. **Online cable monitoring (fibre-based distributed temperature sensing) on underground cables that are costly to access.**
   - The named example is the Western Gap Utility Tunnel between Toronto Island and the mainland. Its cables sit in a tunnel pressurised with lake water, which makes inspection and maintenance costly [EB-2023-0195 / Exhibit 2B / p.546].
   - More generally, these monitors suit parts of the system with physical or access constraints. They would complement the cable testing program, since partial-discharge testing of cables is lengthy and manual [EB-2023-0195 / Exhibit 2B / p.546].
   - Fibre must be in place before a monitor is installed. Toronto Hydro flags that planners need to ensure fibre is installed first at optimum locations that lack it [EB-2023-0195 / Exhibit 2B / p.557].

3. **Transformer monitors on the secondary distribution system.**
   - The stated driver is higher load from electric vehicle adoption and greater residential density in the City of Toronto. The monitors would measure actual transformer loading rather than aggregating customer meter loads [EB-2023-0195 / Exhibit 2B / p.547].
   - The filing does not name specific neighbourhoods or transformers.

4. **Network vaults in the downtown core (Network Condition Monitoring & Control
```

agree: yes

## 10. 1-ED-02: judge says **correct**

> For part a), the reference only refers to 1B-DRC-06 part d) and gives no figures of its own, so the candidate has nothing to contradict. The candidate gives a real answer drawn from the evidence: a range of 0.3–1% of revenues, with Ofgem RIIO-2, New York REV and Enbridge's ETTF as comparators. It also notes, correctly, that the evidence doesn't fully set out the analysis.

**Question**

```
a) Toronto Hydro states that its proposed Innovation Fund “is the low end of a range found in
research of comparable ratepayer-funded initiatives aimed at facilitating innovation by
utilities and regulatory bodies in other jurisdictions, as well as general data on utility
spending for research and development activities.” Please provide this analysis.
```

**Utility's response (reference)**

```
Please see Toronto Hydro’s response to interrogatory 1B-DRC-06 part d).
QUESTION (B):
b) If Toronto Hydro were to set its Innovation Fund budget at the mid-range of comparable
initiatives, what would the budget be?

If Toronto Hydro was to fund its Innovation Fund through a rate rider based on the mid-range of
what it found in its research, Toronto Hydro would calculate an amount equal to 0.5% of its
Revenue Requirement instead of 0.3%, which would result in approximately $27 million of funding
for the Innovation Fund.
QUESTION (C):
c) What additional activities would Toronto Hydro undertake with a mid-range Innovation Fund
budget?

The activities described in the four phases of the Governance Framework present a methodology,
which is flexible with respect to budget, since it provides a roadmap for implementation rather
than setting the scope of work. In contrast, the areas of innovation that can be addressed and the
pilot projects that can be undertaken in connection with areas of innovation are affected by
budget. Since Toronto Hydro has proposed the Innovation Fund to be at the low end of the range
of funding found in its research, it has not considered what additional activities it might be able to
undertake with a mid-range budget. However, the effect of a larger budget would likely be that
Toronto Hydro could propose more areas of innovation and/or more pilot projects or larger scale
pilot projects within the planned areas of innovation.
QUESTION (D):
d) How will the Innovation Fund rate rider be charged to residential customers - variable or
fixed?

The Innovation Fund Rate Rider will be charged to residential customers as a fixed charge, consistent
with the Distribution Revenue rate design for these classes. For a breakdown of how the Innovation
Fund Rate Rider will be collected over the rate period, see Exhibit 9, Tab 3, Schedule 1 (Rate Rider
Table).
QUESTION (E):
e) Is Toronto Hydro open to other Ontario utilities participating in its Innovation Fund pilots
and benefiting from the results?

Please see Toronto Hydro’s response to interrogatory 1B-CCC-46 part a).
```

**Agent answer**

```
The filings don't contain a standalone analysis, study or workpaper behind that statement. They contain a short summary of the research in Exhibit 1B, Tab 4, Schedule 2, Section 2. I searched only for the research behind the Innovation Fund statement. I did not look through interrogatory responses or other exhibits.

**Where the statement appears.** The "low end of a range" sentence is in the Exhibit 1B overview (Section 3.2.2). It says Toronto Hydro allocated 0.3 percent of the proposed revenue requirement, about $16 million over 2025–2029, to the fund [EB-2023-0195 / Exhibit 1B / p.92][EB-2023-0195 / Exhibit 1B / p.84].

**The range.** Section 2 of the Innovation Fund proposal says Toronto Hydro's research found that utility investments in comparable innovation initiatives and R&D activities "range from 0.3 to 1 percent of revenues." It therefore proposes 0.3 percent, or about $16 million [EB-2023-0195 / Exhibit 1B / p.459].

**The comparators it cites** [EB-2023-0195 / Exhibit 1B / p.459][EB-2023-0195 / Exhibit 1B / p.460]:
- **UK, Ofgem RIIO-2:** networks may recover 0.5 to 1 percent of base revenues for innovation. The projects are those that facilitate decarbonization while lowering network costs, address consumer vulnerability, or deliver longer-term financial or environmental benefits.
- **New York, Reforming the Energy Vision (REV):** utilities can recover 0.5 percent of their total revenue requirement, up to a maximum of $10 million per year. This covers REV demonstration projects that advance new utility and third-party service or business models, or enable DER integration without hurting reliability.
- **Ontario, Enbridge Gas Energy Transition Technology Fund (ETTF):** Enbridge proposed $25 million, about 0.4 percent of the test-year revenue requirement. The source is cited as EB-2022-0200, Exhibit 1, Tab 10, Schedule 7. The filing describes this as a proposal, not an approved amount.

**Qualitative examples.** A separate appendix lists regulatory mechanisms that have enabled utility innovation. They include the FortisBC Clean Growth Innovation Fund, the Nova Scotia (NSUARB) innovation justification criteria, Ofgem's Network Innovation Allowance and the OEB Innovation Sandbox. The excerpt I saw gives no funding percentages for these [EB-2023-0195 / Exhibit 1B / p.484].

**What the filings don't show.** The "general data on utility spending for research and development" is not identified or quantified. The only figures given are the three comparators above, and the bottom of the range, 0.3 percent, is not tied to any named comparator. Each comparator is at 0.4 percent or higher, so 0.3 percent is at or below all of them. The filings also don't say how the range was built or what else was considered.

If you want the underlying analysis, ask Toronto Hydro for it in an interrogatory. It would need to include the full list of jurisdictions and sources, the R&D spending data, and the calculations behind 0.3 to 1 percent.
```

agree: yes

## 11. 2B-ED-30: judge says **partially_correct**

> The candidate gets the core figures right. It has $5.7M of opex for local demand response, and it has $22.5M of BESS capex, split 94% provincial and 6% rate base. That works out to about $21.2M and $1.35M, which matches the reference's $21.2M and $1.4M, and it correctly calls the storage assets new. However, it says the filing doesn't show whether demand response will come from new or existing DERs, while the reference states it contracts existing customer-owned DERs. It also adds $35M of generation-protection capex, which pushes its total to about $63M, outside the reference's scope. The reference itself says Toronto Hydro proposes no net spending on DER connections.

**Question**

```
a) Please provide a table showing the forecast spending on distributed energy resources
(DER) in each year, and total over the five-year term, with a breakdown by (i) type of DER
(efficiency, demand response, storage, etc.), (ii) cost amount by source of funding
(ratepayers, government, etc.), (iii) capital versus operational spending, and (iv) whether
the spending is likely to be on new DERs facilities versus existing DERs (e.g. contracting for
an addition service from a pre-existing generator).
```

**Utility's response (reference)**

```
Please see Table 1 below; please note that this table covers equipment or programs owned and
operated by Toronto Hydro and does not address privately owned DERs.
Table 1: Forecasted Spending on DERs
Leveraging existing assets
DER Type
Forecasted Rate-
based spend
Forecasted
Provincial spend
(yes/no)
Local Demand Response1
$5.7 million
(OPEX)
None
Yes, contracts for services from
existing customer owned DERs
$21.2 million
Energy Storage2
$1.4 million
(CAPEX)
(CAPEX)
No, these are new assets
Please note that all project expenses and operational costs to facilitate the connections of DER are
recovered from customers. Toronto Hydro does not propose any net expenditure for DER
Connections for the years 2025 to 2029.
1 Non-Wires Solutions Program, Exhibit 2B, Section E7.2, pages 1-17.
2 Non-Wires Solutions Program, Exhibit 2B, Section E7.2, pages 13-34.
```

**Agent answer**

```
This answer covers Toronto Hydro (EB-2023-0195) only. The filings don't give one consolidated DER spending table with all four breakdowns. I built the table below from three program tables and the funding rules in the filing. I found no DER spending forecast for Hydro One (EB-2026-0164): two searches limited to that case returned errors, and an unfiltered search returned only Toronto Hydro material. So I can't say whether Hydro One has comparable figures.

**Toronto Hydro 2025–2029 DER-related spending ($M, nominal)**

| Program | Type of DER | Capex / Opex | 2025 | 2026 | 2027 | 2028 | 2029 | Total |
|---|---|---|---|---|---|---|---|---|
| Renewable-enabling battery storage (BESS) | Storage | Capex | 3.6 | 3.6 | 7.5 | 3.8 | 4.0 | 22.5 [EB-2023-0195 / Exhibit 2B / p.589] |
| Generation protection: bus-tie reactors | Connection enabling (solar, storage, other generation) | Capex | 3.2 | 3.3 | 3.4 | 3.5 | 7.1 | 20.4 [EB-2023-0195 / Exhibit 2B / p.212] |
| Generation protection: monitoring and control | Connection enabling (solar, storage, other generation) | Capex | 2.6 | 2.8 | 2.9 | 3.0 | 3.2 | 14.5 (sum of the rounded annual figures) [EB-2023-0195 / Exhibit 2B / p.212] |
| Flexibility Services (local demand response) | Demand response | Opex | 0.2 | 0.9 | 1.1 | 1.6 | 1.9 | 5.7 [EB-2023-0195 / Exhibit 2B / p.138] |
| **Total** | | | **9.6** | **10.6** | **14.9** | **11.9** | **17.1** | **~63.2** |

- The monitoring-and-control line is the filed program total of $35.0M minus the bus-tie reactor total of $20.4M. The filed annual totals for the generation-protection program are 5.9, 6.1, 6.3, 6.5 and 10.3, which sum to $35.1M (shown as $35.0M) [EB-2023-0195 / Exhibit 2B / p.212].
- Efficiency/CDM is not in this table. I found no energy-efficiency spending in these DER programs.

**(i) Type.** The spending is storage (BESS), demand response (Flexibility Services) and grid upgrades that let customers' DERs connect (bus-tie reactors, monitoring and control).
- The BESS plan is nine projects totalling 10.2 MW, deployed 1, 2, 2, 2 and 2 across 2025–2029. They are aimed at feeders where solar penetration is high [EB-2023-0195 / Exhibit 2B / p.590].
- Flexibility Services targets are 10 MW in 2026, 15 MW in 2027, 25 MW in 2028 and 30 MW in 2029 [EB-2023-0195 / Exhibit 2B / p.138].

**(ii) Source of funding.**
- **Renewable-enabling BESS:** 94% comes from the provincial renewable-enabling-improvement revenue stream, which is recovered from Ontario ratepayers generally. The other 6% goes into Toronto Hydro's rate base [EB-2023-0195 / Exhibit 2B / p.590]. The filing says this 6% share is $1.6M, but 6% of $22.5M is about $1.35M. I flag the discrepancy rather than resolve it.
- **Generation protection:** the same exhibit lists it as a renewable-enabling improvement [EB-2023-0195 / Exhibit 2A / p.382]. I did not see its provincial/local split stated on the pages I read.
- **Flexibility Services:** this is operating cost, so it is recovered from Toronto Hydro's ow
```

agree: yes

## 12. 1B-AMPCO-12: judge says **abstained**

> The candidate says outright that the evidence doesn't explain why the two categories were dropped. The reference gives two reasons: overhead switches vary too much across utilities in how they are selected, installed and accounted for, and switchgear replacements were too few and sporadic to compare. It also mentions alignment with the Activity Based Performance Benchmarking asset classes. The candidate covers the study's scope and only floats thin peer data as something to ask Toronto Hydro about, so it gives no substantive answer.

**Question**

```
At Reference #1, Toronto Hydro filed a UMS Unit Costs Benchmarking Study. At Reference #2,
Toronto Hydro filed an updated UMS Unit Costs Benchmarking Study dated October 2023.

a) Please explain why unit costs for OH Switch Replacement and Switchgear Replacement
were included in the EB-2018-0165 study but not included in the October 2023 UMS Study.
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
QUESTION (B):
b) Please provide the unit costs for OH Switch Replacement and Switchgear Replacement if
calculated as part of UMS’ work for the October 2023 study but not included in the report.

The OH Switch Replacement and Switchgear Replacement was excluded from the October 2023
study, and thus there was no calculation for unit cost.
QUESTION (C):
c) Please provide the drivers for the increase in unit costs in the October 2023 UMS study
compared to the EB-2018-0165 UMS Study for the following asset categories: UG Cable,
Pole Top Transformers, Padmount/UG Transformer, Network Transformer Replacement
and Breaker.

We have noted a general increase in costs across the industry over the past three years, driven
largely by inflation (including its effect on commodity prices), supply chain challenges (limited
manufacturing capability and excessive lead times, causing demand to exceed supply resulting in
increased prices), and COVID related policies, most notably the requirement that individuals be in
separate vehicles thus increasing crew size and fleet / heavy equipment costs. We understand that
the industry is only recently beginning to relax COVID-related restrictions, but inflation and supply
chain issues have remained an issue.

For Toronto Hydro, the increases can be attributed to various factors, including but not limited to
inflation and supply chain i
```

**Agent answer**

```
The filings available to me don't say why OH Switch Replacement and Switchgear Replacement unit costs were in the earlier study but not in the October 2023 UMS study. I found no interrogatory response or other passage explaining the difference. I also couldn't locate Reference #1 (the earlier study), so I can't confirm what it contained. The explanation would have to come from Toronto Hydro's own answer to this question.

What the October 2023 study does show:

- **Scope:** UMS benchmarked seven asset categories: Wood Poles, UG Cable, Pole Top Transformers, Pad mount/UG Transformers, Network Transformer/Protectors, Breakers, and Cable Chambers/Manholes. It also benchmarked five maintenance programs: Vegetation Management, Pole Test and Treat, Overhead Line Patrol, Substation Maintenance, and Building Vault Inspections [EB-2023-0195 / Exhibit 1B / p.381]. Neither overhead switch replacement nor switchgear replacement appears in either list.
- **Selection:** The study describes the categories as "pre-selected" by Toronto Hydro. UMS says they were chosen as a valid proxy for Toronto Hydro's unit-cost performance [EB-2023-0195 / Exhibit 1B / p.397]. The seven asset categories represent about 52% of planned 2020–2022 capital, and the five programs about 57% of preventative and predictive maintenance spending [EB-2023-0195 / Exhibit 1B / p.388].
- **Data adjustments:** UMS made "a few adjustments to the original asset categories / maintenance programs to facilitate Peer Group comparisons" [EB-2023-0195 / Exhibit 1B / p.397]. This suggests the category list changed during the work. The text doesn't say which categories were adjusted or dropped, so I can't tie it to the two items you asked about.
- **Nearby assets:** The study includes "Breakers" [EB-2023-0195 / Exhibit 1B / p.381]. The DSP discusses MS switchgear replacement (unit cost per feeder) and overhead switch replacement separately [EB-2023-0195 / Exhibit 2B / p.463]. I found no link between those items and the benchmarking scope.

I'd suggest asking Toronto Hydro to produce the earlier version of the study, or to confirm whether peer data for those two categories was too thin or too hard to compare to include.
```

agree: yes

## 13. 2B-EP-28: judge says **correct**

> The reference answers part (a) with a simple "Yes": the Future Energy Scenarios model includes electrified heating (Exhibit 2B, Section D4, Appendices A and B). The candidate also says yes, points to the same modelling, and adds supporting detail about the shift to a winter peak and the stress test. That detail fits the rest of the reference and contradicts none of it.

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
```

**Utility's response (reference)**

```
Yes. The Future Energy Scenarios model includes electrified heating. Please see Exhibit 2B, Section
D4, Appendix A and B for more information.
QUESTION (B):
b) Does Toronto Hydro presently expect the transition to heat pumps for home heating to
have a material effect on peak electricity demand? If not, why not?

In the long-term, Toronto Hydro’s view is that successful decarbonization of the energy system is
very likely dependent upon the widescale adoption of heat pumps. This will ultimately have a
material impact on peak electricity demand, including very likely the shift to a winter peak.
However, as illustrated by the Future Energy Scenarios, the extent and timing of the impact of heat
pump adoption on peak electricity demand is highly uncertain, and dependent on many factors
outside of Toronto Hydro’s control.
QUESTION (C):
c) If significantly more residential customers install heat pumps in a particular area than
Toronto Hydro has presently anticipated, how will this impact service reliability?

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
QUESTION (D):
d) Does Toronto Hydro have a plan in the event that significantly more customers install heat
pumps in a particular area than anticipated?

Toronto Hydro used the Future Energy Scenarios to stress-test whether the utility’s capacity plan
can accommodate energy transition needs (e.g. building heating electrification) in the early part of
the next decade. In an effort to adopt a proactive approach to managing forecasted local
constraints, Toronto
```

**Agent answer**

```
**Yes.** Toronto Hydro has analyzed how heat pump and other heating electrification would affect winter peak demand. It did this at the system level, not as a study of a "sizable portion of residential customers" converting. The filing does not show a separate feeder-level or customer-class study.

**Future Energy Scenarios (FES) modelling.** The utility's Exhibit 2B includes a Future Energy Scenarios report that models heat pump and other heating technology uptake for domestic and industrial/commercial buildings. It uses four scenario "worlds" and two low-efficiency sensitivities [EB-2023-0195 / Exhibit 2B / p.550]. The uptake assumptions include the Greener Homes Grant, which is expected to last at least 7 years from December 2020. The scenarios vary its end date, from 2027 in the Low case to 2030 and 2035 in the higher cases [EB-2023-0195 / Exhibit 2B / p.601] [EB-2023-0195 / Exhibit 2B / p.607] [EB-2023-0195 / Exhibit 2B / p.610].

**Results.** Summer peak exceeds winter peak through the 2020s. In the base year, summer peak is 3.9 GW and winter peak is 3.7 GW. The 2030s see the network peak shift to winter, driven by heat pump and EV uptake [EB-2023-0195 / Exhibit 2B / p.647]. Toronto Hydro also reports that heat pumps and EVs are expected to be primary drivers of peak growth and of the summer-to-winter shift in the 2030s [EB-2023-0195 / Exhibit 2B / p.39].

**2025–2029 stress test.** Toronto Hydro concluded that building electrification is "not yet a significant driver of growth" in the 2025–2029 period. Its System Peak Demand Forecast therefore remains summer-peaking [EB-2023-0195 / Exhibit 2B / p.536]. It still tested whether it could accommodate a growing winter peak. It used the Consumer Transformation scenario and its low-efficiency equivalent as the lower and upper bounds. It chose them because they showed the most variability in building heat and the most material system-peak impact [EB-2023-0195 / Exhibit 2B / p.537].

Its conclusion was that its forecast is generally aligned with the Consumer Transformation scenario. It also concluded that the planned capacity investments can meet higher building heating loads if electrification arrives faster than expected [EB-2023-0195 / Exhibit 2B / p.537].

**Limits.** The same page cautions that the utility could still face incremental capacity constraints at a localized level [EB-2023-0195 / Exhibit 2B / p.537]. The pages I read do not give a percentage of homes converting or a quantified winter-peak result for a given conversion share. I did not find a separate residential-only study, and I did not search for interrogatory responses.
```

agree: yes

## 14. 2B-STAFF-241: judge says **correct**

> The candidate confirms that the program mainly reduces the consequence of failures. Like the reference, it rejects part (i)'s premise by pointing to System Observability, which helps reduce failure risk through asset diagnostics, and it covers the other benefits (fault location and better decision-making). Its hedge ("largely confirmed") does not contradict the reference.

**Question**

```
a) Confirm that the System Enhancements program will reduce the consequence of individual
asset failures in many or most cases.
i.
If not confirmed, explain the purpose of the program, since it will not reduce the
probability of asset failures.
```

**Utility's response (reference)**

```
Confirmed. Please refer to Exhibit 2B, Section E7.1, Page 5 for specific information on this topic.
Note that Toronto Hydro respectfully disagrees with the premise of part (i) of OEB Staff’s question.
The System Enhancements program contains a variety of field technology investments which will
deliver benefits beyond reducing consequences of failure. The proposed System Observability
segment of the program includes adding more sensors, relays and monitoring technology at
specific nodes across the distribution grid. Gradually, these technologies will help the utility
advance three core capabilities:
1. Enhanced Fault Location: Locating faults and other system disturbances faster and more
efficiently in order to improve reliability and operate the grid more cost-effectively.
2. Enhanced Decision-making and Grid Optimization: Providing greater insight into real-time
feeder and asset loading, condition, and other relevant operating characteristics. This
assists the utility in managing short- and long-term uncertainty as well as driving optimal
real-time operational decisions and longer-term investment planning decisions.
3. Enhanced Asset Diagnostics: Greater visibility into high-risk and previously hard-to-
monitor assets will improve asset diagnostics, mitigating the risk of asset failure and
impacts to personnel safety and environmental damage.
For more information on the multi-faceted benefits of Toronto Hydro’s System Enhancements
program, please refer to Exhibit 2B, Section E7, and the Intelligent Grid Section of Toronto Hydro’s
Grid Modernization Strategy (Exhibit 2B, Section D5.2.1).
```

**Agent answer**

```
**Largely confirmed, with a qualification.** The filings don't use the "many or most cases" wording, and I found no statement quantifying how many failures the program would affect. But Toronto Hydro describes the program as mainly reducing the consequence of failures (fewer customers interrupted, shorter outages). It does not describe it as a program that mainly lowers failure probability. Part (i) therefore only partly applies. The program does not claim to cut failure rates for most assets, but one segment is expected to reduce failure likelihood in some cases.

**Consequence reduction (Contingency Enhancement and Downtown Contingency)**
- Contingency Enhancement adds remotely operable feeder tie and sectionalizing points and upgrades undersized lateral-loop conductors and trunk egress cables. The stated aim is to "optimize the grid and efficiently restore power to customers" [EB-2023-0195 / Exhibit 2B / p.524].
- Switching and restoration capability limits how many customers lose power and for how long once an asset fails. The filing doesn't claim it prevents the failure.
- Downtown Contingency targets station-level events. Toronto Hydro estimates that being able to pick up load from another station within one hour could cut Customer Minutes of Interruption from such incidents by about 80 percent over the 2003–2022 pattern [EB-2023-0195 / Exhibit 2B / p.541].
- The 2025–2029 spend is $151.2M, of which $132.9M is Contingency Enhancement. Table 6 puts Downtown Contingency at about $13.6M ($1.7M, $2.9M, $2.9M, $3.0M and $3.1M over the five years) and System Observability at about $4.7M [EB-2023-0195 / Exhibit 2B / p.524] [EB-2023-0195 / Exhibit 2B / p.547].

**Where the program does touch failure probability (System Observability)**
- This segment installs cable and transformer monitors and line sensors. Toronto Hydro says that without them, "the current system waits for cables to fail and then Toronto Hydro reacts" [EB-2023-0195 / Exhibit 2B / p.555].
- Observability is expected to provide "reduced outage times, extended asset life and improved planning in many cases" [EB-2023-0195 / Exhibit 2B / p.555].
- The grid modernization strategy says better asset diagnostics will mitigate "the risk of asset failure" [EB-2023-0195 / Exhibit 2B / p.663].
- This segment is small, so it is a minor part of the program.

**Purpose of the program (the substance of part i)**
- The program aims to give the physical grid, by 2030, the foundational technologies to run efficiently and deliver customer value. It responds to three drivers: electrification, growth in distributed energy resources, and climate-related reliability risks [EB-2023-0195 / Exhibit 2B / p.524].
- It is a component of Toronto Hydro's "Intelligent Grid" vision [EB-2023-0195 / Exhibit 2B / p.547].
- Reducing the probability of failure is handled elsewhere, by the System Renewal programs, which replace assets before they fail. Those programs say timely replacement "will mitigate the frequency an
```

agree: yes

## 15. 2B-AMPCO-30: judge says **partially_correct**

> The reference says Toronto Hydro tracks accomplishments at the segment/program level and can add them up to higher levels if needed. The candidate gets program-level tracking and the roll-up to portfolios right. However, its headline answer is "both" rather than primarily program level. It also says it found no segment-level tracking, which conflicts with the reference treating segment and program as the same level.

**Question**

```
a) Please discuss if Toronto Hydro tracks Program Accomplishments at the segment/program
level or portfolio level, or both.
```

**Utility's response (reference)**

```
Toronto Hydro tracks program accomplishments at the segment/program level, and these can be
aggregated to higher levels of reporting if needed.
QUESTION (B):
b) Please discuss if each program has a specific and unique outcome measure that is formally
tracked. If yes, please provide the Program Accomplishments for each segment in E5 to E8.

Toronto Hydro’s use of the term “program accomplishments” refers to volumetric
accomplishments of work and project-based milestones, whereas “outcome measures” refers to
performance outcomes. Where appropriate (e.g., compliance-driven programs), Toronto Hydro
may treat program accomplishments as the performance outcomes for the program (e.g., box-
framed poles eliminated). Program accomplishments and outcome measures allow Toronto Hydro
to monitor the performance of its investment program, and to determine to what extent projects
have contributed to expected outcomes, including risk reduction.
Each program has a unique set of accomplishments to be tracked (e.g., pole replacements) along
with one or more outcome measures that may be unique to the program (e.g., benefits achieved
from Network Condition Monitoring & Control investments)1 or shared with other programs (e.g.,
SAIDI/SAIFI).
Toronto Hydro has included program accomplishment and outcome measures throughout its
evidence, including within the detailed program evidence found in Exhibit 2B (Sections E5-E7).
Outcome measures that are influenced by multiple programs are discussed in Sections D2, C, and
E2 of Exhibit 2B and in Exhibit 1B, Tab 3, Schedule 2 (e.g., overall asset condition demographics by
asset class; SAIDI/SAIFI results, oil spills, etc.).
1 Exhibit 2B, Section E7.3
RESPONSES TO ASSOCIATION OF MAJOR POWER CONSUMERS IN ONTARIO
INTERROGATORIES
```

**Agent answer**

```
**Answer: both.** The filings show Toronto Hydro tracking at several levels: individual project, program, and portfolio. I found no filing that uses "Program Accomplishments" as a defined term or reporting category. The evidence below is therefore about how Toronto Hydro monitors and reports its work, not a formal "Program Accomplishments" metric.

**Project and program level**
- Program Management staff "track the status of projects in the work program and the roll-up of the projects into programs and portfolios" [EB-2023-0195 / Exhibit 4 / p.329].
- The Scope Issuance and Tracking function tracks all issued scopes to completion. It captures cancellations and unassigned scopes [EB-2023-0195 / Exhibit 4 / p.329].
- Projects are tracked from detailed design through construction. Toronto Hydro monitors changes through monthly executive performance reporting, key program status reporting, change requests and project variance analysis [EB-2023-0195 / Exhibit 2B / p.26].

**Portfolio level**
- Under the annual Investment Planning and Portfolio Reporting (IPPR) process, Toronto Hydro "monitors and assesses the progress of its system capital and maintenance programs against annual and longer-term budget, execution, and performance objectives" [EB-2023-0195 / Exhibit 2B / p.5].
- Portfolio Reporting covers "program level expenditures, project-specific execution status and project expenditures." Toronto Hydro also watches system-level outcomes, such as average reliability. It tracks the effect of specific programs on specific outcomes, such as the reduction in poles at end of serviceable life [EB-2023-0195 / Exhibit 2B / p.20].

**Program-level accomplishments used in planning**
- Toronto Hydro analyzed "actual project accomplishments and costs in each program" to set the project- and volume-based assumptions for its 2025–2029 program cost estimates [EB-2023-0195 / Exhibit 2B / p.56].
- That is a program-level use of accomplishments data. The wording is "project accomplishments," not "Program Accomplishments."

**Utility-wide measures**
- A performance outcomes framework reports 41 measures annually. These include 29 OEB service quality measures and 12 custom metrics [EB-2023-0195 / Exhibit 1B / p.33].
- Those measures sit above the program level.

**Segment level**
- I did not find segment-level tracking of accomplishments. In the operating expense evidence, "segment" is the unit for cost forecasts and year-over-year variance analysis, as in the Program Management and Support segment [EB-2023-0195 / Exhibit 4 / p.333].
- If you meant a specific table or interrogatory titled "Program Accomplishments," please point me to it. I could then search for it directly.
```

agree: no (correct: the agent's program-level tracking rolled up into portfolios does not contradict the reference's 'segment/program level, aggregated to higher levels if needed')

## 16. 2B-VECC-13: judge says **incorrect**

> The reference gives yearly tables for 2020–2029. The candidate gives no year-by-year new-installation figures. Its reverification counts don't match the reference: for 2025, for example, it gives 10,464 against the reference's 9,782. Its aggregate of about 50,000 new meters for 2020–2024 contradicts the reference, whose figures for those years add up to roughly 164,000.

**Question**

```
a) Please provide a table showing the number of new meters installed and, separately, the
number of meters reverified/resealed for the residential and GS<50 rate classes
```

**Utility's response (reference)**

```
Please see Tables 1 and 2 below.
Table 1: New Meter Installation for Residential and GS<50, Suite Meters
2020
2021
2022
2023
2024
2025
2026
2027
2028
2029
New
Meter
Installation
18,922
14,242
11,667
13,270
106,370 159,946 175,514 181,285
70,354
1,177
Residential
and GS <
50, Suite
Meters
Table 2: Meter Reverification/Resealing for Residential, GS<50, Suite Meters
Reverified/
Resealed
2020
2021
2022
2023
2024
2025
2026
2027
2028
2029
16,162
6,745
16,095
9,207
11,066
9,782
12,195 13,816 14,994 12,023
Residential
and GS <
50, Suite
Meters
QUESTION (B):
b) THESL notes that most smart meters were installed between 2006 and 2008 (E5.4.3.3).
What strategy is the Utility employing in order to avoid a repeat of the “bunching up” of
expired meters as has occurred due to concentrating meter replacements within a short
time frame?

As noted in Exhibit 2B, Section E5.4,1 Toronto Hydro’s historical smart meter deployment strategy
was in support of provincial policy objectives concerning the rollout of smart meters and time-of-
use billing in Ontario. Building on the strategy approved in the 2020 Rate Application,2 Toronto
Hydro intends to replace meters surpassing their expected lifespan over a five-year period. Mass
deployment of meters over a period greater than five years results in future risks to billing and
customer experience, while delaying the benefits of AMI 2.0 that can only be realized once a
majority of next generation meters have been installed, as shown in Toronto Hydro’s response to
interrogatory 2B-Staff-194. Toronto Hydro will assess the timing and pace of future metering
programs closer to the implementation of those programs based on the risk of failure, ability to
reseal, and benefits of any replacement meters at that time.
1 At page 9, lines 9-10.
2 EB-2018-0165, Exhibit 2B, Section E5.4; see especially lines 16-27 at page 16.
RESPONSES TO VULNERABLE ENERGY CONSUMERS COALITION
INTERROGATORIES
```

**Agent answer**

```
The filings I can access don't give a table that splits new meters installed and meters reverified/resealed by rate class, either for the Residential class or for GS<50 kW. They give combined totals, so I can't fill in the table you asked for without guessing. I searched the Toronto Hydro application (EB-2023-0195). The Hydro One application (EB-2026-0164) did not surface in any of the metering searches.

**Reverified/resealed (sampling and re-verification units)**

These are forecast totals for all meter classes, not Residential and GS<50 only. They are the "Sampling/Re-verification units" under the seal-expiry testing program [EB-2023-0195 / Exhibit 4 / p.93].

| Year | Seal-expiring meters | Sampling/re-verification units |
|---|---|---|
| 2025 | 196,127 | 10,464 |
| 2026 | 155,463 | 13,201 |
| 2027 | 70,968 | 14,783 |
| 2028 | 68,151 | 15,396 |
| 2029 | 28,242 | 11,311 |
| Total | 518,951 | 65,155 |

If a sampled group passes testing, the seals for all meters in that group are extended, by eight years for smart meters with a ten-year initial seal [EB-2023-0195 / Exhibit 4 / p.93]. So the number of meters resealed is larger than the number of units tested.

The filing says the bulk of Residential and small commercial meters have seals expiring in 2024–2026 [EB-2023-0195 / Exhibit 2B / p.177].

**New meters installed**

The filing gives only aggregate counts for Residential and small commercial & industrial (GS<50) meters combined:
- About 50,000 meters are planned for replacement in 2020–2024 as part of the AMI 2.0 project [EB-2023-0195 / Exhibit 2B / p.187].
- About 630,000 meters are planned for replacement in 2025–2029 [EB-2023-0195 / Exhibit 2B / p.187].
- Elsewhere the filing states approximately 680,000 meters for 2023–2028 [EB-2023-0195 / Exhibit 2B / p.182].

The filing does not say how these replacements divide between Residential and GS<50, or by year. These are also replacements, not new-connection installs.

**Other classes (not the ones you asked about)**
- Suite meters (a separate class from Residential and GS<50): about 2,000 new units a year on average in 2025–2029 [EB-2023-0195 / Exhibit 2B / p.178].
- Large-user ION meters: shown only in a chart [EB-2023-0195 / Exhibit 2B / p.178].

A response to an interrogatory (a written information request) may contain the class-level split, but I did not find one. You could ask Toronto Hydro directly for the new installs and reverified/resealed counts by class and year.
```

agree: yes

## 17. 2B-ED-28: judge says **correct**

> The reference says Toronto has about 1.1 million passenger vehicles. The candidate gives the same figure, about 1.1 million light-duty vehicles in Toronto, though it frames it as a 2030 projection and suggests the current fleet is slightly smaller. That hedge doesn't really contradict the reference's approximate number, and the candidate's other context is consistent with it.

**Question**

```
a) Approximately how many vehicles are owned by Toronto Hydro customers?
```

**Utility's response (reference)**

```
There are approximately 1,100,000 passenger vehicles in the City of Toronto.
QUESTION (B):
b) If approximately 20% of all cars in Toronto were connected to bi-directional chargers with a
10 kW export capability, what would their collective capacity be?

The premise of this question is based on untested assumption that each vehicle could export 10 kW
to the grid, and that this capacity can be aggregated in a targeted manner to provide grid-value,
when and where it is needed. For demand response to provide value, it must be dispatchable and
available reliably in areas of need. Please see the evidence in Exhibit 2B, Section E7.2 and the
response to 1B-ED-11 for more information about Toronto Hydro’s experience with demand
response and openness to working with third-parties (e.g. aggregators) to leverage this capacity if
and when it is available and can provide cost-effective value to the distribution system as a whole.
```

**Agent answer**

```
The filings I can access don't give a single "vehicles owned by Toronto Hydro customers" figure. The closest number is about 1.1 million light-duty vehicles registered in Toronto.

- **Basis:** Toronto Hydro's electric-vehicle forecast says its methodology "estimates 1.1M LDVs registered in Toronto by 2030," growing about 1% a year [EB-2023-0195 / Exhibit 3 / p.21]. That is a 2030 projection, not a current count. It is also a count for the City of Toronto, which I'm using as a proxy for Toronto Hydro's service territory.
- **Scale check:** The same page says 220,000 light-duty EVs would be 20% of the light-duty fleet. That target comes from the City of Toronto's EV Strategy [EB-2023-0195 / Exhibit 3 / p.21]. With a 1% annual growth rate, the current fleet would be a bit under 1.1 million, so "roughly 1 million" is a fair approximation.
- **Medium and heavy vehicles:** These are extra. Toronto Hydro's Table 10 forecasts about 6,462 medium-duty and 6,305 heavy-duty electric vehicles in Toronto by 2029, but that covers electric vehicles only [EB-2023-0195 / Exhibit 3 / p.75]. Other statements say Toronto accounts for about 20% of Ontario's medium- and heavy-duty vehicle population [EB-2023-0195 / Exhibit 3 / p.21].
- **Not customer-owned:** Toronto Hydro's own fleet is separate. It owns 13 electric and 20 hybrid light-duty vehicles [EB-2023-0195 / Exhibit 2B / p.748]. The TTC's roughly 2,357 buses are operated by the TTC, not by Toronto Hydro customers [EB-2023-0195 / Exhibit 2B / p.614].

I did not find a stated current-year total vehicle count in the filings. If you need one, the Future Energy Scenarios report (Exhibit 2B, Section D4, Appendix B) builds a 2021 base-year vehicle stock, but the pages I saw didn't show the number.
```

agree: yes

## 18. 1B-STAFF-46: judge says **partially_correct**

> The candidate matches the reference on parts (a) and (b): SAIFI and TRIF carry over, and SAIDI is redefined, with the customer priority on shorter outages as the reason. For part (c) it says it found no per-measure removal rationale, so it misses most of the reference's explanations, including ISO 55001 and ISO 14001 management, the efficiency measure replacing the cost measures, and the shift to outcome metrics. It also treats System Capacity as redefined around non-wires capacity, while the reference says it was replaced by a timely-connections measure.

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
Two 2020-2024 measures carry over unchanged. The filings I can access give no measure-by-measure reason for dropping the rest.

**Caveats on your premise and my sources.** Toronto Hydro's own table of the 2020-2024 custom measures, which cites the OEB decision at pp. 44-45, lists 16 measures, not 15 [EB-2023-0195 / Exhibit 1B / p.274]. A footnote in that table also refers to "15" proposed 2025-2029 measures, but Table 1 of Exhibit 1B, Tab 3, Schedule 1 shows 12 [EB-2023-0195 / Exhibit 1B / p.274] [EB-2023-0195 / Exhibit 1B / p.191]. I could not access the OEB Decision itself. I relied on Toronto Hydro's description of it.

The 16 measures in the 2020-2024 list are:
- Customers on eBills
- Total Recordable Injury Frequency (TRIF)
- Network Units Modernization
- SAIDI – Defective Equipment
- SAIFI – Defective Equipment
- FESI-7
- FESI-6 (Large Customers)
- MAIFI
- System Capacity (# of stations)
- System Health – Wood Poles
- Direct Buried Cable Replacement
- In-Service Additions
- Average Wood Pole Replacement Cost
- Vegetation Management Cost per km
- Oil Spills Containing PCBs
- Waste Diversion Rate [EB-2023-0195 / Exhibit 1B / p.274]

**a) Same measure, ignoring the target**

1. **Outage Frequency is the same as SAIFI – Defective Equipment.** Toronto Hydro says it "intends to continue reporting on this metric" [EB-2023-0195 / Exhibit 1B / p.279]. The 2025-2029 version is defined as SAIFI – Defective Equipment [EB-2023-0195 / Exhibit 1B / p.191].
2. **TRIF is the same measure.** It is defined as recordable injuries per 200,000 exposure hours, and Toronto Hydro says it "intends to continue reporting TRIF as a custom measure" [EB-2023-0195 / Exhibit 1B / p.276]. The 2025-2029 wording is "injuries per 100 employees (or 200,000 hours worked)" [EB-2023-0195 / Exhibit 1B / p.191].

**b) Same or similar name, different definition**

- **Outage Duration (SAIDI).**
  - The 2020-2024 measure was SAIDI – Defective Equipment, which counts only interruptions caused by equipment failure [EB-2023-0195 / Exhibit 1B / p.279].
  - The 2025-2029 measure is SAIDI excluding Major Event Days, Loss of Supply and Scheduled Outages [EB-2023-0195 / Exhibit 1B / p.191].
  - Toronto Hydro's stated reasons concern excluding Scheduled Outages. There is major forecasting uncertainty from the Oracle Utility Analytics (OUA) outage-data system rollout. Scheduled outages are also expected to rise with a larger work program. Excluding them gives more visibility into unforeseen interruptions [EB-2023-0195 / Exhibit 1B / p.192] [EB-2023-0195 / Exhibit 1B / p.193].
  - The target is a five-year rolling average, "consistent with OEB's approach" on the Electricity Distributor Scorecard (EDS) [EB-2023-0195 / Exhibit 1B / p.193].
  - Customer research showed customers (except Key Accounts) prioritize shorter outages over fewer outages [EB-2023-0195 / Exhibit 1B / p.193].
  - I found no explicit reason for moving from defective-equipment-only to a broader cause base.
- **Customer Satisfac
```

agree: yes

## 19. 9-STAFF-342: judge says **partially_correct**

> The candidate gets the basic design right: a rate rider of about $16M collected only in 2029, plus the IFVA, which tracks rider revenue against actual pilot costs and earns carrying charges. It misses the reference's key mechanics: the account sits in a debit position from 2025 to 2028, 2029 collections credit it, and the balance is reconciled at the end of the term and disposed of in the 2030+ rebasing application. It also leaves out Toronto Hydro's stated reason for symmetry (flexibility and no hard cap, given funding at the low end of the range) and offers only its own inference instead.

**Question**

```
Toronto Hydro proposes to establish an Innovation Fund to support the design and execution of
innovative pilot projects over the 2025-2029 rate period. The pilot projects undertaken through the
Innovation Fund would be focused on testing new technologies, advanced capabilities and
alternative strategies that enable electrification grid readiness and are responsive to the OEB’s
expectations with respect to facilitating DER integration, as expressed in the Framework for Energy
Innovation (FEI) report.
Toronto Hydro proposes to collect an amount of $16M through a rate rider rather than through
base rates to provide transparency to ratepayers on the bill and flexibility to the utility to
determine how the funds should be allocated across capital and operational expenditures on the
basis of the selected pilot projects. Toronto Hydro proposes to establish a new symmetrical
variance account to record variances between the amounts collected by the rate rider and the
actual costs incurred to execute the selected pilot projects as part of the Innovation Fund.
Toronto Hydro expects to collect the $16M during 2029.

a) Please elaborate on the rate mechanism of Toronto Hydro’s collection of the $16M fund in
2029 and how it plans to track the variance, given that the funding will be collected in
2029.
i. Please discuss why it is appropriate for the IFDA to be symmetrical.
```

**Utility's response (reference)**

```
The rate mechanism of Toronto Hydro’s collection for the Innovation Fund consists of a rate rider
(IFRR) and variance account (IFVA). The rate rider will recover an amount equivalent to 0.3% of the
total revenue requirement approved by the OEB for 2025-2029. Assuming that the full revenue
requirement that is being asked for gets approved, the rate rider will recover approximately $16
million. The Innovation Fund Variance Account (IFVA) will track variances between the revenues
collected through the Innovation Fund Rate Rider and the actual costs incurred (i.e. revenue
requirement) by the Innovation Fund pilot projects by the end of the rate period.
As depicted in the Rate Rider table in Exhibit 9, Tab 3, Schedule 1, there are no revenues being
collected through the Innovation Rate Rider in years 2025-2028, meaning that the balance in this
account will be in a debit position during this period of time. In 2029 when the rate rider revenues
are being collected from customers, they will be applied as a credit to reduce the balance in the
account. At the end of the rate term, the delta between the total revenue requirement booked in
this account over the 2025-2029 rate term (inclusive of carrying charges) and the total revenues
collected through the Innovation Fund Rate Rider, will be reconciled. The account will be brought
forward for disposition in the 2030+ rebasing application.
Toronto Hydro considers it appropriate for the IFVA to be symmetrical because it is consistent with
the intent of the Innovation Fund, which is to provide the flexibility needed to undertake innovative
pilot projects by overcoming barriers s discussed at page 4 of the Innovation Fund evidence.This,
coupled with the fact that Toronto Hydro is proposing a level funding that is at the lower end of the
range identified through its research, leads Toronto Hydro to view symmetrical treatment of the
variance account as providing Toronto Hydro with the necessary flexibility to pursue promising
opportunities without being constrained by a “hard cap”. That said, Toronto Hydro faces significant
regulatory oversight risk for overspending, and as such does not intend to stray far outside of its
boundaries, unless there is a strong value proposition for doing so.
QUESTION (B):
b) Please elaborate how external stakeholders will be involved in the execution and
evaluation phases of the pilot projects selected.
i. Please confirm whether the steering committee members mentioned in reference 3 will
involve external stakeholders, and the proposed composition of the committee of external
to internal stakeholders.

Please see Toronto Hydro’s responses to interrogatories 1B-CCC-46 part (a) and 1B-DRC-06 part (i).
QUESTION (C) :
c) Please discuss any quantifiable goals and outcomes Toronto Hydro can establish for the
pilot projects.

As stated in the Innovation Fund evidence, “a key component of the design phase is to maximize
Toronto Hydro’s ability to learn and develop new distribution capabilit
```

**Agent answer**

```
The filings available to me don't answer either part directly. They give the basic design of the rate rider and the variance account, but not how a 2029-only collection is tracked, and not a separate reason for the account being symmetrical. The filings call the account the Innovation Fund Variance Account (IFVA), not "IFDA". I'm treating them as the same account.

**a) Rate mechanism and tracking**

- **Rate rider:** Toronto Hydro proposes to recover about $16M through an Innovation Fund rate rider, not base rates. It gives three reasons: the rider appears as a separate line on the bill, it gives the utility funding certainty, and it keeps the fund outside the base revenue requirement. That last point lets the utility decide whether each project's spending is capital or operating [EB-2023-0195 / Exhibit 1B / p.470].
- **Timing:** The rate rider table shows the Innovation Fund rider with a one-year recovery period, starting and ending in 2029. It is allocated to rate classes on 2022 distribution revenue [EB-2023-0195 / Exhibit 1B / p.50]. The rider is a single fixed or volumetric charge, depending on the class, like the other rate riders [EB-2023-0195 / Exhibit 9 / p.38]. The $16M is therefore not collected evenly across 2025–2029. It is collected in one year, while the pilots run over the whole period.
- **Tracking:** The IFVA records variances between the amounts collected by the rider and the actual costs of the selected pilot projects [EB-2023-0195 / Exhibit 1B / p.470]. The draft accounting order sets it up as a sub-account of Account 1508, Other Regulatory Assets. It records the difference between the Innovation Fund amount in the rider and the actual revenue requirement over the CIR period, and the entry runs through 4080 Distribution Services Revenue. A separate carrying-charges sub-account records interest at the OEB-approved rate for deferral and variance accounts, and Toronto Hydro would apply later to clear the balance [EB-2023-0195 / Exhibit 9 / p.52].
- **What the filings don't say:** They don't explain how costs incurred in 2025–2028 are tracked before the 2029 collection, or whether interest accrues on that spending. They also don't give the exact mechanics of the 2029 true-up or the date of the clearance application. The draft order's wording ("actual revenue requirement") might imply a revenue-requirement basis, but I can't confirm that from what I read.

**i) Why the account is symmetrical**

The filings describe the IFVA as "symmetrical" [EB-2023-0195 / Exhibit 9 / p.40], but I found no passage that argues why that is appropriate. The text that comes closest is the justification for the account as a whole:

- **Causation:** The pilot costs sit outside the base revenue requirement [EB-2023-0195 / Exhibit 1B / p.470].
- **Materiality:** The recorded amounts depend on actual pilot spending, which is set under the governance framework [EB-2023-0195 / Exhibit 1B / p.470].
- **Prudence:** The $16M is based on comparable ratepayer-fu
```

agree: yes

## 20. 2B-STAFF-247: judge says **partially_correct**

> The reference says Toronto Hydro can't provide the data because it doesn't procure energy (kWh) from DERs. It procures only dispatchable demand response capacity. The candidate agrees that the alignment with peak hours isn't quantified, and adds modelled profiles and installed-capacity figures from the evidence. But it misses the reason the reference gives, and it doesn't mention that Toronto Hydro relies on procured dispatchable demand response.

**Question**

```
Toronto Hydro states: “The NWS strategy for the 2025-2029 period is focused on being flexible and
adaptable to help system planners respond to load growth while navigating the underlying
uncertainty that stems from changing demand patterns and increased reliance on electrification.
This strategy builds on Toronto Hydro’s experience utilizing DERs to reduce peak demand, helping
to defer grid expansions or, in most cases, avoid grid expansions should demand not materialize as
expected (e.g., lower than expected demand, fluctuating demand).”

a) Please quantify by technology type the alignment of energy production by the DERs
presently installed in Toronto Hydro’s service area with the summer and winter peak
demand hours on Toronto Hydro’s distribution system.
```

**Utility's response (reference)**

```
As outlined in Exhibit 2B Section E7.2, Toronto Hydro plans for and procures third-party capacity in
the form of dispatchable demand response to complement standard system planning approaches.
The utility is unable to provide the requested data as Toronto Hydro does not procure energy
(kWh) from DERs.
QUESTION (B):
b) Given the response to the prior question, please describe the effectiveness of Toronto
Hydro’s existing DER portfolio in mitigating capacity constraints encountered by Toronto
Hydro during summer and winter peak demand periods.

Toronto Hydro does not control third-party owned, non-dispatchable DERs and thus cannot rely
upon these assets to meet system needs (capacity needs or otherwise) on demand. Until a DER
owner enters into a binding agreement with Toronto Hydro (via LDR procurement) to provide a
specific service to the grid, Toronto Hydro will not consider this DER as a reliable system tool. As
part of its Local Demand Response program, Toronto Hydro procured 8 MW of dispatchable
demand response capacity between 2018-2020, 4 MW between 2022-2023, and 6 MW in 2024.
The non-wires solutions considered for the 2025-2029 rate period are described in Exhibit 2B
Section E7.2. Toronto Hydro’s use of NWSs is targeted and focuses on credible capital deferral
opportunities, and thus, the application of these solutions is limited to instances where such
deferral opportunities can be identified and measured. The use case identified at this time is
limited to bus-level load transfer deferral or avoidance. This can be achieved through the
procurement of dispatchable demand response from aggregators or customers. Toronto Hydro is
agnostic to the technology (type of DER) or approach (load curtailment) utilized by aggregators or
customers to deliver this demand response capacity. Participants are compensated based on
measured and verified performance, utilizing the methodology outlined in IESO’s Market Manual
12 – Issue 16.
```

**Agent answer**

```
The filings I can access don't quantify DER output at the actual summer and winter system peak hours. Toronto Hydro gives hourly capacity-factor profiles by technology, but I found no statement of the system peak hours and no calculation of output at those hours. I also can't say whether Toronto Hydro answered this question in an interrogatory response, because I didn't find one. The closest evidence is below.

**Hourly profile assumed for installed DERs (kWh per kW of nameplate, average day)**

The profiles are in the load-forecast integration model. Toronto Hydro supplied the capacity factors to its consultant, Clearspring [EB-2023-0195 / Exhibit 1B / p.115].

| Technology | Summer | Winter |
|---|---|---|
| Solar (the model treats all renewables as solar) | 0 before 07:00. Output is 0.28–0.35 from 10:00 to 17:00 and peaks at 0.35 in the 13:00 hour. It falls to 0.09 at 19:00 and 0 from 20:00. | Much lower. The maximum is 0.07 at 13:00, and output is 0 from 20:00. |
| Non-renewable (for example CHP) | Flat all day at about 0.65–0.68 | Same as summer |
| Energy storage | 0 in every hour | 0 in every hour |

The solar profile sums to about 3.22 kWh per kW per summer day and about 0.60 kWh per kW per winter day [EB-2023-0195 / Exhibit 3 / p.83].

- **Energy storage:** It is set to zero because "there is not yet evidence" on whether storage will be used to avoid billing demand or other peaks, or only for resiliency [EB-2023-0195 / Exhibit 1B / p.115]. Storage is also assumed not to be actively charged and discharged [EB-2023-0195 / Exhibit 1B / p.112]. So no peak alignment is modelled for storage.
- **Non-renewables:** The model applies no seasonal adjustment to them [EB-2023-0195 / Exhibit 1B / p.112]. Their output is flat across the day, so it should overlap with any peak hour.
- **Basis:** These are modelled average-day assumptions from a revenue and billing-demand model. They are not metered output at coincident system peak.

**Installed capacity by type (end of 2022)**

- Toronto Hydro had 2,424 DER connections totalling over 304.9 MW. Of that, renewables were 116.2 MW [EB-2023-0195 / Exhibit 1B / p.449].
- Non-renewables were the largest category by capacity, at 56% of installed capacity for 2022 [EB-2023-0195 / Exhibit 2B / p.61].
- Energy storage was 28 projects totalling 18.7 MW, mostly commercial and industrial. Many of them are used to reduce global adjustment charges [EB-2023-0195 / Exhibit 2B / p.61].
- The model's renewable nameplate for 2022 is 100,366 kW [EB-2023-0195 / Exhibit 3 / p.82].

**Measured CHP output in a summer peak window**

Exhibit 9 reports M&V results for individual CHP projects against a summer peak period defined as June 1 to August 31, Monday to Friday, 1:00–7:00 pm. Four examples:

- 111 kW summer peak generation against 104 kW average [EB-2023-0195 / Exhibit 9 / p.248].
- 101 kW peak savings against 90 kW average [EB-2023-0195 / Exhibit 9 / p.291].
- 115 kW against 114 kW [EB-2023-0195 / Exhibit 9 / p.393].
- 109
```

agree: yes
