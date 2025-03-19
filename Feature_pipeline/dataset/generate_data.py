import faker
import random
import json
from datetime import datetime

# Initialize Faker
fake = faker.Faker()

# Define possible values for each field
ages = list(range(18, 75))
occupations = [
    "teacher", "engineer", "doctor", "nurse", "software developer", "lawyer", "artist", 
    "entrepreneur", "accountant", "manager", "chef", "student", "police officer",
    "marketing professional", "financial analyst", "freelance writer", "graphic designer",
    "real estate agent", "construction worker", "IT professional", "small business owner",
    "retail worker", "healthcare administrator", "consultant", "scientist"
]

financial_situations = [
    "I have significant student debt but want to start investing.",
    "I have a stable income and want to plan for retirement.",
    "I recently received an inheritance and want to invest it wisely.",
    "I'm looking to buy a home in the next few years.",
    "I have some savings and want to make them grow.",
    "I'm planning for my children's education.",
    "I want to start a side business and need capital.",
    "I'm interested in passive income streams.",
    "I have a significant amount in my emergency fund and want to diversify.",
    "I want to save for a major purchase in the next 3-5 years.",
    "I'm concerned about inflation and want to protect my savings.",
    "I'm considering early retirement and need investment strategies.",
    "I have a variable income and need flexible investment options.",
    "I want to build wealth for long-term financial independence."
]

risk_tolerance = [
    "I have a high risk tolerance and am comfortable with market volatility.",
    "I have a moderate risk tolerance and prefer a balanced approach.",
    "I have a low risk tolerance and prioritize capital preservation.",
    "I'm willing to take calculated risks for potentially higher returns."
]

market_conditions = [
    "Rising interest rates affecting borrowing costs.",
    "Stock market volatility increasing.",
    "Real estate prices steadily climbing.",
    "Inflation concerns influencing investment strategies.",
    "Tech sector experiencing rapid growth.",
    "Cryptocurrency market stabilizing after recent fluctuations.",
    "Green energy sector receiving government subsidies.",
    "Banking sector facing regulatory changes.",
    "Supply chain disruptions affecting manufacturing.",
    "Consumer spending shifting toward services.",
    "Government announces increased focus on renewable energy.",
    "Fluctuations in oil prices impact energy market dynamics.",
    "Several blue-chip companies announce dividend increases.",
    "Current low interest rate environment affects traditional savings options.",
    "Emerging markets showing strong growth potential.",
    "Healthcare sector experiencing innovation and expansion.",
    "Bond yields trending upward after period of decline."
]

investment_types = [
    "index funds tracking major market indices",
    "dividend-paying stocks in established companies",
    "corporate and government bonds",
    "real estate investment trusts (REITs)",
    "certificates of deposit (CDs)",
    "target-date retirement funds",
    "municipal bonds for tax advantages",
    "growth stocks in emerging sectors",
    "value stocks in undervalued companies",
    "sector-specific ETFs",
    "high-yield savings accounts",
    "robo-advisors for automated investing",
    "peer-to-peer lending platforms",
    "treasury inflation-protected securities (TIPS)",
    "international equity funds",
    "balanced mutual funds",
    "alternative investments like commodities"
]

# Function to generate response based on profile and context
def generate_investment_advice(age, occupation, financial_situation, risk, market_conditions):
    # Pick appropriate investment types based on age and risk
    suitable_investments = []
    
    if age < 30:
        if "high risk" in risk.lower():
            suitable_investments = [t for t in investment_types if any(x in t.lower() for x in ["growth", "emerging", "international"])]
        elif "moderate risk" in risk.lower():
            suitable_investments = [t for t in investment_types if any(x in t.lower() for x in ["index", "etf", "balanced"])]
        else:
            suitable_investments = [t for t in investment_types if any(x in t.lower() for x in ["savings", "cd", "target-date"])]
    elif age < 50:
        if "high risk" in risk.lower():
            suitable_investments = [t for t in investment_types if any(x in t.lower() for x in ["growth", "real estate", "sector"])]
        elif "moderate risk" in risk.lower():
            suitable_investments = [t for t in investment_types if any(x in t.lower() for x in ["dividend", "balanced", "mutual"])]
        else:
            suitable_investments = [t for t in investment_types if any(x in t.lower() for x in ["bonds", "tips", "value"])]
    else:
        if "high risk" in risk.lower():
            suitable_investments = [t for t in investment_types if any(x in t.lower() for x in ["dividend", "value", "reits"])]
        elif "moderate risk" in risk.lower():
            suitable_investments = [t for t in investment_types if any(x in t.lower() for x in ["municipal", "corporate", "balanced"])]
        else:
            suitable_investments = [t for t in investment_types if any(x in t.lower() for x in ["cd", "treasury", "savings"])]
    
    # If no suitable investments found, use a default subset
    if not suitable_investments:
        suitable_investments = random.sample(investment_types, 3)
    
    # Generate advice based on profile and market conditions
    primary_investment = random.choice(suitable_investments)
    
    # Reference specific market condition
    relevant_condition = next((c for c in market_conditions if any(x in c.lower() for x in primary_investment.lower().split())), random.choice(market_conditions))
    
    # Generate response
    response_parts = [
        f"Based on your profile as a {age}-year-old {occupation} with {financial_situation.lower()[2:]} and {risk.lower()}, I recommend focusing on {primary_investment}.",
        f"Given the current market where {relevant_condition.lower()}, this approach aligns well with your financial goals.",
        "Consider diversifying your portfolio by allocating your investments across different asset classes to manage risk.",
        "It's also important to establish an emergency fund covering 3-6 months of expenses before making significant investments."
    ]
    
    # Add age-specific advice
    if age < 30:
        response_parts.append("At your age, you have time to weather market volatility and potentially benefit from compound growth over the long term.")
    elif age < 50:
        response_parts.append("At this stage in your career, balancing growth with increasing stability becomes more important as you progress toward retirement planning.")
    else:
        response_parts.append("As you approach retirement, consider gradually shifting toward more conservative investments to protect your accumulated wealth.")
    
    return "\n".join(response_parts)

# Generate dataset
dataset = []
for _ in range(50):  # Generate 50 examples
    age = random.choice(ages)
    occupation = random.choice(occupations)
    financial_situation = random.choice(financial_situations)
    risk = random.choice(risk_tolerance)
    
    # Select 2-3 random market conditions
    selected_conditions = random.sample(market_conditions, random.randint(2, 3))
    
    # Create about_me string
    about_me = f"I am a {age} year old {occupation}.\n{financial_situation}\n{risk}\nWhat investment options should I consider?"
    
    # Create context string
    context = "\n".join(selected_conditions)
    
    # Generate investment advice
    response = "\n" + generate_investment_advice(age, occupation, financial_situation, risk, selected_conditions)
    
    # Build the example
    example = {
        "about_me": about_me,
        "context": context,
        "response": response
    }
    
    dataset.append(example)

# Save the dataset
current_time = datetime.now().strftime("%Y%m%d_%H%M%S")
filename = f"investment_dataset_{current_time}.json"
with open(filename, "w") as f:
    json.dump(dataset, f, indent=4)

print(f"Generated {len(dataset)} investment scenarios and saved to {filename}")

