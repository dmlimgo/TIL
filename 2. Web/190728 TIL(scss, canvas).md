1. scss / string interpolation in variables

   @each문으로 하면 $#{$value}와 같이 되어야 하는데, 아직 지원하지 않는 기능이기 때문에 아래와 같이 해결

   ```scss
   $member-names:  lmk, yco, kbs, ldm;
   $member-colors: #004b8d, #2f4f4f, #ec407a, #f2b705;
   $member-colors-hover: #004b8d, #2f4f4f, #ec407a, #f2b705;
   
   @for $i from 1 through 4 {
       .#{nth($member-names, $i)} {
           background: nth($member-colors, $i);
           animation: nth($member-names, $i) 1.5s ease;
           .home__eachmember__content {
               &:hover {
                   color: nth($member-colors-hover, $i);
               }
           }
       }
   }
   ```

   

2. canvas의 기본에 대해 동영상 강의 시청

3. flex가 만능이 아니란걸 깨닫음... absolute와 relative의 적절한 활용이 필요.. z-index때문에..