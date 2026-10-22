# IR eval set: hand-check sample

Seeded random sample (seed 20261022) of 20 labelled rows.
A row is **correct** if (1) the question is the intervenor's question, complete and not mixed
with another IR, (2) the response is Toronto Hydro's response to it, and (3) every gold exhibit
is cited in the response as a place where the answer/evidence is found.

Mark each `verdict:` as `correct` or `wrong (<reason>)`. `label-for-query:` records the looser question that
matters for the retrieval eval: do the gold exhibits locate the answer to the part of the question that is
actually in the query?

**Reviewed by Claude (claude-opus-5-5 in Claude Code), not a human**, on 2026-10-21, at the user's
request. Each row was checked against the full response text, split by sub-question.

## 1. 2B-VECC-13  (doc `rds-851961`, pp. 335-337)

- gold (response) exhibits: **2B**
- reference-line exhibits: 2B
- PDF: http://localhost:3077/api/pdf/rds-851961#page=335

**Question (as filed)**

```
a) Please provide a table showing the number of new meters installed and, separately, the
number of meters reverified/resealed for the residential and GS<50 rate classes
```

**Query used for retrieval (locations stripped)**

```
a) Please provide a table showing the number of new meters installed and, separately, the
number of meters reverified/resealed for the residential and GS<50 rate classes
```

**Response**

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

verdict: wrong (question holds only part (a); part (b) and its answer are in the response field)
label-for-query: no (gold 2B is cited only in the answer to part (b), which is not in the query)

## 2. 2B-DRC-10  (doc `th-consolidated-interrogatory-responses`, pp. 2227-2230)

- gold (response) exhibits: **2B**
- reference-line exhibits: 2B
- PDF: http://localhost:3077/api/pdf/th-consolidated-interrogatory-responses#page=2227

**Question (as filed)**

```
THESL states that customers are showing a continued interest in participating in the electricity
system as both consumers and producers of power and that DER connections have grown in recent
years as result of government policies and declining costs of technologies such as solar panels.

a) Please elaborate on customer interest related to solar power since the last rebasing period.
b) Please provide any other common constraints to DER installation and comment on (i) any
improvements THESL has implemented over the past five years to address these
constraints and (ii) whether there are areas within THESL’s larger system that are worse for
these constraints than others.
```

**Query used for retrieval (locations stripped)**

```
THESL states that customers are showing a continued interest in participating in the electricity
system as both consumers and producers of power and that DER connections have grown in recent
years as result of government policies and declining costs of technologies such as solar panels.
a) Please elaborate on customer interest related to solar power since the last rebasing period.
b) Please provide any other common constraints to DER installation and comment on (i) any
improvements THESL has implemented over the past five years to address these
constraints and (ii) whether there are areas within THESL’s larger system that are worse for
these constraints than others.
```

**Response**

```
Please refer to Exhibit 2B, Section E3, for information regarding Toronto Hydro’s ability to
accommodate renewable energy generation and other distributed energy resource (“DER”). This
includes renewable DER applications (such as solar), overall DER connection projections, the
distribution system’s ability to connect, as well as known constraints on the distribution system.
For information regarding investments made over the 2020-2024 period, please refer to the
Generation Protection Monitoring and Control program in Exhibit 2B, Section E5.5.
QUESTION (C):
c) Please indicate where there are expected areas of DER growth in THESL’s service territory.

DER connection location probability greatly varies and is determined by customer demand. The
DER forecast is based on growth trends using historical data. DER growth forecasted in specific
station areas is determined based on generation types and pipeline information. For further
details, please refer to Exhibit 2B, Section E3.
QUESTION (D) :
d) Please indicate the areas of THESL’s service territory that THESL has been unable to meet
DER installation demand and indicate whether there are any other areas where installation
demand will not be met over the rebasing period and beyond.

A restricted feeder list posted on Toronto Hydro’s website identifies the stations with no additional
short circuit capacity, i.e. unable to connect generation facilities (DERs). This list is updated
regularly and a snapshot is provided in Exhibit 2B, Section E3. Toronto Hydro’s DER forecast
identified stations expected to have no available short circuit capacity in the next 5 years. Over the
2025-2029 period, the utility proposes investments in the Generation Protection Monitoring and
Control (Exhibit 2B, Section E5.5), Non-Wires Solutions (Section E7.2) and Stations Expansion
(Section E7.4) programs to alleviate these constraints.
QUESTION (E) :
e) Please provide any comments and insights from THESL’s perspective on the adoption and
integration of DERs at a more granular level, such as at the neighbourhood level (which
neighbourhoods are seeing a significant increase in DER and EV adoption, which
neighbourhoods are not seeing any or an increase in demand for DERs and EVs, etc.). If
known, please discuss the characteristics of THESL’s customers that are adopting these
technologies (age, income, location, residential type etc.).

The table below is provides the number of DERs connected to each substation. As described in
Exhibit E3, Toronto Hydro’s investments seek to alleviate constraints at the bus/feeder level. The
utility does not track the requested information at that level of detail, however, from the data
provided below, downtown locations appear to have lesser DER adoptions, which could indicate
that space constraints may be a determining factor.
Table 1: Number of DERs Connected to Each Substation
Number of Connected DERS (as of 2022)
East York
96
Leaside
96
Etobicoke
371
Horner
88
Manby
117
Rexdale
63
Richview
95
```

verdict: wrong (question holds parts (a)-(b); parts (c)-(f) are in the response field)
label-for-query: yes

## 3. 2B-STAFF-186  (doc `th-consolidated-interrogatory-responses`, pp. 1796-1796)

- gold (response) exhibits: **2B**
- reference-line exhibits: 2B
- PDF: http://localhost:3077/api/pdf/th-consolidated-interrogatory-responses#page=1796

**Question (as filed)**

```
Toronto Hydro states: “Toronto Hydro forecasts over 50 additional Energy Storage connections…to
the distribution system. This would increase…the total installed Energy Storage capacity to
89.5MW.”

Does Toronto Hydro anticipate that the total volume of energy storage connected to its system by
2029 will materially assist in mitigating customer outage durations associated with events caused
by freezing rain, windstorms or floods, i.e., similar to the events listed in the Extreme Weather and
Major Event Day sections of this application (e.g. Exhibit 1B Section 2.3.4, Exhibit 2B Section C2.3)?
Please explain.
```

**Query used for retrieval (locations stripped)**

```
Toronto Hydro states: “Toronto Hydro forecasts over 50 additional Energy Storage connections…to
the distribution system. This would increase…the total installed Energy Storage capacity to
89.5MW.”
Does Toronto Hydro anticipate that the total volume of energy storage connected to its system by
2029 will materially assist in mitigating customer outage durations associated with events caused
by freezing rain, windstorms or floods, i.e., similar to the events listed in the Extreme Weather and
Major Event Day sections of this application (e.g. , )?
Please explain.
```

**Response**

```
No. The non-wires solutions proposed for the 2025-2029 period are outlined in detail in Exhibit 2B
Section E7.2. Toronto Hydro intends to utilize DERs, including energy storage resources, as demand
response in a manner that is practical and prudent given the current availability of DER capacity,
and level of market maturity. At this time, Toronto Hydro is not utilizing customer-owned DERs to
manage grid outages. The use of customer-owned DERs for this purpose would require specific
connection arrangements and requires further study. Toronto Hydro will continue to explore such
use cases and determine whether they are practical or prudent.
Toronto Hydro’s ESS program targets the enablement of REG connections and does not
contemplate additional use cases to support the distribution system. Please see Exhibit 2B Section
7.2.2 for more details.
```

verdict: correct
label-for-query: yes

## 4. 2A-SEC-30  (doc `rds-843543`, pp. 41-42)

