#!/bin/zsh

DEPLOYMENTS=("")
ANNOTATION_VALUE="/actuator/prometheus" # /metrics or /actuator prometheus

echo " Adding label and annotation to pod templates in deployments"

for DEPLOYMENT in ${DEPLOYMENTS[@]}; do
    echo "Processing deployment: $DEPLOYMENT"

    oc patch dc/"$DEPLOYMENT" --type='merge' -p " 
    spec:
      template:
        metadata:
          labels:
            prometheus: \"true\"
          annotations: 
            prometheus.io/path: \"$ANNOTATION_VALUE\"
    "
done
