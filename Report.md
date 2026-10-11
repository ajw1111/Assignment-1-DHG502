
Introduction & Research Question

When Jesuit missionaries arrived in China during the late Ming dynasty, they brought with them
not only Catholic theology, but also a wealth of knowledge in calendar science, geography, and
astronomy.

By closely examining word clusters within the Ming Shi (明史), this study sets out to answer a
core question: What kind of textual structure and ideological framing surrounded three key Jesuit
figures—Matteo Ricci (利瑪竇), Johann Adam Schall von Bell (湯若望), and Diego de Pantoja
(龐迪峨)? Furthermore, how did official dynastic historiography institutionalize their scientific
contributions while systematically erasing their religious identity?

Data Collection & Method

For this study, I used the complete text of the Ming Shi from Prof. Maciej Kyuzynski’s private
collection, yielding a corpus of 1,509,139 tokens. Text preprocessing and tokenization were
handled using GLM 5.3 Flash and Jieba. I selected Matteo Ricci (利瑪竇), Johann Adam Schall
von Bell (湯若望), and Diego de Pantoja (龐迪峨) as target words because they are the most
iconic pioneers of the Jesuit mission in China.

To capture meaningful associations, I applied a collocation window size of H10 (ten words to the
left and right of each name) and used Log-Dice as the statistical association measure. Log-Dice
is particularly effective here: unlike raw frequency or standard measures, it doesn't inflate
arbitrarily with corpus size, making it much better at revealing genuine word pairings without
getting thrown off by high-frequency noise.

Results

The collocation results from the Ming Shi corpus reveal a strikingly disciplined, technocratic
character across all three missionaries:

● Matteo Ricci (利瑪竇, Frequency f=12): Top Log-Dice collocates include "Westerner"
(西洋人, logDice=12.30), "Calendar Calculation" (歷算, logDice=12.19), "Nine Hundred
Thousand Miles" (九萬里, logDice=12.09), "Diego de Pantoja" (龐迪峨,
logDice=11.54), and "Atlantic Ocean" (大西洋, logDice=11.48). This shows that official
historical records primarily frame Ricci through his foreign identity and the geographical
and calendrical knowledge he brought from the West.

● Johann Adam Schall von Bell (湯若望, Frequency f=7): Core collocates feature
"Giacomo Rho" (羅雅谷, logDice=12.54), "Westerner" (西洋人, logDice=12.19), and
"Calendar" (曆法, logDice=10.68). The data highlights an immediate, inescapable link
between these missionaries and the imperial calendar.

● Diego de Pantoja (龐迪峨, Frequency f=10): Pantoja's collocates tie him closely to fellow
Jesuit missionaries and the Ming official apparatus. Key terms include "Sabatino de
Ursis" (熊三拔/三撥, logDice=12.42), "Emmanuel Diaz, Junior" (陽瑪諾,
logDice=12.30), "Atlantic Ocean" (大西洋, logDice=12.19), "Naturalization" (歸化,
logDice=11.42), "Calendar" (曆法, logDice=11.16), and his official title in the Imperial
Board of Astronomy, "Fifth Rank" (五官, logDice=10.75).

Taken together, these collocation patterns point toward three core characteristics embedded
within the Ming Shi:

1. Instrumentalization of Knowledge and Technology: Ricci’s data centers heavily on
calendar calculation and geography, while Schall and Pantoja remain strictly tethered to
calendar reform. Because traditional China was fundamentally an agrarian state,
maintaining an accurate calendar was tied directly to dynastic legitimacy and political
stability. The imperial government essentially viewed these missionaries as technical
assets, absorbing them into the state bureaucracy purely for their practical utility.

2. Institutional Co-optation of Networks: Fellow Jesuit names like Sabatino de Ursis (熊
三拔/三撥), Emmanuel Diaz Jr. (陽瑪諾), and Giacomo Rho (羅雅谷) appear frequently
alongside Pantoja and Schall, often paired with the concept of "naturalization" (歸化).
This indicates the court did not view the Jesuits as subversive elements or outside threats.
Instead, they were treated as a cohort of skilled foreign specialists to be systematically
integrated into the existing administrative machinery.

4. Marginalization of the Religious Dimension: Most revealingly, overtly religious terms
like "Bible," "church," or "Jesus Christ" are entirely absent from the top Log-Dice
collocates across all three figures. This stark omission strongly implies that the Qing
officials who compiled and edited the Ming Shi deliberately stripped the missionaries of
their religious motivations and identities, reducing them entirely to court scientists.

Limitations

Despite the strengths of using Log-Dice, several methodological and textual limitations should
be noted:

● Small Corpus Frequency: All three missionaries have very low frequencies within the
overall Ming Shi (Ricci: 12, Schall: 7, Pantoja: 10). When working with such small
sample sizes, statistical tests like Fisher's exact test or Log-Dice become extremely
sensitive to minor textual tweaks. Adding or dropping just a couple of lines can warp the
scores, making the statistical significance vulnerable to random chance.

● Sentiment and Polarity Blindness: Collocation metrics only reveal which words
frequently appear alongside the missionaries' names; they cannot determine sentiment or
polarity. For instance, while "Westerner" strongly correlates with Matteo Ricci, the metric
alone cannot tell us whether Qing court historians viewed that foreign identity with
acceptance, indifference, or suspicion within that specific context.

● Coreference Resolution: Another hurdle is coreference resolution, as historical figures
often appear under multiple transliterated names. Checking the Key Word in Context
(KWIC) lines shows that Sabatino de Ursis is written as both 熊三拔 and 三撥 in
Pantoja’s data, and Giacomo Rho (羅雅谷) appears variously under Schall. Without
manual cleaning, algorithms can easily misinterpret these as different individuals.
Furthermore, classical Chinese style frequently relies on shortcuts like courtesy names
(表字) or official titles rather than full names, making it easy for automated tools to miss
implicit references.

● The Nature of Dynastic History: The Ming Shi is an official history compiled later by
the Qing court, meaning it underwent heavy editorial filtering, political sanitization, and
standardization. It is not a collection of raw, firsthand Ming-era documents like original
court memorials. Consequently, the corpus does not capture a real-time record of the
Ming dynasty; rather, it reflects how the Qing government chose to look back and
reconstruct the legacy of the late Ming Jesuits.

Conclusion

Ultimately, analyzing collocation patterns in the Ming Shi demonstrates that the official narrative
surrounding these late Ming Jesuits was heavily filtered through a lens of state utility. Rather
than recording the full scope of their evangelical mission, the text selectively frames them as
foreign technocrats valued strictly for their mathematical, geographical, and astronomical
expertise. This study highlights how digital text analysis can expose the underlying ideological
mechanisms of dynastic historiography—showing how a state-sponsored text can co-opt
technical knowledge while successfully erasing the religious identities of the historical actors
behind it.