- gold (response) exhibits: **6**
- reference-line exhibits: 2A
- PDF: http://localhost:3077/api/pdf/rds-843543#page=41

**Question (as filed)**

```
SEC seeks to understand the revenue requirement impact of the proposal capital expenditures.
Please provide a table that shows for each year between 2025 and 2029, the revenue
requirements, broken down by component, related only to the proposed 2025 to 2029 capital
expenditures.
```

**Query used for retrieval (locations stripped)**

```
SEC seeks to understand the revenue requirement impact of the proposal capital expenditures.
Please provide a table that shows for each year between 2025 and 2029, the revenue
requirements, broken down by component, related only to the proposed 2025 to 2029 capital
expenditures.
```

**Response**

```
Table 1 below presents an estimate of 2025-2029 revenue requirement associated with 2025-2029
capital expenditures broken down by component. The revenue requirement provided below is
based on an estimate of the updated 2025-2029 total Revenue Requirement, which includes
impact from: (i) the 2023 actuals and updated 2024 forecast (presented in 2A-Staff-104), and (ii)
the January 29, 2024 evidence update. The final PILS models for the updated 2025-2029 total
Revenue Requirement (Exhibit 6) are not yet available because it was not possible to complete this
work within the timelines for responding to interrogatories. This information will be provided in
advance of the Technical Conference as indicated in 1A-Staff-01 and noted in the Application
Evidence Update cover letter.1
Table 1: 2025-2029 Estimated Capital-Related Revenue Requirement
2025
2026
2027
2028
2029
2025-2029
ROE
4.3
19.7
42.1
66.8
90.6
223.5
Deemed Interest
2.8
12.8
27.3
43.3
58.7
144.7
Depreciation
39.6
55.4
83.9
115.9
146.2
441.0
PILS
(0.3)
(12.0)
(29.5)
4.0
(2.9)
(40.7)
1 EB-2023-0195, Toronto Hydro 2025-2029 Custom Rate Application For Electricity Distribution Rates and
Charges – Evidence Update, January 29,2024, page 1.
Revenue Requirement
46.3
75.9
123.8
230.0
292.5
768.5
Rounding variances may exist
```

verdict: wrong (Exhibit 6 is cited as where updated figures are 'not yet available', not where the answer is)
label-for-query: no (same reason)

## 5. 4-VECC-75  (doc `th-consolidated-interrogatory-responses`, pp. 3271-3271)

- gold (response) exhibits: **4**
- reference-line exhibits: 4
- PDF: http://localhost:3077/api/pdf/th-consolidated-interrogatory-responses#page=3271

**Question (as filed)**

```
a) Please complete the above table for the one-time application costs that are to be
amortized over the rate plan period.
```

**Query used for retrieval (locations stripped)**

```
a) Please complete the above table for the one-time application costs that are to be
amortized over the rate plan period.
```

**Response**

```
Please see Toronto Hydro’s response to interrogatory 4-SEC-110. The one-time application costs
incurred to date are listed in the 2022 and 2023 actuals columns of the updated OEB Appendix 2-M.
QUESTION (B):
b) Are the amortized costs of this application included in the presentation tables on OM&A
(e.g. Appendix 2-JC etc.)?

The amortized costs are not broken out in the noted appendices, but are included in the presentation
of the Regulatory Affairs segment at Exhibit 4, Tab 2, Schedule 18.
```

verdict: wrong (question holds only part (a); part (b) is in the response field)
label-for-query: no (gold 4 is cited only in the answer to part (b))

## 6. 1B-SEC-25  (doc `th-consolidated-interrogatory-responses`, pp. 1474-1474)

- gold (response) exhibits: **2B, 1B**
- reference-line exhibits: 1B
- PDF: http://localhost:3077/api/pdf/th-consolidated-interrogatory-responses#page=1474

**Question (as filed)**

```
For each year between 2025-2029, please detail all productivity and efficiency initiatives that
Toronto Hydro plans to undertake. For each please provide a quantitative estimate of forecast
savings, and include the full methodology and assumptions used in the calculation.
```

**Query used for retrieval (locations stripped)**

```
For each year between 2025-2029, please detail all productivity and efficiency initiatives that
Toronto Hydro plans to undertake. For each please provide a quantitative estimate of forecast
savings, and include the full methodology and assumptions used in the calculation.
```

**Response**

```
Consistent with the expectations of the X-factor, the 2025-2029 Custom Scorecard includes an
Efficiency Achievements metric with a target to achieve approximately $6.9 million in sustained and
quantified efficiency benefits per year by the end of the rate period (i.e. 2029). Table 16 in the
referenced evidence details the types of investments that will enable Toronto Hydro to achieve the
$6.9 million target on this custom metric. Please refer to the utility’s response to 1B-SEC-20(f) for an
explanation of how these Efficiency Achievements will be tracked in the next rate period.
In the next rate period, the utility intends to continue to focus on process automation (e.g.
digitization, robotics and predictive analytics) to drive continuous improvement in efficiency and
productivity. A detailed list of specific initiatives will be determined as part of Toronto Hydro’s IT
Investment Planning process and Enterprise Technology Portfolio (ETP) framework as described in
Exhibit 2B, Section D8, pages 7-10. As initiatives are prioritized and approved for execution, expected
savings and benefits will be tracked and evaluated. Please see the evidence in Exhibit 1B, Tab 3,
Schedule 3 for a detailed list and explanation of over 30 productivity initiatives undertaken in the
current rate period, and the response to 1B-AMPCO-07 for more information about these initiatives.
```

verdict: correct
label-for-query: yes

## 7. 1B-CCC-27  (doc `th-consolidated-interrogatory-responses`, pp. 587-587)

- gold (response) exhibits: **1B**
- reference-line exhibits: 1B
- PDF: http://localhost:3077/api/pdf/th-consolidated-interrogatory-responses#page=587

**Question (as filed)**

```
Over the 2025-2029 rate period Toronto Hydro’s operations and capital investment needs are
growing by approximately 37.5% due to a number of distinct and interrelated drivers. Please
attribute a percentage to each of those drivers set out in the evidence. For example, how much of
the increases are related to inflationary pressures? How much s related to the aging and
deterioration of Toronto Hydro’s asset base?
```

**Query used for retrieval (locations stripped)**

```
Over the 2025-2029 rate period Toronto Hydro’s operations and capital investment needs are
growing by approximately 37.5% due to a number of distinct and interrelated drivers. Please
attribute a percentage to each of those drivers set out in the evidence. For example, how much of
the increases are related to inflationary pressures? How much s related to the aging and
deterioration of Toronto Hydro’s asset base?
```

**Response**

```
As noted, the drivers identified on page 7 of Exhibit 1B, Tab 2, Schedule 1 are “interrelated”, and
thus cannot be broken down as requested. At the reference noted, each driver is accompanied by a
footnote directing the reader to the evidence where detailed information, including cost breakdowns
as appropriate, about each driver can be found.
```

verdict: correct
label-for-query: yes

## 8. 4-STAFF-305  (doc `th-consolidated-interrogatory-responses`, pp. 3060-3062)

- gold (response) exhibits: **4, 2B**
- reference-line exhibits: 4
- PDF: http://localhost:3077/api/pdf/th-consolidated-interrogatory-responses#page=3060

**Question (as filed)**

```
a) Please provide a more detailed explanation for the 84% sustained cost increase in
Regulatory Affairs from $3.8M in 2020 to $7.0M in 2025.
i.
Please outline any one-time costs that may have been included in Regulatory
Affairs versus those contained in Regulatory Applications.
```

**Query used for retrieval (locations stripped)**

```
a) Please provide a more detailed explanation for the 84% sustained cost increase in
Regulatory Affairs from $3.8M in 2020 to $7.0M in 2025.
i.
Please outline any one-time costs that may have been included in Regulatory
Affairs versus those contained in Regulatory Applications.
```

