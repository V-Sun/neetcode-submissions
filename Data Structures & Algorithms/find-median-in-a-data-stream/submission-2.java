class MedianFinder {
    PriorityQueue<Integer> pq;
    int count;
    public MedianFinder() {
        pq = new PriorityQueue<>();
        count = 0;
    }
    
    public void addNum(int num) {
        count++;
        pq.offer(num);
    }
    
    public double findMedian() {
        System.out.println(count);
        ArrayList<Integer> temp = new ArrayList<>();
        double result = 0.0;
        if(count % 2 == 0) {
            for(int i = 0; i < count/2 - 1; i++) {
                temp.add(pq.poll());
            }
            int med1 = pq.poll();
            int med2 = pq.poll();
            result = med1 + med2;
            result = result/2.0;
            for(int i = 0; i < temp.size(); i++) {
                pq.offer(temp.get(i));
            }
            pq.offer(med1);
            pq.offer(med2);
        } else {
            for(int i = 0; i < count/2; i++) {
                temp.add(pq.poll());
            }
            int med = pq.poll();
            result = med;
            for(int i = 0; i < temp.size(); i++) {
                pq.offer(temp.get(i));
            }
            pq.offer(med);
        }

        return result;
    }
}
