from collections import defaultdict


def add_streamer(streamerInformation, streamers):
    for i in range(0, len(streamerInformation), 3):
        streamers[streamerInformation[i]] = [streamerInformation[i + 1], streamerInformation[i + 2]]
    

def update_views(streamerInformation, streamers):
    # check if streamer is streaming in that category
    if streamers[streamerInformation[0]][1] == streamerInformation[2]: 
        streamers[streamerInformation[0]][0] = streamerInformation[1] # update the view count


def update_category(streamerInformation, streamers):
    # check if streamer is streaming in that category
    if streamers[streamerInformation[0]][1] == streamerInformation[1]: 
        streamers[streamerInformation[0]][1] = streamerInformation[2] # update the streaming category


def remove_streamer(streamerInformation, streamers):
    # check if streamer is streaming in that category
    if streamers[streamerInformation[0]][1] == streamerInformation[1]: 
        del streamers[streamerInformation[0]] # remove this gamer from the data structure

def get_views(category, streamers):
    return sum([int(stream[0]) for stream in streamers.values() if stream[1] == category])


def get_top_cat(category, streamers):
    return max([int(stream[0]) for stream in streamers.values() if stream[1] == category])


def get_top(streamers):
    top = None
    max_views = max([int(stream[0]) for stream in streamers.values()])

    for streamer, view in streamers.items():
        if int(view[0]) == max_views:
            top = streamer
    
    return top
    
    # return max([int(stream[0]) for stream in streamers.values()])

def solution(streamerInformation, commands):
    res = []

    streamers = defaultdict(list)

    add_streamer(streamerInformation, streamers)
    
    for i in range(len(commands)):
        if commands[i] == 'StreamerOnline':
            add_streamer(commands[i + 1:i + 4], streamers)
        elif commands[i] == 'UpdateViews':
            update_views(commands[i + 1:i + 4], streamers)
        elif commands[i] == 'UpdateCategory':
            update_category(commands[i + 1:i + 4], streamers)
        elif commands[i] == 'StreamerOffline':
            remove_streamer(commands[i + 1:i + 3], streamers)
        elif commands[i] == 'ViewsInCategory':
            res.append(get_views(commands[i + 1], streamers))
        elif commands[i] == 'TopStreamerInCategory':
            res.append(get_top_cat(commands[i + 1], streamers))
        elif commands[i] == 'TopStreamer':
            res.append(get_top(streamers))
        

    return(res)

print(solution(["Ninja", "100000", "Warzone", "Pokimane", "4770000", "Warzone"], ["StreamerOnline", "AOC", "7000", "Warzone", "TopStreamer"]))