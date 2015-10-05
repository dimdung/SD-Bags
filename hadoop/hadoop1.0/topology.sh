while [ $# -gt 0 ] ; do
  nodeArg=$1
  exec< /home/hadoop/topology.data
  result=""
  while read line ; do
    ar=( $line )
    if [ "${ar[0]}" = "$nodeArg" ] ; then
      result="${ar[1]}"
    fi
  done
  shift
  if [ -z "$result" ] ; then
    echo -n "/default"
  else
    echo -n "$result "
  fi
done
