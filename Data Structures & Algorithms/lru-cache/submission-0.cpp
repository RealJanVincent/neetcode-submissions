class LRUCache {
private:
    list<pair<int, int>> lst;
    unordered_map<int, list<pair<int, int>>::iterator> mp;
    int capacity;

public:
    LRUCache(int capacity) 
    : capacity(capacity) {
        
    }
    
    int get(int key) {
        unordered_map<int, list<pair<int, int>>::iterator>::iterator it = mp.find(key);
        if (it == mp.end()) {
            return -1;
        } else {
            lst.splice(lst.begin(), lst, it->second);
            return it->second->second;
        }        
    }
    
    void put(int key, int value) {
        unordered_map<int, list<pair<int, int>>::iterator>::iterator it = mp.find(key);
        if (it == mp.end()) {
            lst.push_front({key, value});
            mp[key] = lst.begin();
        } else {
            it->second->second = value;
            lst.splice(lst.begin(), lst, it->second);
            mp[key] = lst.begin();
        }
        if (lst.size() > capacity) {
            mp.erase(lst.back().first);
            lst.pop_back();
        }
    }
};
