MARRIOTT_BONVOY = """
Card Name
Marriott Bonvoy Bevy American Express Card

Welcome Offer
Earn 85,000 Marriott Bonvoy bonus points after you use your new Card to make $4,000 in purchases within the first 3 months of Card Membership.

Annual Fee
$250

Rewards
- 6X Marriott Bonvoy points on purchases at hotels participating in Marriott Bonvoy
- 4X points at restaurants worldwide and U.S. supermarkets (up to $15,000 in combined purchases per calendar year, then 2X)
- 2X points on all other eligible purchases

Key Benefits
- Complimentary Marriott Bonvoy Gold Elite Status
- 1,000 Marriott Bonvoy Bonus Points with each qualifying stay
- Free Night Award (redemption level at or under 50,000 Marriott Bonvoy points) after spending $15,000 on purchases in a calendar year
- 15 Elite Night Credits towards the next level of Marriott Bonvoy Elite status
- Up to $300 in statement credits per calendar year (up to $25 per month) for eligible purchases at restaurants worldwide

Additional Features
- No foreign transaction fees
- Trip delay insurance
- Baggage insurance plan
- Car rental loss and damage insurance
- Global Assist® Hotline

APR
19.24% - 28.24% Variable

Eligibility
- Must be 18 years or older
- Have a valid Social Security number or Individual Taxpayer Identification Number (ITIN)
- Have a valid U.S. mailing address
"""

DELTA_SKYMILES = """
Card Name
Delta SkyMiles Gold American Express Card

Welcome Offer
Earn 70,000 bonus miles after you spend $2,000 in purchases on your new Card in your first 6 months.

Annual Fee
No annual fee for the first year, then $99 per year.

Rewards
- Earn 2X Miles on Delta purchases, at restaurants worldwide, and at U.S. supermarkets.
- Earn 1X Mile on all other eligible purchases.

Key Benefits
- First checked bag free on Delta flights
- Main Cabin 1 Priority Boarding on Delta flights
- $100 Delta Flight Credit after you spend $10,000 in purchases on your Card in a calendar year
- 20% back on in-flight purchases
- No foreign transaction fees

Additional Features
- Car rental loss and damage insurance
- Baggage insurance plan
- Global Assist Hotline
- American Express Experiences

APR
20.74% - 29.74% Variable

Eligibility
- Must be 18 years or older
- Have a valid Social Security number or Individual Taxpayer Identification Number (ITIN)
- Have a valid U.S. mailing address
"""


def get_article_from_content_engine() -> str:
    return "\n\n####" + MARRIOTT_BONVOY + "\n\n####\n" + DELTA_SKYMILES
