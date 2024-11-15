import pandas as pd

def get_cluster_sensor_list(cluster, matrix):
    '''
        Returns dictionary of sensors with cluster label
        Contextual relational boundary of SeReIn-M

        Parameters:
            cluster : predicted cluster labels
            matrix (dataframe): adjacency matrix as dataframe

    '''
    cluster = pd.DataFrame(cluster,index=matrix.index)
    cluster_dict = {}
    for index, row in cluster.iterrows():
        for value in row:
            if not value in cluster_dict:
                cluster_dict[value] = []
            cluster_dict[value].append(index)
    
    for item in cluster_dict:
        print(cluster_dict[item])
    
    return cluster_dict

def get_adjacency_matrix_list(cluster_dict, matrix):
    '''
        Returns list of adjacency matrix of clustered sensors

        Parameters:
            cluster_dict (dictionary): sensors with cluster label
            matrix (dataframe): adjacency matrix as dataframe
    '''
    list_adjs = []
    list_unique_sensors = []
    for key in cluster_dict:
        adj = pd.DataFrame(0.0, columns=cluster_dict[key], index=cluster_dict[key])
        list_unique_sensors.append(cluster_dict[key])
        for index in cluster_dict[key]:
            for head in cluster_dict[key]:
                adj.loc[index,head] = matrix.loc[index,head]

        list_adjs.append(adj)
    
    return list_adjs, list_unique_sensors

def get_groups(adjacency_matrix, number_of_sensors, unique_sensors):
    sensor_groups = []

    for index,row in adjacency_matrix.iterrows():
        initial_sensor = 0
        sensor_value_dict = {}
        for value in row:
            sensor_value_dict[unique_sensors[initial_sensor]] = value
            initial_sensor += 1
        
        sorted_dict = dict(sorted(sensor_value_dict.items(), reverse=True, key=lambda x: x[1]))
        cnt = 0
        group = []
        group.append(index)
        for key in sorted_dict.keys():
            if key != index:
                cnt+=1
                group.append(key)
            if cnt>=number_of_sensors-1:
                break
        group = sorted(group)
        sensor_groups.append(group)
        
    sensor_set = set()

    for j in range(len(sensor_groups)):
        sensor_set = sensor_set | set([tuple(sensor_groups[j])])

    print('number of unique group ', len(sensor_set))
    sensor_group = {}
    for item in sensor_set:
        print(item)
    
    return sensor_set


def get_groups_sensor_count(adjacency_matrix, number_of_sensors, unique_sensors):
    sensor_groups = []

    if number_of_sensors == 1:
        for index, row in adjacency_matrix.iterrows():
            initial_sensor = 0
            sensor_value_dict = {}
            for value in row:
                sensor_value_dict[unique_sensors[initial_sensor]] = value
                initial_sensor += 1
            
            sorted_dict = dict(sorted(sensor_value_dict.items(), reverse=True, key=lambda x: x[1]))
            group = []
            group.append(index)
            sensor_groups.append(group)
            
        sensor_set = set()

        for j in range(len(sensor_groups)):
            sensor_set = sensor_set | set([tuple(sensor_groups[j])])

        print('number of unique group ', len(sensor_set))
        sensor_group = {}
        for item in sensor_set:
            print(item)
        
        return sensor_set
    else:
        for index, row in adjacency_matrix.iterrows():
            initial_sensor = 0
            sensor_value_dict = {}
            for value in row:
                sensor_value_dict[unique_sensors[initial_sensor]] = value
                initial_sensor += 1
            
            sorted_dict = dict(sorted(sensor_value_dict.items(), reverse=True, key=lambda x: x[1]))
            cnt = 0
            group = []
            group.append(index)
            for key in sorted_dict.keys():
                if key != index:
                    cnt+=1
                    group.append(key)
                if cnt>=number_of_sensors-1:
                    break
            group = sorted(group)
            sensor_groups.append(group)
            
        sensor_set = set()

        for j in range(len(sensor_groups)):
            sensor_set = sensor_set | set([tuple(sensor_groups[j])])

        print('number of unique group ', len(sensor_set))
        sensor_group = {}
        for item in sensor_set:
            print(item)
        
        return sensor_set

def get_groups_knee(adjacency_matrix, unique_sensors):
    sensor_groups = []

    for index,row in adjacency_matrix.iterrows():
        initial_sensor = 0
        sensor_value_dict = {}
        for value in row:
            sensor_value_dict[unique_sensors[initial_sensor]] = value
            initial_sensor += 1
        
        sorted_dict = dict(sorted(sensor_value_dict.items(), reverse=True, key=lambda x: x[1]))
        
        sorted_values = []
        for key in sorted_dict.keys():
            sorted_values.append(sorted_dict[key])

        max_diff = float('-inf')
        for i in range(0, len(sorted_values)-1):
            diff = sorted_values[i] - sorted_values[i+1]
            if diff > max_diff:
                max_diff = diff
                number_of_sensors = i+1
                knee_value = sorted_values[i]
        
        cnt = 0
        group = []
        group.append(index)
        for key in sorted_dict.keys():
            if key != index:
                cnt+=1
                group.append(key)
            if cnt>=number_of_sensors-1:
                break
        group = sorted(group)
        sensor_groups.append(group)
        
    sensor_set = set()

    for j in range(len(sensor_groups)):
        sensor_set = sensor_set | set([tuple(sensor_groups[j])])

    print('number of unique group ', len(sensor_set))
    sensor_group = {}
    for item in sensor_set:
        print(item)
    
    return sensor_set

def get_groups_thresholding(adjacency_matrix, threshold_value, unique_sensors):
    sensor_groups = []

    for index, row in adjacency_matrix.iterrows():
        initial_sensor = 0
        sensor_value_dict = {}
        for value in row:
            sensor_value_dict[unique_sensors[initial_sensor]] = value
            initial_sensor += 1
        
        sorted_dict = dict(sorted(sensor_value_dict.items(), reverse=True, key=lambda x: x[1]))

        group = []
        group.append(index)
        for key in sorted_dict.keys():
            if sorted_dict[key] > threshold_value:
                group.append(key)
        if len(group) > 1:
            group = sorted(group)
            sensor_groups.append(group)

    sensor_set = set()

    for j in range(len(sensor_groups)):
        sensor_set = sensor_set | set([tuple(sensor_groups[j])])

    print('number of unique group ', len(sensor_set))
    sensor_group = {}
    for item in sensor_set:
        print(item)
    
    return sensor_set