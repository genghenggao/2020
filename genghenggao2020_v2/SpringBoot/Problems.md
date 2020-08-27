## 解决WOW.js遇到wow is undefined；

In case you are facing similar issue please make sure that wow is loaded:

```
<scriptsrc="https://cdnjs.cloudflare.com/ajax/libs/wow/1.1.2/wow.min.js"></script>

<scriptsrc="https://cdnjs.cloudflare.com/ajax/libs/web-animations/2.2.2/web-animations.min.js"></script>
```

And initialize:

```
<script>

    new WOW().init();

</script>
```

