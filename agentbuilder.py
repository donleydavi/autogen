import autogen
import requests
from autogen.agentchat.contrib.agent_builder import AgentBuilder
from bs4 import BeautifulSoup

# 1 Configuration
config_path = "/Users/daviddonley/Desktop/autogen_agentbuilders/autogen/agentbuilder/OAI_CONFIG_LIST"
config_list = autogen.config_list_from_json(config_path)
default_llm_config = {'temperature': 0}

# 2 Initialising Builder
builder = AgentBuilder(config_file_or_env=config_path)

# 3 Building agents
building_task = "Agent 1 greets the user and requests the property address. Agent 2, without direct user interaction, researches the property online for the number of bedrooms, bathrooms, square footage, and type of fireplace if applicable. Agent 3 then asks the user for Utilities and Services (Electricity Provider, Internet Provider & Specifications, WiFi Details), Waste Management (Trash Pickup), Parking (availability, type, spots, access codes), Accommodation Details (Kitchen appliances, Capacity, Pets Policy, number of Beds, Router location, Trash Bin Storage), and Amenities (Coffee Maker, BBQ Grill type and model, BBQ Utensils Location). Agent 4 verifies all collected information with the user and asks for any missing details. Finally, Agent 5 compiles all accurate and verified information into a CSV file, reaching out to the user for any necessary clarifications."
agent_list, agent_configs = builder.build(building_task, default_llm_config, use_oai_assistant=True)


# 4 Multi-agent group chat
group_chat = autogen.GroupChat(agents=agent_list, messages=[], max_round=12)
manager = autogen.GroupChatManager(groupchat=group_chat, llm_config={"config_list": config_list, **default_llm_config})

# 5 Initiate chat
agent_list[0].initiate_chat(
    manager,
    message="Ask user_proxy for property address..."
)