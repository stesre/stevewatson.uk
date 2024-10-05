blog_posts = [
    {
        "title": "Optimizing AWS Costs",
        "summary": "Learn how I helped save $10k per month in AWS costs...",
        "contents": """
           <h5>Cutting AWS Costs by $10k Monthly: My Journey</h5>
           
            As a DevOps engineer, optimizing cloud infrastructure costs is essential. While building a Platform Engineering team at a startup, I made cutting AWS costs a priority—something every company should focus on, regardless of size. Through strategies like Compute Savings Plans, VPC Peering, and S3 storage optimization, we were able to save <b>$10k</b> per month.<br/><br/>

            With AWS, the first step is to identify where most of the costs are concentrated, and you can easily do this using <a href="https://aws.amazon.com/aws-cost-management/aws-cost-explorer/" target="_blank">AWS cost explorer</a>. In our case, we found that a significant portion of our monthly spending was on compute instances, including EC2, Lambda, and ECS. While we also had costs from RDS, traffic, Elasticache, and storage, compute was one of the main culprits. After reviewing various options and weighing the pros and cons, we concluded that the best solution was to sign up for a Compute Savings Plan with AWS.<br/><br/>

            <h4>Compute Savings Plans</h4>
            <i>In my various roles, optimizing cloud costs has always been a priority.</i>
             <br/>An effective strategy at one company was to to implement an AWS compute savings plan. Before I delve further, you might want to read more about what they are, and why you should consider them.<br/><br/>
            <h5>What are compute savings plans?</h5>
            Compute savings plans are fairly flexible pricing models that <i>can</i> offer significant savings by exchanging on-demand rates with a commitment to using at least a specified amount of compute power for a 1, or 3 year period. You can read more about that <a href="https://docs.aws.amazon.com/savingsplans/latest/userguide/what-is-savings-plans.html" target="_blank">here</a><br/><br/>
            <h5>Why should you consider a savings plan?</h5>
            There are a few reasons why you <i>might</i> consider a savings plan for your AWS account(s)
            <ul>
                <li><b>Cost Predictability</b>: Commiting to a plan can allow for better budget forecasting
                    <ul>
                        <li>If your monthly budget is fairly reliable, it's easier to make decisions when comparing against other products or even when reviewing technologies in use</li>
                    </ul>
                </li>
                <li><b>Flexibility</b>: Unlike reserving instances, a savings plan will provide flexibility across instance families (t2, m5 etc), instance sizes (small, 2x.large etc) and even which region they live (eu-central-1, eu-west-1)</li>
                <li><b>Immediate savings</b>: The initial upfront commitment will quickly convert into lower monthly bills
                    <ul>
                        <li>There is even an <a href="https://aws.amazon.com/savingsplans/compute-pricing/" target="_blank">estimated cost-saving calculator</a> that you can use before you commit to anything</li>
                    </ul>
                </li>
            </ul>

            <h5>When should you AVOID applying compute savings plans?</h5>
            Even though compute savings plans <i>can</i> lead to significant savings, you shouldn't just jump right in without considering the following.
            <ul>
                <li>
                    <b>Variable workloads</b>: If your compute usage differs from month to month, you may well be better off with an on-demand model.
                </li>
                <li>
                    <b>Short-Term Projects</b>: If you have temporary workloads or short-term projects, then it may not make sense to apply a savings plan, as may not return any investment.
                    <ul>
                        <li>You may be tied into paying for more compute power than you actually need, for at least 1 year or worst-case scenario, 3 years.</li>
                    </ul>
                </li>
            </ul>
            
            <h4>What are the alternative options?</h4>
            If compute savings plans aren't the right fit for your business, you might consider these alternatives.
            <ul>
                <li>
                    <b>Spot Instances</b>: Utilising AWS Spot instances for non-critical workloads could save you some money, as you essentially take advantage of unused EC2 capacity within the AWS Cloud that you previously did not have access to, and could save you up to 90% discount.
                </li>
                <li>
                    <b>Right-Sizing</b>: I'm still not sure I like this term, but essentially it is the act of ensuring that your instances aren't being over or, under-utilized. Reviewing what your compute instances actually use and need. e.g. Memory, CPU, Disk Volume
                    <ul>
                        <li>Reducing your instance sizes can be followed after carefully considering that they are simply using too little of some of the above metrics, and wasting money on them</li>
                    </ul>
                </li>
            </ul>
            
            You may now be thinking, <i>That's great Steve! What did the company save by implementing this?</i><br/><br/>
              By implementing a compute savings plan alone, the company approximately <b>$5k a month</b>. But the journey didn't end there.
            <br/><br/>

            <h4>Tackling Traffic Costs</h4>
            We noticed we were spending around <b>$3k a month</b> on data transfer between AWS accounts. The solution? <strong>VPC Peering</strong>, which significantly reduced these costs.
            <br/><br/>
            <h4>What is VPC Peering?</h4>
            A <b>VPC peering connection</b> allows direct routing between two virtual private cloud (VPC) networks, enabling smooth data transfer between them.
            <br/><br/>
            <h5>Why Use VPC Peering?</h5>
            <ul>
                <li><strong>No Setup Charge</strong>: Establishing a VPC peering connection is free.</li>
                <li><strong>Free Intra-AZ Transfers</strong>: Data transfers within the same availability zone (AZ) can be free.</li>
                <li><strong>Caveats</strong>: Transfers across different AZs or regions may incur charges.</li>
            </ul>
            By implementing VPC peering, we slashed data transfer costs dramatically.
            <br/><br/>
            <h4>Storage, Storage, Storage! <i>S3</i></h4>
            We shifted focus to S3 storage, using Python scripts with the boto3 module to identify the largest files in our S3 buckets. This allowed us to make informed decisions about which data to retain and which to discard.
            <br/><br/>
            By decluttering, we saved approximately <b>$2k</b> in monthly costs. Alternatively, we could have moved lesser-accessed data to cheaper storage like S3 Glacier.
            <br/><br/>
            In total, this journey to save <b>$10k</b> a month was rewarding, and there are countless ways you could start yours. Your mileage may vary!
            <br/><br/>
            Thank you for taking the time to read my blog post. If you're interested in learning more, feel free to check out the rest of the blog and my experiences.<br/>
            <br/>
            Thank you,<br/>
            Steve
            """,
        "image": "/static/images/cutting-monthly-aws-costs.webp",
        "image_caption": "This image was generated with the help of Dall-E",
        "tags": ["AWS", "Cost-Saving"],
        "slug": "learn-how-i-helped-save-10k-per-month-in-aws-costs"
    },
]