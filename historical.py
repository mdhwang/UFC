
import numpy as np
import pandas as pd
from sklearn.neighbors import KNeighborsRegressor
import math

def dummies(df, col_name):
   return pd.concat([df.drop(col_name, axis=1), pd.get_dummies(df[col_name])], axis=1)

def historical_cleaning(df):
    #Removes Unwatned Columns
    #Removes Unwanted Weight Classes
    #Calculate KNN missing Reach Vals
    #Reduce Outlier Data (Weights)
    #Fills Null Values (AGE)
    #Converts Categorical to Dummies
    #Converts Binary to Boolean
    

    #Split data into winners only
    red_winner = df[df["Winner"]=="Red"]
    blue_winner = df[df["Winner"]=="Blue"]
    red_loser = df[df["Winner"]!="Red"]
    blue_loser = df[df["Winner"]!="Blue"]


    #Define cols to drop per each
    red_cols = ['R_current_lose_streak',
    'R_current_win_streak',
    'R_draw',
    'R_avg_BODY_att',
    'R_avg_BODY_landed',
    'R_avg_CLINCH_att',
    'R_avg_CLINCH_landed',
    'R_avg_DISTANCE_att',
    'R_avg_DISTANCE_landed',
    'R_avg_GROUND_att',
    'R_avg_GROUND_landed',
    'R_avg_HEAD_att',
    'R_avg_HEAD_landed',
    'R_avg_KD',
    'R_avg_LEG_att',
    'R_avg_LEG_landed',
    'R_avg_PASS',
    'R_avg_REV',
    'R_avg_SIG_STR_att',
    'R_avg_SIG_STR_landed',
    'R_avg_SIG_STR_pct',
    'R_avg_SUB_ATT',
    'R_avg_TD_att',
    'R_avg_TD_landed',
    'R_avg_TD_pct',
    'R_avg_TOTAL_STR_att',
    'R_avg_TOTAL_STR_landed',
    'R_longest_win_streak',
    'R_losses',
    'R_avg_opp_BODY_att',
    'R_avg_opp_BODY_landed',
    'R_avg_opp_CLINCH_att',
    'R_avg_opp_CLINCH_landed',
    'R_avg_opp_DISTANCE_att',
    'R_avg_opp_DISTANCE_landed',
    'R_avg_opp_GROUND_att',
    'R_avg_opp_GROUND_landed',
    'R_avg_opp_HEAD_att',
    'R_avg_opp_HEAD_landed',
    'R_avg_opp_KD',
    'R_avg_opp_LEG_att',
    'R_avg_opp_LEG_landed',
    'R_avg_opp_PASS',
    'R_avg_opp_REV',
    'R_avg_opp_SIG_STR_att',
    'R_avg_opp_SIG_STR_landed',
    'R_avg_opp_SIG_STR_pct',
    'R_avg_opp_SUB_ATT',
    'R_avg_opp_TD_att',
    'R_avg_opp_TD_landed',
    'R_avg_opp_TD_pct',
    'R_avg_opp_TOTAL_STR_att',
    'R_avg_opp_TOTAL_STR_landed',
    'R_total_rounds_fought',
    'R_total_time_fought(seconds)',
    'R_total_title_bouts',
    'R_win_by_Decision_Majority',
    'R_win_by_Decision_Split',
    'R_win_by_Decision_Unanimous',
    'R_win_by_KO/TKO',
    'R_win_by_Submission',
    'R_win_by_TKO_Doctor_Stoppage',
    'R_wins',
    'R_Stance',
    'R_Height_cms',
    'R_Reach_cms',
    'R_Weight_lbs',
    'R_age',
    'R_fighter',
    'Referee',
    'location',
    'Winner',
    'title_bout',
    'weight_class',
    'B_Stance',
    'B_win_by_Decision_Majority',
    'B_win_by_Decision_Split',
    'B_win_by_Decision_Unanimous',
    'B_win_by_KO/TKO',
    'B_win_by_Submission',
    'B_win_by_TKO_Doctor_Stoppage',
    'B_longest_win_streak',
    'B_current_lose_streak',
    'B_current_win_streak',
    'B_draw',
    'date',
    'B_wins',
    'B_losses']

    blue_cols = ['B_current_lose_streak',
    'B_current_win_streak',
    'B_draw',
    'B_avg_BODY_att',
    'B_avg_BODY_landed',
    'B_avg_CLINCH_att',
    'B_avg_CLINCH_landed',
    'B_avg_DISTANCE_att',
    'B_avg_DISTANCE_landed',
    'B_avg_GROUND_att',
    'B_avg_GROUND_landed',
    'B_avg_HEAD_att',
    'B_avg_HEAD_landed',
    'B_avg_KD',
    'B_avg_LEG_att',
    'B_avg_LEG_landed',
    'B_avg_PASS',
    'B_avg_REV',
    'B_avg_SIG_STR_att',
    'B_avg_SIG_STR_landed',
    'B_avg_SIG_STR_pct',
    'B_avg_SUB_ATT',
    'B_avg_TD_att',
    'B_avg_TD_landed',
    'B_avg_TD_pct',
    'B_avg_TOTAL_STR_att',
    'B_avg_TOTAL_STR_landed',
    'B_longest_win_streak',
    'B_losses',
    'B_avg_opp_BODY_att',
    'B_avg_opp_BODY_landed',
    'B_avg_opp_CLINCH_att',
    'B_avg_opp_CLINCH_landed',
    'B_avg_opp_DISTANCE_att',
    'B_avg_opp_DISTANCE_landed',
    'B_avg_opp_GROUND_att',
    'B_avg_opp_GROUND_landed',
    'B_avg_opp_HEAD_att',
    'B_avg_opp_HEAD_landed',
    'B_avg_opp_KD',
    'B_avg_opp_LEG_att',
    'B_avg_opp_LEG_landed',
    'B_avg_opp_PASS',
    'B_avg_opp_REV',
    'B_avg_opp_SIG_STR_att',
    'B_avg_opp_SIG_STR_landed',
    'B_avg_opp_SIG_STR_pct',
    'B_avg_opp_SUB_ATT',
    'B_avg_opp_TD_att',
    'B_avg_opp_TD_landed',
    'B_avg_opp_TD_pct',
    'B_avg_opp_TOTAL_STR_att',
    'B_avg_opp_TOTAL_STR_landed',
    'B_total_rounds_fought',
    'B_total_time_fought(seconds)',
    'B_total_title_bouts',
    'B_win_by_Decision_Majority',
    'B_win_by_Decision_Split',
    'B_win_by_Decision_Unanimous',
    'B_win_by_KO/TKO',
    'B_win_by_Submission',
    'B_win_by_TKO_Doctor_Stoppage',
    'B_wins',
    'B_Stance',
    'B_Height_cms',
    'B_Reach_cms',
    'B_Weight_lbs',
    'B_age',
    'B_fighter',
    'Referee',
    'location',
    'Winner',
    'title_bout',
    'weight_class',
    'R_Stance',
    'R_win_by_Decision_Majority',
    'R_win_by_Decision_Split',
    'R_win_by_Decision_Unanimous',
    'R_win_by_KO/TKO',
    'R_win_by_Submission',
    'R_win_by_TKO_Doctor_Stoppage',
    'R_longest_win_streak',
    'R_current_lose_streak',
    'R_current_win_streak',
    'R_draw',
    'date',
    'R_wins',
    'R_losses'
    ]

    red_winner["Year"] = red_winner["date"].apply(lambda x: x[:4])
    red_winner["win_pct"] = red_winner["R_wins"]/(red_winner["R_wins"]+red_winner["R_losses"])
    red_winner["win_pct"] = red_winner["win_pct"].fillna(0)
    red_winner["result"] = 1

    red_loser["Year"] = red_loser["date"].apply(lambda x: x[:4])
    red_loser["win_pct"] = red_loser["R_wins"]/(red_loser["R_wins"]+red_loser["R_losses"])
    red_loser["win_pct"] = red_loser["win_pct"].fillna(0)
    red_loser["result"] = 0

    blue_winner["Year"] = blue_winner["date"].apply(lambda x: x[:4])
    blue_winner["win_pct"] = blue_winner["B_wins"]/(blue_winner["B_wins"]+blue_winner["B_losses"])
    blue_winner["win_pct"] = blue_winner["win_pct"].fillna(0)
    blue_winner["result"] = 1

    blue_loser["Year"] = blue_loser["date"].apply(lambda x: x[:4])
    blue_loser["win_pct"] = blue_loser["B_wins"]/(blue_loser["B_wins"]+blue_loser["B_losses"])
    blue_loser["win_pct"] = blue_loser["win_pct"].fillna(0)
    blue_loser["result"] = 0

    red_winner = red_winner.drop(columns = blue_cols,axis =1)
    blue_winner = blue_winner.drop(columns = red_cols,axis =1)
    red_loser= red_loser.drop(columns = blue_cols,axis =1)
    blue_loser = blue_loser.drop(columns = red_cols,axis =1)

    rename = ['Fighter',
    'no_of_rounds',
    'avg_BODY_att',
    'avg_BODY_landed',
    'avg_CLINCH_att',
    'avg_CLINCH_landed',
    'avg_DISTANCE_att',
    'avg_DISTANCE_landed',
    'avg_GROUND_att',
    'avg_GROUND_landed',
    'avg_HEAD_att',
    'avg_HEAD_landed',
    'avg_KD',
    'avg_LEG_att',
    'avg_LEG_landed',
    'avg_PASS',
    'avg_REV',
    'avg_SIG_STR_att',
    'avg_SIG_STR_landed',
    'avg_SIG_STR_pct',
    'avg_SUB_ATT',
    'avg_TD_att',
    'avg_TD_landed',
    'avg_TD_pct',
    'avg_TOTAL_STR_att',
    'avg_TOTAL_STR_landed',
    'avg_opp_BODY_att',
    'avg_opp_BODY_landed',
    'avg_opp_CLINCH_att',
    'avg_opp_CLINCH_landed',
    'avg_opp_DISTANCE_att',
    'avg_opp_DISTANCE_landed',
    'avg_opp_GROUND_att',
    'avg_opp_GROUND_landed',
    'avg_opp_HEAD_att',
    'avg_opp_HEAD_landed',
    'avg_opp_KD',
    'avg_opp_LEG_att',
    'avg_opp_LEG_landed',
    'avg_opp_PASS',
    'avg_opp_REV',
    'avg_opp_SIG_STR_att',
    'avg_opp_SIG_STR_landed',
    'avg_opp_SIG_STR_pct',
    'avg_opp_SUB_ATT',
    'avg_opp_TD_att',
    'avg_opp_TD_landed',
    'avg_opp_TD_pct',
    'avg_opp_TOTAL_STR_att',
    'avg_opp_TOTAL_STR_landed',
    'total_rounds_fought',
    'total_time_fought(seconds)',
    'total_title_bouts',
    'Height_cms',
    'Reach_cms',
    'Weight_lbs',
    'age',
    'Year',
    'Win_Pct',
    'Result']

    red_winner.columns = rename
    blue_winner.columns = rename
    red_loser.columns = rename
    blue_loser.columns = rename

    lists_to_append = [blue_winner, red_loser, blue_loser]

    #Combine winners into single DF
    master = red_winner.append(lists_to_append,ignore_index=True)
    
    master = master[~master["avg_BODY_att"].isnull()]


    #Change missing stats to Orthodox ~75% already there
    #master["Stance"] = master["Stance"].fillna("Orthodox")


    #Replace Missing Values using KNN
    #Combine all B and R values together for single master list
    r_cols = ["R_Height_cms","R_Reach_cms"]
    b_cols = ["B_Height_cms","B_Reach_cms"]
    header = ["Height","Reach"]

    R_heights_to_reach = df[r_cols]
    R_heights_to_reach.columns = header
    B_heights_to_reach = df[b_cols]
    B_heights_to_reach.columns = header
    MasterHR = R_heights_to_reach.append(B_heights_to_reach,ignore_index=True)

    #Train the KNN Model
    num_neighbors = 3 
    trainer = MasterHR.dropna()
    X = np.array(list(trainer["Height"])).reshape(len(trainer),1)
    y = np.array(list(trainer["Reach"])).reshape(len(trainer),1)
    nay = KNeighborsRegressor(n_neighbors=num_neighbors).fit(X,y)

    #Replace vals with KNN predictions
    master["Reach_cms"] = master.apply(lambda x: nay.predict(np.array(x["Height_cms"]).reshape(1,1))[0][0] if math.isnan(x["Reach_cms"]) else x["Reach_cms"],axis=1)
    
    #Add dummy values (should drop low val stances / weight classes?)
    #big_winner = dummies(big_winner,"weight_class")
    #big_winner = dummies(big_winner,"Stance")
    
    master["age"] = master["age"].fillna(int(master["age"].mean()))


    test = master[master["Year"]=="2019"]
    train = master[master["Year"]!="2019"]

    y_test = test["Result"]
    X_test = test.drop(columns=["Result"])
    y_train = train["Result"]
    X_train = train.drop(columns=["Result"])


    return X_train,y_train,X_test,y_test