**Response**

```
Consistent with Toronto Hydro’s principles of developing in-house talent for reasons of both business
continuity and cost-efficiency (see 4-Staff-308), the increase in the Regulatory Affairs segment
budget between 2020 and 2025 is primarily driven by Toronto Hydro investing in building internal
capacity and capability in its regulatory activities, including ensuring the resources necessary to help
increase regulatory acumen throughout the utility’s workforce and processes. This is consistent with
Toronto Hydro’s maturation as a regulated entity, and the utility’s ability to keep pace and ensure
quality standards are met with the increased volume of regulatory policy, compliance, and
applications requirements.
The specific increase in predominately due to the addition of 10 FTEs over this period, as shown in
the response to interrogatory 4-VECC-74, and by market-based annual compensation increases (as
set out in Exhibit 4, Tab 4) associated with attracting and retaining the necessary resource
complement in this area of Toronto Hydro’s operations.
From 2020 to 2022, Toronto Hydro increased the staffing compliment in this area by 6 FTE to address
historical resourcing shortages in this portfolio, 1 and develop internal capacity for regulatory
applications, regulatory compliance, regulatory analytics and reporting, and business support files.
The decision to increase in-house regulatory and legal capacity to prepare the 2025 rate application,
was supported by a decision to also reduce the external legal expenses budget compared to the last
filing, as shown in the response 4-SEC-110.
From 2022 to 2025, increases in payroll are driven by the addition of 4 FTEs (representing an 18%
increase) which are necessary to handle higher volumes of work and complexity emanating from
OEB-related business activities (e.g. regulatory and energy policy development, implementation and
compliance activities). This increase is (i) aligned with the OEB’s expanded priorities articulated in
recent Business Plans and the Letters of Direction,2 and (ii) commensurate with the OEB’s 18%
increase in FTE (from 193 to 228 FTEs) from the 2021-22 budget to the 2023-24 budget.3
Application-related costs that are included in the regulatory affairs budget (rather than Appendix 2-
M) do not constitute one-time costs because they reflect the reprioritization of work in 2023 and
2024 in order to prepare and adjudicate the rate application. After the application is completed,
ongoing application-related work activities and priorities will resume including: (1) preparing, filing,
defending and implementation of annual rate updates; (2) interpreting and implementing the OEB’s
decision, directives and related continuous improvement initiatives; (3) supporting the execution
and implementation of the 2025-2029 Investment Plan through monthly oversight processes as
noted in 2B-AMPCO-29(d) and annual investment planning activities as described in Exhibit 2B,
Section D1; (4) measuring and trackin
```

verdict: correct
label-for-query: yes

## 9. 1B-STAFF-8  (doc `th-consolidated-interrogatory-responses`, pp. 253-255)

- gold (response) exhibits: **3, 1B, 2B**
- reference-line exhibits: 1B
- PDF: http://localhost:3077/api/pdf/th-consolidated-interrogatory-responses#page=253

**Question (as filed)**

```
In Reference 1, Toronto Hydro shows that Toronto Hydro’s customer count has been slowing and is
projected to average 0.3% annually in the last three years of the rate period. The same reference
shows a downward trend in normalized MVA that is forecast to continue.
In Reference 2, Toronto Hydro states that “Toronto Hydro distributes electricity to Canada’s largest
- and North America’s second fastest growing city.”
Reference 4 indicates the City of Toronto’s population growth rate will slow.

a) Please explain Toronto Hydro’s view of the importance of absolute increase in population
as compared to the growth rate of a population in the context of planning a distribution
system. Please confirm that in the context of Toronto Hydro’s distribution system planning,
absolute growth is a more important consideration than the rate of growth. If not, please
explain.
```

**Query used for retrieval (locations stripped)**

```
In Reference 1, Toronto Hydro shows that Toronto Hydro’s customer count has been slowing and is
projected to average 0.3% annually in the last three years of the rate period. The same reference
shows a downward trend in normalized MVA that is forecast to continue.
In Reference 2, Toronto Hydro states that “Toronto Hydro distributes electricity to Canada’s largest
- and North America’s second fastest growing city.”
Reference 4 indicates the City of Toronto’s population growth rate will slow.
a) Please explain Toronto Hydro’s view of the importance of absolute increase in population
as compared to the growth rate of a population in the context of planning a distribution
system. Please confirm that in the context of Toronto Hydro’s distribution system planning,
absolute growth is a more important consideration than the rate of growth. If not, please
explain.
```

**Response**

```
Reference 1 above relates to customer and load growth changes from 2018 to 2029 for the
purpose of establishing a customer and load growth forecast to determine revenue to be collected
through rates, as fully described in Exhibit 3.
Reference 2 above contextualizes the size and characteristics of Toronto Hydro’s system and
customer base. Similar information is relied upon in the productivity evidence at Exhibit 1B, Tab 3,
Schedule 3 at pages 2 to 4, wherein Toronto Hydro describes its unique characteristics as a dense
urban distributor and the resulting operational challenges that it must manage in connecting and
serving its customers and carrying out prudent and necessary work to keep the system safe and
reliable in accordance with good utility practice.
Neither of the above references relate to growth for the purposes of distribution system planning,
which is articulated in full in Exhibit 2B, and summarized in Section A of that Exhibit at page 10:
“The growth is concentrated in certain pockets, namely the downtown core and along the transit
corridors, and is oriented vertically with a continuing trend of high-rise developments. This has
resulted is a marked need for new housing, transit solutions, and infrastructure, all of which needs
to be serviced by Toronto Hydro in the years to come.”
As outlined throughout the evidence in Exhibit 2B, distribution system planning is complex and
relies on a long list of varied inputs and planning considerations. There is no single metric of growth
relied upon to inform system planning.
QUESTION (B) :
b) Please reconcile the apparent discrepancy between the statement that the City of
Toronto’s population is growing, in absolute terms, more than other cities with Toronto
Hydro’s forecasts showing slowing system load growth rates and the Ontario Ministry of
Finance’s projections that population growth is slowing for the City of Toronto.

Based on the response in part (a) above, Toronto Hydro submits there is no discrepancy, as
absolute growth and growth rates are referenced for different purposes in different contexts.
Both Reference 3 and Reference 4 are based on Statistics Canada data released in January 2023.
Reference 3 looks at growth over the preceding 12-month period and concludes that Toronto’s
population grew by 138,240 people, which is second only to Dallas-Fort Worth-Arlington in the cities
compared. Reference 4, on the other hand, is prospective and looks at population projections from
2022-2046. Reference 4 notes that Toronto’s population is projected to rise from 3.03 million in 2022
to 4.20 million in 2046, which is the largest population gain among the census divisions, but that the
rate growth of 37.7 percent is slightly slower than the provincial rate of growth of 43.6 percent.
```

verdict: wrong (question holds only part (a); part (b) is in the response field)
label-for-query: yes

## 10. 1B-STAFF-52  (doc `th-consolidated-interrogatory-responses`, pp. 380-384)

- gold (response) exhibits: **1B, 2B**
- reference-line exhibits: 1B
- PDF: http://localhost:3077/api/pdf/th-consolidated-interrogatory-responses#page=380

**Question (as filed)**

```
With Reference 1, Toronto Hydro shows the proposed 2025-2029 custom scorecard with 12
measures and targets.

a) Please reproduce Reference 1 with the following information:
i.
A column which indicates the total revenue requirement during the rate term of all
identified key programs associated with the delivery of the result, as detailed
throughout Reference 1.
ii.
A column which indicates the dollar value of the PIM at proposed weight and total
PIM envelope of $65M as proposed.
iii.
A column which indicates the calculated value of customer benefits realized in the
2025-2029 period (as identified in Table 21, p. 57, or elsewhere if applicable).
iv.
A column which indicates the ratio of iii) to ii) for each proposed PIM
```

