"use strict";(self.webpackChunktrello_client=self.webpackChunktrello_client||[]).push([[37547],{"./packages/bootstrap/entry.ts":(e,t,n)=>{let r,a;function o(){return window.__bundles}let l={};async function c(e){if(e in l)return l[e];let t=o();if(!(e in t))throw Error("Bundle not supported");return l[e]=new Promise((n,r)=>{let a=document.createElement("script");a.nonce=window.__webpack_nonce__,a.crossOrigin="anonymous",a.onerror=()=>{r(Error("Could not load bundle"))},a.onload=()=>{n()},document.head.appendChild(a),a.src=t[e]}),l[e]}var s=n("./packages/locale/src/localeMatches.ts"),i=n("./packages/locale/src/normalizeLocale.ts");function u(){var e;if(r)return r;let t=o();if(!t||!(null!==(e=Object.keys(t))&&void 0!==e&&e.length))throw Error("No bundles found!");return r=Object.keys(t).filter(e=>e.startsWith("locale.")).map(e=>e.replace(/^locale\./,""))}function d(){for(let e of navigator.languages){let t=(0,i.Q)(e),n=u().find(e=>(0,s.s)(e,t));if(n)return n}return"en-US"}function p(e){var t;let n=null===(t=document.cookie.split("; ").find(t=>t.startsWith(`${e}=`)))||void 0===t||null===(t=t.split("="))||void 0===t?void 0:t[1];if(n)return decodeURIComponent(n)}async function f(e){if(!u().includes(e))throw Error("Locale not supported");return c(`locale.${e}`)}async function g(){await c("ltp"),await c("app"),window.startTrello()}!async function(){await function(){if(a)return a;let e=function(){let e=p("langOverride");if(e&&u().includes(e))return e;let t=p("idMember");if(!t)return d();let n=function(e){try{let t=window.localStorage.getItem(`locale-${e}`);return t?JSON.parse(t):null}catch(e){return null}}(t);return n&&u().includes(n)?n:d()}();return window.locale=e,a=f(e)}(),"loading"===document.readyState?document.addEventListener("DOMContentLoaded",g):g()}()},"./packages/locale/src/languageParts.ts":(e,t,n)=>{n.d(t,{H:()=>r});function r(e){let[,t="",n="",r="",a=""]=e.match(/^([a-zA-Z]{2,3})(?:[_-]+([a-zA-Z]{3})(?=$|[_-]+))?(?:[_-]+([a-zA-Z]{4})(?=$|[_-]+))?(?:[_-]+([a-zA-Z]{2}|[0-9]{3})(?=$|[_-]+))?/)||[];return{language:t.toLowerCase(),extlang:n.toLowerCase(),script:`${r.slice(0,1).toUpperCase()}${r.substr(1).toLowerCase()}`,region:a.toUpperCase()}}},"./packages/locale/src/localeMatches.ts":(e,t,n)=>{n.d(t,{s:()=>a});var r=n("./packages/locale/src/normalizeLocale.ts");function a(e,t){let n=(0,r.Q)(e).split("-"),a=(0,r.Q)(t).split("-");return n.length>a.length&&([n,a]=[a,n]),n.every((e,t)=>a[t]===e)}},"./packages/locale/src/normalizeLocale.ts":(e,t,n)=>{n.d(t,{Q:()=>a});var r=n("./packages/locale/src/languageParts.ts");function a(e){let t=e.split(/[@.]/)[0],{language:n,script:a,region:o}=(0,r.H)(t),l=[n];return a&&l.push(a),o&&l.push(o),l.join("-")}}},e=>{e(e.s="./packages/bootstrap/entry.ts")}]);
//# sourceMappingURL=bootstrap.d7fc9241f5735c338396.js.map