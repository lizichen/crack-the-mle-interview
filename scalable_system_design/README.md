# System Design Questions:

4. Design Yelp, 经典题目，quadtree或者grid，geohash我自己没多看，觉着重点不在这里
1. Push notification
3. Information Aggregation System (Fast and slow)

5. Translation System 两种思路，一个是google translate这种，你可以assume已经有一个现成可用的translation service，然后你要设计一个系统满足三高。另外一个思路可以借鉴一下airbnb的翻译系统 https://medium.com/airbnb-engineering/building-airbnbs-internationalization-platform-45cf0104b63c 
6. newsfeed
7. Design netflix
8. i18n
10. Subscription system (youtube subscription)
11. Hashtag trend (top k)
12. Proximity server backend
13. Ad click counter
15. Design typeahead suggestions经典题autocomplete

**Infra Components:**
- Memcached
- KV store, 常考题， 高并发高可用高一致性
- Design load balancer 
- Web crawler

**Search:**
- Real-time twitter search: https://blog.twitter.com/engineering/en_us/a/2011/the-engineering-behind-twitter-s-new-search-experience 

**Messaging:**
- Facebook messenger (include group chat)
- WhatsApp

**Multi-media:**
- Netflix

**Recommendation:**
- Amazon (recommend products)
- Netflix (recommend movie)
- Airbnb (recommend hotel)
- Linkedin (recommend job)

**Social Media:**
- Twitter (view, post, follow)
- Linkedin 
- Facebook 
- Instagram
- Live commenting system
- Design privacy settings (facebook/social media) 

**Ticket Booking:**
- Ticketmaster
- Airbnb
- bookings.com 

**Domain specific:**
- Google Maps / Routing
- Zoom / Video Streaming 
- Google doc
- Design coding contest platform https://medium.com/@jnu_saurav/system-design-online-coding-judge-platform-5b39380818fc