**Query used for retrieval (locations stripped)**

```
With Reference 1, Toronto Hydro shows the proposed 2025-2029 custom scorecard with 12
measures and targets.
a) Please reproduce Reference 1 with the following information:
i.
A column which indicates the total revenue requirement during the rate term of all
identified key programs associated with the delivery of the result, as detailed
throughout Reference 1.
ii.
A column which indicates the dollar value of the PIM at proposed weight and total
PIM envelope of $65M as proposed.
iii.
A column which indicates the calculated value of customer benefits realized in the
2025-2029 period (as identified in Table 21, p. 57, or elsewhere if applicable).
iv.
A column which indicates the ratio of iii) to ii) for each proposed PIM
```

**Response**

```
Please see attached a table which lists each of the 12 scorecard metrics and targets, alongside a
column which assign a proportion of the proposed $65 million incentive to each metric, and a
column which assigns a proportion of quantifiable benefits realized over 2025 to 2029, as
presented in Exhibit 1B, Tab 3, Schedule 1.
Toronto Hydro cannot assign portions of its total revenue requirement to each metric on the
custom scorecard as there is not a one to one relationship between expenditures in these
programs and achieving specific performance metrics. Multiple programs contribute to multiple
performance objectives and it is not possible to attribute specific costs to specific measures and
targets. Toronto Hydro also notes that the request appears to infer that the capital and operational
programs detailed in this application are proposed on the basis and justification of target
achievement and associated economic benefits for customers. This is not the case. The capital and
OM&A program budgets proposed stand on their own merits, on the basis of the detailed evidence
submitted in Exhibits 2B and 4 describing the processes, needs, inputs, and other factors relied on
to conclude that the proposed 2025 to 2029 investment plan is the appropriate plan to meet the
needs of Toronto Hydro’s system and customers. The performance incentive is a complimentary
proposal to improve the balance of risk between the utility and ratepayers in responsiveness to the
OEB’s feedback in the last rate application.
QUESTION (B):
b) Please Discuss:
i.
The proportion and significance of the PIM and its weighting within the PIM
framework, relative to the proportion and significance of identified key programs,
as provided in part i) above, in the context of Toronto Hydro’s overall spending
plan. Please evaluate how well the scope and value of its proposed PIMs
correspond with the scope and value of Toronto Hydro’s key spending and
investment areas within its plan.
ii.
The rationale and basis for the proportions of costs and benefits calculated in iv)
above, including variations in the observed ranges.
iii.
For any value where iii) is less than or equal to i), please explain Toronto Hydro’s
rationale for the particular PIM proposed, including its weight.

Please see a) above with respect to the comparison of program costs and PIM incentives and
benefits. With respect to the PIM incentive relative to quantified benefits, the benefits received by
customers outweigh the cost of the PIM incentive in all scenarios, with the lifetime benefits
significantly outweighing the size of the PIM. This analysis does not take into account numerous
measures and targets (e.g. Customer Satisfaction, Customer Escalations, TRIF, Security
Enhancements, Grid Automation Readiness, ISO Certification) which although cannot reliably
quantified nonetheless provide long-term value to customers.
Page 1 of 2
Quantified Benefits
Ratio: Incentive vs.
Performance
Weight
Measures
Five-Year
Target
Incentive
Qu
```

verdict: wrong (question holds only part (a); part (b) is in the response field)
label-for-query: yes

## 11. 1B-STAFF-63  (doc `th-consolidated-interrogatory-responses`, pp. 415-416)

- gold (response) exhibits: **4, 9**
- reference-line exhibits: 1B
- PDF: http://localhost:3077/api/pdf/th-consolidated-interrogatory-responses#page=415

**Question (as filed)**

```
Toronto Hydro states that increase in costs occurred in 2019 and 2020 due to switching from bi-
monthly billing to monthly billing.

Provide detailed explanation of increase in Billing O&M cost from 2018 to 2022 of more than
double 2018 customer billing costs.
Explain how productivity and economies of scale was not achieved with the adjustment of billing
period?
```

**Query used for retrieval (locations stripped)**

```
Toronto Hydro states that increase in costs occurred in 2019 and 2020 due to switching from bi-
monthly billing to monthly billing.
Provide detailed explanation of increase in Billing O&M cost from 2018 to 2022 of more than
double 2018 customer billing costs.
Explain how productivity and economies of scale was not achieved with the adjustment of billing
period?
```

**Response**

```
The Billing O&M costs provided in Table 10 do not provide a consistent representation of Toronto
Hydro’s unit cost per customer over the 2018-2022 period. The key contributing factors are: 1) the
introduction of monthly billing costs into the calculation; and 2) enhanced mapping precision
between the Ontario Energy Board USoA accounts 5315 and 5320 following the utility’s conversion
from the its legacy accounting system, Ellipse, to its current accounting system, SAP, in 2019.
As shown in Table 1, when USoA accounts 5315 and 5320 are combined from 2018 to 2022,
Toronto Hydro’s costs are accurately represented, including the impact of monthly billing starting
in 2020. Other variances are explained throughout Exhibit 4, Tab 2, Schedule 14.
Table 1: Combined USoA Accounts – 2018 to 2022
Accounts ($ million)
2018
Actual
2019
Actual
2020
Actual
2021
Actual
2022
Actual
Combined USoA accounts 5315 and 5320
23.3
22.2
26.4
25.1
28.5
As shown above, costs are relatively flat during the period of 2018 to 2022, when normalized for the
inclusion of $4.8 million in incremental costs for the conversion from bi-monthly billing to monthly
billing in 2020. A detailed discussion of the impact on costs related to the mandatory transition to
monthly billing can be found in Toronto Hydro’s 2020-2024 CIR rate application.1
The vast majority of costs associated with billing customers monthly are not subject to economies
of scale benefits. For example, postage, paper and printing, and payment processing costs, which
combined make up 64% of the incremental operational costs, are directly related to the number of
bills sent.
To minimize the incremental labour costs, Toronto Hydro undertook a number of initiatives,
including automation, process improvements, outsourcing and campaigns to drive ebill adoption.
An example was the replacement of "gatekeeper systems" which gather and transmit data from
meters to Toronto Hydro's billing system, which resulted in more timely and accurate data being
gathered automatically and reduced the labour (and associated costs) required to manually collect
and estimate hard to read meters. Along with the higher transactional volumes, labour economies
of scale were further improved through these initiatives, such that the FTE per 100,000 bills issued
reduced from approximately 4.5 FTEs in 2015 to 3.0 FTEs in 2020.
1 EB-2018-0165, Exhibit 9, Tab 1, Schedule 1, Page 20 to 31
```

verdict: wrong (gold 9 comes from 'EB-2018-0165, Exhibit 9', an exhibit of the previous rate case)
label-for-query: no (same reason)

## 12. 1A-CCC-2  (doc `rds-845747`, pp. 212-215)

- gold (response) exhibits: **4, 1B, 3, 2A, 2B**
- reference-line exhibits: 1A
- PDF: http://localhost:3077/api/pdf/rds-845747#page=212

**Question (as filed)**

```
a) Please provide a complete list of all external consultants/lawyers Toronto engaged to assist it in
the development of the Application and pre-filed evidence;
b) For each engagement please provide the nature of the work and the retainer and terms of
reference;
c) Please provide the budgeted cost for the work for each engagement and the costs incurred to
date. Please indicate how the costs are to be recovered;
```

**Query used for retrieval (locations stripped)**

```
a) Please provide a complete list of all external consultants/lawyers Toronto engaged to assist it in
the development of the Application and pre-filed evidence;
b) For each engagement please provide the nature of the work and the retainer and terms of
reference;
c) Please provide the budgeted cost for the work for each engagement and the costs incurred to
date. Please indicate how the costs are to be recovered;
```

