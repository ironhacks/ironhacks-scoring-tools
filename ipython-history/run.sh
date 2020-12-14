
SUBMISSION_ID=submission-1-mandatory
HACK_ID=damqtV7yE8O5JfMk0WQw
USER_ID=${1?'USER_ID is required'}

echo "Exporting hub history for ${USER_ID}"

./hub-history/ipython_history.py \
    --hack ${HACK_ID} \
    --submission ${SUBMISSION_ID} \
    --user ${USER_ID}
