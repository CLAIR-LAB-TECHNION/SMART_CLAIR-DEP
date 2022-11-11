from typing import List
import numpy as np

###########################################################################
#####                Specify your reward function here                #####
###########################################################################

def get_reward(electricity_consumption: List[float], carbon_emission: List[float], electricity_price: List[float], agent_ids: List[int]) -> List[float]:
        """CityLearn Challenge user reward calculation.

        Parameters
        ----------
        electricity_consumption: List[float]
            List of each building's/total district electricity consumption in [kWh].
        carbon_emission: List[float]
            List of each building's/total district carbon emissions in [kg_co2].
        electricity_price: List[float]
            List of each building's/total district electricity price in [$].
        agent_ids: List[int]
            List of agent IDs matching the ordering in `electricity_consumption`, `carbon_emission` and `electricity_price`.

        Returns
        -------
        rewards: List[float]
            Agent(s) reward(s) where the length of returned list is either = 1 (central agent controlling all buildings) 
            or = number of buildings (independent agent for each building).
        """

        # *********** BEGIN EDIT ***********
        # Replace with custom reward calculation
        electricity_consumption = np.array(electricity_consumption)
        electricity_price = np.array(electricity_price)
        carbon_emission = np.array(carbon_emission)
        # reward = -electricity_price - np.abs(electricity_consumption)
        # reward =  -20*np.clip(electricity_price, -20, 0.1) - np.abs(electricity_consumption)
        reward = -electricity_price - 2*np.abs(electricity_consumption)
        # reward = -electricity_price -carbon_emission
        # ************** END ***************
        
        return reward