**Response**

```
The table below includes a list of all the consultants Toronto Hydro engaged to prepare expert
evidence for this rate application, the costs incurred to date (as of year-end 2023), and notes whether
the expert was engaged pursuant to an RFP. The total expected costs of the consultants depends on
the work required by these third parties to answer interrogatories, and the extent to which the OEB
and intervenors seek to have these third parties attend the hearing and be involved with other
procedural steps in this application. With the exception of certain studies undertaken in the normal
course of business, the cost of this work is managed through the consulting budget in Appendix 2-M
and is to be recovered through the Regulatory Affairs segment of the Public, Legal and Regulatory
Affairs program at Exhibit 4, Tab 1, Schedule 18. The budgeted costs for legal expenses are also set
out in Appendix 2-M. Please refer to 1B-SEC-11 for retainers for external service providers engaged
to prepare expert evidence.
Expert
Nature of Work /Evidence
Evidence Reference
RFP
Actual Costs
Reference
Customer Engagement
Incurred to
Date (2023)
Innovative
Research Group
Study
Exhibit 1B, Tab 5,
Schedule 1, App A
Yes
$760,661
Total Cost and Reliability
Benchmarking
Exhibit 1B, Tab 3,
Schedule 3, App A
Yes
Clearspring
Energy Advisors
$588,536
Load Forecast EV & DER
Integration
Exhibit 3, Tab 1,
Schedule 1, Appendix J
Yes
UMS Group Inc.
Unit Cost Benchmarking
Exhibit 1B, Tab 3,
Schedule 3, App C
No
$276,300
Scott Madden
Associates
Rate Framework Review
Exhibit 1B, Tab 2,
Schedule 1, Appendix A
Yes
$97,780
(USD)
Guidehouse
Lead/Lag Study
Exhibit 2A, Tab 3,
Schedule 2
No
$92,000
Concentric
Advisors
Financial Useful Lives
Exhibit 2A, Tab 2,
Schedule 1, Appendix D
Yes
$225,857
Exhibit 2B, Section D4,
EA Technology
Asset Condition
Assessment (ACA) Review
Appendix C
No
$53,500
(USD)
Element Energy
Future Energy Scenarios
Exhibit 2B, Section D4,
App B
Yes
$125,0001
IT Cost & Maturity
Exhibit 2B, Section D8,
Gartner
Consulting
Benchmarking
App A
No
$137,500
Stantec
Climate Change
Exhibit 2B, Section D2,
Vulnerability
App A
Yes
$29,374
Exhibit 4, Tab 4, Schedule
Mercer Canada
Compensation
Benchmarking
5
Yes
$79,999.75
QUESTION (D) :
Please explain, in detail, how Toronto Hydro determined which areas of the Application should be
reviewed and validated by external experts;
1 Toronto Hydro notes that the cost noted here is only for the preparation of the report. For details on the
model development and implementation costs, please see Exhibit 2B-Staff-156.

Toronto Hydro used experience and professional judgment to determine which areas of the
application would benefit from review and/or validation from external consultants. Factors
included: guidance provided by the OEB in the RRF, the Handbook for Utility Rate Applications and
the Filing Requirements; what may be helpful to the OEB in understanding and assessing Toronto
Hydro’s application; and precedent from prior proceedings. In
```

