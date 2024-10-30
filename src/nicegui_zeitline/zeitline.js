import "zeitline";

export default {
  template: `<svg :width="width" :height="height" />`,
  props: {
    conf: Object,
    width: Number,
    height: Number,
  },
  watch: {
    conf(newConf) {
      this.updateConf(newConf);
    },
  },
  methods: {
    updateConf(conf) {
      this.line.update(conf);
    },
  },
  data() {
    return {
      linePromise: new Promise((resolve) => {
        this.resolveLine = resolve;
      }),
    };
  },
  async mounted() {
    for (var key in this.conf) {
      if (Array.isArray(this.conf[key])) {
        this.conf[key].forEach((item, index) => {
          if (Array.isArray(item)) {
            // If the item is an array, iterate over its elements
            item.forEach((subItem, subIndex) => {
              if (typeof subItem === "string" && !isNaN(Date.parse(subItem))) {
                item[subIndex] = new Date(subItem);
              }
            });
          } else if (typeof item === "string" && !isNaN(Date.parse(item))) {
            // If the item itself is a string (like in dateRange)
            this.conf[key][index] = new Date(item);
          } else if (item && typeof item === "object" && item.date) {
            // If the item is an object with a date key
            if (
              typeof item.date === "string" &&
              !isNaN(Date.parse(item.date))
            ) {
              item.date = new Date(item.date);
            }
          }
        });
      }
    }

    var t = new Zeitline.Timeline(this.conf);
    t.render();
  },
};
