# Web Traffic Time Series Forecasting

Forecast future traffic to Wikipedia pages

## Getting Started

This Project is about predicting the future behaviour of time series’ that describe the web traffic for Wikipedia articles. The data contains about 145k time series and comes in two separate files: train_1.csv, train_2.csv holds the traffic data, where each column is a date and each row is an article, and key_1.csv , key_2.csv contains a mapping between page names and a unique ID column (to be used in the submission file).

### Prerequisites

What things you need to install the software and how to install them

```
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import re
%matplotlib inline
from statsmodels.tsa.arima_model import ARIMA
import warnings
```

### Installing

A step by step series of examples that tell you have to get a development env running

Say what the step will be

```
Give the example
```

And repeat

```
until finished
```

End with an example of getting some data out of the system or using it for a little demo


## Deployment

Add additional notes about how to deploy this on a live system

## Built With

* [Dropwizard](http://www.dropwizard.io/1.0.2/docs/) - The web framework used
* [Maven](https://maven.apache.org/) - Dependency Management
* [ROME](https://rometools.github.io/rome/) - Used to generate RSS Feeds

## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags). 

## Authors

* **Billie Thompson** - *Initial work* - [PurpleBooth](https://github.com/PurpleBooth)

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Hat tip to anyone who's code was used
* Inspiration
* etc