verdict: wrong (question holds parts (a)-(c); parts (d)-(g) are in the response field)
label-for-query: yes (exhibits are cited as where each consultant's evidence is filed; borderline)

## 13. 3-STAFF-274  (doc `rds-843536`, pp. 1-4)

- gold (response) exhibits: **3**
- reference-line exhibits: 3
- PDF: http://localhost:3077/api/pdf/rds-843536#page=1

**Question (as filed)**

```
Toronto Hydro has included CDM as a multivariate regression variable as part of its proposed load
forecast in an attempt to represent conservation that occurs through formal programming as well
as naturally.

a) Please discuss how Toronto Hydro considered guidance from the OEB’s Regional Planning
Process Advisory Group’s Load Forecast Guideline for Ontario, including how it considered how to
adjust the gross demand forecast to reflect the forecast impact of non-wires alternative activities
(including DERs, CDM and distributed generation).
```

**Query used for retrieval (locations stripped)**

```
Toronto Hydro has included CDM as a multivariate regression variable as part of its proposed load
forecast in an attempt to represent conservation that occurs through formal programming as well
as naturally.
a) Please discuss how Toronto Hydro considered guidance from the OEB’s Regional Planning
Process Advisory Group’s Load Forecast Guideline for Ontario, including how it considered how to
adjust the gross demand forecast to reflect the forecast impact of non-wires alternative activities
(including DERs, CDM and distributed generation).
```

**Response**

```
Toronto Hydro reviewed but did not incorporate OEB’s Regional Planning Process Advisory Group’s
Load Forecast Guideline for Ontario for its Revenue load forecast. It is Toronto Hydro’s
understanding that the purpose of the OEB’s Regional Planning Process Advisory Group’s Load
Forecast Guideline for Ontario, is to provide guidance to Ontario LDC’s in the preparation of Peak
Demand Forecasts used for Regional Planning. Where the proposed revenue load forecast in the
Exhibit 3 focuses on projecting distribution electricity consumption and billing demand at the
customer level. Thus, Toronto Hydro’s view is that the guidance and underlying assumptions are
not applicable for the use of the revenue load forecast.
QUESTION (B):
b) Toronto Hydro has based its annual forecasted CDM savings for the 2025 to 2029 period on the
assumption that there will be a continuation of the current IESO CDM Framework. Please confirm
that should there be any changes to IESO CDM program delivery, including expanded delivery to
residential and business customers, that there will be no subsequent changes to Toronto
Hydro’s proposed 2025-2029 CDM savings after the OEB has approved Toronto Hydro’s application.

Toronto Hydro confirms that should there be any changes to IESO CDM program delivery there will
be no subsequent changes to Toronto Hydro’s proposed 2025-2029 CDM savings embedded in the
load forecast after the OEB has approved Toronto Hydro’s application.
QUESTION (C):
c) Please discuss the basis for Toronto Hydro’s forecasted 2025-2029 Gross Energy Efficiency and
Demand Response savings. In particular, please discuss the basis for the increase in demand
savings for the residential class.

The 2025-2029 CDM savings mirror the final year of the IESO’s 2021-2024 CDM Framework for the
province, with an extrapolation for Toronto Hydro’s portion. Residential demand savings are not
used in the CDM variable, and are only shown for display purposes.
QUESTION (D):
d) Please discuss how Toronto Hydro has included any naturally occurring conservation during the
2025 to 2029 period?

Toronto Hydro has moved towards including CDM as a multivariate regression variable to
represent conservation that occurs through CDM program delivery. Naturally occurring
conservation may be captured through the CDM variable, as well as the time trend variables used.
QUESTION (E):
e) Please discuss how Toronto Hydro has incorporated information from the IESO’s Annual Planning
Outlook to inform its CDM forecasts.

Toronto Hydro reviewed but did not incorporate IESO’s Annual Planning Outlook to inform its CDM
forecasts.
QUESTION (F-H):
f) On what basis has Toronto Hydro concluded that the impact of heat pumps on overall load and
demand is not yet material. Please discuss how, if at all, Toronto Hydro has considered
recommendations from the Electrification and Energy Transition Panel and/or OEB findings in
Enbridge Gas Inc.’s recent rate proceeding (EB-2022-0200) related to the revenue horizon for new
cu
```

verdict: wrong (question holds only part (a); parts (b)-(h) are in the response field)
label-for-query: yes

## 14. 4-STAFF-306  (doc `th-consolidated-interrogatory-responses`, pp. 3063-3064)

- gold (response) exhibits: **4**
- reference-line exhibits: 4
- PDF: http://localhost:3077/api/pdf/th-consolidated-interrogatory-responses#page=3063

**Question (as filed)**

```
Please provide a more detailed explanation for the 83% cost increase in Communications and
Public Affairs from $3.6M in 2020 to $6.6M in 2023.
```

**Query used for retrieval (locations stripped)**

```
Please provide a more detailed explanation for the 83% cost increase in Communications and
Public Affairs from $3.6M in 2020 to $6.6M in 2023.
```

**Response**

```
Based on the quoted numbers, Toronto Hydro assumes that the question is asking about the increase
in this segment from 2020 to 2025, rather than 2020-2023.
The increase in the Communications and Public Affairs segment budget between 2020 and 2025 is
driven by: (i) $1.9 million increase in external services costs related to a return to pre-pandemic levels
of customer communications, and (ii) $1.1 million increase due to market-based annual wage
increase of existing headcount (in accordance with the compensation philosophy in Exhibit 4, Tab 4)
and the addition of 5 FTEs over this period, as shown in the response to interrogatory 4-VECC-74.
Customer communications focus on crucially important topics such as rates, financial assistance,
public safety, crew safety, fraud prevention, outages, emergency preparedness, online tools and
services, and customer education generally, including about the energy transition and related topics.
Increased costs in this area reflect a return to normal levels of communication following the COVID-
19 pandemic, along with an increase that is prudent and necessary to meet growing customer
expectations. This includes engaging with customer through an increasing number of
communications channels (e.g. additional social media channels and online tools) and being
responsive to customers’ expectations for more timely and frequent communications with Toronto
Hydro as an essential service provider.
External costs support the planning, development and execution of frequent communications with
customers through a variety of channels, as outlined in Exhibit 4, Tab 2, Schedule 18 at Page 28. For
example, Toronto Hydro recently planned and executed a multi-channel public safety campaign,
including an email deployment to customers sharing important public safety information. The email
had an open rate of 60% -- well above the average email open rate of around 40% -- reflecting a high
level of customer engagement and interest in the subject matter.
The increase is also attributable to the addition of 4 FTEs to support the day-to-day management of
digital communications channels and increasing customer expectations with respect to engagement
through these channels. Since 2020, there have been more than 45,000 online mentions of Toronto
Hydro, and the utility has resolved 5,226 customer issues via social media. As of July 2023, Toronto
Hydro has over 121,400 followers on X (formerly known as Twitter), approximately 40%-60% more
followers than the other three large distributors in Ontario. Additionally, the resources are necessary
to respond to an overall increase operational volume of work, associated with customer
communications and engagement needs. For example, the volume of customers contacting Toronto
Hydro regarding equipment placement has increased approximately 258 % since 2019.
```

verdict: correct
label-for-query: yes

## 15. 2B-STAFF-161  (doc `th-consolidated-interrogatory-responses`, pp. 1740-1740)

- gold (response) exhibits: **2B**
- reference-line exhibits: 2B
- PDF: http://localhost:3077/api/pdf/th-consolidated-interrogatory-responses#page=1740

**Question (as filed)**

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

**Query used for retrieval (locations stripped)**

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

**Response**

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

verdict: correct
label-for-query: yes

## 16. 1B-PP-12  (doc `th-consolidated-interrogatory-responses`, pp. 780-780)

- gold (response) exhibits: **1B**
- reference-line exhibits: -
- PDF: http://localhost:3077/api/pdf/th-consolidated-interrogatory-responses#page=780

**Question (as filed)**

```
“the majority of Key Account customers surveyed have goals to reduce their net
GHG emissions to zero, and expect Toronto Hydro to support them in meeting their
climate objectives by ensuring that the system has capacity for growth and by
providing them advisory services to support their decarbonization-through-
electrification journey” [Investment Plan Section 3.1] Please provide any references
that support this observation (e.g. THESL key account interactions, survey
questions, etc.).
```

**Query used for retrieval (locations stripped)**

```
“the majority of Key Account customers surveyed have goals to reduce their net
GHG emissions to zero, and expect Toronto Hydro to support them in meeting their
climate objectives by ensuring that the system has capacity for growth and by
providing them advisory services to support their decarbonization-through-
electrification journey” [Investment Plan ] Please provide any references
that support this observation (e.g. THESL key account interactions, survey
questions, etc.).
```

**Response**

```
Customers were asked “Does your organization have a carbon reduction program in place? Page 31
of Exhibit 1B, Tab 5, Schedule 1, Appendix A, - Customer Engagement Report, Appendix.06 – Key
Accounts shows that a majority (64%) of Toronto Hydro’s key account customers had “net zero”
targets or carbon reduction initiatives in place at the time of the Phase I Needs and Preferences
Survey consisting of:
•
38% reporting carbon reduction targets currently in place, and
•
26% reporting “net zero” targets.
Additionally, page 28 of Appendix.01 – Qualitative Research documents that many key account
participants interviewed in Phase I “shared their hopes that Toronto Hydro would increase their
support in helping them transition to lower or non-emitting carbon energy sources, building out
more distributed energy resources (including battery storage), and enabling grid modernization,
such as microgrids technologies”.
```

verdict: correct
label-for-query: yes

## 17. 1B-CCC-37  (doc `th-consolidated-interrogatory-responses`, pp. 598-602)

- gold (response) exhibits: **4, 2B**
- reference-line exhibits: 1B
- PDF: http://localhost:3077/api/pdf/th-consolidated-interrogatory-responses#page=598

**Question (as filed)**

```
Toronto Hydro is proposing a Demand-Related Variance Account (DRVA) to record the demand
driven revenue requirement impacts arising from variances in actual versus forecast capital and
operational expenditures for certain demand-based programs and the revenue impacts arising
from variances in forecast versus actual billing determinants over the rate period. The Council
is interested in understanding the scope of the DRVA;

a) For each year 2020-2024 please provide the forecast and actual expenditures for the
following capital and operating programs: Customer Connections, Customer Operations,
Stations Expansion, Load Demand, Non-Wires Solutions, Generation Protection Monitoring
and Control and Externally-initiated Plant Relocations and Expansions. Also, please provide
the forecast and actual revenue requirement that would have been dealt with through the
DRVA Expenditure sub-account had one been in place for that period;
```

**Query used for retrieval (locations stripped)**

```
Toronto Hydro is proposing a Demand-Related Variance Account (DRVA) to record the demand
driven revenue requirement impacts arising from variances in actual versus forecast capital and
operational expenditures for certain demand-based programs and the revenue impacts arising
from variances in forecast versus actual billing determinants over the rate period. The Council
is interested in understanding the scope of the DRVA;
a) For each year 2020-2024 please provide the forecast and actual expenditures for the
following capital and operating programs: Customer Connections, Customer Operations,
Stations Expansion, Load Demand, Non-Wires Solutions, Generation Protection Monitoring
and Control and Externally-initiated Plant Relocations and Expansions. Also, please provide
the forecast and actual revenue requirement that would have been dealt with through the
DRVA Expenditure sub-account had one been in place for that period;
```

**Response**

```
Please see below Table 1 for Actuals/Bridge Capital Expenditures and Table 2 for Actuals/Bridge
Operating Expenditures. In responding to this interrogatory Toronto Hydro has only included
OM&A segments that would have been dealt with through the DRVA expenditure sub-account had
one been in place for that period.
Table 1: Actuals/Bridge Capital Expenditures that would have been subject to the DRVA sub-
account (in $ millions)
Actuals
Bridge
Programs
2020
2021
2022
2023
2024
Customer Connections
35.6
92.4
76.1
86.8
78.2
Stations Expansion
18.2
50.3
47.5
10.4
16.1
Load Demand
24.0
29.7
30.8
26.7
23.2
Non-Wires Solutions1
1.0
0.5
0.1
0.0
0.6
Generation Protection Monitoring & Control1
0.8
0.8
0.1
0.2
7.8
Externally Initiated Plant Relocations &
Expansions
8.7
9.3
12.9
16.0
13.0
Table 2: Actuals/Bridge Operating Expenditures that would have been subject to the DRVA sub-
account (in $ millions)
OM&A Segments2
Actuals
Bridge
2020
2021
2022
2023
2024
Customer Connections, Exhibit 4, Tab 2, Schedule
8, Section 5
3.7
1.6
1.6
3.1
3.6
Key Accounts, Exhibit 4, Tab 2, Schedule 8,
Section 6
-
0.5
0.8
0.8
1.2
Flexibility Services, Exhibit 2B, Section E7.2
0.4
0.2
0.2
0.8
0.8
Please see Table 3 for approved Capital Expenditures and Table 4 for approved Operating
Expenditures that would have been dealt with through the DRVA expenditure sub-account had one
been in place for that period.
Table 3: Approved Capital Expenditures that would have been subject to DRVA sub-account (in $
millions)
Approved
Programs
2020
2021
2022
2023
2024
Customer Connections
40.1
40.9
41.7
42.6
43.4
1 94% of the Renewable Enabling portions of these investments will be provincially funded and not included
in the DRVA
2 Only includes segments associated with the DRVA
Approved
Programs
2020
2021
2022
2023
2024
Stations Expansion
19.5
40.0
49.3
12.5
15.2
Load Demand
11.3
11.4
18.5
22.6
23.6
Non-Wires Solutions3
1.0
3.7
3.8
1.0
1.0
Generation Protection Monitoring & Control3
3.7
2.3
2.4
2.5
2.7
Externally Initiated Plant Relocations &
Expansions
11.4
20.8
4.6
4.7
4.5
As noted in Toronto Hydro’s response to interrogatory 4-SEC-89(a), the total OM&A cost approved
by the OEB for 2020 was $266.7 million, which was lower than the 2020 test year OM&A funding
requested by Toronto Hydro. 4 The OEB approved OM&A on an envelope basis and therefore,
Toronto Hydro cannot provide a breakdown by the specific programs or segments such as Customer
connections. However, in order to provide a directional view of the segments that would have been
dealt through the DRVA expenditure sub-account had one been in place for that period, Toronto
Hydro has used its 2020 test5 costs for Customer Connections, Key Accounts and Flexibility Services
and have escalated it by the OEB approved Custom Price Cap Index (“CPCI”) formula6 for 2021-2024
using OEB’s prescribed rates.
Table 4: Approved* Operating Expenditures that would have been subject to the DRVA sub-
account (in $ millions)
Approved*
OM&A Segments
2020
2021
2022
20
```

verdict: wrong (exhibits appear as table row labels for segments, not as where the requested figures are; parts (b)-(d) in response)
label-for-query: no (same reason)

## 18. 1B-STAFF-19  (doc `th-consolidated-interrogatory-responses`, pp. 287-290)

- gold (response) exhibits: **1B**
- reference-line exhibits: 1B
- PDF: http://localhost:3077/api/pdf/th-consolidated-interrogatory-responses#page=287

**Question (as filed)**

```
Page 2 of Reference 1, Toronto Hydro states:
“the Company’s proposed changes to the Rate Framework are generally consistent with
how other electric utilities have responded to developments in the energy industry. [italics
added]”
On page 3:
“Given these developments in the energy industry, many regulatory jurisdictions have
implemented changes to ratemaking frameworks and practices. These changes are
designed to incorporate expanded objectives and priorities, such as clean energy goals,
affordability, reliability, emission reduction, and utility financial integrity.”

a) Please confirm the following statements. If Toronto Hydro disagrees with any or all of
these statements, please explain why.
i.
Toronto Hydro already operates under an approach to custom incentive rate-
setting that it has dubbed CIR 1.0.
1. This ratemaking system includes a price cap index formula with a C factor
that effectively replaces capital revenue growth based primarily on
inflation and productivity indexing with capital revenue growth based
primarily on a cost forecast.
2. The inflation measure in this formula includes a relevant input price index:
the average weekly earnings on Ontario workers.
3. An asymmetrical Capital-Related Revenue Requirement Variance Account
returns any and all capital-related revenue requirement savings to
customers.
4. There is also a two-way variance account for miscellaneous externally-
driven costs.
ii.
Toronto Hydro’s new CIR proposal entails the following changes from its old
proposal.
1.A revenue growth factor (“RGF”) would effectively replace OM&A as well
as capital revenue growth based primarily on inflation and productivity
indexing with growth that is based primarily on cost forecasts.
2. A revenue cap index would replace the price cap index, and a demand
revenue variance account (“DRVA”) would effectively establish weather-
normalized revenue decoupling.
3. The DRVA would also establish two-way variance account treatment for a
wide range of demand-sensitive costs.
4. The Capital-Related Revenue Requirement Variance Account would be
discontinued.
5.There would, additionally be an Innovation Fund, a Getting Ontario
Connected Act Variance Account, and PIM tied to customer service quality
and various policy goals.
```

**Query used for retrieval (locations stripped)**

```
of Reference 1, Toronto Hydro states:
“the Company’s proposed changes to the Rate Framework are generally consistent with
how other electric utilities have responded to developments in the energy industry. [italics
added]”
On :
“Given these developments in the energy industry, many regulatory jurisdictions have
implemented changes to ratemaking frameworks and practices. These changes are
designed to incorporate expanded objectives and priorities, such as clean energy goals,
affordability, reliability, emission reduction, and utility financial integrity.”
a) Please confirm the following statements. If Toronto Hydro disagrees with any or all of
these statements, please explain why.
i.
Toronto Hydro already operates under an approach to custom incentive rate-
setting that it has dubbed CIR 1.0.
1. This ratemaking system includes a price cap index formula with a C factor
that effectively replaces capital revenue growth based primarily on
inflation and productivity indexing with capital revenue growth based
primarily on a cost forecast.
2. The inflation measure in this formula includes a relevant input price index:
the average weekly earnings on Ontario workers.
3. An asymmetrical Capital-Related Revenue Requirement Variance Account
returns any and all capital-related revenue requirement savings to
customers.
4. There is also a two-way variance account for miscellaneous externally-
driven costs.
ii.
Toronto Hydro’s new CIR proposal entails the following changes from its old
propos
```

**Response**

```
i.
Confirm.
1. Partially confirm. The C factor is subject to inflation and productivity factors.
2. Partially confirmed. The inflation factor includes a labour and non-labour component.
3. Confirm.
4. Confirm.
ii.
1) Partially confirm. The RGF factor is still subject to inflation and productivity factors.
2) Partially confirm. DRVA trues up billing determinants on a weather normalized basis.
3) Confirm.
4) Confirm.
5) Confirm.
QUESTION (B):
b) Does Toronto Hydro mean that each of these changes is individually consistent with
industry trends or instead that many of these changes are consistent with industry trends?

ScottMadden did not evaluate industry trends. Instead, ScottMadden evaluated Toronto Hydro’s
proposed custom IR plan for its relative consistency with other electric utility ratemaking
frameworks and practices that support a clean energy transition. Please refer to the response to
1B-EP-23, part (a).
QUESTION (C):
c) Is Toronto Hydro stating that ratemaking in North America is moving away from the use of
price and productivity indexing to escalate OM&A revenue and towards its escalation
based on forecasts? If so, please substantiate.

ScottMadden did not evaluate industry trends. Instead, ScottMadden evaluated Toronto Hydro’s
proposed custom IR plan for its relative consistency with other electric utility ratemaking
frameworks and practices that support a clean energy transition. Please refer to the response to
1B-EP-23, part (a).
QUESTION (D):
d) Is Toronto Hydro stating that that ratemaking in North America is moving towards variance
account treatment of most costs of demand growth, including the traditional costs of
customer connections, billing, and collection? If so, please substantiate.

ScottMadden did not evaluate trends in variance account treatment. Please refer to the response
to 1B-EP-23, part (a).
QUESTION (E):
e) Please list the approved multi-year rate plans that Toronto Hydro thinks are most similar to
Toronto Hydro’s proposed CRCI plan and explain the similarities and differences.

Please refer to Figure 1 in Exhibit 1B-2-1 Appendix A, (Review of Rate Framework), pp. 5-6.
```

verdict: wrong (question holds only part (a); parts (b)-(e) are in the response field)
label-for-query: no (gold 1B is cited only in the answer to part (e))

## 19. 1B-STAFF-16  (doc `th-consolidated-interrogatory-responses`, pp. 274-278)

- gold (response) exhibits: **2B, 4, 1B**
- reference-line exhibits: -
- PDF: http://localhost:3077/api/pdf/th-consolidated-interrogatory-responses#page=274

**Question (as filed)**

```
At page 26, Reference 1 states:
“Custom IR is not a multi-year cost of service; explicit financial incentives for continuous
improvement and cost control targets must be included in the application.”

a) Please describe Toronto Hydro’s proposals for continuous improvement within the rate
term, with specific reference to its preference for targets to be established on a five-year
basis rather than annually, as noted at page 31 of Reference 2.
```

**Query used for retrieval (locations stripped)**

```
At , Reference 1 states:
“Custom IR is not a multi-year cost of service; explicit financial incentives for continuous
improvement and cost control targets must be included in the application.”
a) Please describe Toronto Hydro’s proposals for continuous improvement within the rate
term, with specific reference to its preference for targets to be established on a five-year
basis rather than annually, as noted at of Reference 2.
```

**Response**

```
Toronto Hydro’s proposals for continuous improvements within the rate term are found both
within and beyond the 2025-2029 Custom Scorecard and related targets that underpin the
Performance Incentive Mechanism (“PIM”).
Within the 2025-2029 Custom Scorecard and related PIM, Toronto Hydro has put forward various
new performance measures and objectives that reflect the utility’s ongoing commitment to
continuous improvement. More specifically:
•
reducing the duration of unplanned outages that customers experience;
•
enhancing physical and cyber security threat detection and mitigation in accordance with
NIST standards;
•
advancing grid automation readiness for the horseshoe area of the grid by increasing
remote operability of the distribution system and laying the foundation for self-healing;
•
holding itself accountable for delivering demonstrative efficiency achievements
commensurate with the expectations of the empirical stretch-factor proposed as part of
the rate framework;
•
tracking and reporting post-transactional customer satisfaction performance with respect
to customer inquiries (phone and email), Key Accounts engagements, customer
connections, and customer communications re planned outages and construction projects.
•
tracking, reporting and resolving customer escalations in a timely manner.
•
achieving and maintaining certification with international best practices (ISO) in various key
management systems.
•
reducing the company’s GHG emissions in a paced and prudent manner
•
expanding the scope of non-wires solutions by procuring 30MW of flexible capacity to
address system capacity constraints.
The proposal for targets to be established on a five-year basis rather than annually reflect the
necessary and practical considerations of: (i) operational complexity and uncertainty that the utility
must manage in the normal course of business serving the needs of customers in a large, dense,
urban environment; (ii) the multi-year nature of the work that utility needs to perform in order to
achieve the target objectives reflects an integrated five-year plan (not five one-year plans); and (iii)
the need to preserve operational flexibility within this integrated five-year plan to execute work
programs effectively.
Outside of the 2025-2029 Custom Scorecard, Toronto Hydro’s commitment to continuous
improvement is detailed throughout the evidence. Notable examples include:
•
Continuous improvement of the Asset management system, including:
o Continue to improve the maturity of Toronto Hydro’s asset risk management
framework through the full implementation of the Condition Based Risk
Management (“CBRM”) methodology and fully embedding the Engineering Asset
Investment Planning (“EAIP”) solution within asset management processes,
including a custom value framework to enable portfolio optimization.
o Develop Toronto Hydro’s Asset Information Strategy to improve the quality of
asset data and related data sources to support improved analytics & asset
manageme
```

verdict: wrong (question holds only part (a); part (b) is in the response field)
label-for-query: yes

## 20. 2B-AMPCO-27  (doc `th-consolidated-interrogatory-responses`, pp. 2094-2096)

- gold (response) exhibits: **2B**
- reference-line exhibits: 2B
- PDF: http://localhost:3077/api/pdf/th-consolidated-interrogatory-responses#page=2094

**Question (as filed)**

```
As part of the IPPR process, Toronto Hydro monitors and reports on the progress of capital
programs, which includes program level expenditures, project-specific execution status and project
expenditures.
Over the period 2020-2023, please provide the list of material projects/programs that performed
poorly over 2020-2023, explain why and provide the key lessons learned for execution of the 2025-
2029 portfolio.
```

**Query used for retrieval (locations stripped)**

```
As part of the IPPR process, Toronto Hydro monitors and reports on the progress of capital
programs, which includes program level expenditures, project-specific execution status and project
expenditures.
Over the period 2020-2023, please provide the list of material projects/programs that performed
poorly over 2020-2023, explain why and provide the key lessons learned for execution of the 2025-
2029 portfolio.
```

**Response**

```
Toronto Hydro does not have a definition for “poor performing” programs/projects. Project costs
and program completion rates may vary from initial estimates and plan lines due to myriad factors,
including unforeseen challenges during execution.
All projects are reviewed at a project level for adherence to plan. As mentioned in Exhibit 2B,
Section D1.2.3, Toronto Hydro monitors changes to projects through a change management and
governance process. This process includes the change request process, project variance analysis,
and numerous metrics to drive process adherence and continuous improvement. For further
details on the project variance analysis process refer to the response to interrogatory 2B-AMPCO-
29 part (d).
Toronto Hydro’s integrated, portfolio-based forecasting and planning processes focus on delivery
over the five years of the utility’s Distribution System Plan period, allowing for adjustments to be
made when the utility finds that long-term program execution is not on track. Additionally, part of
the Investment Planning and Portfolio Reporting (“IPPR”) process is to review spend variances of
10% and $1 million (over or under) from the previous year in order review common drivers,
emerging issues, and process adherence, and to encourage continuous improvement at all stages
of planning and execution. Portfolio targets may be adjusted based on new findings and emerging
requirements as part of the IPPR process. As work is being executed, the work mix can be adjusted
for multiple reasons such as resource availability, changes in priority, or emerging urgent work. All
of these processes provide continuous feedback to the planning teams on lessons learned during
execution that are then reviewed and considered as part of future work planning, and Toronto
Hydro expects these improvements to benefit execution of the 2025-2029 portfolio.
One recent process improvement included updating the checklist that planners use to ensure
inclusion of all expected costs. This list is updated based on execution variances and challenges
identified through the project variance analysis process. The utility has also introduced additional
review steps to confirm inclusion of all expected costs in estimates during the hand-off from
planning to program management. Another improvement based on recent experience is an
ongoing review of the material management process and its alignment with the project execution
process. This review has identified the need to start the procurement process earlier in the
planning process, for key material with long lead times (>1 year), in advance of the formal design
phase to reduce cycle time for project execution.
Toronto Hydro also expects its implementation of an Engineering Asset Investment Planning
(“EAIP”) tool will improve transparency and reporting with respect to project portfolios and create
new opportunities to enhance program execution effectiveness in the 2025-2029 period. Please
see Exhibit 2B, Section D1, page 14 fo
```

verdict: correct
label-for-query: yes
